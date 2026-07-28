---
title: "Nota — Produção e aniquilação de pares conjugados"
---

# Nota — Produção e aniquilação de pares conjugados

## 1. Enunciado e status

Esta nota estende o setor eletromagnético assintótico da GDQ para:

$$
e^-+e^+
\longrightarrow
\gamma+\gamma,
$$

$$
\gamma+N
\longrightarrow
e^-+e^++N,
$$

e:

$$
\gamma+B_{\rm ext}
\longrightarrow
e^-+e^++B_{\rm ext}.
$$

O resultado possui duas camadas que não devem ser confundidas:

1. a reciprocidade e os limiares são consequências estruturais da ação, das
   conservações e do domínio;
2. as taxas apresentadas ao final pertencem ao setor eletromagnético efetivo
   projetado e não substituem a avaliação dos jatos no background 8D.

O status é:

$$
\boxed{
\text{fechamento condicional no setor eletromagnético efetivo}.
}
$$

## 2. Background conjugado

Escrevemos o campo constitutivo como:

$$
f
=
F+\frac{i}{\hbar}S_R.
$$

A conjugação de carga inverte a orientação da fase e da linha de carga:

$$
\mathsf C:
\left(
F,S_R,L_Q
\right)
\longmapsto
\left(
F,-S_R,L_Q^{-1}
\right).
$$

Como:

$$
\rho
=
e^{-F},
$$

a densidade geométrica é preservada:

$$
\rho_{\mathsf C\Phi}
=
\rho_\Phi.
$$

O pósitron é, portanto, o background eletrônico na classe conjugada de
contorno e holonomia. Isso não significa que carga e spin sejam a mesma
orientação: a circulação de Hopf que representa spin deve ser projetada
separadamente.

## 3. Backgrounds externos

O núcleo e o magneto não são termos fundamentais novos. Eles são fontes
clássicas e dados de contorno:

$$
\Phi_N
=
\operatorname{Crit}_{\mathcal C_N}\mathcal S_{\rm GDQ},
$$

$$
\Phi_B
=
\operatorname{Crit}_{\mathcal C_B}\mathcal S_{\rm GDQ}.
$$

No limite externo, o núcleo fixa o fluxo de carga:

$$
\frac{1}{2\pi i}
\oint_{\partial\Sigma_N}
\mathcal A_Q
=
Z,
$$

e o magneto fixa a conexão clássica, por exemplo:

$$
\mathbf A_B
=
\frac12\mathbf B\times\mathbf r.
$$

Essas expressões especificam as classes de fonte. A sela completa exige
resolver a ação oficial nessas classes.

## 4. Jatos físicos e reciprocidade

Depois de projetar gauge e vínculos e eliminar modos internos por Schur, a
terceira variação reduzida define:

$$
C_{\gamma+-}^{(X)}
=
D^3\mathcal S_{\rm red}[\Phi_X]
[\psi_\gamma,\eta_+,\eta_-],
\qquad
X\in\{0,N,B\}.
$$

A simetria de Fréchet fornece a permutação algébrica:

$$
C_{\gamma+-}^{(X)}
=
C_{+-\gamma}^{(X)}.
$$

Para que ela seja reciprocidade física, também são necessários:

1. domínio causal preservado;
2. gerador reconstruído autoadjunto;
3. condição de realidade apropriada;
4. reversão do background magnético em processos reversos.

Sob essas hipóteses:

$$
\mathcal M_{i\to f}[B]
=
\overline{
\mathcal M_{f\to i}[-B]
}.
$$

As amplitudes são relacionadas, mas as taxas não precisam ser iguais porque
os espaços de fase e as fontes são diferentes.

## 5. Por que dois fótons

Um par em repouso possui quadrimomento total temporal:

$$
P^\mu
=
(2m_ec,\mathbf0),
\qquad
P^2>0.
$$

Um único fóton satisfaz $k^2=0$ e não pode carregar esse quadrimomento no
vácuo. O canal livre mínimo é:

$$
e^-+e^+
\longrightarrow
\gamma+\gamma.
$$

No centro de massa:

$$
E_{\gamma,1}
=
E_{\gamma,2}
=
m_ec^2.
$$

O canal físico de dois fótons vem da quarta variação ou de dois vértices
cúbicos ligados pelo resolvente:

$$
\mathcal V_{\gamma\gamma+-}^{\rm phys}
=
D^4\mathcal S_{\rm red}
-
D^3\mathcal S_{\rm red}
G_{\rm int}
D^3\mathcal S_{\rm red}
+\text{permutações}.
$$

No limite externo Dirac--Bismut, a conexão eletromagnética entra linearmente,
e o canal líder é formado pelas duas inserções cúbicas. Um contato quártico
solitônico pode existir no background 8D completo e não deve ser descartado
antes do cálculo.

## 6. Seleção de dois e três fótons

Se o estado conjugado total possui autovalor de conjugação:

$$
\eta_{\mathsf C}
=
(-1)^{N_\gamma},
$$

o setor par permite dois fótons e o setor ímpar exige três no menor canal.
Essa leitura é condicional à identificação entre o autovalor de circulação
GDQ e a conjugação do canal reconstruído. Ela não é uma identidade puramente
cinemática.

