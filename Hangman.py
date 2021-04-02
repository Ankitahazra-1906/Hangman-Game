import random
def Hangman():
    words_list=["education","computer","history","engineering","classroom","friends","gossip","college","tiffin","dance","state","minister","house","clothes","morning","calendar","footpath","cellphone","kolkata","photoframe"]
    word=random.choice(words_list)
    turns=10
    user_guess=""
    valid_characters=set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        actual_word=""
        for letter in word:
            if letter in user_guess:
                actual_word=actual_word+letter
            else:
                actual_word=actual_word + " - "
        if actual_word==word:
            print(f"{word}\n Congratulations you won!")
            break
        print(f"You can guess the word {actual_word}")
        guess=input()
        if guess in valid_characters:
            user_guess=user_guess+guess
        else:
            print("Enter a valid character")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("Only 9 turns are left")
                print("---------------")
            if turns==8:
                print("Only 8 turns are left")
                print("---------------")
                print("       O       ")
            if turns==7:
                print("Only 7 turns are left")
                print("---------------")
                print("       O       ")
                print("       |       ")
            if turns==6:
                print("Only 6 turns are left")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      /        ")
            if turns==5:
                print("Only 5 turns are left")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      / \      ")
            if turns==4:
                print("Only 4 turns are left")
                print("---------------")
                print("      \O       ")
                print("       |       ")
                print("      / \       ")
            if turns==3:
                print("Only 3 turns are left")
                print("---------------")
                print("      \O/       ")
                print("       |       ")
                print("      / \       ")
            if turns==2:
                print("Only 2 turns are left")
                print("---------------")
                print("      \O/ |      ")
                print("       |       ")
                print("      / \       ")
            if turns==1:
                print("Only 1 turn is left")
                print("---------------")
                print("      \O/_|      ")
                print("       |       ")
                print("      / \       ")
            if turns==0:
                print("\n You loose! You couldn't guess the word ! So your man is hanged")
                print("---------------")
                print("       O _|     ")
                print("      /|\       ")
                print("      / \       ")
name=input("Enter your name: ")
print(f"Welcome {name} to the game of Hangman")
Hangman()