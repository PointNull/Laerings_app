from tkinter import *
import random


#Make Tk window
root = Tk()

#Open Tk window
root.geometry('500x500')

resultInput = Text(root, height = 5, width = 52)


#først skal vi have vores funktioner 
def addition():
    rnum1 = random.randint(0, 9)
    rnum2 = random.randint(0, 9)
    equation = f"{rnum1} + {rnum2}"
    right_answer = rnum1 + rnum2
    return equation, right_answer

def subtraktion():
    rnum3 = random.randint(0, 9)
    rnum4 = random.randint(1, rnum3)
    equation = f"{rnum3} - {rnum4}"
    right_answer = rnum3 - rnum4
    return equation, right_answer

#denne funktion er med til at trække regnestykker for øvrige funktioner og viser dem nede i terminalen
#derudover har den også en indbygget exit funktion
def main():
    while True:
        operation = input("Vælg matematik (plus/minus) eller 'exit' for at afslutte: ").lower()

        if operation == "exit":
            print("Exiting the program. Farvel!")
            break

        if operation == "plus":
            equation, right_answer = addition()
        elif operation == "minus":
            equation, right_answer = subtraktion()
        else:
            print("Ugyldig valg. Vælg enten 'plus', 'minus', eller 'exit'.")
            continue  # Go back to the start of the loop if the input is invalid

        user_Answer = int(input(f"Løs ligningen: {equation} = "))

        if user_Answer == right_answer:
            print("Korrekt!")
        else:
            print(f"Forkert. Det korrekte svar er {right_answer}.")

if __name__ == "__main__":
    main()


root.mainloop()

