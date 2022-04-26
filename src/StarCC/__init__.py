import jieba
from os import path
from pygtrie import CharTrie
from typing import Callable, List, Optional, Sequence

from .Dicts import Dicts

here = path.abspath(path.dirname(__file__))

def _dicts2trie(dicts: str) -> CharTrie:
    trie = CharTrie()

    for filename in dicts:
        if not path.exists(filename):
            filename_ = path.join(here, 'dict', f'{filename}.txt')
            if path.exists(filename_):
                filename = filename_
            else:
                raise ValueError(f'Dictionary file {filename} is not accessible')

        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')

                if line and not line.startswith('#'):
                    k, vs = line.split('\t')
                    vs = vs.split(' ')

                    trie[k] = vs[0]  # only select the first one

    return trie

def _convert_inner(trie: CharTrie, s: str) -> str:
    results = []

    total_len = len(s)
    start_pos = 0

    while start_pos < total_len:
        substr = s[start_pos:]

        longest_prefix = trie.longest_prefix(substr)
        if not longest_prefix:
            result = substr[0]
            start_pos += 1
        else:
            k = longest_prefix.key
            v = longest_prefix.value

            result = v
            start_pos += len(k)

        results.append(result)

    return ''.join(results)

def _convert(tries: Sequence[CharTrie], s: str):
    for trie in tries:
        s = _convert_inner(trie, s)
    return s

def _run_once(f):
    is_executed = False
    def wrapper():
        nonlocal is_executed
        if not is_executed:
            f()
            is_executed = True
    return wrapper

@_run_once
def _jieba_add_words():
    filenames = ['STPhrases', 'TWPhrasesIT', 'TWPhrasesName', 'TWPhrasesOther']
    for filename in filenames:
        phrase_file = path.join(here, 'dict', f'{filename}.txt')
        with open(phrase_file, encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')

                if line and not line.startswith('#'):
                    k, _ = line.split('\t')
                    jieba.add_word(k)

class Conversion:
    def __init__(self, dicts_list: Sequence[str], seg_func: Optional[Callable]=None) -> None:
        self.tries = [_dicts2trie(dicts) for dicts in dicts_list]
        self.seg_func = (lambda x: [x]) if seg_func is None else seg_func

    def __call__(self, s: str) -> str:
        results = []
        for seg in self.seg_func(s):
            seg = _convert(self.tries, seg)
            results.append(seg)
        return ''.join(results)

class PresetConversion(Conversion):
    def __init__(self, src: str='cn', dst: str='hk', with_phrase: bool=False, use_seg: bool=True) -> None:
        '''
        Initialize a `PresetConversion` object.

        `use_seg` Whether to use an external segmentation tool (i.e. jieba) or not when
        at least one of the following two conditions is satisfied: (1) converting from
        Simplified Chinese; (2) converting to Traditional Chinese (Taiwan) with phrase
        conversion. If the conditions are not meet, this option has no effect.
        '''

        if src not in ('st', 'cn', 'hk', 'tw', 'cnt', 'jp'):
            raise ValueError(f'Invalid src value: {src}')
        if dst not in ('st', 'cn', 'hk', 'tw', 'cnt', 'jp'):
            raise ValueError(f'Invalid dst value: {dst}')
        assert src != dst

        dicts_list = []

        if src != 'st':
            if not with_phrase:
                dicts_list.append({
                    'cn': Dicts.CN2ST,
                    'hk': Dicts.HK2ST,
                    'tw': Dicts.TW2ST,
                    'cnt': Dicts.CNT2ST,
                    'jp': Dicts.JP2ST,
                }[src])
            else:  # with_phrase
                if src not in ('cn', 'tw'):
                    raise ValueError(f'Phrase conversion for {src} is currently not supported')
                dicts_list.append({
                    'cn': Dicts.CN2ST,  # CN does not need to convert phrases
                    'tw': Dicts.TWP2ST,
                }[src])

        if dst != 'st':
            if not with_phrase:
                dicts_list.append({
                    'cn': Dicts.ST2CN,
                    'hk': Dicts.ST2HK,
                    'tw': Dicts.ST2TW,
                    'cnt': Dicts.ST2CNT,
                    'jp': Dicts.ST2JP,
                }[dst])
            else:  # with_phrase
                if dst not in ('cn', 'tw'):
                    raise ValueError(f'Phrase conversion for {dst} is currently not supported')
                dicts_list.append({
                    'cn': Dicts.ST2CN,  # CN does not need to convert phrases
                    'tw': Dicts.ST2TWP,
                }[dst])

        use_seg_func = use_seg and (src == 'cn' or dst == 'tw' and with_phrase)
        if use_seg_func:
            _jieba_add_words()
        seg_func = None if not use_seg_func else jieba.cut

        super().__init__(dicts_list, seg_func)
