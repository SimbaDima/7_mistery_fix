from math import sqrt

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    try:
        sqrt(discriminant)
    except ValueError:
        b = 0
        discriminant = 0
#если корни равны (0.0, None) значит дискриминант равен отрицательному числу
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2


print(get_roots(10, 6, 100))



