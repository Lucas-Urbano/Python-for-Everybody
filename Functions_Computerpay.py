def computepay(h, r):
    if h > 40:
        p = ((h - 40) * (r * 1.5)) + (40 * r)
    if h <= 40:
        p = (h * r)
    print('Pay',p)
    return p


h = float(input("Enter Hours:"))
r = float(input("Enter rate/hour:"))

computepay(h, r)