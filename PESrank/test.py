import math
import PESrank

[rank,explain] = PESrank.main(username, password, path)
n=905*(10**6)
ex=False

print("Your password is ",end="")
if rank<0:
    print("strong")
else:
    if math.log2(rank)<=30:
        print("weak", end="")
        ex=True
    elif math.log2(rank)<=50:
        print("sub-optimal", end="")
        ex=True
    else:
        print("strong", end="")

    print(", according to this study, based on 905 million leaked passwords")
        
if ex==True:
    print("Your password is based on the leaked word: '"+str(explain[0][1])+ "' that was used by",int(float(explain[0][2])*n), "people")
    for lst in explain:
        if math.ceil(float(lst[1])*n)>=100:
            if lst[0]==1:
                print("It uses a prefix that was used by",math.ceil(float(lst[1])*n), "people")
            if lst[0]==3:
                print("It uses a suffix that was used by",math.ceil(float(lst[1])*n), "people")
            if lst[0]==4:
                print("It uses a capitaliation pattern that was used by",math.ceil(float(lst[1])*n), "people")
            if lst[0]==5:
                print("It uses a l33t pattern that was used by",math.ceil(float(lst[1])*n), "people")

