def check_number(num):
    return num % 3 == 0


def find_first(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            continue

        if check_number(i):
            print("Found:", i)
            break


n = int(input("Enter the limit: "))
result = find_first(n)
print(result)
