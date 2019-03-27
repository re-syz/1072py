"""
131072
170318
107-2 Python HW1
3030



"""


# =============

import math

score = float(input())

new_score = math.sqrt(score) * 10

compare = int(round(new_score - score, 0))

print("Original: " + "%.2f" % score)
print("Adjusted: " + "%.2f" % new_score + "(+" + str(compare) + ")")