## 7. Produção no campo nuclear

Para um núcleo inicialmente em repouso:

$$
\gamma+N
\longrightarrow
e^-+e^++N,
$$

a conservação do quadrimomento produz:

$$
\boxed{
E_{\gamma,\rm th}^{(N)}
=
2m_ec^2
\left(
1+\frac{m_e}{M_N}
\right).
}
$$

No limite de núcleo pesado:

$$
E_{\gamma,\rm th}^{(N)}
\simeq
1.0219979\ {\rm MeV}.
$$

O núcleo fornece recuo e impedância de interface; a energia de repouso do par
vem do fóton.

## 8. Produção em campo magnético

Para propagação com ângulo $\theta$ em relação ao campo:

$$
E_\gamma\sin\theta
\geq
2m_ec^2.
$$

A escala crítica correta em SI é:

$$
B_Q
=
\frac{m_e^2c^2}{e\hbar}
=
4.4140052\times10^9\ {\rm T}.
$$

O parâmetro adimensional é:

$$
\chi_\gamma
=
\frac{E_\gamma}{2m_ec^2}
\frac{B\sin\theta}{B_Q}.
$$

Um campo magnético puramente estático não fornece sozinho a energia de
repouso. Ele absorve momento transversal e modifica o espectro; o fóton
fornece energia.

## 9. Taxas líderes no setor projetado

Com a normalização $U(1)_Q$ herdada e o estado ligado de positrônio:

$$
\Gamma_{2\gamma}^{(0)}
=
\frac12
\alpha^5
\frac{m_ec^2}{\hbar},
$$

$$
\Gamma_{3\gamma}^{(0)}
=
\frac{2(\pi^2-9)}{9\pi}
\alpha^6
\frac{m_ec^2}{\hbar}.
$$

As vidas líderes são:

| Canal | cálculo reduzido | referência experimental | erro |
|---|---:|---:|---:|
| $p$-Ps $\to2\gamma$ | $124.494196935$ ps | $125.142349422$ ps | $-0.517932\%$ |
| $o$-Ps $\to3\gamma$ | $138.673807699$ ns | $142.050000000$ ns | $-2.376763\%$ |

Os resíduos não são absorvidos em parâmetros. Eles marcam correções
superiores e resposta material ausentes da fórmula líder.

## 10. Benchmark nuclear

No limite de blindagem completa:

$$
\sigma_N
=
\frac{28}{9}
Z^2\alpha r_e^2
\left[
\ln\left(183Z^{-1/3}\right)
-f_C(Z\alpha)
-\frac1{42}
\right],
$$

com:

$$
f_C(a)
=
a^2
\sum_{n=1}^{\infty}
\frac{1}{n(n^2+a^2)}.
$$

Para fótons de $2.5$ GeV:

| Alvo | cálculo assintótico | medida | desvio |
|---|---:|---:|---:|
| Al | $1.316166251$ barn | $1.22\pm0.17$ barn | $+0.566\sigma$ |
| Pb | $41.034539221$ barn | $34.6\pm6.6$ barn | $+0.975\sigma$ |

A comparação testa a redução eletromagnética; não substitui estrutura nuclear
completa.

## 11. Opacidade magnética assintótica

No regime $\chi_\gamma\ll1$, a redução assintótica é:

$$
\kappa_B
\simeq
0.23
\frac{\alpha}{\bar\lambda_C}
\frac{B_\perp}{B_Q}
\exp\left(
-\frac{4}{3\chi_\gamma}
\right).
$$

Ela demonstra a sensibilidade exponencial, mas não é uma comparação
experimental independente.

## 12. O que foi demonstrado

Ficam estabelecidos:

1. o background positrônico conjugado;
2. a função de fontes nuclear e magnética;
3. a impossibilidade do canal de um fóton no vácuo;
4. os limiares nuclear e magnético;
5. a forma variacional dos vértices;
6. a identidade de Ward no limite projetado;
7. taxas líderes e benchmarks sem pós-ajuste.

Ficam em extensão:

1. $\Phi_N$ e $\Phi_B$ 8D completos;
2. $P_{\rm phys}$ e os modos normalizados nesses backgrounds;
3. avaliação direta de $D^3\mathcal S_{\rm GDQ}$ e
   $D^4\mathcal S_{\rm GDQ}$;
4. polarizações, contatos solitônicos e correções superiores.

O script
[[../scripts/pares_eletromagneticos_reduzidos.py]]
reproduz limiares, identidade de Ward, taxas e benchmarks.

## 13. Referências de comparação

- A. Ishida, “Precise measurement of positronium,” *Progress of Theoretical
  and Experimental Physics* **2012**, 04D003:
  <https://doi.org/10.1093/ptep/pts073>.
- J. M. Brabant, R. W. Kenney e R. Wallace, “Electron Pair-Production Cross
  Sections at 2.5 Bev,” *Physical Review* **107**, 604 (1957):
  <https://doi.org/10.1103/PhysRev.107.604>.
- T. Erber, “High-Energy Electromagnetic Conversion Processes in Intense
  Magnetic Fields,” *Reviews of Modern Physics* **38**, 626 (1966):
  <https://doi.org/10.1103/RevModPhys.38.626>.
