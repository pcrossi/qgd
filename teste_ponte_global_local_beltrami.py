#!/usr/bin/env python3
import numpy as np
from ponte_global_local_beltrami import *


def main():
    assert torus_beltrami_dimension(2)==4
    # Primeiro representante fora da diagonal; constante e não exato no toro compacto.
    mu=np.array([[0,1],[0,0]],dtype=complex)
    assert np.linalg.norm(maurer_cartan_constant(mu))==0
    H2=quadratic_torsion_form_constant(mu)
    assert np.linalg.norm(H2)==0
    q,p=interface_trace_constant(mu)
    assert q[1]==1 and np.linalg.norm(p)==0
    print('BELTRAMI TOROIDAL: teste exato aprovado')
    print('dim_C H^{0,1}(T^{1,0}T4) =',torus_beltrami_dimension())
    print('Maurer-Cartan = 0; delta H = 0; momento normal = 0')
    print('AVISO: módulo global/zero, não modo estabilizador do colo')


if __name__=='__main__':main()
