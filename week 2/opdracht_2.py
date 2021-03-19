"""
General Info:
    Alex Remstedt
    https://secure.ans-delft.nl/universities/1/courses/63457/assignments/144684/quiz/show/37991336
    Week 2 - Opdracht 2 - Schroefloze boot - Interpolatie
\
Opdracht beschrijving:
    We gaan verder met de simulatie van de schoefloze boot en de volgende gegevens:

    coordinate(0)    |   0 m         \n
    v(0)	|   4.5 m/s     \n
    P	    |   11 N        \n
    m	    |   105 kg      \n
    dt	    |   0.1 s       \n
\
    Gebruik bij de volgende opgaven de functie np.interp uit numpy om de snelheid op een specifieke afstand te vinden
    of om een afstand bij een specifieke snelheid te vinden. Als je niet (meer) weet hoe deze functie werkt kan je dit
    online opzoeken in de documentatie van numpy.
\
Vragen:
    a) Wat is de numerieke waarde van de snelheid van de boot bij de derde boei (3000 m)?
    b) Hoe lang duurde het voordat de boot de tweede boei (2000 m) bereikte? Gebruik hiervoor ook de numerieke oplossing.
    c) Bereken de snelheid van de boot bij de derde boei (3000 m) en bereken de afwijking tussen de analytische en de numerieke oplossing. Wat is de absolute grootte van deze fout?
"""
# Imports
from Kinematics import Kinematics
import numpy as np

opdracht2 = Kinematics(v0=4.5, mass=105, formula=1)

a = np.interp(x=3000, xp=opdracht2.numeric_position(), fp=opdracht2.numeric_velocity())
b = np.interp(x=2000, xp=opdracht2.numeric_position(), fp=opdracht2.time)
c = abs(a - 25.47608589)

# Prints
print(f'a: {a}')
print(f'b: {b}')
print('{0:.20f}'.format(c))
