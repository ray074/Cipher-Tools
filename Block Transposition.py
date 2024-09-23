from itertools import permutations
from trigrams import trigrams


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
    nums = list(range(n))
    perms = permutations(nums)

    return list(perms)


def unshuffle(cipher_text, order, n):
    
    plaintext = ""

    while len(list(plaintext)) != len(list(cipher_text)):
        for num in order:
            try:
                plaintext += cipher_text[num]
            except IndexError:
                pass

        order = [(x + n) for x in order]

    return plaintext


def main():
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    clean = "".join([l for l in input("\nEnter cipher text: ") if l in alpha])
    order4, order5, order6, order7, fitness_list_4, fitness_list_5, fitness_list_6, fitness_list_7 = create_orders(4), create_orders(5), create_orders(6), create_orders(7), [], [], [], []

    for order in order4:
        fitness_list_4.append(fitness(unshuffle(clean, order, 4)))
    
    for order in order5:
        fitness_list_5.append(fitness(unshuffle(clean, order, 5)))
    
    for order in order6:
        fitness_list_6.append(fitness(unshuffle(clean, order, 6)))
    
    for order in order7:
        fitness_list_7.append(fitness(unshuffle(clean, order, 7)))

    fitness_lists = [max(fitness_list_4), max(fitness_list_5), max(fitness_list_6), max(fitness_list_7)]
    highest = find_best(fitness_lists) + 4 # x + 4

    match highest:
        case 4:
            plaintext = unshuffle(clean, order4[find_best(fitness_list_4)], 4)
            num_order = [(x + 1) for x in order4[find_best(fitness_list_4)]]
        case 5:
            plaintext = unshuffle(clean, order5[find_best(fitness_list_5)], 5)
            num_order = [(x + 1) for x in order5[find_best(fitness_list_5)]]
        case 6:
            plaintext = unshuffle(clean, order6[find_best(fitness_list_6)], 6)
            num_order = [(x + 1) for x in order6[find_best(fitness_list_6)]]
        case 7:
            plaintext = unshuffle(clean, order7[find_best(fitness_list_7)], 7)
            num_order = [(x + 1) for x in order7[find_best(fitness_list_7)]]

    print("\n", plaintext, "\n\n", "Order: ", num_order, "\n", sep="")


if __name__ == "__main__":
    main()
