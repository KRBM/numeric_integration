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
error_range = float(integral.error.split()[-1]) - float(integral.error.split()[0])
print(f"\nThe accuracy of this result is\n{integral.error} which gives us an error range of +- {error_range}")
```