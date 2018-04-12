from Vigenere import *


def parse_input(data: str, alph: list):
    return "".join(list(filter(lambda x: x in alph, str.upper(data))))


with open("G:/Labs/CRYPTO/lab_1/task_3_source.txt") as file:
    msg = parse_input(file.read(), alphabet)

k = "PASSWD"
e = vigenere_encrypt(data=msg, key=k)
d = vigenere_decrypt(data=e, key=k)

print("MSG: {}\nENC: {}\nDEC: {}".format(msg, e, d))
print("REAL KEY LENGTH: ", len(k))

predicted_key = vigenere_find_key(enc=e)

print("REAL KEY: {}\nPRED KEY: {}".format(k, predicted_key))
print("DEC: ", vigenere_decrypt(data=e, key=predicted_key))
