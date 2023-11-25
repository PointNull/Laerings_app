import tkinter as tk
from tkinter import font as tkfont
from abc import ABC, abstractmethod
import random


#Make Tk window
root = tk.Tk()

#Open Tk window
root.geometry('500x500')
root.resizable(True, True)

#titel på program (kan ses øverst)
root.title('Matematik for børn')

#knap til at vælge addition
knap_plus = tk.Button(root, text="addition", bd = '10')
knap_plus.pack(expand= tk.FALSE, fill= tk.X, side= tk.LEFT)



#knap til at vælge subtraktion
knap_minus = tk.Button(root, text="subtraktion", bd = '10')
knap_minus.pack(expand= tk.FALSE, fill= tk.X, side= tk.RIGHT)



#tekstfelt til svar
#resultInput = Text(root, height = 5, width = 52)
textbox = tk.Text(root, height = 5, width = 20)
textbox.pack(padx = 30, pady = 30)

root.mainloop()

#mat_addition = start_addition()
#mat_subtraktion = start_subtraktion()

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

#først skal vi have vores funktioner 
class start_addition(Command):
    def addition():
        rnum1 = random.randint(0, 9)
        rnum2 = random.randint(0, 9)
        equation = f"{rnum1} + {rnum2}"
        right_answer = rnum1 + rnum2
        return equation, right_answer

class start_subtraktion(Command):
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