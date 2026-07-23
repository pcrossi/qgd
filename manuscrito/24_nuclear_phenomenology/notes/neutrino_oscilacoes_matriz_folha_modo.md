---
title: "Nota — Oscilações neutras, massas e matriz folha--modo"
---

# Nota — Oscilações neutras, massas e matriz folha--modo

Esta nota preserva a construção reduzida das oscilações de neutrinos na
linguagem própria da GDQ. O objetivo não é inserir a matriz PMNS como dado
fundamental. O objetivo é mostrar como a matriz observada aparece quando o
setor neutro torsional é projetado da base de folhas leptônicas para a base de
modos próprios inerciais.

## 1. Canal neutro local

O canal neutro local já aparece no decaimento beta como modo torsional sem
estômato carregado. Escrevemos:

$$
\psi_{\bar\nu}
\in
\ker D_{0,-3/2}^{(0)}.
$$

Esse modo é neutro porque está no kernel da carga elétrica:

$$
Q\psi_{\bar\nu}=0.
$$

Ele é propagante porque não está preso a uma borda estomatal carregada. Em
vez de um defeito localizado, o neutrino é uma onda de torção/fase no setor
neutro da Hessiana física.

## 2. Transporte entre folhas leptônicas

As três folhas leptônicas são obtidas transportando o mesmo canal neutro por
caminhos geométricos no fibrado neutro:

$$
\Psi_\alpha^{\rm folha}
=
\mathcal P_{\alpha e}\psi_{\bar\nu},
\qquad
\alpha=e,\mu,\tau.
$$

O transporte é induzido pela conexão de Bismut projetada:

$$
\mathcal P_{\alpha e}
=
\operatorname{Pexp}
\left(
-\int_{\mathcal C_{\alpha e}}
\nabla^B_{\rm neutro}
\right).
$$

Assim, o espaço reduzido de oscilação é:

$$
\mathcal H_\nu^{\rm folha}
=
\operatorname{span}
\left\{
\Psi_e^{\rm folha},
\Psi_\mu^{\rm folha},
\Psi_\tau^{\rm folha}
\right\}.
$$

## 3. Gram, Hessiana e problema generalizado

O produto interno físico não é o produto plano arbitrário. Ele é ponderado
pela medida GDQ:

$$
\langle A,B\rangle_{\mathcal U}
=
\int_M
\overline A B\,\mathcal U\,dV_g.
$$

Com isso, a matriz de Gram dos canais de folha é:

$$
G^\nu_{\alpha\beta}
=
\left\langle
\Psi_\alpha^{\rm folha},
\Psi_\beta^{\rm folha}
\right\rangle_{\mathcal U}.
$$

O bloco dinâmico vem da Hessiana física oficial projetada no setor neutro:

$$
K^\nu_{\alpha\beta}
=
\left\langle
\Psi_\alpha^{\rm folha},
K_{\rm neutro}^{\rm phys}
\Psi_\beta^{\rm folha}
\right\rangle_{\mathcal U}.
$$

O problema correto é generalizado:

$$
K^\nu c_i
=
\lambda_i G^\nu c_i.
$$

Os estados observados como estados de massa são os modos próprios desse
problema. A matriz de mistura é a matriz de projeção entre folhas e modos:

$$
\mathsf U_{\alpha i}^{\rm GDQ}
=
\frac{
\left\langle
\Psi_\alpha^{\rm folha},
\Psi_i^{\rm neutro}
\right\rangle_{\mathcal U}
}{
\|\Psi_\alpha^{\rm folha}\|_{\mathcal U}
\|\Psi_i^{\rm neutro}\|_{\mathcal U}
}.
$$

Na linguagem operacional de laboratório:

$$
U_{\rm PMNS}
=
\mathsf U^{\rm GDQ}.
$$

## 4. Escala reduzida de massas quadradas

Na construção reduzida preservável, a escala neutra é:

$$
S_\nu
=
\alpha^7 Q_\beta^2.
$$

Aqui $Q_\beta$ é a energia disponível no canal beta livre. A potência
$\alpha^7$ representa sete filtros de vazamento neutro:

1. três direções espaciais reais do suporte de tensão;
2. três folhas leptônicas;
3. uma seleção causal de borda do canal neutro.

Essa leitura é reduzida. Para virar previsão metrológica final, a mesma
potência deve sair como elemento de matriz da corrente simplética neutra da
ação oficial.

O espectro candidato preservado é:

$$
\lambda
=
\left(
0,
\frac{\chi_\nu^2}{2},
\frac{6\pi}{5}
\right),
$$

com:

$$
\chi_\nu
=
\frac{12}{25}e^{-\alpha/4}.
$$

O fator $12/25$ é a projeção bicanal $3$--$4$--$5$:

$$
\frac{12}{25}
=
\frac35\frac45.
$$

O fator $1/2$ vem da normalização do subespaço relativo de duas folhas. O
fator $6\pi/5$ é a circulação neutra superior reduzida:

$$
\frac{6\pi}{5}
=
3\frac{2\pi}{5}.
$$

Essa última etapa usa o transporte global de cinco ciclos no espaço
cosmológico de Einstein e deve ser lida como ponte global--local reduzida.

## 5. Diferenças de massas quadradas

