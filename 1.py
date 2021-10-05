N = int(input("количество мест в 1-м ряду кинотеатра: "))
K = int(input("порядковый номер проданного билета: "))

oddStep = N
evenStep = N + 1

isOdd = True
sum = 0
step = 0

while sum < K:
    step += 1
    if isOdd:
        isOdd = False
        sum += oddStep
    else:
        isOdd = True
        sum += evenStep

print(step)
if isOdd:
    print(K - (sum-oddStep))
else:
    print(K - (sum-evenStep))
