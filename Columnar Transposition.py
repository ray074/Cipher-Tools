from itertools import permutations
from trigrams import trigrams

def clean(text):
    text = text.upper()
    global alpha
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    final = "".join([l for l in list(text) if l in alpha])
    return final


def find_best(arr):
    return (arr.index(max(arr)))


def fitness(clean_text):
    final_score = 0
    try:
        for i in range(0, len(clean_text), 3):
            final_score += trigrams[clean_text[i:i+3]]
    except KeyError:
        pass
    
    return final_score


def create_orders(n):
    nums = list(range(1, n+1))
    perms = permutations(nums)

    return list(perms)


def unshuffle(cleaned, key):
    value = int(len(cleaned) / len(key))
    split = []
    final = []
    plaintext = ""

    for i in range(0, len(cleaned), value):
        split.append(list(cleaned[i:i+value]))

    for num in key:
        final.append(split[num-1])

    for j in range(len(final[0])):
        for i in range(len(final)):
            plaintext += final[i][j]

    return plaintext


def main():
    cipher_text = input("\nEnter cipher text: ").upper()
    cleaned = clean(cipher_text)
    order4, order4_plaintexts, order4_fitness = create_orders(4), [], []
    order5, order5_plaintexts, order5_fitness = create_orders(5), [], []
    order6, order6_plaintexts, order6_fitness = create_orders(6), [], []
    order7, order7_plaintexts, order7_fitness = create_orders(7), [], []
    order8, order8_plaintexts, order8_fitness = create_orders(8), [], []
    # order9, order9_plaintexts, order9_fitness = create_orders(9), [], []
    
    for order in order4:
        order4_plaintexts.append(unshuffle(cleaned, order))

    for order in order5:
        order5_plaintexts.append(unshuffle(cleaned, order))

    for order in order6:
        order6_plaintexts.append(unshuffle(cleaned, order))
    
    for order in order7:
        order7_plaintexts.append(unshuffle(cleaned, order))

    for order in order8:
        order8_plaintexts.append(unshuffle(cleaned, order))
 
    # for order in order9:
    #     order9_plaintexts.append(unshuffle(cleaned, order))
    
    for text in order4_plaintexts:
        order4_fitness.append(fitness(text))

    for text in order5_plaintexts:
        order5_fitness.append(fitness(text))

    for text in order6_plaintexts:
        order6_fitness.append(fitness(text))

    for text in order7_plaintexts:
        order7_fitness.append(fitness(text))

    for text in order8_plaintexts:
        order8_fitness.append(fitness(text))

    # for text in order9_plaintexts:
    #     order9_fitness.append(fitness(text))
    
    max_fitness_list = [order4_fitness[find_best(order4_fitness)], 
                        order5_fitness[find_best(order5_fitness)],
                        order6_fitness[find_best(order6_fitness)],
                        order7_fitness[find_best(order7_fitness)],
                        order8_fitness[find_best(order8_fitness)]]
                        
                        # order9_fitness[find_best(order9_fitness)]]

    optimum_order = find_best(max_fitness_list) + 4

    match optimum_order:
        case 4:
            print()
            print(order4_plaintexts[find_best(order4_fitness)])
            print()
            print(order4[find_best(order4_fitness)])
        case 5:
            print()
            print(order5_plaintexts[find_best(order5_fitness)])
            print()
            print(order5[find_best(order5_fitness)])
        case 6:
            print()
            print(order6_plaintexts[find_best(order6_fitness)])
            print()
            print(order6[find_best(order6_fitness)])
        case 7:
            print()
            print(order7_plaintexts[find_best(order7_fitness)])
            print()
            print(order7[find_best(order7_fitness)])
        case 8:
            print()
            print(order8_plaintexts[find_best(order8_fitness)])
            print()
            print(order8[find_best(order8_fitness)])
        
        
        # case 9:
        #     print(order9_plaintexts[find_best(order9_fitness)])


if __name__ == "__main__":
    main()


# fix for monogram analysis for this and block
# fix 9