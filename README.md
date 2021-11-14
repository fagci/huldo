# huldo

Human language deobfuscator/obfuscator

Tags: 1337, leet speak, русский 1337

## Examples

```sh
./huldo.py '4n0nym0u5'
anonymous
```

```sh
./huldo.py -r 'anonymous'
4n0nym0u5
```

```sh
./huldo.py -rR -d ru 'Шла Саша по шоссе'
W/|a СAw@ пo wocc3
```

```sh
./huldo.py -d ru 'W/|a СAw@ пo wocc3'
Шла Саша по шоссе
```

```sh
./huldo.awk dict/en.txt <(echo '1337')
leet
```

## Usage

```
huldo.py [-h] [-r] [-R] [-d DICTIONARY] text

positional arguments:
  text

options:
  -h, --help            show this help message and exit
  -r, --reverse
  -R, --random
  -d DICTIONARY, --dictionary DICTIONARY
```
