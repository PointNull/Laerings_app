# Python learning application

## Formål
Vi vil gerne lave et matematikprogram med meget basal matematik (addition og subtraktion). Appen er lavet til små børn som er startet i indskoling (5-7-årige) som skal lære basal matematik. Vi forsøger at gøre matematik sjovt for børn ved at sætte dem foran en skærm så det kan virke som et computerspil. Programmet er taget af inspiration af Matematikfessor som også leverer tilfældige regnestykker inden for bestemt sværhedsgrad og emne.

## Design mønster
Command struktur: Vi opretter en ”Command” klasse som bruges til at opbevare en masse grundlæggende commands som ”StartAddition” og ”StartSubtraktion”. For at vi kan bruge de grundlæggende commands skal vi have en invoker.

Her er vores ”Command” klasse.
```python

from  abc  import  ABC, abstractmethod
import  random

// #Define an abstract class for commands (kopiret fra tkinter opgave med knap)
class  Command(ABC):
	@abstractmethod
	def  execute(self):
		pass

```

Dette er vores grundlæggende commands ”StartAddition” og ”StartSubtraktion”.
```python
class  StartAddition(Command):
	@staticmethod
	def  execute():
		rnum1 = random.randint(0, 9)
		rnum2 = random.randint(0, 9)
		equation = f"{rnum1} + {rnum2}"
		right_answer = rnum1 + rnum2
		return  equation, right_answer

//# klasse som har metoden for at lave subtraktions regnestykker
class  StartSubtraktion(Command):
	@staticmethod
	def  execute():
		rnum3 = random.randint(0, 9)
		rnum4 = random.randint(1, rnum3) # det anden nummer er sat til "rnum3" for at vi ikke får et regne stykke som giver minus
		equation = f"{rnum3} - {rnum4}"
		right_answer = rnum3 - rnum4
		return  equation, right_answer

```

Vores grundlæggende commands i eksemplet laver regnestykkerne.  



Dette er invokeren i programmet
````python
class  Mat_menu(tk.Frame):
	def  __init__(self, root, controller):
	tk.Frame.__init__(self, root, bg="SkyBlue1")
	self.controller = controller  # Opbevar en reference til controlleren
	self.topButtons()

//# Metode til at lave knapper, som starter addition og subtraktion
def  topButtons(self):
	//# Knap til at starte addition
	self.additionButton = tk.Button(self, text="Start Addition", 			background="WHITE", height=2, width=16, command=self.start_addition, font=('Arial', 14))
	self.additionButton.pack(pady=10)

//# Knap til at starte subtraktion
	self.subtraktionButton = tk.Button(self, text="Start Subtraktion", background="WHITE", height=2, width=16, command=self.start_subtraktion, font=('Arial', 14))
	self.subtraktionButton.pack(pady=10)

//# Metode til at starte et additions regnestykke
def  start_addition(self):
	self.controller.show_page(self.controller.mathLearningPage)
	self.controller.mathLearningPage.start_addition()

//# Metode til at start et subtraktions regnestykke
def  start_subtraktion(self):
	self.controller.show_page(self.controller.mathLearningPage)
	self.controller.mathLearningPage.start_subtraktion()
````
Invokeren kan vi se som en chef og de grundlæggende commands er to arbejdere. Chefen kan ikke udføre opgaverne som arbejderne kan, så chefen får opgaven og giver den til arbejderen hvis job det er. Dette kunne være at lave et additionsregnestykke.

## Udviklingsprocessen
Først skrev vi vores ide ned sådan at vi kunne lægge en plan for hvordan vi ville arbejde. Vi opdelte det på den måde at David startede med at arbejde på GUI imens William arbejde på at lave en funktion som kunne fremstille tilfældige matematik regnestykker inden for addition og subtraktion. Da vi havde fået matematikfunktionen til at fungere begyndte William også at lave på GUI. Efter David have fået knapperne til at virke begyndte begge at arbejde på hvordan vi kunne lave en ny frame hvor matematikken skulle vises. Efter at have opstillet en frame til matematikken lavede, satte vi det hele sammen og lavede nogle små rettelser til udseendet og endte ud med det endelige program.

## Brugergrænseflade
Vi har valgt en meget simpel brugergrænseflade. Man har valget mellem 2 knapper hvor muligheder leder dig til at skulle lave regnestykker med addition eller subtraktion. Når man kommer ind på en frame med matematik, så har vi tekst hvor vores regnestykker står og et inputfelt under hvor man kan skrive sit svar. Vi har også implementeret en knap som går tilbage til hovedmenuen. Man kan nok godt kalde vores GUI meget simpel, men vi har også haft fokus på funktionaliteten.

## Testing
| Test iteration | Plan og testing                                                             | Resultat                                                                                                               |
| -------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 1.0            | Få matematik funktion til at køre                                           | Vi fik to funktion til at lave addition og subtraktions regnestykker som kunne besvares nede i terminalen              |
| 2.0            | Lave en tekstbox og knapper                                                 | Vi fik knapper og tekstfelt ind i vores root.                                                                          |
| 3.0            | Lave en ny frame til matematik                                              | Vi kiggede på nettet og fandt noget inspiration til hvordan man lave en ny frame                                       |
| 4.0            | Få tekstbox og knapper til at virke med matematikken                        | Efter at have sat vores widget ind i vores matematik frame fik vi det hele til at arbejde sammen så programmet virkede |
| 5.0            | Finpudsning af program så tekst bliver slettet efter man er trykket videre. | Nu efter man har skrevet et svar og man er trykket ind på et nyt regnestykke bliver svaret resetted                    |


## kilder til inspiration

