def fibonacci(num: int):
    if num <= 1:
        return num

    return fibonacci(num - 1) + fibonacci(num-2)

def memoziation(num: int, cache):
    print(f'num begin: {num}')
    if num <= 1:
        return num

    if num in cache:
        print(f'num: {num}')
        return cache[num]

    cache[num] = memoziation(num-1, cache) + memoziation(num-2, cache)
    print(f'num, cache: {num}, {cache[num]}')

    return cache[num]

def dp(num: int):
    if num < 2:
        return num

    dp = [0, 1]
    i = 2

    #we are replacing in place
    while i <= num:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1

    return dp[1] 







if __name__ == "__main__":
    num = 15

    #print(fibonacci(14))
    #print(fibonacci(13))

    num = 5
    memoziation(num, {})
    print(dp(5))