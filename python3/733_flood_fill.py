# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# class Solution01:
#     def floodFill(self, image, sr, sc, newColor):
#         """
#         :type image: List[List[int]]
#         :type sr: int
#         :type sc: int
#         :type newColor: int
#         :rtype: List[List[int]]
#         """
#         def dfs(x, y, prevColor):
#             # base case
#             if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
#                 return
#             currColor = image[x][y]
#
#             # end condition
#             if currColor != prevColor or currColor == newColor:
#                 return
#
#             image[x][y] = newColor
#             dfs(x-1, y, prevColor)
#             dfs(x, y-1, prevColor)
#             dfs(x, y+1, prevColor)
#             dfs(x+1, y, prevColor)
#
#         dfs(sr, sc, image[sr][sc])
#
#         return image


class Solution02:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        R, C = len(image), len(image[0])
        color = image[sr][sc]

        if color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r-1, c)
                if r+1 < R:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r, c-1)
                if c+1 < C:
                    dfs(r, c+1)

        dfs(sr, sc)

        return image

if __name__ == "__main__":
    image = [[0, 0, 1],
            [1, 1, 0],
            [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2

    print(Solution02().floodFill(image, sr, sc, newColor))
