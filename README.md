### Build a function
```
def double_gaussian(x, y):
    return exp(-(x**2 + y**2))
```

### Build an Integrate object
```
integral = Integrate(double_gaussian)
```

### Calculate the integral
```
result = integral.double_integral([[-500, 500], [-500, 500]], precision=3)
```

### Show the result and the accuracy
```
print("The result is", result)
```

### Calculate the error range
```
print("\nThe accuracy of this result is", integral.error)
```