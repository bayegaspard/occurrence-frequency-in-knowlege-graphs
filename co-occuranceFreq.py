import pandas as pd
import math
import numpy as np
import random

random.seed(2)

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
# cnt = 0
# #function to get nl
# def getnl(item,subitem):
#     if all_in((item), subitem)==True:
#         cnt+=1

#function to get co-occurence
def getnllprime():
    for i in range(len(extract_concepts().values.tolist())):
        item1, item2, item3, item4  = extract_concepts().loc["i"+str(i)].values.tolist()
        for subitem in extract_concepts().values.tolist():
            if all_in((item1, item2), subitem)==True:
                conceptsdict_item1item2 ["i"+str(i)]=item1, item2
            else:
                pass

            if all_in((item1, item3), subitem)==True:
                conceptsdict_item1item3["i"+str(i)]=item1, item3
            else:
                pass

            if all_in((item1, item4), subitem)==True:
                conceptsdict_item1item4[str(i)]=item1, item4
            else:
                pass

            if all_in((item2, item3), subitem)==True:
                conceptsdict_item2item3["i"+str(i)]=item2, item3
            else:
                pass

            if all_in((item2, item4), subitem)==True:
                conceptsdict_item2item4["i"+str(i)]=item2, item4
            else:
                pass

            if all_in((item3, item4), subitem)==True:
                conceptsdict_item3item4["i"+str(i)]=item1, item4
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
# item1_2 =  {i:MyList.count(i) for i in MyList}
item1_3 = []
item1_4 = []
item2_3 = []
item2_4 = []
item3_4 = []
countcooccur = 0
#list of unique occurrence of nl and nl'
# for k in conceptsdict_item1item2:
#     print(conceptsdict_item1item2[k][1], k)


def group_like_items(dict_item):
    flipped ={}
    for key, value in dict_item.items():
        #print(key, value)
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    return flipped


all_freqa = []

def show_co_occurence_frequency(dict_items):
    cnt=    all_items=[]
    flipped = group_like_items(dict_items)
    for key,value in flipped.items():
        print(key," co-occured ",len([k for k in value]), "times")
        #print(len([k for k in value]))
        all_items.append(key[0])
        all_items.append(key[1])
        if key[0] or key[1] in key:
            #s = max(math.log(len(str([k for k in value]))/len(len(str(key[0]))*len(str(key[1])))),0)
            s = max(math.log(len([k for k in value])/(len(str(key[0][:2]))*1)),0) #len(str(key[1][:6])))),0) 
            print("coocurance frequency for ", key[0], key[1],"is", s)
            all_freqa.append(s)
        else:
            print(0)
            s = 0
            all_freqa.append(s)

show_co_occurence_frequency(conceptsdict_item1item2)
show_co_occurence_frequency(conceptsdict_item1item3)
show_co_occurence_frequency(conceptsdict_item1item4)
show_co_occurence_frequency(conceptsdict_item2item3)
show_co_occurence_frequency(conceptsdict_item2item4)
show_co_occurence_frequency(conceptsdict_item3item4)

import sys
#all_freqa = np.ndarray()
np.set_printoptions(threshold=sys.maxsize)
N = len(all_freqa[11:]);value = 100
#Note all leading diagonal is 100 equivalent to 1.
b = np.ndarray((N)).reshape(20,20)
np.fill_diagonal(b, value)
print(b)