# Dynamics
De Python code behorend bij het vak Dynamica. 

### Gebruikte Packages:
- [NumPy](https://numpy.org/)
- [MatPlotLib](https://matplotlib.org/stable/index.html)
- [SciPy](https://www.scipy.org/)

## [Week 1](https://github.com/AlexRemstedt/dynamics/tree/master/week%201)
In week 1 is er vooral veel aandacht besteed aan numeriek integreren:

```python
for i in range(len(time) - 1):
    v[i + 1] = v[i] + a[i] * dt
    s[i + 1] = s[i] + v[i] * dt
```

## [Week 2](https://github.com/AlexRemstedt/dynamics/tree/master/week%202)
In week 2 komt ook de `np.interp` meekijken, dit helpt bij het zoeken vn bijvoorbeel de tijd die hoort bij een bepaalde positie. Ik heb voor deze week een class structure gemaakt, waarbij Kinematics de integraties vooral doet en ForceFormula de krachten. De laatste opdracht van week 3 is er een extra moeilijkheidsgraad toegevoegd, want de kracht hangt nu af van de snelheid, waardoor een extra loop ontstaat.

## [Week 3](https://github.com/AlexRemstedt/dynamics/tree/master/week%203)
In week 3 worden er functies gegeven aan ons, die er zo uitzien:

```python
def afgeleiden(state, t):
    y = state[0]
    v = state[1]
    a = g
    return [v, a]
```

```python
def numeriek(t, begin_y, begin_v):
    y_num = np.full(len(t), begin_y)
    v_num = np.full(len(t), begin_v)
    for n in range(len(t) - 1):
        dt = t[n + 1] - t[n]
        snelheid, versnelling = afgeleiden([y_num[n], v_num[n]], t[n])
        y_num[n + 1] = y_num[n] + snelheid * dt
        v_num[n + 1] = v_num[n] + versnelling * dt
    return y_num, v_num

```

Voor opdracht 2 moet er een oscilerende beweging ontstaan. Dit wordt gedaan door `a = -omega_n ** 2 * y`, waarbij `omega_n = np.sqrt(k/m)`.

## [Week 4](https://github.com/AlexRemstedt/dynamics/tree/master/week%204)
In week 4 word er meer gekeken naar H15 met Energie en impuls (linear momentum)

## [Week 5](https://github.com/AlexRemstedt/dynamics/tree/master/week%205)
Week 5 opdracht 1: Modelleren van verschillende slingers.

Deze set opgaven bestaat uit zes opgaven die grotendeels hetzelfde zijn. Alleen de berekening van het traagheidsmoment verschilt. Werk de eerste net uit, dan zouden de andere vijf redelijk snel moeten gaan.

Na [opdracht 5](https://github.com/AlexRemstedt/dynamics/blob/master/week%205/opdracht_4.py) blijft de code vrijwel hetzelfde alleen verandert het traagheidsmoment `i` en `i_o`.

## [Week 6](https://github.com/AlexRemstedt/dynamics/tree/master/week%206)
Week 6 is niet heel lastig, na het kijken van de colleges + wat inspiratie uit het boek, valt opdracht 1 behoorlijk mee. Om het mezelf wat makkelijker te maken heb ik [converter.py](https://github.com/AlexRemstedt/dynamics/blob/master/converter.py) toegevoegd. 

Het is belangrijk om duidelijk verschil te houden tussen wat volgens het normale assenstelsel gaat en wat via de gedraaide. Bij opdracht 2 wordt de kracht constant parallel gehouden, dit maakt de hoekversnelling makkelijker, maar de lineaire versnelling lastiger.

## Useful References
- [Maritieme Techniek Discord Server](https://discord.gg/gc8EsQxTcu)
- [Werktuigbouwkunde Discord Server](https://discord.gg/gc8EsQxTcu)
