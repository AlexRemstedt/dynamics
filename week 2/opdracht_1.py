"""
General Info:
    Alex Remstedt
    https://secure.ans-delft.nl/universities/1/courses/63457/assignments/144684/quiz/show/37991335
    Week 2 - Opdracht 1 - Schroefloze boot
\
Opdracht beschrijving:
    Gebruik één van de bestanden uit de vorige Python opdracht om een simulatie van een boot te maken.
    Net als in die opdracht zullen wij de kracht geven als functie van de tijd en zal jij een numerieke en een
    analytische oplossing bepalen van de beweging als functie van de tijd.
\
    Een schroefloze boot begint met een initiële snelheid van 4.5 m/s en versnelt eenparig. De aandrijfkracht is 11 N,
    en de massa van de boot is 105 kg. Simuleer het pad dat de boot aflegt. Gebruik tijdstappen van 0.1s en een totale
    simulatietijd van 200s.
\
Vragen:
    a) Wat is de versnelling van de boot in [m/s^2]
    b) Wat is het numerieke resultaat voor de snelheid van de boot na t = 154.3 seconden?
    c) Wat is het analytische resultaat voor de positie van de boot na 154.3 seconden?
    d) Vergelijk de analytische en de numerieke oplossingen van de positie van de boot na 154.3 seconden. Wat is de absolute grootte van de fout?
    e) Maak een plot met de snelheid op de verticale as en de positie op de horizontale as. Hoe ziet deze plot eruit?
"""
# Imports
import numpy as np
from matplotlib import pyplot as plt
from Kinematics import Kinematics

opdracht1 = Kinematics(v0=4.5,
                       mass=105,
                       time=[0, 154.3],
                       dt=0.1,
                       formula=1)
# Answers
print(f'a: {opdracht1.analytic_acceleration()[-1]}')
print(f'b: {opdracht1.numeric_velocity()[-1]}')
print(f'c: {opdracht1.analytic_position()[-1]}')
print(f'd: {abs(opdracht1.numeric_position()[-1] - opdracht1.analytic_position()[-1])}')

fig, ax = plt.subplots(1)
plt.plot(opdracht1.numeric_position(), opdracht1.numeric_velocity())  # e
plt.show()
