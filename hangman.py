import random
def hangman():
    list_of_words=["india","hangman","laptop","eduyear"]
    word=random.choice(list_of_words)
    turns=10
    guessmade=""
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    while(turns>=0):
        mainword=""
        for letter in word:
            if letter in guessmade:
                mainword+=letter
            else:
                mainword+="_"
        if mainword==word:
            print(mainword)
            print("CONGRATULATIONS!!YOU WON!!")
            break
        print("Guess the word ",mainword)
        guess=input()
        if guess in valid_entry:
            if guess in guessmade:
                print("you have already guessed that letter try another letter")
                guess=input()
            else:
                guessmade+=guess
        else:
            print("please enter a valid character")
            guess=input()
        if guess not in word:
            turns-=1
            if turns==9:
                print("9 turns left!!")
                print("--------------")
            elif turns==8:
                print("8 turns left!!")
                print("--------------")
                print("       O      ")
            elif turns==7:
                print("7 turns left!!")
                print("--------------")
                print("       O      ")
                print("       |      ")
            elif turns==6:
                print("6 turns left!!")
                print("--------------")
                print("       O      ")
                print("       |      ")
                print(r"      /      ")
            elif turns==5:
                print("5 turns left!!")
                print("--------------")
                print("       O      ")
                print("       |      ")
                print(r"      / \     ")
            elif turns==4:
                print("4 turns left!!")
                print("--------------")
                print(r"      \O      ")
                print("       |       ")
                print(r"      / \     ")
            elif turns==3:
                print("3 turns left!!")
                print("--------------")
                print(r"      \O/      ")
                print("       |       ")
                print(r"      / \     ")
            elif turns==2:
                print("2 turns left!!")
                print("--------------")
                print(r"      \O/ |    ")
                print("       |       ")
                print(r"      / \     ")
            elif turns==1:
                print("only 1 turn left!! The HANGMAN is on his last breath!!")
                print("--------------")
                print(r"      \O/_|    ")
                print("       |       ")
                print(r"      / \     ")
            elif turns==0:
                print("You lose")
                print("You let a goodman Die")
                print("--------------")
name=input("ENTER YOUR NAME-> ")
print(f"Welcome {name}!!")
print("------------------------")
print("try to guess the word in less than 10 attempts")
print("GOOD LUCK!!")
hangman()
