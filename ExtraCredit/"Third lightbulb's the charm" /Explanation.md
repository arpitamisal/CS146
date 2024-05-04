Solutions:

1. Recursively: Time Comp is O(2^n) where first we have the base cases where given the function fib(int N) if N == 0 then return 0, and if N == 1 then return 1, then return fib(N-1) + fib(N-2);
2. Iteratively: Where first we have the base cases where given the function fib(int N) if N == 0 then return 0, and if N == 1 then return 1. Then have values a = 0 and b = 1, while (N > 1) have int sum = a + b; and the b = sum; and then N - - ; TIME COMP is O(n)
