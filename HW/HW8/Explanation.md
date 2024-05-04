Count Character Frequencies:
Count how many times each character appears in the string. This can be efficiently done using a hash map where keys are characters, and values are their respective counts.

Calculate Maximum Palindrome Length:
A palindrome has a symmetrical structure, so pairs of characters can be placed on either side of the palindrome. For every character that appears an even number of times, all of those instances can be part of the palindrome.
Characters that appear an odd number of times can also contribute to the palindrome length by using count - 1 characters (to make it even), and potentially one of those characters (if not already used) can be used as the center of the palindrome.
