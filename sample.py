def solve(n, m):
    candies = input().split()
    if len(candies) > n:
        exit()
    else:
        free.append(candies)
        sum1 = 0
        for k in free[0]:
            sum1 = int(k) + int(sum1)

        divide = sum1 % m
        print(f"Case #{i+1}:",divide)


loop = int(input())

for i in range(loop):
    free = []
    n, m = map(int, input().split())
    solve(n, m)
