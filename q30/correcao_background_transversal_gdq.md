# Q30 — Correção: o background transversal é o pescoço Ricci--Bohm

## 1. Correção conceitual

A rota por uma superfície abstrata de três bordos e uma conexão plana
clock--shift é uma auditoria espectral externa útil, mas não é o background
transversal fundamental da Q30.

Na GDQ, o tubo é uma deformação mecânico-geométrica do próprio bulk. Sua seção
transversal é o pescoço do sóliton de Ricci--Bismut estabilizado pelo balanço
entre contração de curvatura e pressão de Bohm:

$$
\boxed{
R_{\perp\perp}
=\frac14\nabla_\perp\nabla_\perp Q
}
$$

na convenção do Capítulo 27, ou pela equação métrica equivalente derivada da
ação oficial. Esse equilíbrio fixa

$$
\boxed{
\mathcal A_0=\pi r_\perp^2>0.
}
$$

As três câmaras/estômatos descrevem a estrutura interna e a colagem bariônica;
elas não substituem a seção transversal física por uma variedade de gauge.

## 2. Ausência de elongação longitudinal

No bulk do tubo, a invariância por translação ao longo de $z$ fornece

$$
\partial_z\mathcal L_\perp=0.
$$

Para os campos transversais $q$,

$$
E[q]=\int_0^L\mathcal L_\perp(q,\partial_zq)\,dz.
$$

A identidade de Beltrami e o minimizador estacionário dão

$$
\partial_zq_*=0,
\qquad
r_\perp(z)=r_\perp,
\qquad
\mathcal A(z)=\mathcal A_0.
$$

Esse é o sentido correto de “torções são permitidas e elongações não”: a
torção/circulação interna permanece, enquanto a seção estabilizada não se
alonga ao longo do bulk homogêneo.

## 3. Tensão GDQ

Defina a densidade transversal física pela diferença entre o sóliton e o
vácuo, usando a redução da ação oficial:

$$
\varepsilon_\perp^{\rm GDQ}
:=\frac{1}{\mathcal A_0}
\left(
\mathcal S_\perp[q_*]-\mathcal S_\perp[q_{\rm vac}]
\right).
$$

A tensão é

$$
\boxed{
\sigma_{\rm GDQ}
=\mathcal A_0\varepsilon_\perp^{\rm GDQ}
=\mathcal S_\perp[q_*]-\mathcal S_\perp[q_{\rm vac}]>0.
}
$$

A positividade não vem de $|F_C|^2$ de uma QCD importada. Ela vem do custo de
manter uma classe torsional/circulante não trivial contra o vácuo no
minimizador transversal estável. Se a diferença fosse zero, o representante
não trivial seria degenerado com o vácuo e o pescoço não seria um sóliton
confinado isolado.

## 4. Potencial linear

Como $\sigma_{\rm GDQ}$ é constante no bulk homogêneo,

$$
V(L)
=\int_0^L\sigma_{\rm GDQ}\,dz
=\boxed{\sigma_{\rm GDQ}L}.
$$

Portanto, a lei linear é consequência da solução tubular GDQ, não de Wilson
loops fundamentais.

## 5. Mass gap transversal

Na seção compacta estabilizada, o primeiro modo transversal possui momento
geométrico da ordem de

$$
p_\perp=\hbar\sqrt{\frac{\pi}{\mathcal A_0}}
=\frac{\hbar}{r_\perp}.
$$

Logo,

$$
\boxed{
\Delta_{\rm GDQ}
=\hbar c\sqrt{\frac{\pi}{\mathcal A_0}}
=\frac{\hbar c}{r_\perp}>0.
}
$$

Essa é a origem mecânico-geométrica do gap na GDQ. O teorema de holonomia
$SU(3)$ fornece uma auditoria compatível do setor efetivo, mas não é o
fundamento da existência da seção ou da tensão.

## 6. O que está fechado e o que é numérico posterior

Ficam fechados estruturalmente:

1. emergência de seção constante por equilíbrio transversal;
2. tensão positiva como diferença de ação do sóliton e do vácuo;
3. $V(L)=\sigma L$;
4. gap positivo pela compacidade de $\mathcal A_0$.

Permanece quantitativo:

$$
\boxed{
\text{avaliar }r_\perp,\quad
\sigma_{\rm GDQ},\quad
\Delta_{\rm GDQ}
\text{ em unidades de }\Lambda_C.
}
$$

Esses números exigem o perfil do sóliton, mas não reabrem a demonstração de
confinamento e gap positivo.

## 7. Reclassificação das rotas auxiliares

1. `q30/minimizador_irredutivel_tres_camaras.md`: auditoria espectral efetiva
   da holonomia, não background fundamental;
2. `q30/no_go_sigma_holonomia_plana.md`: no-go correto apenas para tentar
   extrair tensão de uma conexão plana;
3. `q30/conexao_su3_wilson_gap.md`: tradução efetiva externa;
4. presente documento: rota física fundamental GDQ da Q30.

A reconstrução operacional foi executada posteriormente em
`q30/calculo_operacional_heaviside_potencial.md`, obtendo
$\widetilde V(k)=-8\pi\sigma_{\rm GDQ}/k^4$ como resposta estática do tubo.

## 8. Status

$$
\boxed{
\text{Q30 fechada estruturalmente na GDQ;
valores numéricos de }(\sigma,\Delta)\text{ são avaliação posterior.}
}
$$
