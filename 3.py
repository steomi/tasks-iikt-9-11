T = str(input("ключ шифрования: "))
S = str(input("строка S: "))
N = int(input("количество повторений строки S: "))

stroka = ""
for i in range(0, N):
    stroka += S

isChiper = False
count = 0
k = 0

for i in range(0, len(stroka)):
    if stroka[i] == T[0] and (len(stroka) - i >= len(T)):
        isChiper = True

    if isChiper:
        for j in range(0, len(T)):
            if stroka[i+j] == T[j]:
                k += 1
        if k == len(T):
            count += 1

        k = 0
        isChiper = False

print(count)
