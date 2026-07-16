#!/usr/bin/env python3
"""Contagem de Betti relevante ao possível vínculo Kähler de Berger."""

from math import comb


def betti_torus(n, k):
    return comb(n, k)


if __name__ == "__main__":
    b1_t5s3 = betti_torus(5, 1)  # S3 não contribui a H1
    b2_t5s3 = betti_torus(5, 2)  # S3 não contribui a H1/H2
    print("Q29 — COHOMOLOGIA DO SETOR BERGER")
    print("H²(S³)             = 0")
    print("H²(B⁴)             = 0")
    print(f"b1(T⁵×S³)          = {b1_t5s3}")
    print(f"b2(T⁵×S³)          = {b2_t5s3}")
    print("classes H² vêm somente de T⁵")
    print("compacto Kähler exige b1 par -> falha")
    assert b1_t5s3 == 5
    assert b2_t5s3 == 10
    assert b1_t5s3 % 2 == 1
