#Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

def diff21(n):
    if n > 21:
        return abs(21 - n) * 2
    else:
        return 21 - n
diff21(10)
print(diff21(10))

