import random
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


def return_most_probable_list(clean_text):
    freq_dict = {}
    for letter in alpha:
        freq_dict[letter] = ((list(clean_text).count(letter)) / len(clean_text)) * 100

    sorted_letters = sorted(freq_dict, key=freq_dict.get, reverse=True)
    return sorted_letters


def create_starting_point(clean_text):
    clean_text = list(clean_text)
    freqs = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'G', 'P', 'W', 'Y', 'B', 'V', 'K', 'J', 'X', 'Z', 'Q']
    most_probable_list = return_most_probable_list(clean_text)
    new = []

    for i in range(len(clean_text)):
        new += freqs[most_probable_list.index(clean_text[i])]

    return "".join(new)


def main():
    cipher_text = input("\nEnter cipher text: ")
    cleaned = clean(cipher_text)
    
    original = create_starting_point(cleaned)
    original_fitness = fitness(original)
    
    start = create_starting_point(cleaned)
    start_fitness, n = fitness(start), 0
    start = list(start)

    add, temp, temp_fitness = [], [], []

    final, final_fitness_list = [], []

    for _ in range(10):
        while n < 50:
            random_letter = alpha[random.randint(0, 25)]
            for letter in alpha:
                for i in range(len(start)):
                    if start[i] == random_letter:
                        add.append(letter)
                    elif start[i] == letter:
                        add.append(random_letter)
                    else:
                        add.append(start[i])        

                temp.append("".join(add))
                temp_fitness.append(fitness("".join(add)))
                
                add.clear()

            optimal = temp[find_best(temp_fitness)]

            if fitness(optimal) > start_fitness:
                start = list(optimal)
                start_fitness = fitness(optimal)
                n = 0

            else:
                n += 1

            temp.clear()
            temp_fitness.clear()

        plain_text = "".join(start)
        final.append(plain_text)

        start = original
        start_fitness = original_fitness
        n = 0

    for text in final:
        final_fitness_list.append(fitness(text))

    best = final[find_best(final_fitness_list)]
    print(f"\n{best}\n")


if __name__ == "__main__":
    main()
