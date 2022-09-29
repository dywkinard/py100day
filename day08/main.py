from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_caesar = False
print(f"{logo}\n")


def caesar(text, shift, direction):
  new_text = list()
  for c in text:
    if ord(c) >= 65 and ord(c) <= 90 and direction.lower() == "encode":
      new_c = ((((ord(c) - 65) + shift) % 26) + 65)
      new_text.append(chr(new_c))
    elif ord(c) >= 97 and ord(c) <= 122 and direction.lower() == "encode":
      new_c = ((((ord(c) - 97) + shift) % 26) + 97)
      new_text.append(chr(new_c))
    elif ord(c) >= 65 and ord(c) <= 90 and direction.lower() == "decode":
      new_c = ((((ord(c) - 65) - shift) % 26) + 65)
      new_text.append(chr(new_c))
    elif ord(c) >= 97 and ord(c) <= 122 and direction.lower() == "decode":
      new_c = ((((ord(c) - 97) - shift) % 26) + 97)
      new_text.append(chr(new_c))
    
  print(f"The encoded/decoded text is:\n\n----------\n{''.join(new_text)}\n----------\n")



while not end_caesar:
  accept_strings = ["encode", "decode"]
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower().strip()
  print("\n")
  if direction not in accept_strings:
    continue
  
  text = input("Type your message: ")
  print("\n")
  try: 
    shift = int(input("Type the shift number: "))
    print("\n")
  except:
    print("Must be a digit\n")
    continue
  caesar(text, shift, direction)
  restart = input("Would you like to run cipher again? (Type Yes or No): ")
  if restart.lower() == "yes":
    print("\n")
    valid = False
    continue
  else:
    end_caesar = True
