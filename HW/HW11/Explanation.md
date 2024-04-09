We can perform a flood fill by altering the color of a starting pixel and then continue to alter the color of adjacent pixels that share the original color. To solve this problem, I followed this logic:
If the color of the starting pixel image[sr][sc] is already the target color, return the image as no change is needed.
Save the original color of the starting pixel to identify which pixels need to be changed.
Define a recursive function that:

    Changes the color of the current pixel to the target color.
    Looks at the four adjacent pixels (up, down, left, right).
    Recursively calls itself for any adjacent pixels that have the original color.

Invoke the recursive function starting from the provided pixel 'image[sr][sc]'.
