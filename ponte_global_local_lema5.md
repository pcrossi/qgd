# Ponte global--local da GDQ — Lema 5: resolventes e projetores de Riesz

> [!important] Atualização arquitetural
> A dependência de BI foi removida na formulação sem colar artificial. Ver
> `ponte_global_local_lemas_sem_colar.md`.

## 1. Objetivo

Este lema estabelece o transporte espectral dos modos ligados do estômato.
Ele não afirma convergência em norma do resolvente sobre todo o espaço: na
descompactificação, parte do espectro discreto global pode condensar no
contínuo planar.

As hipóteses são:

1. Hipótese BI;
2. convergência das formas do Lema 3;
3. condições L4.1--L4.6 no setor físico escolhido;
4. identificações isométricas locais $I_\varepsilon$ construídas no Lema 3.

## 2. Espaços variáveis e operadores identificados

Sejam

$$
K_\varepsilon:=K_\varepsilon^{\rm phys}
$$

e

$$
K_P:=K_P^{\rm phys}
$$

os operadores auto-adjuntos associados às formas físicas fechadas. Para
compará-los, use operadores de extensão e restrição

$$
I_\varepsilon:
\mathcal H_P^{\rm loc}\longrightarrow\mathcal H_\varepsilon,
$$

$$
I_\varepsilon^*:
\mathcal H_\varepsilon\longrightarrow\mathcal H_P.
$$

Com os cortes crescentes e a tightness de BI.7,

$$
I_\varepsilon^*I_\varepsilon
\longrightarrow1
$$

fortemente em $\mathcal H_P$. Não se exige que
$I_\varepsilon I_\varepsilon^*=1$ em todo $\mathcal H_\varepsilon$, pois o
espaço global contém regiões que escapam de qualquer carta apontada.

## 3. Convergência Mosco no setor ligado

O Lema 3 fornece sequências de recuperação. O Lema 4 fornece localização de
Agmon, que impede fuga de massa para sequências com energia no intervalo
$I_a$. Logo, nesse setor:

### Condição liminf

Se

$$
I_\varepsilon^*\Phi_\varepsilon
\rightharpoonup\Phi
$$

fracamente e

$$
\sup_\varepsilon
\left(
q_\varepsilon[\Phi_\varepsilon]
+\|\Phi_\varepsilon\|^2
\right)<\infty,
$$

então, após extração local e uso da localização,

$$
q_P[\Phi]
\leq\liminf_{\varepsilon\to0}
q_\varepsilon[\Phi_\varepsilon].
$$

### Sequência de recuperação

Para cada $\Phi\in\operatorname{Dom}q_P$, existem cortes crescentes e
$\Phi_\varepsilon$ tais que

$$
I_\varepsilon^*\Phi_\varepsilon\to\Phi
$$

fortemente e

$$
q_\varepsilon[\Phi_\varepsilon]	o q_P[\Phi].
$$

Assim, as formas convergem no sentido de Mosco no setor localizado.

## 4. Resolvente forte

Escolha $c>0$ tal que

$$
K_\varepsilon+c\geq1,
\qquad
K_P+c\geq1
$$

uniformemente. A convergência Mosco implica

$$
\boxed{
I_\varepsilon^*(K_\varepsilon+c)^{-1}I_\varepsilon
\longrightarrow(K_P+c)^{-1}
}
$$

fortemente.

Pela identidade do resolvente, o mesmo vale para todo
$z\in\mathbb C\setminus\mathbb R$:

$$
\boxed{
I_\varepsilon^*(K_\varepsilon-z)^{-1}I_\varepsilon
\longrightarrow(K_P-z)^{-1}
}
$$

fortemente.

Para $z$ real no conjunto resolvente, é necessária uma distância espectral
uniforme de $z$ ao espectro dos operadores aproximantes.

## 5. Semigrupo

Pelo cálculo funcional para operadores auto-adjuntos semilimitados,

$$
\boxed{
I_\varepsilon^*e^{-tK_\varepsilon}I_\varepsilon
\longrightarrow e^{-tK_P}
}
$$

fortemente para todo $t>0$, uniformemente em intervalos compactos
$t\in[t_0,t_1]$ com $t_0>0$.

Essa é uma afirmação sobre o semigrupo da Hessiana euclidiana. Ela não
identifica $t$ com tempo físico nem substitui a reconstrução causal da GDQ.

## 6. Contorno espectral uniforme

Seja $I_a$ o intervalo isolado pelo Lema 4. Escolha uma curva de Jordan
$\Gamma_a$ orientada positivamente tal que:

$$
I_a\subset\operatorname{int}\Gamma_a,
$$

$$
\operatorname{dist}
(\Gamma_a,\operatorname{spec}K_\varepsilon)
\geq d_a>0
$$

uniformemente, e analogamente para $K_P$. Então

$$
\|(K_\varepsilon-z)^{-1}\|
\leq d_a^{-1},
\qquad z\in\Gamma_a.
$$

Os projetores são

$$
P_{a,\varepsilon}
=\frac1{2\pi i}
\oint_{\Gamma_a}(K_\varepsilon-z)^{-1}dz,
$$

