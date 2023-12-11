def caesarSolver(cipherText, shift):
    cipherText = cipherText.upper()
    cipherCopy = list(cipherText);
    alpha = {chr(i + 65): i + 1 for i in range(26)}
    rev, res, inc = {k: v for v, k in alpha.items()}, [], 0

    for i in range(len(cipherText)):
        if cipherText[i] in alpha.keys():
            letter = cipherText[i]
            num1 = alpha[letter]
            num2 = num1 + shift
            while num2 > 26:
                num2 -= 26
            res.append(rev[num2])

    for j in range(len(cipherCopy)):
        if cipherCopy[j] in alpha.keys():
            cipherCopy[j] = res[inc]
            inc += 1

    return "".join(cipherCopy)


def diffs(cipher):
    
    distributions = [
      8.55, 1.60, 3.16, 3.87, 12.10, 2.18, 2.09, 4.96, 7.33, 0.22, 0.81, 4.21, 2.53,
      7.17, 7.47, 2.07, 0.10, 6.33, 6.73, 8.94, 2.68, 1.06, 1.83, 0.19, 1.72, 0.11
    ]
    
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    counts, diff = {}, 0
    length = len([l for l in cipher if l in alpha])

    for letter in alpha:
        value = cipher.count(letter) / length
        value *= 100
        counts[letter] = round(value, 8)
       
    for expected, real in zip(distributions, counts.values()):
        diff += abs(expected - real)
        
    return diff
 

def main():
    final, absDiffs = [], []
    cipherText = input("Enter text encrypted with a Caesar Cypher: \n\n")

    for shift in range(1, 26):
        final.append([caesarSolver(cipherText, shift)])

    for cipher in final:
        absDiffs.append(diffs("".join(cipher)))
    
    print(f"\nSHIFT: {absDiffs.index(min(absDiffs)) + 1}")
    print("\n", caesarSolver(cipherText, absDiffs.index(min(absDiffs)) + 1), "\n")
    
    check = input("Check other Shifts? (y/n) ").lower()
    if check == "n" or check == "no":
        return
    else:
        for cipher in final:
            print()
            print(cipher)


if __name__ == "__main__":
    main()
