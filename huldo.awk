#!/usr/bin/env -S awk -f
# Usage: ./huldo.awk dict/en.txt <(echo '1337')

NR == FNR {
    dict[$1] = $2
    next
}

{
    for(k in dict) {
        gsub(k, dict[k], $0)
    }
    print
}
