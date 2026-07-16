#!/usr/bin/env python3
import numpy as np
from ponte_global_local_hopf_planura import *


def main():
    q=.37
    for e in (-.4,-.1,0,.2,.5): assert abs(determinant_ratio(q,e)-1)<1e-14
    es=np.linspace(-.3,.3,9);S=action_samples(1.234,es)
    p=np.polynomial.polynomial.polyfit(es,S,4)
    assert max(abs(p[1:]))<1e-12
    assert all(v==0 for v in effective_coefficients().values())
    print('HOPF PLANURA: identidades aprovadas')
    print('det Q_eps = q²; ação compatível constante; coeficientes estáticos = 0')


if __name__=='__main__':main()
