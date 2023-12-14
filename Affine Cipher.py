from sympy import mod_inverse

def affineConverter(cipherText, a, b):
    alpha, final = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), []
    
    for letter in list(cipherText):
        if letter in alpha:
            letterVal = alpha.index(letter)
            result = (mod_inverse(a, 26) * (letterVal - b)) % 26
            final.append(alpha[result])
        else:
            final.append(letter)

    plainText = "".join(final)
    return plainText
            
def calculateMostProbable(cipherText):
    alpha, final = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), []
    coprimes = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    letterDistributions = [
      8.55, 1.60, 3.16, 3.87, 12.10, 2.18, 2.09, 4.96, 7.33, 0.22, 0.81, 4.21, 2.53,
      7.17, 7.47, 2.07, 0.10, 6.33, 6.73, 8.94, 2.68, 1.06, 1.83, 0.19, 1.72, 0.11
    ]
    
    for a in coprimes:
        for b in range(26):
            result = affineConverter(cipherText, a, b)
            absDiffs, counts = 0, {}
            
            for letter in alpha:
                value = (result.count(letter) / len(result)) * 100
                counts[letter] = round(value, 4)
            
            for expected, real in zip(letterDistributions, counts.values()):
                absDiffs += abs(expected - real)
                
