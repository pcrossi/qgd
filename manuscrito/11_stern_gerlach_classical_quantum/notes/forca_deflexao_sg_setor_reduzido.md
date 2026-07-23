---
title: "Força e deflexão no setor reduzido"
---

# Força e deflexão no setor reduzido

## Enunciado

Em um canal adiabático fixo, a energia de interface reduzida:

$$
E_\pm(\mathbf x)=\mp\mu|\mathbf B(\mathbf x)|
$$

gera a força:

$$
\mathbf F_\pm=\pm\mu\nabla|\mathbf B|.
$$

## Prova

Por definição:

$$
\mathbf F_\pm=-\nabla E_\pm.
$$

Substituindo:

$$
\mathbf F_\pm
=
-\nabla(\mp\mu|\mathbf B|)
=
\pm\mu\nabla|\mathbf B|.
$$

Se o campo está alinhado com $z$ e o gradiente dominante é vertical:

$$
|\mathbf B|\simeq B_z,
$$

então:

$$
m\ddot z
=
\kappa\mu\frac{\partial B_z}{\partial z}.
$$

Para velocidade longitudinal $v_y$ e comprimento do ímã $L$:

$$
t=\frac{L}{v_y}.
$$

Com aceleração aproximadamente constante:

$$
\Delta z
=
\frac12\ddot z\,t^2.
$$

Logo:

$$
\Delta z
=
\kappa
\frac{\mu L^2}{2mv_y^2}
\frac{\partial B_z}{\partial z}.
$$

## Alcance

Essa é uma redução clássica de centro de massa em canal fixo. Ela não calcula
os pesos dos canais.
