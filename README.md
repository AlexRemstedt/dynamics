# Dynamics
De Python code behorend bij het vak Dynamica. 

## Week 1
In week 1 is er vooral veel aandacht besteed aan numeriek integreren:
```python
for i in range(len(time) - 1):
    v[i + 1] = v[i] + a[i] * dt
    s[i + 1] = s[i] + v[i] * dt
```

## Week 2
In week 2 komt ook de `np.interp` meekijken.