$$
P_{a,P}
=\frac1{2\pi i}
\oint_{\Gamma_a}(K_P-z)^{-1}dz.
$$

## 7. Convergência forte dos projetores

A convergência forte do resolvente, uniforme em norma ao longo de
$\Gamma_a$, permite integrar vetor a vetor:

$$
\boxed{
I_\varepsilon^*P_{a,\varepsilon}I_\varepsilon
\longrightarrow P_{a,P}
}
$$

fortemente.

Convergência forte isolada não preserva automaticamente o posto: uma sequência
de projeções de posto crescente pode convergir fortemente. Aqui, a condição
L4.5 fornece previamente

$$
\operatorname{rank}P_{a,\varepsilon}=m_a.
$$

Se o limite também possui posto $m_a$, não há perda nem ganho de
multiplicidade.

## 8. Convergência em norma no setor ligado

A localização uniforme de Agmon implica que as imagens das bolas unitárias de
$\operatorname{Ran}P_{a,\varepsilon}$ ficam concentradas num compacto comum.
Elipticidade e regularidade local fornecem precompacidade nesse compacto.
Logo, a família transportada de projetores é coletivamente compacta.

Convergência forte mais compacidade coletiva e posto finito constante implicam

$$
\boxed{
\left\|
I_\varepsilon^*P_{a,\varepsilon}I_\varepsilon-P_{a,P}
\right\|\longrightarrow0.
}
$$

Consequentemente, o resolvente comprimido ao cluster também converge em norma:

$$
\boxed{
\sup_{z\in\Gamma_a}
\left\|
I_\varepsilon^*P_{a,\varepsilon}
(K_\varepsilon-z)^{-1}
P_{a,\varepsilon}I_\varepsilon
-P_{a,P}(K_P-z)^{-1}P_{a,P}
\right\|
\to0.
}
$$

Essa conclusão não se estende automaticamente ao complemento contínuo.

## 9. Autovalores e autoespaços

Se o cluster contém autovalores ordenados com multiplicidade,

$$
\lambda_{a,1}^{(\varepsilon)},\ldots,
\lambda_{a,m_a}^{(\varepsilon)},
$$

então a convergência em norma do operador comprimido implica, após ordenação,

$$
\lambda_{a,j}^{(\varepsilon)}
\longrightarrow\lambda_{a,j}^{(P)}.
$$

Quando há degenerescência, não existe base canônica de autovetores. O objeto
invariante transportado é o subespaço
$\operatorname{Ran}P_{a,\varepsilon}$, não um vetor escolhido dentro dele.

## 10. Estabilidade sob uma sonda local

Se uma fonte ou condição de interface induz uma perturbação simétrica
$V_{\rm app}$ relativamente limitada e

$$
\|V_{\rm app}\|_{m forma}<\frac{\Delta_a}{2},
$$

o contorno $\Gamma_a$ continua no conjunto resolvente e a dimensão do setor é
preservada. A sonda pode:

1. deslocar autovalores;
2. quebrar degenerescências;
3. misturar estados dentro do cluster;
4. produzir largura após reconstrução causal e acoplamento a canais abertos.

Ela não muda a classe topológica ou o posto do setor sem fechamento do gap,
fluxo espectral ou cirurgia.

## 11. Interação com o contorno causal

O resolvente acima é o da Hessiana obtida depois da integração causal
autorizada. Alternativamente, pode-se trabalhar com uma família
$K_\varepsilon(\tau)$ e integrar depois. A troca

$$
\oint_\gamma d\tau
\oint_{\Gamma_a}dz
$$

exige a dominação uniforme BI.8 e ausência de cruzamento de polos em ambos os
contornos. Se ocorrer cruzamento, o evento deve ser registrado como fluxo
espectral causal, não removido por deformação informal do caminho.

## 12. O que o lema transporta

Sob suas hipóteses, o Lema 5 transporta:

1. a dimensão do setor ligado;
2. o subespaço espectral;
3. os autovalores ligados da Hessiana;
4. a resposta interna a perturbações menores que o gap.

Ele não transporta por si só:

1. a normalização absoluta de um acoplamento;
2. uma massa física sem o mapa entre autovalor e unidade observável;
3. larguras e tempos sem dinâmica causal;
4. estados que se aproximem do limiar essencial;
5. todo o espectro global compacto.

## 13. Status

### Demonstrado sob BI e L4.1--L4.6

1. convergência Mosco no setor ligado;
2. convergência forte do resolvente e do semigrupo;
3. convergência forte dos projetores de Riesz;
4. convergência em norma dos projetores no cluster localizado de posto fixo;
5. convergência dos autovalores ligados e preservação da multiplicidade.

### Dependência ainda aberta na GDQ

Todas as conclusões físicas dependem da verificação das desigualdades do
Lema 4 no background BI. O presente lema demonstra a implicação analítica,
não a existência do cluster físico.

$$
\boxed{
\text{Lema 5: demonstrado como teorema condicional de transporte;}
\qquad
\text{aplicação física depende de BI e do gap do Lema 4.}
}
$$
