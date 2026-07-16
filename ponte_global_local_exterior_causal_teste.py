#!/usr/bin/env python3
"""Validação algébrica da redução causal do exterior Berger.

Classificação: teste de consistência simbólica; não é solução da sela.
"""
import sympy as sp

def main():
    M=sp.Matrix([
        [-sp.Rational(1,2),sp.Rational(5,2),2,1,-1],
        [sp.Rational(5,2),sp.Rational(7,2),6,3,-3],
        [2,6,0,2,-2],
        [1,3,2,0,-1],
        [-1,-3,-2,-1,1],
    ])
    Minv=M.inv()
    # Restrição isotrópica x0=xs deve reproduzir os coeficientes do exterior
    # Berger não separado: x²=8, xy=16, xz=8, xu=-8.
    x0,xs,y,z,u=sp.symbols('x0 xs y z u')
    q=sp.Matrix([x0,xs,y,z,u])
    K=sp.expand((q.T*M*q)[0])
    Kiso=sp.expand(K.subs({x0:sp.Symbol('x'),xs:sp.Symbol('x')}))
    expected=8*sp.Symbol('x')**2+16*sp.Symbol('x')*y+8*sp.Symbol('x')*z-8*sp.Symbol('x')*u+4*y*z-4*y*u-2*z*u+u**2
    p0_expected=-x0+5*xs+4*y+2*z-2*u
    print('det_M =',M.det())
    print('inverse_M =');sp.pprint(Minv)
    print('isotropic_reduction_residual =',sp.simplify(Kiso-expected))
    print('clock_momentum_residual =',sp.simplify(sp.diff(K,x0)-p0_expected))
    print('passed =',M.det()!=0 and sp.simplify(Kiso-expected)==0
          and sp.simplify(sp.diff(K,x0)-p0_expected)==0)

if __name__=='__main__':
    main()
