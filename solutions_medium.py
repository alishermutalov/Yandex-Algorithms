#2. Самый дешевый путь
def cheapest_way():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]

    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
    print(dp[n-1][m-1])
    
#cheapest_way()

#3. Вывести маршрут максимальной стоимости
def max_way():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * M for _ in range(N)]
    path = [[None] * M for _ in range(N)]
    
    dp[0][0] = grid[0][0]
    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        path[0][j] = 'R'
    
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        path[i][0] = 'D' 
    
    for i in range(1, N):
        for j in range(1, M):
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j] + grid[i][j]
                path[i][j] = 'D'  
            else:
                dp[i][j] = dp[i][j-1] + grid[i][j]
                path[i][j] = 'R' 
    
    print(dp[N-1][M-1])
    
    result_path = []
    x, y = N-1, M-1
    while x > 0 or y > 0:
        result_path.append(path[x][y])
        if path[x][y] == 'D':
            x -= 1
        else:
            y -= 1
    
    print(' '.join(result_path[::-1]))

#4. Ход конём
def knights_move():
    N, M = map(int, input().split())
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(M):
            if i - 2 >= 0 and j - 1 >= 0:
                dp[i][j] += dp[i-2][j-1]  # (2 Down, 1 right)
            if i - 1 >= 0 and j - 2 >= 0:
                dp[i][j] += dp[i-1][j-2]  # (1 Down, 2 right)

    print(dp[N-1][M-1])

#5. Кафе
def cafe():
    days = int(input())
    expenses = []
    spend_money = 0
    coupon = [] #kupon olgan kuni  kiritiladi
    spend_coupon = [] #kupon ishlatgan kuni kiritiladi
    
    for day in range(1, days+1):
        money = int(input())
        expenses.append([day, money])
        if money>=100: 
            coupon.append(day)
    
    cost_list = [money for day, money in expenses]  
    for i in range(len(expenses)):
        print( expenses[i][1])
        if expenses[i][1] == max(cost_list) and len(coupon)>0 and expenses[i][0]>coupon[0]:
            expenses[i][1] = 0
            coupon.pop(0)
        
    print(expenses, coupon)

cafe()