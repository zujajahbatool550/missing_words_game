import random

def main():

    print("Welcome to the Word Puzzle!")
    print("Try to guess the word by entering letters one at a time.")
    print("Remember you have to type the complete word in order to win the game.")
    print("You have 5 attempts to guess the word correctly.")
    print("The word will be displayed with some letters hidden.")
    print("Let's start the game!")

    count = 0

    #Initialize count to keep track of correct guesses.
    
    attempts = 5

    while attempts >= 1:

        #Loop to run the game for 5 times.

        words_lst = read_words_from_file("wordlist.txt")
        word = get_random_words(words_lst)

        #print(word)  Use this line for testing.

        hide = len(word) //2 
        
        #hide half of the letters in the word.

        hidden_word = hide_parts(word, hide)
        print(hidden_word)

        your_guess = get_guess()

        if check_guess(your_guess, word) == True:

            count += 1

        else:

            if other_possible_words(hidden_word, words_lst) == True:

                print(" This word is not the correct one, but it's possible so it goes to the extras list")
                continue

            else:
                attempts -=1
                print(f"You have {attempts} attempts left.")

    if attempts == 0:

        print("Game Over!")
        print(f"You guessed {count} words correctly.")
        print("Thanks for playing!")

       
def get_random_words(words_lst):      

    #get a random word from the list (words).

    return random.choice(words_lst)

def hide_parts(word, hide):       

    #hide some alphabets of the word.

    word = list(word)

    indices = list(range(len(word))) 

    #create a list of indices of the word.

    random.shuffle(indices)   

    """shuffle the indices so that we can generate missing places at random sites of the word."""

    for i in indices[0:hide]:

        word[i] = "_"       

        #replace the word with dashes.

    return " ".join(word) 

    #returns the list by converting each letter into one word.

def get_guess():

    #Prompts the user to guess the word.

    while True:
        
        guess = input("Enter your guess: ").strip().lower()

        if guess:
            return guess
        
        else:

            print("Please enter a valid guess!")

def check_guess(your_guess, word):

    #checks if the user's guess is correct or not.

    if your_guess.lower() == word.lower():

        print("Correct!")
        return True
            
    else:

        print("Wrong")
        print("The word was "+ word)
        return False

def other_possible_words(hidden_word, words_lst):

    #This function is used to find other possible words that match the hidden word pattern.

    possible_words = []

    for word in words_lst:

        if len(word) == len(hidden_word):

            match = True

            for j in range(len(hidden_word)):

                if hidden_word[j] != "_" and hidden_word[j] != word[j]:
                    
                    match = False
                    break

            if match:

                possible_words.append(word)

    return len(possible_words) > 0

def read_words_from_file(wordlist): 

    #Reads words from a file and returns a list of words.

    with open (wordlist, 'r') as file:

        all_words = file.read().splitlines()

    return all_words

if __name__ == "__main__":

    main()