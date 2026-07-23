---
title: "Seleção quiral Hopf--Bismut"
---

# Seleção quiral Hopf--Bismut

## 1. Enunciado

Esta nota fixa qual espaço interno carrega o vetor axial de Hopf usado no
Stern--Gerlach geométrico.

O ponto técnico é simples: o aparelho escolhe uma direção $\mathbf n$; ele não
escolhe o espaço tridimensional onde essa direção vive. Esse espaço já vem da
estrutura complexa normal do estômato e da conexão de Bismut.

## 2. Fatia normal

A fatia normal regular de um estômato primitivo é localmente

$$
\mathbb C^2\simeq\mathbb R^4.
$$

Escreva

$$
z_1=x^1+ix^2,
\qquad
z_2=x^3+ix^4.
$$

Com coframe ortonormal $e^a=dx^a$, adotamos a orientação complexa oficial:

$$
e^1\wedge e^2\wedge e^3\wedge e^4>0.
$$

A forma Hermitiana elementar é

$$
\Omega_1
=
e^1\wedge e^2
+
e^3\wedge e^4.
$$

Nessa orientação,

$$
*\Omega_1=\Omega_1.
$$

## 3. Triplet hipercähler

A estrutura quaterniônica de $\mathbb R^4$ fornece três 2-formas:

$$
\begin{aligned}
\Omega_1&=e^1\wedge e^2+e^3\wedge e^4,\\
\Omega_2&=e^1\wedge e^3-e^2\wedge e^4,\\
\Omega_3&=e^1\wedge e^4+e^2\wedge e^3.
\end{aligned}
$$

Aplicando o operador de Hodge da orientação acima:

$$
*\Omega_i=+\Omega_i.
$$

Logo o triplet axial natural é o triplet auto-dual:

$$
\Sigma_i^+=\frac{\Omega_i}{\sqrt2},
\qquad
i=1,2,3.
$$

A base normalizada satisfaz

$$
\langle\Sigma_i^+,\Sigma_j^+\rangle=\delta_{ij}.
$$

## 4. Relação com Hopf

Para $u=(z_1,z_2)^T\in S^3\subset\mathbb C^2$, o mapa de Hopf é

$$
n_i(u)=u^\dagger\sigma_i u,
\qquad
\mathbf n(u)\in S^2.
$$

A forma axial associada ao estado interno é

$$
\Omega_{\rm Hopf}(u)
=
n^i(u)\Sigma_i^+.
$$

Assim, a orientação interna do sóliton é uma direção dentro de
$\operatorname{span}\{\Sigma_1^+,\Sigma_2^+,\Sigma_3^+\}$.

Essa é a versão geométrica do fato operacional de que um spinor normalizado
define um ponto de $\mathbb CP^1\simeq S^2$.

## 5. Papel da conexão de Bismut

A conexão de Bismut preserva a métrica e a estrutura complexa:

$$
\nabla^B g=0,
\qquad
\nabla^B J=0.
$$

Portanto, enquanto a evolução admissível não inverte a orientação complexa
nem atravessa uma degenerescência, ela pode girar e vestir a base interna, mas
não troca automaticamente o setor $SU(2)_+$ pelo setor $SU(2)_-$.

O setor usado pelo aparelho é, portanto,

$$
\omega_{\rm SG}(P)
=
n^i(P)\Sigma_i^+.
$$

## 6. O que o aparelho faz

O campo clássico do aparelho fornece uma fonte magnética levantada ao bulk.
Projetando essa fonte no triplet acima, obtém-se um vetor de interface
$\mathbf j_{\rm SG}$.

A direção efetiva do Stern--Gerlach é

$$
\mathbf n_{\rm app}
=
\frac{\mathbf j_{\rm SG}}{|\mathbf j_{\rm SG}|}.
$$

Os dois canais são então os projetores

$$
P_{\mathbf n_{\rm app}}^\pm
=
\frac12
\left(
I\pm \mathbf n_{\rm app}\cdot\sigma
\right).
$$

Essa cadeia preserva a distinção essencial:

$$
\boxed{
\text{a estrutura complexa seleciona o triplet;}
\qquad
\text{o aparelho seleciona uma direção dentro do triplet.}
}
$$

## 7. Limites

O resultado acima não calcula sozinho a intensidade metrológica da resposta
do aparelho. Essa intensidade depende da fonte clássica real, do operador DtN
da interface e da mobilidade causal. O que fica demonstrado aqui é o domínio
geométrico correto do acoplamento axial.

## 8. Verificação simbólica

O script
`scripts/verificar_triplet_hopf_bismut.py` calcula o operador de Hodge na
base de 2-formas de $\mathbb R^4$, verifica que as três formas $\Omega_i$ são
auto-duais e confirma que a base $\Sigma_i^+$ é ortonormal.
