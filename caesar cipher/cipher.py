alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def init():
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
    if direction not in ["encode", "decode"]:
        exit()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(direction, text, shift)


def cipher(direction, text, shift):
    cipText = ""
    if direction == "decode":
        shift *= -1

    maxLen = len(alphabet)

    for x in text:
        position = alphabet.index(x)
        position += shift
        if position > maxLen:
            position = position - maxLen
        cipText += alphabet[position]

    print(f"Your new text: {cipText}")


init()
