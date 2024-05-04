Solutions:

1. Brute Force: Where we sort the characters, and then compare it both the strings. but the fastest sort, quick sort also takes O(n log n ) time.
2. Bucket Array: First remove all space and make it lowercase. Where we keep the count of the characters that appear in the string s and then decrement each char from that array for string s, then if we have a valid anagram the array should return empty. Time COMP will be O(n).
