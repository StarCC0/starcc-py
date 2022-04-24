import os
import pygtrie

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
        if not os.path.exists(filename):
            filename_ = f'dict/{filename}.txt'
            if os.path.exists(filename_):
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

convert = Conversion((Dicts.CN2ST, Dicts.ST2TWP))

print(convert('为什么你在床里面睡着？我们的硅二极管坏了，要去老挝修理。'))
