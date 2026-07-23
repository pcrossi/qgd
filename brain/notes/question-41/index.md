---
title: Questão 41 — poço e oscilador
status: closed-consistency-test
source: questoes/q41/questao_41.md
updated: 2026-07-16
---

# Questão 41 — poço e oscilador

## Estado vigente

A Q41 está encerrada como teste de correspondência e consistência da redução
GDQ. Poço e oscilador não são validação independente da dinâmica métrica
completa.

## Resultados demonstrados

1. A redução plana estacionária produz continuidade e Hamilton--Jacobi--Bohm.
2. O poço com Dirichlet recupera:

$$
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}.
$$

3. A circulação reproduz a mesma quantização como holonomia da fase.
4. O estado fundamental do oscilador é minimizador:

$$
R_0(x)\propto e^{-m\omega x^2/(2\hbar)},
\qquad
E_0=\frac12\hbar\omega.
$$

5. O fluxo de gradiente normalizado converge para $R_0$.
6. A Hessiana tem índices de Morse corretos.
7. A correção de Maslov $1/2$ é interpretável como torção de fronteira.

## Parede física

A condição Robin é derivada como mapa Dirichlet--Neumann da Hessiana física da
parede:

$$
\lambda_\partial(E,q)=\Lambda_{\rm DN}[K_{\rm w}](E,q).
$$

Com modos auxiliares:

$$
\lambda_\partial
=
\lambda_{\rm bare}
-J_\partial^\dagger K_{\rm w}^{-1}J_\partial.
$$

## Limite

Correções de parede finita ou oscilador curvo dependem de material/geometria
específica. Não são universais sem definir o aparelho/background.

## Ponteiros

- Resultado: `brain/conditional-results/q41-basic-quantum-tests/index.md`
- Pendência: `brain/open-problems/q41-material-specific-corrections/index.md`

