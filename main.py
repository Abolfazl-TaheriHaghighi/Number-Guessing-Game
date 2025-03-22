from random import randint

def Levels():
    while True:
        try:
            level = int(input(f"Select the game level:{"\n"} 1_Easy {"\n"} 2_Medium {"\n"} 3_Hard {"\n"} 4_Customization {"\n"} {"\n"} ************************************************** {"\n"} 5_Help {"\n"} 0_Exit(Close Game) {"\n"} {"\n"}>>"))
            if level in [1 , 2 , 3 , 4 , 5]:
                return level
            elif level == 0 :
                EXit()
        except ValueError:        
             print("Give Me Only One Numbers From :  (1 , 2 , 3 , 4 , 5 , 0)")


def get_number():
    while True:
        try:
           return int(input("Enter the number you think is correct: "))
            
        except ValueError:
            print("Please use only Integers numbers like (..., -3, -2, -1, 0, 1, 2, 3, ...)")

def easy():
    ai = randint(1 , 10)
    for i in range (5):
        number = get_number()
        
        if number > ai :
            print("The number you guessed is bigger than the number chosen by the computer.")
           
        elif number < ai :
            print("The number you guessed is smaller than the number chosen by the computer.")

        elif number == ai:
            print("You did a great job! You won.")
            return
    print(f"Unfortunately, you lost the game. (The number chosen by the computer was: '{ai}' )")

def Medium():
    ai = randint(1 , 50)
    for i in range (10):
        number = get_number()
        
        if number > ai :
            print("The number you guessed is bigger than the number chosen by the computer.")
           
        elif number < ai :
            print("The number you guessed is smaller than the number chosen by the computer.")

        elif number == ai:
            print("You did a great job! You won.")
            return
    print(f"Unfortunately, you lost the game. (The number chosen by the computer was: '{ai}' )")


def Hard():
    ai = randint(1 , 100)
    for i in range (15):
        number = get_number()
        
        if number > ai :
            print("The number you guessed is bigger than the number chosen by the computer.")
           
        elif number < ai :
            print("The number you guessed is smaller than the number chosen by the computer.")

        elif number == ai:
            print("You did a great job! You won.")
            return
    print(f"Unfortunately, you lost the game. (The number chosen by the computer was: '{ai}' )")

              
def Customization():
    while True:
        try:
            Min = int(input("Enter the lower bound: "))
            while True:
                Max = int(input("Enter the upper bound: "))
                if Min >= Max :
                    print("You did not meet the upper and lower bounds, try again.")
                else:
                    break

            while True:
                chances  = int(input("How many chances would you like to have? "))
                if chances <= 0:
                    print("The number of chances cannot be negative or equal to 0, the minimum chance is 1.")
                elif chances > (Max - Min) :
                    print("The number of chances cannot be bigger than the difference between the upper and lower bounds.")
                else:
                    break
            break
        except ValueError:
            print("Please use only Integers numbers like (..., -3, -2, -1, 0, 1, 2, 3, ...)")
    ai = randint(Min , Max)
    for i in range (chances ):
        number = get_number()
        
        if number > ai :
            print("The number you guessed is bigger than the number chosen by the computer.")
           
        elif number < ai :
            print("The number you guessed is smaller than the number chosen by the computer.")

        elif number == ai:
            print("You did a great job! You won.")
            return
    print(f"Unfortunately, you lost the game. (The number chosen by the computer was: '{ai}' )")  


def Help():
    while True:
        print("\nThe rules and usage of this game are very simple!\n")
        print("Game rules at different levels:")
        print("'Easy': I will choose an integer between 1 and 10, and you have 5 chances to find that number.")
        print("'Medium': I will choose an integer between 1 and 50, and you have 10 chances to find that number.")
        print("'Hard': I will choose an integer between 1 and 100, and you have 15 chances to find that number.")
        print("'Customization': You set the lower and upper bounds and decide how many chances you get!\n")
        print("**************************************************")
        print("\nHow can I play?\n")
        print("1. Choose a game level.")
        print("2. Try to guess the secret number within the given attempts.")
        print("3. If your guess is greater than the number, I'll tell you to try a smaller one.")
        print("4. If your guess is smaller, I'll tell you to try a bigger one.")
        print("5. If you find the right number, you win!")
        print("**************************************************")
        
        try:
            x = int(input(f" 0_Exit(Close Game) {"\n"} 1_Back{"\n"} {"\n"}Enter your choice: "))
            if x == 0 :
                EXit()
            if x == 1 :
                return x
        except ValueError:
            print("Give Me Only One Numbers From :  (0 , 1)")

def EXit():
    input("Press 'Enter' to exit.")
    exit()

def Back():
    Maim()

def Maim():
    level = Levels()
    if level == 1 :
        easy()
    elif level == 2:
        Medium()
    elif level == 3:
        Hard()
    elif level == 4:
        Customization()
    elif level == 5:
        y = Help()
        if y == 0:
            EXit()
        elif y == 1:
            Back()
    elif level == 0:
        EXit()

def Loop():
    while True:
        Maim()
        while True:
            x = input("Try Again? (yes or no)")
            y = x.lower()
            if y == "yes":
                break
            elif y == "no":
                EXit()
            else:
                print("You can only answer with yes or no.")
    
Loop()


#Abolfazl Taheri Haghighi
#Bachelor's student of statistics at Fasa University
# v1.0.0