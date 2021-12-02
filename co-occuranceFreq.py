import pandas as pd
import math
import numpy as np

coocurance_freq = []
concepts = "concepts.csv"
# for i in range(100):
#     print("item"+str(i)+"=[]")

def extract_concepts():
    df=pd.read_csv("concepts.csv", index_col="images")
    return df
    # print(df) 
# print(extract_concepts().loc[["i"+str(0)]]

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

def getnl():
    for i in range(len(extract_concepts().values.tolist())):

        item1, item2, item3, item4  = extract_concepts().loc["i"+str(i)].values.tolist()
        for subitem in extract_concepts().values.tolist():

            # print(item1,item2,item3,item4)
            # if check_if_in(item1,item2,subitem)==True:
            #     print("true")
            # else :
            #     print("false")
            if all_in((item1, item2), subitem)==True:
                print(item1,"and",item2, "coocurs in image",i)
            else:
                print(item1,"and",item2," do not coocur in ", i)


            if all_in((item1, item3), subitem)==True:
                print(item1,"and",item3, "coocurs in image",i)
            else:
                print(item1,"and",item3," do not coocur in ", i)



            if all_in((item1, item4), subitem)==True:
                print(item1,"and",item4, "coocurs in image",i)
            else:
                print(item1,"and",item4," do not coocur in ", i)


            if all_in((item2, item3), subitem)==True:
                print(item2,"and",item3, "coocurs in image",i)
            else:
                print(item2,"and",item3," do not coocur in ", i)


            if all_in((item2, item4), subitem)==True:
                print(item2,"and",item4, "coocurs in image",i)
            else:
                print(item2,"and",item4," do not coocur in ", i)


            if all_in((item3, item4), subitem)==True:
                print(item1,"and",item3, "coocurs in image",i)
            else:
                print(item3,"and",item4," do not coocur in ", i)
            
            
                
         

getnl()
