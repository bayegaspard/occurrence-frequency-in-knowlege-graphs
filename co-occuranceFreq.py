import pandas as pd
import math

concepts = "concepts.csv"
first1 = []
second2 = []
third3 = []
fourth4 = []

def extract_concepts():
    df=pd.read_csv("concepts.csv", index_col="images")
    return df
    # print(df) 
# print(extract_concepts().loc[["i"+str(0)]]

def extract_all_concepts(i):
    item = iter(extract_concepts().loc["i"+str(i)].values.tolist())
    return next(item) , next(item) , next(item),  next(item)

def getnl():
    for i in range(len(extract_concepts().loc["i5"].values.tolist())):
        item1, item2, item3, item4  = extract_all_concepts(i)
        print(item1)
        first = [first1.append(item1) for item1 in extract_concepts().loc["i"+str(i)].values.tolist() if item1 in extract_concepts().loc["i"+str(i)].values.tolist()]
        second = [second2.append(item2) for item2 in extract_concepts().loc["i"+str(i)].values.tolist() if item2 in extract_concepts().loc["i"+str(i)].values.tolist()]
        third = [third3.append(item3) for item3 in extract_concepts().loc["i"+str(i)].values.tolist() if item3 in extract_concepts().loc["i"+str(i)].values.tolist()]
        fourth = [fourth4.append(item4) for item4 in extract_concepts().loc["i"+str(i)].values.tolist() if item4 in extract_concepts().loc["i"+str(i)].values.tolist()]

    print(first1)
    print(second2)
    print(third3)
    print(fourth4)
#         print(extract_concepts().loc["i"+str(i)].values.tolist()[i])
#         # for j in extract_concepts().loc["i"+str(i)].values.tolist():
#         #for j in extract_concepts().loc["i"+str(i)].values.tolist():
#         item = iter(extract_concepts().loc["i"+str(i)].values.tolist())
#         for i in range(len(len(extract_concepts().loc["i5"].values.tolist()))):
#             # result = map(lambda x: x + x, numbers)
#             first = [next(item) for next(item) in extract_concepts().loc["i"+str(i)].values.tolist() if next(item) in extract_concepts().loc["i"+str(i)].values.tolist()]
#             print(next(item))
#             print(next(item))
#             print(next(item))
#             print(next(item))
#             print("end of image")
            # if k in extract_concepts().loc["i"+str(i)].values.tolist()[i] :
            #     print(k, "is in this image")
            # elif l in extract_concepts().loc["i"+str(i+1)].values.tolist():
            #     print(l," is in same image")
            # else:
            #     print("none")

            # if j in extract_concepts().loc[["i"+str(i)]]

            
getnl()