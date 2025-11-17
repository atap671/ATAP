# 1
def max_path_sum(triangle):
    """
    Знаходить максимальну суму шляху від вершини до основи
    у трикутнику чисел (динамічне програмування).
    """
    if not triangle:
        return 0

    # Створюємо копію трикутника для динамічного програмування
    dp = [row[:] for row in triangle]
    
    # Рухаємося від передостаннього рядка до вершини
    for i in range(len(dp) - 2, -1, -1):
        for j in range(len(dp[i])):
            # Оновлюємо значення: поточне число + максимум із двох сусідів знизу
            dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])
            
    # Результат у вершині
    return dp[0][0]

# Приклад використання #1
triangle_example = [
     [2],
    [3, 4],
   [6, 5, 7],
  [4, 1, 8, 3]
]
result1 = max_path_sum(triangle_example)
print(result1) 


# 2
def bell_number(n):
    """
    Обчислює n-те число Белла B_n, використовуючи трикутник Белла.
    """
    if n == 0:
        return 1
    
    # Трикутник Белла: dp[i][j] - елементи трикутника
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Ініціалізація: B_0 = 1
    dp[0][0] = 1

    for i in range(1, n + 1):
        # 1. Початок нового рядка
        dp[i][0] = dp[i-1][i-1]
        
        # 2. Обчислення інших елементів
        for j in range(1, i + 1):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    # n-те число Белла B_n = dp[n][0]
    return dp[n][0]

# Приклад використання #2 (B_5 = 52)
n_bell = 5
result2 = bell_number(n_bell)
print(result2)
