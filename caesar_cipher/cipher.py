from caesar_cipher.corpus_loader import word_list, name_list


def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

def crack(encrypted_text):
    for shift in range(26):
        counter = 0
        unencrypted_text = encrypt(encrypted_text, shift)
        list_word = unencrypted_text.split()
        for letter in list_word:
            if letter in name_list or letter in word_list:
                counter += 1
        if (counter/len(list_word)) > .5:
          return ' '.join(list_word)
    return ''
