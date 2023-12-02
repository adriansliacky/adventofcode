vals = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}
snafu_to_dec = lambda d: sum(
    [(list(vals.keys())[list(vals.values()).index(d[i])] * 5 ** r) for i, r in enumerate(reversed(range(len(d))))])
dec_to_snafu = lambda d: (dec_to_snafu((d + 2) // 5) + vals[(d + 2) % 5 - 2]) if d != 0 else ''
print(dec_to_snafu(sum([snafu_to_dec(i) for i in open('input.txt').read().rstrip().splitlines()])))
