# Q39 — Rota GDQ intrínseca para a hierarquia leptônica

## 1. Objetivo

Este documento inicia a rota correta da Q39 depois da revisão H-01.

A meta é derivar a hierarquia leptônica pela ontologia própria da GDQ:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_e,\Phi_\mu,\Phi_\tau
\to
H_e,H_\mu,H_\tau
\to
\mathcal E_e,\mathcal E_\mu,\mathcal E_\tau
\to
M_e:M_\mu:M_\tau.
$$

A rota Rosen--Morse com \(n_\tau=17\) fica preservada apenas como benchmark
auxiliar.

## 2. Separação conceitual

Na GDQ, uma geração leptônica não é um nível radial de uma equação de
Schrödinger. Uma geração é um setor físico de tensão/topologia do sóliton:

$$
\mathcal S_1,\mathcal S_2,\mathcal S_3
\longleftrightarrow
e,\mu,\tau.
$$

Interpretação:

1. \(e\): torção primária;
2. \(\mu\): primeira torção transversal/biespacial;
3. \(\tau\): saturação tridimensional do suporte de tensão.

## 3. Massa como energia de tensão

Para cada setor:

$$
M_\ell c^2
=
\mathcal E_{\rm GDQ}[\Phi_\ell]
-
\mathcal E_{\rm vac}.
$$

No modelo reduzido, usamos massas relativas:

$$
R_\ell=\frac{M_\ell}{M_e},
\qquad
R_e=1.
$$

O cálculo final deve obter \(R_\mu\) e \(R_\tau\) sem escolher níveis
intermediários artificiais.

## 4. Setor do múon: custo biespacial

O múon é o segundo setor físico, no qual a torção precisa ocupar dois planos
ortogonais. A rigidez eletrogeométrica entra por \(\alpha^{-1}\).

O modelo reduzido candidato, extraído do Capítulo 24 legado mas agora
reclassificado como setor de tensão e não como nível de MQ, é:

$$
R_\mu^{\rm GDQ,red}
=
\frac{3}{2}\alpha^{-1}
+
\frac65
+
2\alpha.
$$

Leitura dos termos:

1. \(\frac32\alpha^{-1}\): custo biespacial dominante em três dimensões;
2. \(\frac65\): impedância de interface/Fredholm--Fano reduzida;
3. \(2\alpha\): autoenergia eletrogeométrica de duas circulações ortogonais.

Esse cálculo não usa \(M_\mu\) como alvo.

## 5. Setor do tau: saturação tridimensional

O tau é o terceiro setor físico. Ele não é \(n=17\). Ele representa a
saturação do suporte tridimensional de tensão.

Use amplitudes:

$$
A_\ell=\sqrt{R_\ell}.
$$

O quociente de tensão global é:

$$
Q
=
\frac{R_e+R_\mu+R_\tau}
{(A_e+A_\mu+A_\tau)^2}.
$$

A condição reduzida de saturação tridimensional é:

$$
Q=\frac23.
$$

Importante: essa forma é matematicamente equivalente à relação de Koide, mas
na rota GDQ ela deve ser lida como condição variacional de saturação
tridimensional. A derivação reduzida está em
`derivacao_gdq_intrinseca_1a5_q39.md`; a pendência remanescente é elevar essa
condição à Hessiana física 8D da ação oficial.

## 6. Cálculo executável

O script associado:

$$
\texttt{modelo\_gdq\_tensao\_intrinseca\_q39.py}
$$

calcula:

1. \(R_\mu\) pelo custo biespacial;
2. \(R_\tau\) pela saturação tridimensional;
3. comparação com o benchmark Rosen--Morse e com razões experimentais.

Classificação inicial:

$$
\boxed{
\text{modelo reduzido GDQ candidato; não prova final 8D.}
}
$$

Após a derivação dos cinco pontos em
`derivacao_gdq_intrinseca_1a5_q39.md`, esta rota passa a ter status de
fechamento reduzido intrínseco. A elevação para a Hessiana física 8D da ação
oficial foi fechada no background estacionário produto/bloco em
`calcula_background_8d_estacionario_q39.py`.

## 7. Critério de avanço

Esta rota só fecha a Q39 quando:

1. \(\frac32\alpha^{-1}\), \(\frac65\), \(2\alpha\), \(Q=2/3\) e a exclusão
   de uma quarta configuração forem derivados no setor reduzido intrínseco;
2. essa redução for elevada à Hessiana física 8D da ação oficial no
   background estacionário produto/bloco;
3. Rosen--Morse aparecer apenas como limite assintótico ou benchmark,
   nunca como seleção de geração.

O item 1 foi fechado em `derivacao_gdq_intrinseca_1a5_q39.md`.

## 8. Status

Status desta rota:

$$
\boxed{
\text{fechada no modelo reduzido intrínseco; Hessiana 8D produto fechada.}
}
$$

Backgrounds warped/mistos reais permanecem como setores condicionais a avaliar
pelo critério de Schur, sem pós-ajuste.
