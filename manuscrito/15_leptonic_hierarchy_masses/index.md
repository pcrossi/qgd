---
title: "15. Hierarquia leptônica e massas"
---

# 15. Hierarquia leptônica e massas

Este capítulo trata a massa como custo geométrico de sustentar um defeito
material. Na GDQ, o alvo primário não é obter diretamente números em MeV. O
alvo primário é obter razões adimensionais entre autovalores físicos.

A tese do capítulo é:

$$
\text{massa é rigidez geométrica de um setor físico;}
$$

$$
\text{razões de massa são preditivas;}
$$

$$
\text{massa absoluta exige calibração metrológica.}
$$

Essa distinção impede circularidade. Definir o elétron como padrão de escala
não explica sua massa absoluta em MeV, mas permite testar se a teoria prediz
$M_\mu/M_e$ e $M_\tau/M_e$.

## Roteiro

- [[15.1 - O que significa massa na GDQ]]
- [[15.2 - Escalas unidades e razões adimensionais]]
- [[15.3 - Evolução da construção e depuração conceitual]]
- [[15.4 - Rosen-Morse como benchmark auxiliar]]
- [[15.5 - Setores intrínsecos de tensão leptônica]]
- [[15.6 - Derivação reduzida da razão do múon]]
- [[15.7 - Koide como saturação geométrica e razão do tau]]
- [[15.8 - Hessiana 8D e herança por Schur]]
- [[15.9 - Background produto e critério warped-misto]]
- [[15.10 - Comparação numérica e alcance]]

## Resultado central

Com $\alpha$ herdada da ponte global--local:

$$
R_\mu
=
\frac{M_\mu}{M_e}
=
\frac32\alpha^{-1}
+
\frac65
+
2\alpha.
$$

A saturação tridimensional impõe:

$$
\frac{1+R_\mu+R_\tau}
{(1+\sqrt{R_\mu}+\sqrt{R_\tau})^2}
=
\frac23.
$$

Isso fornece o ramo pesado:

$$
R_\tau
\simeq
3477.446405098.
$$

O resultado é elevado ao background produto 8D pela Hessiana em blocos:

$$
H_8
=
\begin{pmatrix}
H_B & J\\
J^\dagger & H_\perp
\end{pmatrix},
\qquad
H_B^{\rm eff}
=
H_B-JH_\perp^{-1}J^\dagger.
$$

No produto estacionário:

$$
J=0,
\qquad
R_\ell^{(8)}=R_\ell^{(0)}.
$$

## Estatuto do resultado

| Bloco | Status | Observação |
|---|---|---|
| Massa como custo geométrico | Interpretação GDQ estrutural | Não é massa pontual inserida. |
| Escala absoluta | Calibração metrológica | MeV exige padrão de unidade. |
| Rosen--Morse | Benchmark auxiliar | Não é ontologia da hierarquia. |
| Razão do múon | Fechada no modelo reduzido intrínseco | Usa tensão/topologia e $\alpha$. |
| Relação tipo Koide | Teorema geométrico reduzido | Saturação tridimensional, não fórmula empírica. |
| Razão do tau | Fechada condicionalmente no tripleto carregado | Usa ramo pesado estável. |
| Quarta geração | Excluída no suporte reduzido $R^3$ | Não há quarto projetor ortogonal. |
| Elevação 8D produto | Fechada | Schur preserva razões quando $J=0$. |
| Warped/misto | Condicional | Avaliar por critério de Schur. |

## Controle editorial

- [[checklist_operacional|Checklist operacional do capítulo]]
- [[notes/provas_lemas_definicoes|Provas, lemas e definições associados]]
- [[notes/construcao_gdq_hierarquia_leptonica|Construção GDQ da hierarquia leptônica]]
- [[notes/escala_dimensional_calibracao|Escala dimensional e calibração]]
- [[notes/rosen_morse_benchmark_auxiliar|Rosen-Morse como benchmark auxiliar]]
- [[notes/muon_tensao_intrinseca|Razão do múon por tensão intrínseca]]
- [[notes/koide_saturacao_geometrica|Koide como saturação geométrica]]
- [[notes/reducao_perelman_3d_bulk8|Redução Perelman 3D no bulk 8D]]
- [[notes/background_8d_estacionario|Background 8D estacionário da hierarquia]]
- [[notes/hessiana_8d_schur_hierarquia|Hessiana 8D e Schur]]
- [[notes/scripts_preservados_hierarquia|Scripts preservados da hierarquia leptônica]]

[[../index|← Home]] | [[15.1 - O que significa massa na GDQ|Next →]]
