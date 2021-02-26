# Dynamics
De Python code behorend bij het vak Dynamica. 

## [Week 1](week 1)
In week 1 is er vooral veel aandacht besteed aan numeriek integreren:
```python
for i in range(len(time) - 1):
    v[i + 1] = v[i] + a[i] * dt
    s[i + 1] = s[i] + v[i] * dt
```

## [Week 2](week 2)
In komt ook de `np.interp` meekijken, dit helpt bij het zoeken vn bijvoorbeel de tijd die hoort bij een bepaalde positie. Ik heb voor deze week een class structure gemaakt, waarbij Kinematics de integraties vooral doet en ForceFormula de krachten.
