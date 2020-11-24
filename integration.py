import numpy as np
from numpy import sin, pi, exp
from tqdm import tqdm


class IntegrationError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return self.message
        return "Custom Error"


class Integrate:
    def __init__(self, function):
        self.function = function
        self.error = 0
        self.sign = 1

    def integral(self, lower, upper, precision=10000):
        if lower > upper:
            lower, upper = upper, lower
            self.sign = -1
        number_of_points = (upper - lower) * precision
        xs = np.linspace(lower, upper, int(number_of_points))
        integral = 0
        super_sum = 0
        sub_sum = 0
        for index in tqdm(range(len(xs) - 1)):
            delta = xs[index + 1] - xs[index]
            try:
                y1 = self.function(xs[index])
                sub_area = y1 * delta
                y2 = self.function(xs[index + 1])
                super_area = y2 * delta

                area = (y2 + y1) / 2 * delta
                integral += area
                sub_sum += sub_area
                super_sum += super_area
            except ZeroDivisionError:
                print(f"\nAvoided pole")

        self.error = super_sum - sub_sum
        return self.sign * integral

    def double_integral(self, limit_list, precision=500):
        if type(limit_list) != list:
            raise IntegrationError("The bounds must be given as a list of lists")
        x_list, y_list = limit_list
        (a, b), (c, d) = x_list, y_list
        x_points, y_points = (b - a) * precision, (d - c) * precision
        xs, ys = np.linspace(a, b, int(x_points)), np.linspace(c, d, int(y_points))
        integral = 0
        sub_sum = 0
        super_sum = 0
        for i in tqdm(range(len(xs) - 1)):
            delta_x = xs[i + 1] - xs[i]
            for j in range(len(ys) - 1):
                delta_y = ys[j + 1] - ys[j]
                delta = delta_x * delta_y
                try:
                    f1 = self.function(xs[i], ys[j])
                    sub_area = f1 * delta
                    f2 = self.function(xs[i + 1], ys[j + 1])
                    super_area = f2 * delta

                    area = (f2 + f1) / 2 * delta
                    integral += area
                    sub_sum += sub_area
                    super_sum += super_area
                except ZeroDivisionError:
                    print(f"\nAvoided pole\n")

        self.error = super_sum - sub_sum
        return integral


if __name__ == "__main__":

    def double_gaussian(x, y):
        return exp(-(x ** 2 + y ** 2))


    # Build an Integrate object
    integral = Integrate(double_gaussian)

    # Calculate the integral
    result = integral.double_integral([[-500, 500], [-500, 500]], precision=3)

    # Show the result and the accuracy
    print("The result is", result)

    # Calculate the error range
    print("\nThe accuracy of this result is", integral.error)