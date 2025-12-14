import numpy as np


def f_value(x):
    return (x - 0.3)**2
    #return (1/3) * x**3 + (4/3) * x**2 - 3
    #return np.sin(x**3 + x**2+x)


def dihotomia(eps, a, b):
    step = 0
    f_calc = 0

    while abs(b - a) >= eps:
        x1 = (a + b) / 2 + eps / 2
        x2 = (a + b) / 2 - eps / 2
        f1 = f_value(x1)
        f2 = f_value(x2)

        if f1 > f2:
            b = x2
        else:
            a = x1

        step += 1
        f_calc += 2

    print("Метод дихотомии:")
    print(f"f_calc = {f_calc}")
    
    if f1 < f2:
        print(f"min = {x1:.4f}\n")
    else:
        print(f"min = {x2:.4f}\n")


def golden_ratio(eps, a, b):
    phi = (np.sqrt(5) - 1) / 2

    step = 0
    f_calc = 0

    x1 = b - phi * (b - a)
    x2 = a + phi * (b - a)

    f1 = f_value(x1)
    f2 = f_value(x2)
    f_calc += 2

    while abs(b - a) >= eps:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - phi * (b - a)
            f1 = f_value(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + phi * (b - a)
            f2 = f_value(x2)

        step += 1
        f_calc += 1

    print("Метод золотого сечения:")
    print(f"f_calc = {f_calc}")
    print(f"min = {((a + b) / 2):.4f}\n")

def fibonacci_method(eps, a, b):
    F = [1, 1]
    while F[-1] < (b - a) / eps:
        F.append(F[-1] + F[-2])

    N = len(F)     
    f_calc = 0
    k = 0           

    x1 = a + F[N-3] / F[N-1] * (b - a)
    x2 = a + F[N-2] / F[N-1] * (b - a)

    f1 = f_value(x1)
    f2 = f_value(x2)
    f_calc += 2

    while k < N - 3:      
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1

            x1 = a + F[N-k-4] / F[N-k-2] * (b - a)
            f1 = f_value(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2

            x2 = a + F[N-k-3] / F[N-k-2] * (b - a)
            f2 = f_value(x2)

        k += 1
        f_calc += 1

    print("Метод Фибоначчи:")
    print(f"f_calc = {f_calc}")
    print(f"min = {((a + b) / 2):.4f}\n")




def main():
    eps = 0.001
    a, b = -2, 1
    
    print(f"Epsilon = {eps}, a, b = [{a},{b}]")
    dihotomia(eps, a, b)
    golden_ratio(eps, a, b)
    fibonacci_method(eps, a, b)


if __name__ == "__main__":
    main()
