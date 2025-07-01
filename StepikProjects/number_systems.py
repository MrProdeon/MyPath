def BOH(n):
    return bin(digit), oct(digit), hex(digit)


digit = int(input())

a, b, c = BOH(digit)
print(a[2:], b[2:], c[2:].upper(), sep="\n")
