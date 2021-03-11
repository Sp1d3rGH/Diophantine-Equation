def Euclid(a, b): # Нахождение НОД алгоритмом Евклида
    if a != 0 and b != 0:
        a, b = max(a,b), min(a,b)
        while a % b != 0:
            a, b = b, a % b
        return abs(b)

def Bezout(a, b): # Нахождение частного решения уравнения ax + by = (НОД(a, b)) соотношением Безу
    if b == 0:
        return 1, 0
    y, x = Bezout(b, a % b)
    return x, y - (a // b) * x

print("Решение диофантова уравнения вида Ax + By = C.\nВведите через пробел значения A, B и C.")
A, B, C = map(int, input().split())
if A != 0 and B != 0 and C != 0:
    gcd = Euclid(A, B)
    if C % gcd == 0: # Проверка существования целочисленных решений
        a, b, c = A // gcd, B // gcd, C // gcd
        x1, y1 = Bezout(a, b)
        x, y = c * x1, c * y1
        if B // gcd > 0:
            print("x = " + str(x) + " - " + str(B // gcd) + " * k, где k - любое целое число")
        else:
            print("x = " + str(x) + " + " + str(abs(B // gcd)) + " * k, где k - любое целое число")
        if A // gcd > 0:
            print("y = " + str(y) + " + " + str(A // gcd) + " * k, где k - любое целое число")
        else:
            print("y = " + str(y) + " - " + str(abs(A // gcd)) + " * k, где k - любое целое число")
    else:
        print("Не существует целочисленных решений.")

#---------Другие случаи----------
elif A == 0 and B != 0 and C != 0:
    print("x - любое")
    if C % B == 0:
        print("y = " + str(C//B))
    else:
        print("y = " + str(C) + " / " + str(B))
elif A != 0 and B == 0 and C != 0:
    if C % A == 0:
        print("x = " + str(C//A))
    else:
        print("x = " + str(C) + " / " + str(A))
    print("y - любое")
elif (A != 0 and B != 0) and C == 0:
    if A % B == 0:
        print("y = " + str(int(-(A / B))) + "x, где x - любое")
    else:
        print("y = -(" + str(A) + " / " + str(B) + ") * x, где x - любое")
elif A == 0 and B != 0 and C == 0:
    print("x - любое\ny = 0")
elif A != 0 and B == 0 and C == 0:
        print("x = 0\ny - любое")
elif A == 0 and B == 0 and C == 0:
    print("x - любое\ny - любое")
elif A == 0 and B == 0 and C != 0:
    print("Решений нет")