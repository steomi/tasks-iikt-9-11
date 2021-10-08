def pos_sum(arr):
    sum = 0
    for el in arr:
        if el > 0:
            sum += el
        else:
            sum += el * (-1)
    return sum


N = int(input())
M = int(input())


pos_trains = []
neg_trains = []
for i in range(1, M + 1):
    train = int(input())
    pos_trains.append(train)
for i in range(1, N + 1):
    train = int(input())
    neg_trains.append(train)

minSum = pos_sum(pos_trains) + pos_sum(neg_trains)
t = 0
for i in range(1, 10**5):
    for k in range(0, len(neg_trains)):
        neg_trains[k] += 1
    for k in range(0, len(pos_trains)):
        pos_trains[k] -= 1

    currentSum = pos_sum(pos_trains) + pos_sum(neg_trains)

    if minSum > currentSum:
        minSum = currentSum
        t = i

print(t)
