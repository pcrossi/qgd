#!/usr/bin/env python3
import numpy as np
from ponte_global_local_kodaira_harmonicos import *


def main():
    assert invariant_linear_dimension(0)==1
    assert invariant_linear_dimension(.5)==0
    assert invariant_linear_dimension(1)==0
    b=np.array([1+2j,-.3+.7j]); norm,trip=doublet_invariants(b)
    U=np.array([[0,1],[-1,0]],complex) # elemento SU(2)
    norm2,_=doublet_invariants(U@b)
    assert abs(norm-norm2)<1e-13
    assert norm>0 and trip.shape==(3,)
    print('KODAIRA HARMÔNICOS: regras de seleção aprovadas')
    print('j=1/2: nenhum vetor invariante; |b|² é singlet quadrático')


if __name__=='__main__':main()
