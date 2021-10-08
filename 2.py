def is_correct(x, y):
    if (max(x, X) - min(x, X)) == (max(y, Y) - min(y, Y)):
        return True
    else:
        return False

result = ""
X = int(input())
Y = int(input())

if X == Y:
    print(0)
else:
    x = 0
    y = 0

    for i in range(0, 100000):
        x += 1
        y += 1

        cond = is_correct(x, y)

        if cond:
            result = str(x) + " " + str(y)
            break

if len(result) > 1:
    print("1" + result)
else:
    print("-1")
