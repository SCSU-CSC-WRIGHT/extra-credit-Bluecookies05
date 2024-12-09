def length_of_last_word(s):
    stripped_string=s.strip()

    words = stripped_string.split()

    last_word = word[-1]

    return len(last_word)


print(length_of_last_word(input_string))

