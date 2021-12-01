import pandas as pd
import math

concepts = 'concepts.csv'


def extract_concepts():
    df=pd.read_csv(concepts)
    print(df)
extract_concepts()