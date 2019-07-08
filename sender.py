import argparse
import requests
import re
from pathlib import Path


LANGS = {
    'fpc': 31,
    'vc': 39,
    'vcpp': 40,
    'gcc': 45,
    'g++': 46,
    'clang': 47,
    'java': 32,
    'csharp': 41,
    'py2': 34,
    'py3': 48,
    'go': 14,
    'ruby': 18,
    'haskell': 19,
    'scala': 33,
    'rust': 55,
    'kotlin': 49,
}

DEFAULT_COMPILERS = {
    '.pas': 'fpc',
    '.c': 'gcc',
    '.cpp': 'g++',
    '.java': 'java',
    '.py': 'py3',
    '.cs': 'csharp',
    '.rb': 'ruby'
}

parser = argparse.ArgumentParser(description='Submit solution to acm.timus.ru')
parser.add_argument('--judge-id', '-j', nargs='?', help='Judge ID')
parser.add_argument('--compiler', '-c', nargs='?', help='Langage/compiler')
parser.add_argument('--problem', '-p', nargs='?', help='Problem ID')
parser.add_argument('file', nargs=1, help='Source code file')

args = parser.parse_args()

args.file = args.file[0]

if not args.judge_id:
    with open(Path.home() / '.judge_id') as f:
        args.judge_id = f.read().strip()

if not args.problem:
    folder_name = Path(args.file).parent.name
    match = re.search(r'^(.+-)?(?P<number>\d+)(-.+)?$', folder_name)
    if match and match.group('number'):
        args.problem = match.group('number')
    else:
        print('Error: Cannot parse problem number from path')
        exit(1)

if not args.compiler:
    ext = Path(args.file).suffix
    if ext in DEFAULT_COMPILERS:
        args.compiler = DEFAULT_COMPILERS[ext]
    else:
        print(f'Error: Cannot define compiler for extension {ext}')
        exit(1)


url = 'http://acm.timus.ru/submit.aspx?space=1'

data = {
    'Action': (None, 'submit'),
    'SpaceID': (None, '1'),
    'JudgeID': (None, args.judge_id),
    'Language': (None, LANGS[args.compiler]),
    'ProblemNum': (None, args.problem),
    'Source': (None, ''),
    'SourceFile': (
        args.file,
        open(args.file, 'rb'),
    )
}

r = requests.post(url, files=data)
if r.status_code != 200:
    print(f'Warn: statuc sode is {r.status_code}')
    exit(1)
else:
    exit(0)
