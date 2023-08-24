def solve_word_problem():
    
    # Import three letter words from file
    try:
        three_letter_words = []
        with open('./three_letter_words.txt') as f:
            for word in f:
                three_letter_words.append(word.strip())

    except FileNotFoundError:
        print("Three Letter Words list not found!")

    # Import nine letter words from file
    try:
        nine_letter_words = []
        with open('./nine_letter_words.txt') as f:
            for word in f:
                nine_letter_words.append(word.strip())
    
    except FileNotFoundError:
        print("Three Letter Words list not found!")

    # Set possible letters for each cell color
    blue_cells = ["p", "a", "r", "t"]
    green_cells = ["e", "y", "e", "s"]
    gold_cells = ["u", "n", "c", "u", "r", "l"]
    white_cells = ["r"]

    # Find valid words per row
    valid_words_row_one = []
    valid_words_row_two = []
    valid_words_row_three = []

    for letter_1 in gold_cells:
        for letter_2 in blue_cells:
            for letter_3 in white_cells:
                potential_word = letter_1 + letter_2 + letter_3
                if potential_word in three_letter_words:
                    valid_words_row_one.append(potential_word)

    for letter_1 in blue_cells:
        for letter_2 in green_cells:
            for letter_3 in gold_cells:
                potential_word = letter_1 + letter_2 + letter_3
                if potential_word in three_letter_words:
                    valid_words_row_two.append(potential_word)

    for letter_1 in blue_cells:
        for letter_2 in gold_cells:
            for letter_3 in green_cells:
                potential_word = letter_1 + letter_2 + letter_3
                if potential_word in three_letter_words:
                    valid_words_row_three.append(potential_word)
                
    print(valid_words_row_one)
    print(valid_words_row_two)
    print(valid_words_row_three)

    # Find valid nine letter words from the previous valid words
    valid_nine_letter_words = []

    for word1 in valid_words_row_one:
        for word2 in valid_words_row_two:
            for word3 in valid_words_row_three:
                potential_word = word1 + word2 + word3
                if potential_word in nine_letter_words:
                    valid_nine_letter_words.append(potential_word)

    print(valid_nine_letter_words)

solve_word_problem() # Answer is Carpentry
