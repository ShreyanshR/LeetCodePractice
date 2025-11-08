def smallest_string(word: str) -> str:
    smallest = word

    for i in range(0, len(word)-1):
        if word[i] > word[i+1]:
            print(f'word, next_word: {word[i], word[i+1]}')
            smallest = word[:i] + word[i+1:]
            print(smallest)
            return smallest
    
    smallest = word[:-1]
    
    return smallest


if __name__ == "__main__":
    word = 'house'

    print(smallest_string(word))
    print(smallest_string('wedding'))
    print(smallest_string('trading'))
    print(smallest_string('abcd'))
