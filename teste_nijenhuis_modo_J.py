#!/usr/bin/env python3
"""Testes simbólicos das condições de integrabilidade de J_chi."""
import sympy as s
import derivar_nijenhuis_modo_J as d


def all_components():
    return [s.trigsimp(x) for i in range(4) for j in range(i+1,4) for x in d.Nv(i,j)]


def main():
    comps=all_components()
    # Ramo oficial original: chi=0 exige e implica q=0.
    at0=[s.simplify(x.subs(d.ch,0)) for x in comps]
    assert any(x==d.q for x in at0) and all(s.simplify(x.subs(d.q,0))==0 for x in at0)
    # Ramo antipodal quaternionico: chi=pi/2, q=0, resta uma única relação.
    D=d.A-d.C-d.P+d.Q
    ath=[s.trigsimp(x.subs({d.ch:s.pi/2,d.q:0})) for x in comps]
    assert all(s.simplify(x.subs(d.A,d.C+d.P-d.Q))==0 for x in ath)
    assert any(s.simplify(x-D)==0 or s.simplify(x+D)==0 for x in ath)
    # Um chi genérico não permite q != 0: N_12^6=-q sin²chi.
    assert s.simplify(d.Nv(1,2)[1]+d.q*s.sin(d.ch)**2)==0
    # No colo mínimo refletido redondo, a relação do ramo pi/2 é satisfeita.
    assert s.simplify(D.subs({d.A:0,d.C:0,d.P:2,d.Q:2}))==0
    print('NIJENHUIS: teste simbólico aprovado')
    print('ramos: chi=0 mod pi; ou chi=pi/2 mod pi com A-C-P+Q=0')
    print('em ambos: chi_dot=0')


if __name__=='__main__': main()
