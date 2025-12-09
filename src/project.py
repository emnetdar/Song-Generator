
import sys

def main():

    chosen_album = determine_album()
    print(f"Your album is {str(chosen_album)}! Thanks for participating!")

def ask_question():

    input1 = input("Hello there! Wanna know what album I'd give you? (yes/no): ").lower()

    if input1 == "yes":
        print(f"Yay! Here's your first question.")
    elif input1 == "no":
        print(f"Too bad! Here's the first question.")
    else:
        print("Sorry, I didn't catch that. Let's start over.")
        sys.exit()

    question_bank = ["What's your favorite color?", "Do you like cats? (yes/no)", "Do you like the arts? (yes/no)"]
    user_score = 0

    input2 = input(f"{question_bank[0]}: ").lower()

    if input2 == "red":
        print(f"Oh, that's one of my favorites too! Here's the next one.")
        user_score += 1
    elif input2 == "yellow":
        print(f"Oh, that's one of my favorites too! Here's the next one.")
        user_score += 1
    elif input2 == "orange":
        print(f"Not my fave, but I get the appeal hehe. Next one!")
        user_score += 1
    elif input2 == "blue":
        print(f"Not my fave, but I get the appeal hehe. Next one!")
        user_score += 1
    elif input2 == "green":
        print(f"Ew... Moving on.")
        user_score += 0
    elif input2 == "purple":
        print(f"Ew... Moving on.")
        user_score += 0
    else:
        print("Sorry, I don't know that one. No mistakes!")
        sys.exit()

    input3 = input(f"{question_bank[1]}: ").lower()

    if input3 == "yes":
        print("Me too! I'm glad we think alike :D. Last one, last one!!")
        user_score += 1
    elif input3 == "no":
        print("Aw. I'd ask why not but I don't really care. Last one!")
        user_score += 1
    else:
        print("Dang, a mistake? Once again!")
        sys.exit()

    input4 = input(f"{question_bank[2]}: ").lower()

    if input4 == "yes":
        print("Yay, I was hoping it was a yes! Okay, time to decide what to give you!")
        user_score += 1
    elif input4 == "no":
        print("That's weird, but whatever! Time to make a decision.")
        user_score += 0
    else:
        print("Messing it up right at the end? Try again.")
        sys.exit()

    return

def determine_album():

    album_bank = ["Songs in the Key of Life by Stevie Wonder", "Falsettos (2016 Broadway Cast Recording) by William Finn", 
                "Songs about Jane by Maroon 5", "I Know I'm Funny Haha by Faye Webster"]

    user_score = ask_question()

    if user_score == 3:
        chosen_album = album_bank[1].strip()
        return chosen_album
    elif user_score == 2:
        chosen_album = album_bank[0].strip()
        return chosen_album
    elif user_score == 1:
        chosen_album = album_bank[2].strip()
        return chosen_album
    elif user_score == 0:
        chosen_album = album_bank[3].strip()
        return chosen_album

if __name__ == "__main__":
    main()