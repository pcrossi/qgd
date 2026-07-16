#!/usr/bin/env python3
"""Derivação simbólica do Nijenhuis da família J_chi no frame Berger."""
import sympy as s

A,C,P,Q=s.symbols('A C P Q', real=True) # a'/a,c'/c,2/c,2c/a²
ch,q=s.symbols('chi q', real=True)
sn,co=s.sin(ch),s.cos(ch)
n=4 # 0,1,2,3 = 5,6,7,8

# C_ij^k para [e_i,e_j].
B={}
def put(i,j,k,v): B[i,j,k]=v; B[j,i,k]=-v
put(0,1,1,-A);put(0,2,2,-A);put(0,3,3,-C)
put(2,3,1,-P);put(1,3,2,P);put(1,2,3,-Q)

J=s.Matrix([[0]*n for _ in range(n)])
# colunas são J(e_i)
J[:,0]=s.Matrix([0,sn,0,co])
J[:,1]=s.Matrix([-sn,0,co,0])
J[:,2]=s.Matrix([0,-co,0,-sn])
J[:,3]=s.Matrix([-co,0,sn,0])

def e_der(i,expr):
    return s.diff(expr,ch)*q if i==0 else 0

def bracket(X,Y):
    out=[0]*n
    for k in range(n):
        val=0
        for i in range(n):
            val += X[i]*e_der(i,Y[k])-Y[i]*e_der(i,X[k])
            for j in range(n): val += X[i]*Y[j]*B.get((i,j,k),0)
        out[k]=s.trigsimp(s.expand_trig(val))
    return s.Matrix(out)

def Nv(i,j):
    ei=s.eye(n)[:,i];ej=s.eye(n)[:,j]
    return s.simplify(bracket(J*ei,J*ej)-J*bracket(J*ei,ej)-J*bracket(ei,J*ej)-bracket(ei,ej))

if __name__=='__main__':
    for i in range(n):
        for j in range(i+1,n):
            print(i,j,[s.trigsimp(x) for x in Nv(i,j)])