Com:

$$
\Delta m_{ij}^2
=
S_\nu(\lambda_i-\lambda_j),
$$

obtém-se:

$$
\Delta m_{21}^2
=
7.741214557111\times10^{-5}\,{\rm eV}^2,
$$

$$
\Delta m_{31}^2
=
2.542566638608\times10^{-3}\,{\rm eV}^2.
$$

Comparação com os valores de referência usados no script:

| quantidade | GDQ reduzido | referência | erro relativo |
|---|---:|---:|---:|
| $\Delta m_{21}^2$ | $7.741214557111\times10^{-5}\,{\rm eV}^2$ | $7.49\times10^{-5}\,{\rm eV}^2$ | $+3.353999\%$ |
| $\Delta m_{31}^2$ | $2.542566638608\times10^{-3}\,{\rm eV}^2$ | $2.534\times10^{-3}\,{\rm eV}^2$ | $+0.338068\%$ |

As massas mínimas no ramo normal, tomando $m_1=0$ como origem espectral
reduzida, são:

$$
m_1=0,
\qquad
m_2=8.798417219655\times10^{-3}\,{\rm eV},
\qquad
m_3=5.042386973059\times10^{-2}\,{\rm eV}.
$$

Logo:

$$
\sum_i m_i
=
5.922228695025\times10^{-2}\,{\rm eV}.
$$

## 6. Ângulos reduzidos e matriz de mistura

Os ângulos reduzidos preserváveis são:

$$
\theta_{12}
=
\arctan\left(\frac1{\sqrt2}\right),
$$

$$
\theta_{23}
=
\frac{\pi}{4},
$$

$$
\theta_{13}
=
\arcsin\left(\frac{\chi_\nu}{\pi}\right).
$$

Numericamente:

| parâmetro | GDQ reduzido | referência usada | diferença |
|---|---:|---:|---:|
| $\theta_{12}$ | $35.264389683^\circ$ | $33.680000000^\circ$ | $+1.584389683^\circ$ |
| $\theta_{23}$ | $45.000000000^\circ$ | $48.500000000^\circ$ | $-3.500000000^\circ$ |
| $\theta_{13}$ | $8.772427998^\circ$ | $8.520000000^\circ$ | $+0.252427998^\circ$ |

A fase:

$$
\delta_{\rm CP}
=
\arg
\operatorname{Hol}_{\Gamma_{\rm folhas}}
(\nabla^B_{\rm neutro})
$$

ainda deve ser calculada como holonomia orientada neutra. O valor histórico
$3.84$ radianos pode ser usado apenas como marcador comparativo, não como
previsão final.

## 7. Probabilidade de oscilação na redução de laboratório

Uma vez obtidos $\mathsf U^{\rm GDQ}$ e $\Delta m^2$, a tradução operacional
para o laboratório é:

$$
P_{\alpha\to\beta}(L,E)
=
\left|
\sum_i
\mathsf U_{\beta i}^{\rm GDQ}
\exp\left(
-i\frac{m_i^2L}{2E}
\right)
\overline{\mathsf U_{\alpha i}^{\rm GDQ}}
\right|^2.
$$

Em unidades usuais de oscilação:

$$
\phi_{ij}
=
1.267\,
\Delta m_{ij}^2
\frac{L/{\rm km}}{E/{\rm GeV}}.
$$

Essa fórmula não é axioma novo. Ela é a expressão operacional obtida depois
que a GDQ fornece as diferenças de escalas inerciais e a matriz folha--modo.

## 8. Sensibilidade dos coeficientes

Com a escala fixa:

$$
S_\nu
=
6.744367477916\times10^{-4}\,{\rm eV}^2,
$$

os coeficientes requeridos pelas referências seriam:

| coeficiente | requerido | GDQ reduzido | erro relativo |
|---|---:|---:|---:|
| $\lambda_2$ | $1.110556330824\times10^{-1}$ | $1.147804383800\times10^{-1}$ | $+3.353999\%$ |
| $\lambda_3$ | $3.757209268768$ | $3.769911184308$ | $+0.338068\%$ |
| $\chi_\nu$ | $4.712868194260\times10^{-1}$ | $4.791251159771\times10^{-1}$ | $+1.663169\%$ |
| $\lambda_3/(2\pi)$ | $5.979784273551\times10^{-1}$ | $6.000000000000\times10^{-1}$ | $+0.338068\%$ |

O gargalo metrológico principal é o bloco bicanal que determina
$\lambda_2$. O modo superior já está muito próximo da circulação global
$3/5$.

## 9. Status

O resultado preservado é:

$$
\boxed{
\text{neutrinos = modos neutros torsionais; oscilações = projeção folha--modo.}
}
$$

O setor está fechado estruturalmente e possui candidato quantitativo reduzido.
O fechamento metrológico final exige:

1. construir o background neutro $\Phi_*^\nu$;
2. calcular $G^\nu$ e $K^\nu$ diretamente da Hessiana oficial;
3. obter $Z_\nu$ pela ponte global--local;
4. calcular $\delta_{\rm CP}$ como holonomia orientada neutra;
5. calcular o potencial de meio $V_{\rm GDQ}(n_e)$ como refração torsional por
   fonte clássica de matéria.

