# Решатель квадратных уравнений

Данный проект способен решать квадратное уравнение.

# Как использовать

Пользователь вводить в функцию параметры квадратного уравнения. а стоит при х^2, b при x, c - это const, если при входных параметрах пользователя discriminant < 0, то выйдет сообщения "values belong no real numbers ", если discriminant >= 0 будут найдена корни квадратного уравнения.
 def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c 
    if discriminant >= 0: #
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        if discriminant == 0:
            return root1, None
        else:
            return root1, root2
    else:
        print("values belong no real numbers ")


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
