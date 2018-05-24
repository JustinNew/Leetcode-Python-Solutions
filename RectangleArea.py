# 223. Rectangle Area

# Sort all x and pick the middle two to get the overlap x-axis.
# Do the same for y-axis overlap.
# Get the area of two rectangle and minus the overlap area.

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        area = (C - A) * (D - B) + (G - E) * (H - F)

        # x-axis overlap
        x_a = [("A", A), ("C", C), ("E", E), ("G", G)]
        x_a.sort(key=lambda x: x[1])

        if x_a[1][0] == "C" and x_a[2][0] == "E":
            x_length = 0
        elif x_a[1][0] == "G" and x_a[2][0] == "A":
            x_length = 0
        else:
            x_length = x_a[2][1] - x_a[1][1]

        # y-axis overlap
        y_a = [("B", B), ("D", D), ("F", F), ("H", H)]
        y_a.sort(key=lambda x: x[1])
        
        if y_a[1][0] == "D" and y_a[2][0] == "F":
            y_length = 0
        elif y_a[1][0] == "H" and y_a[2][0] == "B":
            y_length = 0
        else:
            y_length = y_a[2][1] - y_a[1][1]  

        area -= x_length * y_length

        return area      
