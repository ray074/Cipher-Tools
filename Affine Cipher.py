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
            
def calculateMostProbabln zip(letterDistributions, counts.values()):
                absDiffs += abs(expected - real)
                
            final.append(absDiffs)
            
    minIndex = final.index(min(final))
    aValue = coprimes[minIndex // 26]
    bValue = minIndex % 26
    
    return (affineConverter(cipherText, aValue, bValue), aValue, bValue)
            

def main():
    cipherText = input("Enter text encrypted with an Affine Cipher: ").upper()
    plainText, a, b, = calculateMostProbable(cipherText)
    print(f"\n Plaintext: \n\n {plainText} \n\n A VALUE: {a} \n B VALUE: {b} \n\n")
    
    searching = True
    while searching:
        v
