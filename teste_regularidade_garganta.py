#!/usr/bin/env python3
"""Verificação algébrica das condições de regularidade da garganta."""
import numpy as np


def velocities_at_throat(a, c, u, pc, pu, tau):
    h0 = -2*c*c
    adot = (2*c*c+h0)/(2*a*c)
    cdot = -(c*pc+pu)*np.exp(u)/(2*a*a*tau)
    udot = (4*c*c*tau-c*pc*np.exp(u)+2*h0*tau)/(2*a*a*c*tau)
    return np.array([adot, cdot, udot])


def main():
    a, c, u, tau = 0.7, 0.4, 1.2, 0.08
    regular = velocities_at_throat(a, c, u, 0.0, 0.0, tau)
    assert np.max(np.abs(regular)) < 1e-14

    # As derivadas em relação aos momentos têm posto dois nas componentes
    # (c,u); logo cdot=udot=0 seleciona unicamente pc=pu=0.
    step = 1e-7
    dpc = (velocities_at_throat(a,c,u,step,0,tau)-regular)/step
    dpu = (velocities_at_throat(a,c,u,0,step,tau)-regular)/step
    matrix = np.column_stack((dpc[1:], dpu[1:]))
    determinant = np.linalg.det(matrix)
    assert abs(determinant) > 1e-12
    print("regular_velocities =", regular)
    print("moment_to_velocity_matrix =", matrix)
    print("determinant =", determinant)
    print("unique_regular_solution = pc=pu=0")


if __name__ == "__main__":
    main()
