%matplotlib qt #Jupyter command to open graph in a new window

import matplotlib.pyplot as plt
import numpy as np


def plotFrequencies(extractFrequencies):
    barWidth = 0.35
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    xIndexes = np.arange(len(letters))

    standardFrequencies = [
        8.55, 1.60, 3.16, 3.87, 12.10, 2.18, 2.09, 4.96, 7.33, 0.22, 0.81, 4.21, 2.53,
        7.17, 7.47, 2.07, 0.10, 6.33, 6.73, 8.94, 2.68, 1.06, 1.83, 0.19, 1.72, 0.11
    ]

    titleFont = {"fontname":"Century"}
    labelFont = {"fontname":"Century"}
    plt.style.use("Solarize_Light2")
    plt.bar(xIndexes - barWidth / 2, extractFrequencies, width=barWidth, color="#D98A31", label="Extract")
    plt.bar(xIndexes + barWidth / 2, standardFrequencies, width=barWidth, color="#3E6DC1", label="Standard")
    plt.title("Monogram Frequency Analysis", **titleFont)
    plt.xlabel("Letter", **labelFont)
    plt.ylabel("Frequency (%)", **labelFont)
    plt.xticks(ticks=xIndexes, labels=letters)
    plt.legend()
    plt.show()

    
def calculateLetterFrequencies(extract):
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    freqs = []
    
    for letter in alpha:
        frequency = (extract.count(letter) / len(extract)) * 100
        freqs.append(round(frequency, 2))
        
    return freqs
    
def main():
    extract = input("Enter Extract to Analyse: ").upper()
    extractFrequencies = calculateLetterFrequencies(extract)
    plotFrequencies(extractFrequencies)
    

if __name__ == "__main__":
    main()
