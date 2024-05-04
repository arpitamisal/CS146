dp[0]`is initialized to 0 since no coins are needed to make the amount 0.
All other indices in`dp` are initialized to a value greater than the maximum amount to signify that they are initially unreachable.

Dynamic Programming
For each coin, update the dp array to reflect the minimum coins needed if that coin is used.
For each possible amount, the value is updated to the minimum of its current value or the value of `amount - coin` plus one (indicating the addition of that coin).

If `dp[amount]` is greater than `amount`, it means it is not possible to get the amount with the available coins, hence return -1.
Otherwise, `dp[amount]` gives the minimum coins needed.
