alphabet = [chr(upper) for upper in range(ord('A'), ord('Z') + 1)]


def rot_encrypt(data: str, key: int, alph: list=alphabet):
    return ''.join(list(map(
        lambda x: x if x not in alph
        else alph[(alph.index(x) + (key % len(alph))) % len(alph)], data)))


def rot_decrypt(data: str, key: int, alph: list=alphabet):
    return rot_encrypt(data, (len(alph) - (key % len(alph))), alph)


def rot_find_key(encrypted: str, alph: list=alphabet):
    from FreqAnalysis import calculate_frequency
    a = list(calculate_frequency(encrypted))[0][0]

    if alph.index(a) >= alph.index("E"):
        return alph.index(a) - alph.index("E")
    else:
        return len(alph) - alph.index("E") - alph.index(a)


def rot_decrypt_no_key(encrypted: str, alph: list=alphabet):
    return rot_decrypt(encrypted, rot_find_key(encrypted, alph), alph)


