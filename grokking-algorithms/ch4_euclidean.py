def gcd(a=0, b=0):
    """
    Greatest common divisor
    """
    if a == 0 or a == b:
        return b
    if b == 0:
        return a
    if a < b:
        a = a + b
        b = a - b
        a = a - b
    mod = a % b
    if mod != 0:
        return gcd(b, mod)
    return b

if __name__ == "__main__":
    a = 270
    b = 192
    result = gcd(a,b)
    print(result)