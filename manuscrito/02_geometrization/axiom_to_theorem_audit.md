---
title: Auditoria de axiomas e teoremas
---

# Auditoria de axiomas e teoremas

Esta nota verifica quais elementos usados na construção da GDQ precisam ser
mantidos como axiomas e quais já seguem de escolhas anteriores, de teoremas
matemáticos ou de resultados posteriores do próprio programa.

## Critério de promoção

Uma afirmação deixa de ser axioma apenas quando existe uma cadeia do tipo

$$
\text{dados anteriores}
\longrightarrow
\text{hipóteses explícitas}
\longrightarrow
\text{resultado demonstrado}.
$$

Concordância numérica, motivação física ou unicidade dentro de um ansatz não
bastam. Se a demonstração vale somente numa classe de backgrounds ou sob
condições adicionais, o resultado é um **teorema condicional**.

## Elementos promovidos

| Elemento | Classificação corrigida | Razão |
|---|---|---|
| $n=4$ | consequência | Escolhido $M=\mathbb R^4\times T^4$, tem-se dimensão real oito; admitida uma estrutura complexa, a dimensão complexa é quatro. |
| Existência de estruturas de spin | teorema | Os fatores são paralelizáveis; logo $M$ é paralelizável e $w_2(M)=0$. |
| Número de estruturas de spin no toro | teorema | Elas formam um torsor sobre $H^1(T^4;\mathbb Z_2)\cong(\mathbb Z_2)^4$, dando $16$ escolhas. |
| Conexão de Bismut | teorema de unicidade | Numa variedade Hermitiana complexa, é a única conexão que preserva $g$ e $J$ e tem torção totalmente antissimétrica. |
| Expoente $4$ em $(4\pi z_\tau)^{-4}$ | consequência dimensional | Em dimensão real $d=2n=8$, o kernel plano tem potência $d/2=4$. |
| Dimensão de $\tau$ | consequência dimensional | De $\tau\mathcal R$ adimensional e $[\mathcal R]=L^{-2}$ segue $[\tau]=L^2$. |
| Decomposição de $f$ | identidade | Das definições constitutivas segue $f=-\ln\rho+iS_R/\hbar$. |
| Variação de $\mathcal U$ | identidade | Para métrica fixa, $\delta\mathcal U/\mathcal U=-\delta(f+\bar f)/2$. |
| Métrica lorentziana reconstruída | teorema | Dada uma forma-relógio admissível, a reflexão em sua direção produz assinatura $(-,+,+,+)$. |
| Seleção da forma-relógio | teorema no background cosmológico adotado | A simultaneidade comóvel de $T^5\times S^3$ distingue a 1-forma normal; a sincronização no evento comum fixa sua escala, o limite apontado fornece a direção temporal local e $\gamma$ fixa a orientação. Não resta escolha local arbitrária. |
| Spin antiperiódico | teorema condicional | Dada holonomia $-1$, a antiperiodicidade segue; a produção dinâmica da holonomia deve ser demonstrada no background. |
| Transporte global--local | teorema aplicado | Admitidos a família apontada, localização e gap uniforme, seguem a convergência dos operadores e projetores físicos. |
| Três centros estacionários | teorema no modelo reduzido | Vale na classe estacionária e com os vínculos demonstrados; não é ainda um teorema universal de todo background cosmológico. |

## Núcleo axiomático reduzido

Permanecem como escolhas estruturais:

1. a ação oficial e seus campos fundamentais;
2. a classe geométrica local, incluindo $M=\mathbb R^4\times T^4$ e a
   admissão de estrutura complexa Hermitiana;
3. a classe causal do contorno $\gamma$;
4. as condições globais e de bordo que selecionam o setor físico;
5. as escalas físicas ainda não derivadas, como $\ell_C$ ou
   $E_C=\hbar c/\ell_C$, e a escala difusiva $\nu_0$. O símbolo
   $\Lambda_C$ da ação é o corte adimensional, não uma dessas escalas.

O valor $n=4$, a existência de spin, a conexão de Bismut e a potência do kernel
de calor não devem reaparecer como axiomas independentes.

## Candidatos a teoremas condicionais de unicidade

### Medida ponderada

A forma

$$
\mathcal U=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^4}
$$

pode ser caracterizada como única, a menos de normalização, se forem exigidos:
positividade euclidiana, dependência multiplicativa em $\operatorname{Re}f$,
limite plano do kernel de calor em oito dimensões e continuação causal em
$z_\tau$. Sem essa prova, ela permanece uma definição constitutiva.

### Variável causal complexa

A escolha

$$
z_\tau=\tau+i\nu_0t
$$

pode ser única dentro da classe afim mínima sob homogeneidade dimensional,
conjugação por reversão temporal e recuperação do setor difusivo em $t=0$.
Isso não exclui construções causais não lineares.

### Realidade da ação

A realidade de $\mathcal S_{\rm GDQ}$ é demonstrável para contornos invariantes
por conjugação e backgrounds com reflexão de Schwarz. Portanto, é condicional
à classe de $\gamma$, não automática para todo contorno complexo.

## Elementos ainda não promovíveis

- seleção dinâmica exclusiva de $\mathbb R^4\times T^4$;
- escolha física entre as $16$ estruturas de spin do toro;
- existência dinâmica da foliação cosmológica comóvel que fornece o relógio;
- determinação absoluta de todas as escalas e constantes;
- existência e unicidade de backgrounds em todos os setores;
- resultados universais inferidos de ansätze reduzidos ou simulações;
- qualquer coeficiente escolhido pelo alvo experimental.

## Consequência editorial

O manuscrito deve apresentar primeiro o núcleo mínimo de escolhas. Cada
consequência deve então aparecer como proposição, lema ou teorema condicional,
com suas hipóteses próximas. Isso reduz a carga axiomática sem esconder o que
ainda precisa ser demonstrado.
