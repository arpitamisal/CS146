from typing import List


# Recursive Approach
def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    original_color = image[sr][sc]
    if original_color == color:
        return image

    def dfs(r, c):
        if image[r][c] == original_color:
            image[r][c] = color
            if r >= 1:
                dfs(r - 1, c)
            if r + 1 < len(image):
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < len(image[0]):
                dfs(r, c + 1)

    dfs(sr, sc)
    return image


# Iterative Approach
from typing import List
from collections import deque


def floodFill(
    image: List[List[int]], sr: int, sc: int, newColor: int
) -> List[List[int]]:
    original_color = image[sr][sc]
    if original_color == newColor:
        return image

    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])

    while queue:
        r, c = queue.popleft()
        if image[r][c] == original_color:
            image[r][c] = newColor
            if r >= 1:
                queue.append((r - 1, c))
            if r + 1 < rows:
                queue.append((r + 1, c))
            if c >= 1:
                queue.append((r, c - 1))
            if c + 1 < cols:
                queue.append((r, c + 1))

    return image
