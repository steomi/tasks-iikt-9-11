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

k = 1
if x < 0 and y > 0:
    k += 1
elif x < 0 and y > 0:
    k += 1
elif x > 0 and y < 0:
    k += 1
elif x<0 and y < 0:
    k += 2

if len(result) > 1:
    print(str(k) + " " + str(result))
else:
    print("-1")
