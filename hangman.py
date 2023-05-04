HANGMAN_ASCII_ART="""
Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""

MAX_TRIES=6

photos="""
    x-------x

:
    x-------x
    |
    |
    |
    |
    |

:
    x-------x
    |       |
    |       0
    |
    |
    |

:
    x-------x
    |       |
    |       0
    |       |
    |
    |

:
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |

:
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |

:
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
""".split(":")
HANGMAN_PHOTOS={}
key =0
for photo in photos:
    HANGMAN_PHOTOS[key]=photo
    key+=1

def print_hangman(num_of_tries):
    """Prints a hangman drawing based on the number of tries.
       :param num_of_tries: the number of failed attempts
       :type num_of_tries: int
       """
    print(HANGMAN_PHOTOS[num_of_tries])
def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks if the guessed letter is a valid input.
    :param letter_guessed: the letter that the user guessed
    :param old_letters_guessed: list of all previously guessed letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the guessed letter is a valid input, False otherwise
    :rtype: bool
    """
    if(len(letter_guessed)==1 and letter_guessed.isalpha() and
            not letter_guessed.lower() in old_letters_guessed and
            not letter_guessed.upper() in old_letters_guessed):
        return True
    else: return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Updates the list of previously guessed letters if the guess is valid.
        :param letter_guessed: the letter that the user guessed
        :param old_letters_guessed: list of all previously guessed letters
        :type letter_guessed: str
        :type old_letters_guessed: list
        :return: True if the guess was valid and the list of guessed letters was updated, False otherwise
        :rtype: bool
        """
    if(check_valid_input(letter_guessed,old_letters_guessed)):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        for letter in old_letters_guessed[:-1]:
            print(letter,end=" -> ")
        print(old_letters_guessed[-1])
        return False
    old_letters = ['a', 'p', 'c', 'f']
    try_update_letter_guessed('A', old_letters)

def show_hidden_word(secret_word, old_letters_guessed):
    """Constructs a string showing the letters of a secret word that have been guessed correctly and
        hiding the letters that have not been guessed yet.
        :param secret_word: the word to be guessed
        :param old_letters_guessed: a list of letters that have already been guessed
        :type secret_word: str
        :type old_letters_guessed: list
        :return: a string representing the current state of the guessing process
        :rtype: str
        """
    result=""
    for tav in secret_word:
        if (tav in old_letters_guessed):
            result=result+tav+" "
        else: result=result+"_ "
    return result

def check_win(secret_word, old_letters_guessed):
    """Checks if the player has won the game.
       :param secret_word: the word to be guessed
       :param old_letters_guessed: a list of letters that have already been guessed
       :type secret_word: str
       :type old_letters_guessed: list
       :return: True if all the letters in the word have been guessed, False otherwise
       :rtype: bool
       """
    if("_" not in show_hidden_word(secret_word,old_letters_guessed)):
        return True
    else: return False

def choose_word(file_path, index):
    """Returns the number of unique words in the file and the word in the index that got as param from a file.
       :param file_path: the path to the file containing the words
       :param index: an index to use for selecting a word from the file
       :type file_path: str
       :type index: int
       :return: a tuple containing the number of unique words in the file and the selected word
       :rtype: tuple
       """
    file=open(file_path,"r")
    words= file.read().split(" ")
    temp= []
    index = (index - 1) % len(words)
    secret_word =words[index]
    count=0
    for word in words:
        if (word not in temp):
            count+=1
            temp.append(word)
    return count, secret_word

def main():
    print(HANGMAN_ASCII_ART)
    path=input("please enter the words file path: ")
    index=int(input("please enter the secret word index : "))
    secret_word=choose_word(path,index)[1]
    old_letters_guessed=[]
    num_of_tries=0
    while not check_win(secret_word,old_letters_guessed) and num_of_tries<MAX_TRIES:
        print_hangman(num_of_tries)
        print(show_hidden_word(secret_word,old_letters_guessed))
        guessed_letter=input("guess a letter : ")
        while(not try_update_letter_guessed(guessed_letter,old_letters_guessed)):
            guessed_letter=input("try a valid letter, guess a letter! : ")
        if(guessed_letter not in secret_word):
            num_of_tries+=1
            print("):")
    if(check_win(secret_word,old_letters_guessed) and num_of_tries<MAX_TRIES):
        print("WIN")
    if(num_of_tries==MAX_TRIES):
        print_hangman(num_of_tries)
        print("LOSE")
if __name__ == "__main__":
    main()