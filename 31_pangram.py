def is_pangram(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in alphabet:
        if char not in text.lower():
            return False

    return True


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    if is_pangram(sentence):
        print("The sentence is a Pangram.")
    else:
        print("The sentence is not a Pangram.")