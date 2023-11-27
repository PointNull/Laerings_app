import tkinter as tk
from tkinter import simpledialog, messagebox
from abc import ABC, abstractmethod
import random

# Define an abstract class for commands (kopiret fra tkinter opgave med knap)
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# klasse som har metoden for at lave additions regnestykker
class StartAddition(Command):
    @staticmethod
    def execute():
        rnum1 = random.randint(0, 9)
        rnum2 = random.randint(0, 9)
        equation = f"{rnum1} + {rnum2}"
        right_answer = rnum1 + rnum2
        return equation, right_answer

# klasse som har metoden for at lave subtraktions regnestykker
class StartSubtraktion(Command):
    @staticmethod
    def execute():
        rnum3 = random.randint(0, 9)
        rnum4 = random.randint(1, rnum3) # det anden nummer er sat til "rnum3" for at vi ikke får et regne stykke som giver minus
        equation = f"{rnum3} - {rnum4}"
        right_answer = rnum3 - rnum4
        return equation, right_answer

# Frame klassen for matematik læringssiden
class MathLearningPage(tk.Frame):
    def __init__(self, root, controller):
        tk.Frame.__init__(self, root, bg="SkyBlue1")

        # Lav en container frame for at centrere
        center_frame = tk.Frame(self, bg="SkyBlue1")
        center_frame.pack(expand=False)

        self.controller = controller  # Opbevar en reference til controlleren

        # tekst som viser regnestykke og om man svarer rigtigt eller forkert
        self.label = tk.Label(center_frame, text="", font=('Arial', 16), height=3, width=30, bg="SkyBlue1")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        # tekstfelt hvor man kan skrive sit svar
        self.answer_entry = tk.Entry(center_frame, font=('Arial', 14))
        self.answer_entry.grid(row=1, column=0, padx=10, pady=10)
    
    

        # Knap til at indsende svar
        self.submit_button = tk.Button(center_frame, text="Submit", command=self.check_answer, font=('Arial', 14))
        self.submit_button.grid(row=2, column=0, padx=10, pady=10)

        # Knap til at gå tilbage til hoved menu
        self.backButton = tk.Button(center_frame, text="Back to Main Menu", command=self.back_to_main_menu, font=('Arial', 14))
        self.backButton.grid(row=3, column=0, padx=10, pady=10)
        
            

    # Metode til at starte et additions regnestykke
    def start_addition(self):
        equation, right_answer = StartAddition.execute()
        self.label.config(text=f"Solve the equation: {equation}", fg="black")
        self.right_answer = right_answer

    # Metode til at starte et subtraktions regnestykke
    def start_subtraktion(self):
        equation, right_answer = StartSubtraktion.execute()
        self.label.config(text=f"Solve the equation: {equation}", fg="black")
        self.right_answer = right_answer

    # Metode til at tjekke brugerens svar
    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = int(user_answer)
            if user_answer == self.right_answer:
                self.label.config(text="Rigtigt!", fg="green")
            else:
                self.label.config(text=f"Desværre forkert. Svaret er: {self.right_answer}.", fg="red")
        except ValueError:
            self.label.config(text="Dette er ikke et nummer", fg="red")

    # Metode til at gå tilbage til hoved menu
    def back_to_main_menu(self):
        self.controller.show_page(self.controller.menu)
        self.answer_entry.delete(0, 'end')
        

# Frame klasse til hoved menuen
class Mat_menu(tk.Frame):
    def __init__(self, root, controller):
        tk.Frame.__init__(self, root, bg="SkyBlue1")
        self.controller = controller  # Opbevar en reference til controlleren
        self.topButtons()

    # Metode til at lave knapper, som starter addition og subtraktion
    def topButtons(self):
        # Knap til at starte addition
        self.additionButton = tk.Button(self, text="Start Addition", background="WHITE", height=2, width=16, command=self.start_addition, font=('Arial', 14))
        self.additionButton.pack(pady=10)

        # Knap til at starte subtraktion
        self.subtraktionButton = tk.Button(self, text="Start Subtraktion", background="WHITE", height=2, width=16, command=self.start_subtraktion, font=('Arial', 14))
        self.subtraktionButton.pack(pady=10)

    # Metode til at starte et additions regnestykke
    def start_addition(self):
        self.controller.show_page(self.controller.mathLearningPage)
        self.controller.mathLearningPage.start_addition()

    # Metode til at start et subtraktions regnestykke
    def start_subtraktion(self):
        self.controller.show_page(self.controller.mathLearningPage)
        self.controller.mathLearningPage.start_subtraktion()

# Klasse til at kontrollere flowet af programmet
class Controller(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root, bg="SkyBlue1")

        # Lav versioner af hver side
        self.menu = Mat_menu(self, self)
        self.menu.grid(row=0, column=0, sticky='nsew')

        self.mathLearningPage = MathLearningPage(self, self)
        self.mathLearningPage.grid(row=0, column=0, sticky='nsew')

        # Vis menu,(TestOverlap),siden til at starte med
        self.show_page(self.menu)

    # Metode til at vise en specifik side
    def show_page(self, page):
        # Løft den givne side til toppen
        page.tkraise()

# Hoved funktion til at køre programmet
def main():
    root = tk.Tk()
    root.title("Matematik for børn")
    root.geometry('400x260')  # Forstørrede vinduesstørrelsen for et pænere layout
    root.resizable(0,0) #gør lige at vores app ikke kan blive større størrelse da vi ikke har en funktion at tilpasse vores widget i forhol til window size
    root.pack_propagate(0)
    app = Controller(root)
    app.pack(expand=False, fill=tk.BOTH)

    root.mainloop()

# Tjek om scriptet kører som hoved programmet
if __name__ == '__main__':
    main()
