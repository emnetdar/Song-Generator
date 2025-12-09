
import sys

def main():

    question_bank = ["What's your favorite color?", "Do you like cats? (yes/no)", "Do you like the arts? (yes/no)"]
    album_bank = ["Songs in the Key of Life by Stevie Wonder", "Falsettos (2016 Broadway Cast Recording) by William Finn", 
                "Songs about Jane by Maroon 5", "I Know I'm Funny Haha by Faye Webster"]
    user_score = 0

    input1 = input("Hello there! Wanna know what album I'd give you? (yes/no): ").lower()

    if input1 == "yes":
        print(f"Yay! Here's your first question.")
    if input1 == "no":
        print(f"Aw, okay. Byebye!")
        sys.exit
    else:
        input(f"Sorry, I didn't catch that. Would you like to know what album I'd give you? (Y/N): ")

    input2 = input(f"{question_bank[0]}: ").lower()

    if input2 == "red" or "yellow":
        print(f"Oh, that's one of my favorites too! Here's the next one.")
        user_score += 1
    if input2 == "orange" or "blue":
        print(f"Not my fave, but I get the appeal hehe. Next one!")
        user_score += 2
    if input2 == "green" or "purple":
        print(f"Ew... Moving on.")
        user_score += 0
    else:
        input("Sorry, I don't know that one. Maybe try something basic?: ")

    input3 = input(f"{question_bank[1:2]}: ").lower()

    if input3 == "yes":
        print("Me too! I'm glad we think alike :D. Last one, last one!!")
        user_score += 1
    if input3 == "no":
        print("Aw. I'd ask why not but I don't really care. Last one!")
        user_score += 0
    else:
        input("Dang, could you try that again? I didn't understand that.")







if __name__ == "__main__":
    main()