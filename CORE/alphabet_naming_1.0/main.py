import pandas
#TODO 1. Create a dictionary in this format:
w=pandas.read_csv("nato_phonetic_alphabet.csv")
dw={r.letter:r.code for (i,r) in w.iterrows()} 
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print("WELCOME TO MY GITHUB 'alphabet naming 1.0' PROJECT.")
inp=input("Enter a word: ").upper()
outp=[dw[i] for i in inp]
print(outp)
