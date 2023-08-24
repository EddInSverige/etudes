# Solutions to https://www.gchq.gov.uk/files/The%20GCHQ%20Christmas%20Challenge%202022.pdf


def solve_coding_problem():
    # Import three and nine letter words from dictionary
    try:
        three_letter_words = []
        nine_letter_words = []

        with open('./words.txt') as f:
            for word in f:
                # Strip /n
                word = word.strip()    

                 # We only want strings
                if word.isalpha():
                    if len(word) == 3:
                        three_letter_words.append(word.lower())
                    elif len(word) == 9:
                        nine_letter_words.append(word.lower())

    except FileNotFoundError:
        print("Dictionary not found!")

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

    # Find valid nine letter words from the previous valid words
    valid_nine_letter_words = []

    for word1 in valid_words_row_one:
        for word2 in valid_words_row_two:
            for word3 in valid_words_row_three:
                potential_word = word1 + word2 + word3
                if potential_word in nine_letter_words:
                    valid_nine_letter_words.append(potential_word)

    return valid_nine_letter_words[0]


def solve_engineering_problem():
    # Our cogs in the problem
    cog_1 = ["r", "m", "n", "o", "p", "q"]
    cog_2 = ["e", "f", "g", "h", "i", "j", "k", "l"]
    cog_3 = ["j", "b", "c", "d", "e", "f", "g", "h", "i"]
    cog_4 = ["k", "l", "m", "n", "o"]
    cog_5 = ["x", "y", "z", "t", "u", "v", "w"]

    # Get the required cog (really just the head of our array)
    def head(cog):
        return cog[0]
    
    assert(head(["a", "b", "c"]) == "a")

    # Functions for rotating the cog, or really our array
    def rotate_cog_clockwise(cog):
        return cog[-1:] + cog[:-1]

    def rotate_cog_anticlockwise(cog):
        return cog[1:] + cog[:1]
    
    assert(rotate_cog_clockwise(["a", "b", "c"]) == ["c", "a", "b"])
    assert(rotate_cog_anticlockwise(["a", "b", "c"]) == ["b", "c", "a"])

    # We need to rotate multiple times 
    def rotate_n_times_clockwise(cog, n):
        if n == 0:
            return cog
        
        return rotate_n_times_clockwise(rotate_cog_clockwise(cog), n - 1)

    def rotate_n_times_anticlockwise(cog, n):
        if n == 0:
            return cog
        
        return rotate_n_times_anticlockwise(rotate_cog_anticlockwise(cog), n - 1)

    assert(rotate_cog_clockwise(rotate_cog_clockwise(["a", "b", "c"])) == rotate_n_times_clockwise(["a", "b", "c"], 2))
    assert(rotate_cog_anticlockwise(rotate_cog_anticlockwise(["a", "b", "c"])) == rotate_n_times_anticlockwise(["a", "b", "c"], 2))

    # Rotate 20 times as per the problem
    letter_1 = head(rotate_n_times_clockwise(cog_1, 20))
    letter_2 = head(rotate_n_times_anticlockwise(cog_2, 20))
    letter_3 = head(rotate_n_times_anticlockwise(cog_3, 20))
    letter_4 = head(rotate_n_times_clockwise(cog_4, 20))
    letter_5 = head(rotate_n_times_clockwise(cog_5, 20))

    # And print the result!
    return letter_1 + letter_2 + letter_3 + letter_4 + letter_5

def solve_cyber_security_problem():
    # This is a directed graph / shortest path problem *but* we know the 
    # letters and the length of the solution and that the answer is a word
    # 
    # ...
    # RAMMING SPEED!
    def brute_force_solution():
        from itertools import combinations_with_replacement

        seven_letter_words = []
        with open("./words.txt") as f:
            for word in f:
                if len(word) == 7:
                    seven_letter_words.append(word.lower().split())
        
        combinations = list(combinations_with_replacement(["a", "d", "e", "n", "s", "w"], 7))

        possible_solutions = []
        
        for combination in combinations:
            if ''.join(combination) in seven_letter_words:
                possible_solutions.append(combination)

        return possible_solutions

    print(brute_force_solution())


print(solve_coding_problem())       # Answer is Carpentry
print(solve_engineering_problem())  # Answer is Picky
# solve_cyber_security_problem()
