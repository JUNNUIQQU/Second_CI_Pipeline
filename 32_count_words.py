def count_words(sentence):
    words = sentence.split()
    return len(words)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    result = count_words(sentence)

    print("Total number of words:", result)