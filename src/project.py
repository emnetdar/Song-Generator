
import sys

def main():

    chosen_album = ask_question()
    print(f"Your album is {chosen_album}! Thanks for participating!")

def ask_question():

    input1 = input("Hello there! Wanna know what album I'd give you? (yes/no): ").lower()

    if input1 == "yes":
        print(f"Yay! Here's your first question.")
    elif input1 == "no":
        print(f"Aw, okay. Byebye!")
        return
    else:
        input(f"Sorry, I didn't catch that. Would you like to know what album I'd give you? (Y/N): ")

    question_bank = ["What's your favorite color?", "Do you like cats? (yes/no)", "Do you like the arts? (yes/no)"]
    user_score = 0

    input2 = input(f"{question_bank[0]}: ").lower()

    if input2 == "red" or "yellow":
        print(f"Oh, that's one of my favorites too! Here's the next one.")
        user_score += 1
    if input2 == "orange" or "blue":
        print(f"Not my fave, but I get the appeal hehe. Next one!")
        user_score += 1
    if input2 == "green" or "purple":
        print(f"Ew... Moving on.")
        user_score += 0
    else:
        input("Sorry, I don't know that one. Maybe try something basic?: ")

    input3 = input(f"{question_bank[1]}: ").lower()

    if input3 == "yes":
        print("Me too! I'm glad we think alike :D. Last one, last one!!")
        user_score += 1
    elif input3 == "no":
        print("Aw. I'd ask why not but I don't really care. Last one!")
        user_score += 1
    else:
        input("Dang, could you try that again? I didn't understand that.: ")

    input4 = input(f"{question_bank[2]}: ").lower()

    if input4 == "yes":
        print("Yay, I was hoping it was a yes! Okay, time to decide what to give you!")
        user_score += 1
    if input4 == "no":
        print("That's weird, but whatever! Time to make a decision.")
        user_score += 0
    else:
        input("Sorry, try again one more time?: ")

    return

    
def determine_album(user_score, album_bank):

    album_bank = ["Songs in the Key of Life by Stevie Wonder", "Falsettos (2016 Broadway Cast Recording) by William Finn", 
                "Songs about Jane by Maroon 5", "I Know I'm Funny Haha by Faye Webster"]

    if user_score == 3:
        chosen_album = album_bank[1]
    if user_score == 2:
        chosen_album = album_bank[0]
    if user_score == 1:
        chosen_album = album_bank[2]
    if user_score == 0:
        chosen_album = album_bank[3]

if __name__ == "__main__":
    main()