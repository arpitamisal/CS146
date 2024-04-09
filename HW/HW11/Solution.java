package HW.HW11;

import java.util.LinkedList;
import java.util.Queue;

// Recursive Approach
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int originalColor = image[sr][sc];
        if (originalColor == color) {
            return image;
        }

        floodFillHelper(image, sr, sc, color, originalColor);
        return image;
    }

    private void floodFillHelper(int[][] image, int sr, int sc, int color, int originalColor) {
        if (sr < 0 || sr >= image.length || sc < 0 || sc >= image[0].length || image[sr][sc] != originalColor) {
            return;
        }

        image[sr][sc] = color;

        floodFillHelper(image, sr - 1, sc, color, originalColor); // up
        floodFillHelper(image, sr + 1, sc, color, originalColor); // down
        floodFillHelper(image, sr, sc - 1, color, originalColor); // left
        floodFillHelper(image, sr, sc + 1, color, originalColor); // right
    }
}

// Iterative Approach
class Solution2 {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int originalColor = image[sr][sc];
        if (originalColor == newColor) {
            return image;
        }

        int rows = image.length, cols = image[0].length;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { sr, sc });

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1];

            if (image[r][c] == originalColor) {
                image[r][c] = newColor;
                if (r >= 1)
                    queue.add(new int[] { r - 1, c });
                if (r + 1 < rows)
                    queue.add(new int[] { r + 1, c });
                if (c >= 1)
                    queue.add(new int[] { r, c - 1 });
                if (c + 1 < cols)
                    queue.add(new int[] { r, c + 1 });
            }
        }

        return image;
    }
}
