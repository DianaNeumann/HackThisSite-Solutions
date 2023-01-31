def get_alphabetical_order_words():
    result_map = {}
    with open('external_resources/wordlist.txt') as wordlist:
        for word in wordlist:
            sorted_word = ''.join(sorted(word.strip('\n')))
            result_map[sorted_word] = word.strip('\n')
    return result_map

def get_words(scrambled_words, sorted_map):
    words = []
    for scrambled_word in scrambled_words:
        sorted_word = ''.join(sorted(scrambled_word))
        words.append(sorted_map[sorted_word])
    return words


if __name__ == "__main__":
    sorted_map = get_alphabetical_order_words()
    scrambled_words = input('Enter scrambled words: ').split()
    unscrambled_words = get_words(scrambled_words, sorted_map)
    print(','.join(unscrambled_words))
