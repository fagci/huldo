#!/usr/bin/env python3

from pathlib import Path
from argparse import ArgumentParser
from random import shuffle

DIR = Path(__file__).resolve().parent
RU = DIR / 'ru.txt'


def main(text, rev=False, random=False):
    sp = map(str.split, RU.read_text().splitlines(False))

    if rev:
        d = [(v, k) for k, v in sp]
    else:
        d = [(k, v) for k, v in sp]

    res = []
    for c in text:
        if rev and random:
            shuffle(d)

        found = False
        for k, v in d:
            if k == c:
                res.append(v)
                found = True
                break
        if not found:
            res.append(c)
    print(''.join(res))


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument('-r', '--reverse', default=False, action='store_true')
    p.add_argument('-R', '--random', default=False, action='store_true')
    p.add_argument('text', type=str)
    a = p.parse_args()
    main(a.text, a.reverse, a.random)
