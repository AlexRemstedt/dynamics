# -*- Coding: UTF-8 -*-
"""
General Info:
    Alex Remstedt
    https://secure.ans-delft.nl/universities/1/courses/63457/assignments/144684/quiz/show/37991336
    Week 2 - Opdracht 3 - Een Grotere Boot
\
Opdracht bescrijving:
    Laten we nu naar een andere (grotere) boot kijken. Deze versnelt niet, maar heeft een initiële snelheid en zal
    afremmen door de weerstand van het water. Deze boot komt ook voor in een vak van Maritieme Techniek, en daarom
    laten we ook zien hoe het blokdiagram van dat vak aansluit bij de numerieke integratie die we hier doen.
\
    In de rechter figuur zie je een blokdiagram. In dit diagram staan de dynamische vergelijkingen van de boot
    schematisch weergegeven. De vergelijkingen kunnen hier eenvoudig uitgehaald worden:

    1) Linksboven: Som van de krachten De neerwaartse pijl die uit het +-teken komt heeft de totale som van de krachten
        op de boot F_prop - F_ship, waar F_ship eigenlijk de weerstandskracht op het ship betekent. De vergelijking
        die hier weergegeven is is:

    2) Rechtsboven: Snelheidsafhankelijke weerstandskracht Het blok “Ship Resistance” kan simpelweg een
        vermenigvuldigingsfactor zijn waarbij de uitgaande pijl F_ship gelijk is aan de inkomende pijl (snelheid v_s)
        maal een constante weerstandsfactor. Als dit het geval zou zijn noemen we dit “Lineaire demping”. In de opgave
        vandaag zal de weerstand echter niet-linear afhangen van de snelheid. Dit is niet te zien in het blokkenschema,
        maar de formule is als volgt: F_ship = 1000 * v_s^3

    3) Links midden: De wet van Newton Het blok links in het midden kan ook gezien worden als een soort
        vermenigvuldiging. Letterlijk staat er "neem de inkomende pijl (som van de krachten), vermenigvuldig dit met 1/m
        en integreer dit over de tijd om de uitgaande pijl te krijgen (v_s). De vergelijkingen hiervoor zijn dus:
        a = 1/m * F_tot en v_s = integrate(a*dt)
\
    Deze set vergelijkingen is bijna exact hetzelfde als wat we in de vorige vragen hebben gebruikt. Het enige verschil
    is dat de kracht nu een functie is van de snelheid, wat dan weer een effect heeft op de versnelling en de snelheid.
    Dit is een “closed loop” zoals te zien in de figuur.
\
    Gebruik de volgende initiële toestand en parameters:

    x0      |       0       [m]     \n
    v0      |       10      [m/s]   \n
    m       |       100000  [kg]    \n
    F_prop  |       0       [N]     \n

Vragen:
    a)

"""
from Kinematics import Kinematics
import numpy as np

opdracht3 = Kinematics(v0=10.0, time=[0, 20], mass=100_000, formula=2)

print(f'a: {opdracht3.numeric_velocity()[-1]}')
print(f'b: {np.interp(x=8, xp=opdracht3.time, fp=opdracht3.numeric_position())}')
