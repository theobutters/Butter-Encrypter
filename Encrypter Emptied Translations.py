from random import randint as rint

global dict
dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -=!\"£$%^&*()_+[]{};\'#:@~\\|,./<>?`¬¦"


def translate(text, reverse=False):
  translations = {
      # Emptied due to use of previous character set being used for encryption of data elsewhere.

      # Left character is original character, right character is the character after translation.
      # Example format:
      'a': '3',
      'b': '2',
      'c': '1',
  }

  if reverse:
    translations = {v: k for k, v in translations.items()}

  translated_text = ''
  isrtl = False
  for char in text:
    if char == "\u200e":
      isrtl = True
      continue

    if isrtl:
      isrtl = False
      char = '\u200e' + char
    translated_text += translations.get(char, char)
  return translated_text


def shift_cipher(text, shift, dict):
  result = []
  dict_len = len(dict)
  char_to_index = {char: idx for idx, char in enumerate(dict)}

  for char in text:
    if char in char_to_index:
      new_index = (char_to_index[char] + shift) % dict_len
      result.append(dict[new_index])
    else:
      result.append(char)
  return ''.join(result)


def encrypter():
  input_txt = input("\nInput text to be encrypted:\n\n ")
  keycount = (len(input_txt) // 8) + 1
  print("\nKeycount:", keycount)
  encrypted_text = ""
  print("Encrypted Text:", encrypted_text)

  for i in range(keycount):
    key = rint(0, len(dict) - 1)
    print("Key:", key)
    current_segment = input_txt[i * 8:i * 8 + 8]
    print("Current Segment:", current_segment)
    encrypted_segment = shift_cipher(current_segment, key, dict)
    print("Encrypted Segment:", encrypted_segment)
    encrypted_text += "{:02d}".format(key) + encrypted_segment
    print("Encrypted Text:", encrypted_text)
  encrypted_text = translate(encrypted_text)
  print("\n\nEncrypted text:\n\n", encrypted_text)


def decrypter():
  input_txt = input("\nInput text to be decrypted:\n\n ")
  keycount = (len(input_txt) // 10) + 1
  print("\nKeycount:", keycount)
  decrypted_text = ""
  print("Decrypted Text:", decrypted_text)
  input_txt = translate(input_txt, True)
  print("Translated Text:", input_txt)
  for i in range(keycount):
    current_segment = input_txt[i * 10:i * 10 + 10]
    print("Current Segment:", current_segment)
    key = int(current_segment[:2])
    print("Key:", key)
    decrypted_segment = shift_cipher(current_segment[2:10], -key, dict)
    print("Decrypted Segment:", decrypted_segment)
    decrypted_text += decrypted_segment
    print("Decrypted Text:", decrypted_text)
  print("\n\nDecrypted text:\n\n", decrypted_text)


def start():
  usr_choice = input("Select Mode:\n\n1. Encrypt\n2. Decrypt\n\n ")
  if usr_choice == "1":
    encrypter()
  elif usr_choice == "2":
    decrypter()
  else:
    print("Invalid input")
    start()

start()