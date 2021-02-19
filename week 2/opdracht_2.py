"""
General Info:
    Alex Remstedt
    https://secure.ans-delft.nl/universities/1/courses/63457/assignments/144684/quiz/show/37991336
    Week 2 - Opdracht 2 - Schroefloze boot - Interpolatie
\
Opdracht beschrijving:
    We gaan verder met de simulatie van de schoefloze boot en de volgende gegevens:

    x(0)    |   0 m         \n
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
"""
# Imports
from opdracht_1 import Kinetics
import numpy as np


opdracht2 = Kinetics(v0=4.5, mass=105)

print(np.interp(opdracht2.numeric_position(), 3000, opdracht2.))
