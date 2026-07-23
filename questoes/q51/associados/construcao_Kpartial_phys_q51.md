# Q51 — Construção de \(K_\partial^{\rm phys}\) para o canal alfa

## 1. Objetivo

O fechamento da Q51 exige calcular:

$$
P_\perp
=
P_\alpha(1-P_{\rm filho}),
$$

com:

$$
P_\alpha
=
\frac{1}{2\pi i}
\oint_{\mathcal C_\alpha}
(z-K_\partial^{\rm phys})^{-1}\,dz.
$$

Portanto, precisamos construir \(K_\partial^{\rm phys}\).

## 2. Forma mínima do operador de superfície

Na superfície nuclear \(\partial\Omega_N\simeq S^2\), o operador físico deve
ter a estrutura:

$$
K_\partial^{\rm phys}
=
P_{\rm red}
\left[
K_{\rm geom}
+K_{\rm tors}
+K_{\rm shell}
+K_{\rm canal}
\right]
P_{\rm red}.
$$

Aqui:

1. \(P_{\rm red}\) remove gauge, translações e rotações rígidas;
2. \(K_{\rm geom}\) é a rigidez geométrica/curvatura de superfície;
3. \(K_{\rm tors}\) é a cola torsional herdada da Q40;
4. \(K_{\rm shell}\) é o espectro de camada gerado pela Hessiana de superfície;
5. \(K_{\rm canal}\) impõe os vínculos do canal alfa.

## 3. Setor harmônico

No nível angular:

$$
K_{\rm geom}
\sim
a_0
+a_2\Delta_{S^2}
+a_4\Delta_{S^2}^2.
$$

Como:

$$
-\Delta_{S^2}Y_{\ell m}
=
\ell(\ell+1)Y_{\ell m},
$$

temos:

$$
\lambda_\ell^{\rm geom}
=
a_0
+a_2\ell(\ell+1)
+a_4[\ell(\ell+1)]^2.
$$

## 4. Cluster alfa

O cluster alfa de emissão par-par \(0^+\to0^+\) entra no setor escalar
dominante:

$$
\ell=0,
$$

mas a preformação real não depende apenas de \(\ell\). Ela depende da
compatibilidade do modo \(4N\) com o espectro de superfície do núcleo pai e
com o subespaço do núcleo filho.

Logo, o projetor não é apenas angular. Ele é espectral:

$$
P_\alpha
\ne
P_{\ell=0}
$$

em geral.

## 5. Papel do subespaço do núcleo filho

O núcleo filho já contém modos de superfície estabilizados. A emissão alfa só
usa a componente ortogonal a esse subespaço:

$$
P_\perp\Phi_{4N}
=
P_\alpha(1-P_{\rm filho})\Phi_{4N}.
$$

Essa é a razão matemática pela qual alguns núcleos podem ter impedância média
grande, mas energia efetiva quase nula: a componente alfa admissível é
projetada fora.

## 6. Diagnóstico espectral

O arquivo:

- `diagnostico_espectral_projetor_q51.py`

converte os pesos requeridos em:

1. ângulo espectral \(\theta_\alpha\);
2. razão gap/largura \(\Delta/\Gamma\) de uma janela Lorentziana.

Isso não fecha o problema, mas define a escala que \(K_\partial^{\rm phys}\)
deve produzir.

## 7. Critério de fechamento

A Q51 fecha quando:

1. \(K_\partial^{\rm phys}\) for construído do background nuclear;
2. \(P_\alpha\) for calculado por Riesz;
3. \(P_{\rm filho}\) for calculado no mesmo produto físico;
4. \(E_\partial^{\rm GDQ}\) for obtido sem usar \(E_\partial^{\rm req}\);
5. a série isotópica for comparada com parâmetros congelados.

