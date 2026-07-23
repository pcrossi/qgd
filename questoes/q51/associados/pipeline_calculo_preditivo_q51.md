# Q51 — Pipeline preditivo para decaimento alfa na GDQ

## 1. Objetivo

Este documento fixa a forma operacional mínima para transformar a cadeia
variacional formal da Q51 em cálculo preditivo.

A cadeia é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{N,*}
\to
K^{\rm phys}
\to
K_\partial^{\rm phys}
\to
P_\alpha
\to
E_\partial^{\rm GDQ}
\to
\Gamma_{\rm GDQ}.
$$

O pipeline não altera a ação oficial. Ele apenas organiza as quantidades que
devem ser extraídas da Hessiana física do background nuclear.

## 2. Dados de entrada físicos

Para cada decaimento:

$$
(A,Z)\to(A-4,Z-2)+\alpha,
$$

os dados externos permitidos na comparação são:

1. \(A\) e \(Z\) do núcleo pai;
2. \(Q_\alpha\);
3. spins e paridades, quando determinarem canal orbital;
4. meia-vida experimental apenas para comparação, nunca para construir os
   operadores;
5. massas nucleares auditadas, quando usadas na massa reduzida.

## 3. Objetos que devem vir da GDQ

O fechamento preditivo exige calcular, para cada núcleo, mas com regras
universais congeladas:

$$
\Phi_{N,*},
\qquad
K_{II},
\qquad
K_{I\partial},
\qquad
K_{\partial\partial}.
$$

Aqui:

- \(I\) representa os modos interiores eliminados;
- \(\partial\) representa os traços físicos na interface alfa--núcleo;
- os modos de gauge, translação e normalização já devem estar removidos por
  \(P^{\rm phys}\).

O operador de superfície é:

$$
K_\partial^{\rm phys}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

## 4. Seleção do canal alfa

O canal alfa não deve ser selecionado por etiqueta fenomenológica. Ele é o
subespaço espectral:

$$
P_\alpha
=
\frac1{2\pi i}
\oint_{\mathcal C_\alpha}
(z-K_\partial^{\rm phys})^{-1}\,dz.
$$

No setor físico:

$$
P_\perp
=
P_\alpha(1-P_{\rm filho}).
$$

O fator de pré-formação/overlap fica:

$$
S_\alpha^{\rm GDQ}
=
\exp(-E_\partial^{\rm GDQ}),
$$

com:

$$
E_\partial^{\rm GDQ}
=
\left\langle
P_\perp\Phi_{4N},
K_\partial^{\rm phys}
P_\perp\Phi_{4N}
\right\rangle_\partial.
$$

## 5. Frequência de tentativa

A frequência não deve ser \(\nu_0\) fixa. A forma GDQ é:

$$
\nu_{\rm GDQ}
=
\frac1{2\pi}
\sqrt{
\frac{\lambda_{\alpha,{\rm int}}}{M_\alpha^{\rm eff}}
}.
$$

Na ausência temporária da Hessiana interna, a aproximação cinemática

$$
\nu_{\rm int}
=
\frac{c}{2R_N}
\sqrt{\frac{2Q_\alpha}{\mu}}
$$

pode ser usada apenas como comparação reduzida.

## 6. Ação radial

A ação radial sob a barreira é:

$$
W_{\rm rad}^{\rm GDQ}
=
\frac2\hbar
\int_{r_1}^{r_2}
\sqrt{2\mu(V_{\rm eff}^{\rm GDQ}(r)-Q_\alpha)}
\sqrt{g_{rr}^{\rm eff}(r)}
\,dr.
$$

O \(g_{rr}^{\rm eff}\) deve vir da Hessiana radial/Schur/DtN. A forma legada

$$
\exp(-\alpha^2V_C/Q_\alpha)
$$

permanece apenas uma hipótese reduzida compatível com Q45, não uma derivação.

## 7. Observável final

O observável é:

$$
\Gamma_{\rm GDQ}
=
\nu_{\rm GDQ}
\exp(-E_\partial^{\rm GDQ})
\exp(-W_{\rm rad}^{\rm GDQ}).
$$

Logo:

$$
T_{1/2}^{\rm GDQ}
=
\frac{\ln2}{\Gamma_{\rm GDQ}}.
$$

## 8. Critério de fechamento

A Q51 fecha quando:

1. \(K_\partial^{\rm phys}\) for calculado de um background nuclear GDQ real;
2. \(P_\alpha\) e \(P_{\rm filho}\) forem obtidos espectralmente;
3. \(\nu_{\rm GDQ}\) for obtida do modo normal interno;
4. \(g_{rr}^{\rm eff}\) for extraído do operador radial;
5. os parâmetros forem congelados antes da comparação;
6. a série isotópica for comparada contra NUBASE/AME/ENSDF;
7. os resíduos forem preservados.

Até isso ocorrer, o estado correto é:

$$
\boxed{
\text{Q51 fechada formalmente como cadeia; não fechada metrologicamente.}
}
$$
