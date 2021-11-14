#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from random import shuffle

DIR = Path(__file__).resolve().parent / 'dict'


def deobfuscate(d, text):
    for k, v in d:
        text = text.replace(k, v)
    return text


def obfuscate(d, text, random):
    res = []
    for c in text:
        if random:
            shuffle(d)

        found = False
        for k, v in d:
            if k == c:
                res.append(v)
                found = True
                break

        if not found:
            res.append(c)

    return ''.join(res)


def main(text, rev=False, random=False, dictionary='en'):
    RU = DIR / ('%s.txt' % dictionary)
    sp = map(str.split, RU.read_text().splitlines(False))

    if rev:
        d = [(v, k) for k, v in sp]
        print(obfuscate(d, text, random))
    else:
        d = [(k, v) for k, v in sp]
        print(deobfuscate(d, text))


if __name__ == "__main__":
    p = ArgumentParser()

    p.add_argument('-r', '--reverse', default=False, action='store_true')
    p.add_argument('-R', '--random', default=False, action='store_true')
    p.add_argument('-d', '--dictionary', type=str, default='en')
    p.add_argument('text', type=str)

    a = p.parse_args()

    main(a.text, a.reverse, a.random, a.dictionary)
