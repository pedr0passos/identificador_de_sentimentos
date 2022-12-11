import pandas as pd
import string
import spacy
import random
import seaborn

spacy.load()
random()
seaborn()
b_dados = pd.read_csv('base_treinamento.txt', encoding='utf-8')
print(b_dados.shape)
print(b_dados.head())
print(b_dados.tail())
string.digits
