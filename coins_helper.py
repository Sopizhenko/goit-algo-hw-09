import timeit

def find_coins_greedy(amount):
	coins = [50, 25, 10, 5, 2, 1]
	result = {}
	
	for coin in coins:
		if amount >= coin:
			count = amount // coin
			amount -= count * coin
			result[coin] = count
	
	return result

def find_min_coins(amount):
	coins = [50, 25, 10, 5, 2, 1]
	# Ініціалізація таблиці dp, де dp[i] зберігає мінімальну кількість монет для суми i
	dp = [float('inf')] * (amount + 1)
	dp[0] = 0
	
	# Ініціалізація таблиці track для відслідковування монет
	track = [-1] * (amount + 1)
	
	# Заповнення таблиці dp
	for coin in coins:
		for i in range(coin, amount + 1):
			if dp[i - coin] + 1 < dp[i]:
				dp[i] = dp[i - coin] + 1
				track[i] = coin
	
	# Формування результату
	result = {}
	while amount > 0:
		coin = track[amount]
		if coin not in result:
			result[coin] = 0
		result[coin] += 1
		amount -= coin
	
	return result


if __name__ == '__main__':
	amount = 113
	print(find_coins_greedy(amount))
	print(find_min_coins(amount))

	# Вимірювання часу виконання
	print(timeit.timeit('find_coins_greedy(10000)', globals=globals(), number=500))
	print(timeit.timeit('find_min_coins(10000)', globals=globals(), number=500))
