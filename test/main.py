import os
from os import path
from StarCC import PresetConversion

tests = (
    ('hk2s', ('hk', 'cn', False)),
    ('hk2t', ('hk', 'st', False)),
    ('jp2t', ('jp', 'st', False)),
    ('s2hk', ('cn', 'hk', False)),
    ('s2t', ('cn', 'st', False)),
    ('s2tw', ('cn', 'tw', False)),
    ('s2twp', ('cn', 'tw', True)),
    ('t2hk', ('st', 'hk', False)),
    ('t2jp', ('st', 'jp', False)),
    ('t2s', ('st', 'cn', False)),
    ('tw2s', ('tw', 'cn', False)),
    ('tw2sp', ('tw', 'cn', True)),
    ('tw2t', ('tw', 'st', False)),
)

if not path.exists('test/testcases'):
    os.system('git -C test clone https://github.com/StarCC0/testcases.git')
os.system('git -C test pull')

def run_test(name, config):
    with open(f'test/testcases/{name}.in', encoding='utf-8') as f:
        xs = f.read()
    with open(f'test/testcases/{name}.ans', encoding='utf-8') as f:
        ys = f.read()

    convert = PresetConversion(*config)
    ys_ = convert(xs)

    if ys != ys_:
        print(f'Error found in {name}\n'
              f'Expected: {ys}\n'
              f'Got: {ys_}\n\n')

for test in tests:
    run_test(*test)
