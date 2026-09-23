# minimum_coins_for_amount

minimum_coins_for_amount(coin_values, target_amount) FUNCTION
Return the fewest coins that sum to target_amount, or -1 if impossible.
REMEMBER fewest[a] = 1 + min(fewest[a - coin]) over every coin that fits. fewest[0] = 0; everything else starts at infinity.
WHEN TO USE Coin systems where greedy fails (coins [1,3,4], amount 6: greedy 4+1+1 = 3 coins, DP 3+3 = 2 coins).
AVOID WHEN Canonical systems like real currencies (greedy is enough).
REQUIRES Positive integer coin values, unlimited supply of each.
TIME O(amount × number of coins). SPACE O(amount).
USED FOR Change-making, "minimum steps" problems, unbounded knapsack.
def minimum_coins_for_amount(coin_values, target_amount):
infinity = float("inf")
fewest_coins_for_amount = [0] + [infinity] * target_amount
for amount in range(1, target_amount + 1):
for coin_value in coin_values:
if coin_value <= amount:
coins_using_this_coin = fewest_coins_for_amount[amount - coin_value] + 1
if coins_using_this_coin < fewest_coins_for_amount[amount]:
fewest_coins_for_amount[amount] = coins_using_this_coin
if fewest_coins_for_amount[target_amount] == infinity:
return -1
return fewest_coins_for_amount[target_amount]
INPUT minimum_coins_for_amount([1, 3, 4], 6) # 3 + 3 (greedy would use 4 + 1 + 1)
OUTPUT 2
INPUT minimum_coins_for_amount([2], 3) # impossible
OUTPUT -1
IN PRODUCTION No standard routine: this DP is the usual production answer. Integer-programming solvers (scipy.optimize.milp)
handle larger or constrained variants.
CS Algorithms Toolkit Dynamic programming
56
