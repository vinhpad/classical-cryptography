def Substitution_encode(mes, dic):
    encodedMes = ""
    for c in mes:
        encodedMes += dic[c]
    return encodedMes

def inverseDict(dic):
    inverseDic = {}
    for x in dic:
        inverseDic[dic[x]] = x
    return inverseDic

def Substitution_decode(mes, dic):
    decodedMes = ""
    for c in mes:
        decodedMes += dic[c]
    return decodedMes

def main():
    dic = {'a':'X', 'b':'N', 'c':'Y', 'd':'A', 'e':'H',
           'f':'P', 'g':'O', 'h':'G', 'i':'Z', 'j':'Q',
           'k':'W', 'l':'B', 'm':'T', 'n':'S', 'o':'F',
           'p':'L', 'q':'R', 'r':'C', 's':'V', 't':'M',
           'u':'U', 'v':'E', 'w':'K', 'x':'J', 'y':'D', 'z':'I'}
    inverseDic = inverseDict(dic)
    print(inverseDic)
    X = 'MGZVYZLGHCMHJMYXSSFMNHAHYCDLMHA'
    print(Substitution_decode(X, inverseDic))

# main()