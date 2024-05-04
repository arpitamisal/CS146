package HW.HW8;

public class Solution {
    public int longestPalindrome(String s) {
        int[] charCounts = new int[128]; // ASCII size for all upper and lower case letters
        for (char c : s.toCharArray()) {
            charCounts[c]++;
        }

        int length = 0;
        boolean centerAdded = false;
        for (int count : charCounts) {
            length += (count / 2) * 2;
            if (count % 2 == 1 && !centerAdded) {
                length += 1;
                centerAdded = true;
            }
        }
        return length;
    }

}
