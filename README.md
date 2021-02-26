# Dynamics
De Python code behorend bij het vak Dynamica. 

### Gebruikte Packages:
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/stable/index.html)

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
In week 3 komt het volgende aan bod.
