def charShift(c, k):
    x = ord(c) - ord('a')
    x = (x + k + 26) % 26
    return chr(x + ord('a'))

def ShiftCipher_encode(mes, k):
    encodedMes = ""
    for c in mes:
        encodedMes += charShift(c, k)
    return encodedMes

def ShiftCipher_decode_withKey(mes, k):
    decodedMes = ""
    for c in mes:
        decodedMes += charShift(c, -k)
    return decodedMes

def ShiftCipher_decode(mes):
    #brute force
    possibleRes = []
    for k in range(26):
        possibleRes.append(ShiftCipher_decode_withKey(mes, k))
    return possibleRes

def main():
    X = 'wewillmeetatmidnight'
    print(ShiftCipher_encode(X, 11)) #hphtwwxppelextoytrse
    Y = 'jbcrclqrwcrvnbjenbwrwn'
    print(ShiftCipher_decode(Y)) #astitchintimesavesnine

# main()