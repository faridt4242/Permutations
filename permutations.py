import itertools
def permutations(string):
    a=list(set(itertools.permutations(string)))
    res=[]
    st=""
    for i in range (len(a)):
        for j in range (len(a[i])):
            st+=a[i][j]
        res.append(st)
        st=""
    return res
