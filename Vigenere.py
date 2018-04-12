alphabet = [chr(upper) for upper in range(ord('A'), ord('Z') + 1)]
           # + \
           # [chr(lower) for lower in range(ord('a'), ord('z') + 1)] + \
           # [chr(digit) for digit in range(ord('0'), ord('9') + 1)] + \
           # [',', '.', ';', "'", ' ', '\n', '-', '(', ')', ':']

vigenere_matrix = [(alphabet[i:] + alphabet[:i]) for i in range(len(alphabet))]


def _generate_vigenere_key_sequence(data: str, key: str):
    intermediate_key = str()
    for i in range(len(data)):
        intermediate_key += key[i % len(key)]
    return intermediate_key


def vigenere_encrypt(data: str, key: str):
    ik = _generate_vigenere_key_sequence(data=data, key=key)
    e = str()
    for i, v in enumerate(ik):
        e += vigenere_matrix[alphabet.index(v)][alphabet.index(data[i])]
    return e


def vigenere_decrypt(data: str, key: str):
    ik = _generate_vigenere_key_sequence(data=data, key=key)
    d = str()
    for i, v in enumerate(ik):
        d += alphabet[vigenere_matrix[alphabet.index(v)].index(data[i])]
    return d


def calculate_index_of_coincidence(data: str):
    entrance_amount = {c: 0 for c in alphabet}
    for c in data:
        entrance_amount[c] += 1
    entrance_amount = {k: v for k, v in entrance_amount.items() if v > 0}
    return sum(list(map(lambda x: x**2, entrance_amount.values()))) / len(data)**2


def detect_vigenere_key_length(data: str, lens_to_check: list=None, max_len: int=10):
    en_index_of_coincidence = 0.065
    cis = dict()
    for t in lens_to_check if lens_to_check else range(1, max_len):
        tmp_data = str()
        for i in range(0, len(data), t):
            tmp_data += data[i]
        cis[t] = (calculate_index_of_coincidence(data=tmp_data))
    tmp = {k: abs(en_index_of_coincidence - v) for k, v in cis.items()}
    return min(tmp, key=tmp.get)


def vigenere_find_key(enc: str, key_len=None):
    from ROT import rot_find_key
    if key_len:
        return "".join([alphabet[rot_find_key(enc[i::key_len])] for i in range(key_len)])
    else:
        key_len = detect_vigenere_key_length(enc)
        print("PRED KEY LENGTH: ", key_len)
        return "".join([alphabet[rot_find_key(enc[i::key_len])] for i in range(key_len)])
