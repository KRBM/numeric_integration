import numpy as np


def two_var(f, s):
    def g(x):
        return f(x, s)
    return g


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
        self.error = ""

    def integrate(self, lower, upper, precision=1000):
        number_of_points = (upper - lower) * precision
        xs = list(np.linspace(lower, upper, int(number_of_points)))
        integral = 0
        super_sum = 0
        sub_sum = 0
        for index in range(len(xs) - 1):
            delta = xs[index + 1] - xs[index]
            try:
                last = xs[index]
                y1 = self.function(xs[index])
                sub_area = y1 * delta
                last = xs[index + 1]
                y2 = self.function(xs[index + 1])
                super_area = y2 * delta

                area = (y2 + y1) / 2 * delta
                integral += area
                sub_sum += sub_area
                super_sum += super_area
            except ZeroDivisionError:
                print(f"\nAvoided pole at {last}\n")

        error = super_sum - sub_sum
        self.error = f"{integral - error} < integral < {integral + error}\n"
        return integral

    def double_integral(self, limit_list, precision=500):
        x_list, y_list = limit_list
        a, b = x_list
        c, d = y_list
        x_points = (b - a) * precision
        y_points = (d - c) * precision
        xs = list(np.linspace(a, b, int(x_points)))
        ys = list(np.linspace(c, d, int(y_points)))
        integral = 0
        sub_sum = 0
        super_sum = 0
        for i in range(len(xs) - 1):
            delta_x = xs[i + 1] - xs[i]
            for j in range(len(ys) - 1):
                delta_y = ys[j + 1] - ys[j]

                delta = delta_x * delta_y
                try:
                    last = (xs[i], ys[j])
                    f1 = self.function(xs[i], ys[j])
                    sub_area = f1 * delta
                    last = (xs[i + 1], ys[j + 1])
                    f2 = self.function(xs[i + 1], ys[j + 1])
                    super_area = f2 * delta

                    area = (f2 + f1) / 2 * delta
                    integral += area
                    sub_sum += sub_area
                    super_sum += super_area
                except ZeroDivisionError:
                    print(f"\nAvoided pole at {last}\n")

        error = super_sum - sub_sum
        self.error = f"{integral - error} < integral < {integral + error}\n"
        return integral


if __name__ == "__main__":

    def double(x, y):
        return x * y**2

    integrate = Integrate(double)
    result = integrate.double_integral([[0, 3], [1, 2]])
    print(result)