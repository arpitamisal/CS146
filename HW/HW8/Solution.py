def longestPalindrome(self, s: str) -> int:
    from collections import Counter

    char_count = Counter(s)
    length = 0
    center_added = False

    for count in char_count.values():
        length += (
            count // 2
        ) * 2  # Add the largest even number less than or equal to count
        if count % 2 == 1 and not center_added:
            length += 1  # Add a center character if not added yet
            center_added = True

    return length
