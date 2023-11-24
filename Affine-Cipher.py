def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def Affine_encode(mes, a, b):
    encodedMes = ""
    for c in mes:
        encodedMes += chr((a * (ord(c)-ord('a')) + b) % 26 + ord('a'))
    return encodedMes

def Affine_decode(mes, a, b):
    tmp1, inverseA, tmp2 = extended_euclid(a, 26)
    if (inverseA < 0): 
        inverseA = (inverseA % 26 + 26) % 26
    decodedMes = ""
    for c in mes:
        decodedMes += chr(inverseA * (ord(c)-ord('a') - b + 26) % 26 + ord('a'))
    return decodedMes

def main():
    X = 'hot'
    Y = Affine_encode(X, 7, 3)
    print(Y)
    Z = Affine_decode(Y, 7, 3)
    print(Z)

# main()