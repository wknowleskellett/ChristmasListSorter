from functools import cmp_to_key as ctk


def clean_pair(pair, len):
    return f'{pair[0]: <{max_len}}\t{pair[1]}'

def compare(item1, item2):
    print("Prefer 1, or 2:", end="\n\n")

    pad_len = max(len(item1[0]), len(item2[0]))
    print("0")
    print("1", clean_pair(item1, pad_len))
    print("2", clean_pair(item2, pad_len), end="\n\n")

    ans = " "
    while ans not in ["0", "1", "2"]:
        ans = input()

    print(end="\n\n")

    # Highest ranked items at the top of the list
    if ans == "1":
        return -1
    elif ans == "2":
        return 1
    else:
        return 0


with open("wish_list.tsv") as present_list:
    pairs = {k:v[:-1] for k, v in [s.split('\t') for s in present_list.readlines()]}.items()

max_len = max([len(p[0]) for p in pairs])

for p in sorted(pairs, key=ctk(lambda item1, item2: compare(item1, item2))):
    print(clean_pair(p, max_len))