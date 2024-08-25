#!/usr/bin/python3
def frontPass(s,t,t2):
    l2=[]
    for i in range(64):
        m=0
        for j in range(256):
            m+=s[j]*t[i][j]
        l2.append(1/(1+2.718281828**(-m)))
    o=[]
    for i in range(10):
        m=0
        for j in range(64):
            m+=l2[j]*t2[i][j]
        o.append(1/(1+2.718281828**(-m)))
    return [o,l2]
