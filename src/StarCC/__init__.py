from os import path
import pygtrie

here = path.abspath(path.dirname(__file__))

class Dicts:
    CN2ST = ('STCharacters', 'STPhrases')
    TW2ST = ('TWVariantsRev', 'TWVariantsRevPhrases')
    TWP2ST = ('TWVariantsRev', 'TWVariantsRevPhrases', 'TWPhrasesRev')
    HK2ST = ('HKVariantsRev', 'HKVariantsRevPhrases')
    JP2ST = ('JPVariantsRev', 'JPShinjitaiCharacters', 'JPShinjitaiPhrases')

    ST2CN = ('TSCharacters', 'TSPhrases')
    ST2HK = ('HKVariants',)
    ST2TW = ('TWVariants',)
    ST2TWP = ('TWVariants', 'TWPhrasesIT', 'TWPhrasesName', 'TWPhrasesOther')
    ST2JP = ('JPVariants',)

def _dicts2trie(dicts):
    trie = pygtrie.CharTrie()

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

def _convert(trie, s: str) -> str:
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

class Conversion:
    def __init__(self, dicts_list) -> None:
        self.tries = [_dicts2trie(dicts) for dicts in dicts_list]

    def __call__(self, s: str) -> str:
        for trie in self.tries:
            s = _convert(trie, s)
        return s

class PresetConversion(Conversion):
    def __init__(self, src='cn', dst='hk', with_phrase: bool=False) -> None:
        if src not in ('st', 'cn', 'hk', 'tw', 'jp'):
            raise ValueError(f'Invalid src value: {src}')
        if dst not in ('st', 'cn', 'hk', 'tw', 'jp'):
            raise ValueError(f'Invalid dst value: {dst}')
        assert src != dst

        dicts_list = []

        if src != 'st':
            if not with_phrase:
                dicts_list.append({
                    'cn': Dicts.CN2ST,
                    'hk': Dicts.HK2ST,
                    'tw': Dicts.TW2ST,
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
                    'jp': Dicts.ST2JP,
                }[dst])
            else:  # with_phrase
                if src not in ('cn', 'tw'):
                    raise ValueError(f'Phrase conversion for {src} is currently not supported')
                dicts_list.append({
                    'cn': Dicts.ST2CN,  # CN does not need to convert phrases
                    'tw': Dicts.ST2TWP,
                }[dst])

        super().__init__(dicts_list)
