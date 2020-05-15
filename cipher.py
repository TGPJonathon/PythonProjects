import string

alphabet = list(string.ascii_lowercase)


def ciper_encrypt(num, word):
    word = word.lower()
    new_word = []
    for letter in word:
        if letter == ' ' or letter == ',' or letter == '?' or letter == '!' or letter == '.':
            new_word.append(letter)
            continue
        else:
            x = alphabet.index(letter)
            new_word.append(alphabet[(x+num) % 26])
    return ''.join(new_word)

def cipher_decrypt(num, word):
    word = word.lower()
    new_word = []
    for letter in word:
        if letter == ' ' or letter == ',' or letter == '?' or letter == '!' or letter == '.':
            new_word.append(letter)
            continue
        else:
            x = alphabet.index(letter)
            new_word.append(alphabet[(x-num % 26)])
    return ''.join(new_word)


print(ciper_encrypt(39, "Hello, How are You?"))

print(cipher_decrypt(39, "uryyb, ubj ner lbh").title())