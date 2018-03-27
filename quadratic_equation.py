from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        raise Exception("discriminant < 0, roots will not be real")

    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
    
    
print(get_roots(10, 1, 10))



