#!/usr/bin/python3
import fpass as p
import random as r
def loss(dist,exp):
    e=[1.0 if i==exp else 0.0 for i in range(10)]
    s=0
    for i in range(len(dist)):
        s+=(dist[i]-e[i])**2
    return s
s=[]
for i in range(256):
    if r.randint(0,1)==1:
        s.append(1)
    else: s.append(0)
t=[]
for i in range(64):
    t.append([r.random()*0.1 for j in range(256)])
t2=[]
for i in range(10):
    t2.append([r.random()*0.1 for j in range(64)])
gamma=0.001
f=open('data.txt').read()
f=f.split('\n')
f=[i.split('=>') for i in f]
for i in f:
    if i!=['']:
        s=[int(i) for i in i[1]]
        pa=p.frontPass(s,t,t2)
        pas=pa[0]        
        los=loss(pas,int(i[0]))
        dSecond=[0 for i in range(64)]
        sigma=lambda x:1/(1+2.718281828**(-x))
        for j in range(10):
            for k in range(64):
                t2[j][k]-=(pas[j]*sigma(pas[j])*(1-sigma(pas[j])))*gamma
                dSecond[k]+=(pas[j]*sigma(pas[j])*(1-sigma(pas[j])))
        print(los)
        for j in range(64):
            for k in range(256):
                t[j][k]-=(pa[1][j]*sigma(pa[1][j])*(1-sigma(pa[1][j]))*dSecond[j])*gamma*0.001

            
            
