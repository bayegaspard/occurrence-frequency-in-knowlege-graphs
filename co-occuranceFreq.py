import pandas as pd
import math
import numpy as np
import random

random.seed(2)
cnt = 0
conceptsdict_item1item2 = {}
conceptsdict_item1item3 = {}
conceptsdict_item1item4 = {}
conceptsdict_item2item3 = {}
conceptsdict_item2item4 = {}
conceptsdict_item3item4 = {}

all_concepts = np.zeros([4,100])

concepts = "concepts.csv"
def extract_concepts():
    df=pd.read_csv("concepts.csv", index_col="images")
    return df

def extract_all_concepts(i):
    item = iter(extract_concepts().loc["i"+str(i)].values.tolist())
    return next(item) , next(item) , next(item),  next(item)
# def check_if_in(item1,item2, listitem):
#     if set([item1, item2]).issubset(set(listitem)):
#         return True
#     else:
#         return False
def all_in(candidates, sequence):
    for element in candidates:
        if element not in sequence:
            return False
    return True

#function to get nl
def getnl(item,subitem):
    if all_in((item), subitem)==True:
        cnt+=1

#function to get co-occurence
def getnllprime():
    for i in range(len(extract_concepts().values.tolist())):
        item1, item2, item3, item4  = extract_concepts().loc["i"+str(i)].values.tolist()
        for subitem in extract_concepts().values.tolist():
            if all_in((item1, item2), subitem)==True:
                conceptsdict_item1item2 ["coocur"+item1+item2+str(i)]=item1, item2
            else:
                pass

            if all_in((item1, item3), subitem)==True:
                conceptsdict_item1item3["coocur"+item1+item3+str(i)]=item1, item3
            else:
                pass

            if all_in((item1, item4), subitem)==True:
                conceptsdict_item1item4["coocur"+item1+item4+str(i)]=item1, item4
            else:
                pass

            if all_in((item2, item3), subitem)==True:
                conceptsdict_item2item3["coocur"+item2+item3+str(i)]=item2, item3
            else:
                pass

            if all_in((item2, item4), subitem)==True:
                conceptsdict_item2item4["coocur"+item2+item4+str(i)]=item2, item4
            else:
                pass

            if all_in((item3, item4), subitem)==True:
                conceptsdict_item3item4["coocur"+item3+item4+str(i)]=item1, item4
            else:
                pass
            
getnllprime()
#function to remove duplicates
# def clean_dict(conceptsdict_item):
#     temp = {val : key for key, val in conceptsdict_item.items()}
#     conceptsdict_item = {val : key for key, val in temp.items()}
#     return conceptsdict_item

# conceptsdict_item1item2 = clean_dict(conceptsdict_item1item2)
# conceptsdict_item1item3 = clean_dict(conceptsdict_item1item3)
# conceptsdict_item2item3 = clean_dict(conceptsdict_item2item3)
# conceptsdict_item2item4 = clean_dict(conceptsdict_item2item4)
# conceptsdict_item3item4 = clean_dict(conceptsdict_item3item4)
# print(conceptsdict_item1item2)

#list of unique occurrence of nl and nl'
for k in conceptsdict_item1item2:
    print(conceptsdict_item1item2[k], k)

#calculate coocurance frequency
