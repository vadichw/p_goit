def solve_riddle(riddle, word_length, start_letter, reverse=False):
    
    if not isinstance(riddle, str) or not isinstance(word_length, int) or not isinstance(start_letter, str) or not isinstance(reverse, bool) or word_length <= 0:
        return ""

    possible_words = [riddle[i:i+word_length] for i in range(0, len(riddle) - word_length + 1)]

    for word in possible_words:
        if reverse:
            word = word[::-1]
        if word[0] == start_letter:
            return word

    return ""