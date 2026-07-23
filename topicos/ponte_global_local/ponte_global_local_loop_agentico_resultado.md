# Ponte global--local — resultado do loop agêntico de fechamento

## 1. Objetivo executado

Foi executado o plano de fechamento da ponte global--local, incluindo:

1. reconstrução causal da energia;
2. busca numérica da sela bulk--interface;
3. auditoria e ampliação controlada do ansatz de estrutura complexa;
4. preparação do projetor e da Hessiana física;
5. testes de estabilidade permitidos pelo background efetivamente obtido.

Nenhum parâmetro cosmológico ou espectral foi ajustado pelo alvo.

## 2. Porta A — aprovada no setor estacionário

O mapa físico já usado nas Questões 4, 9 e 29 é o projetor causal normalizado

$$
\mathfrak P_\gamma[F]
=\frac{1}{2\pi i w_\gamma}
\oint_\gamma F(z)\frac{dz}{z}.
$$

Logo,

$$
\mathfrak P_\gamma[1]=1
$$

e, no ansatz estacionário,

$$
\boxed{K_\gamma=1.}
$$

Esse resultado é uma extração de Laurent, não uma alteração da ação nem uma
calibração do solver. Para uma família causal não estacionária, o projetor
deve atuar no integrando completo e não pode ser fatorado.

## 3. Ramo integrável original

O solver causal foi reconstruído com:

- duas interfaces independentes;
- normalização global acumulada;
- vínculo de raio;
- vínculo energético com $K_\gamma=1$;
- Jacobiana transportada pelas equações variacionais;
- validação independente por diferenças centrais.

Os dez vínculos anteriores à energia possuem posto dez. Com a energia, o
sistema possui posto onze ao longo do ramo regular testado.

A homotopia reduziu o resíduo até aproximadamente

$$
\|\mathfrak F\|_\infty=1{,}29\times10^{-4}
$$

no setor energético parcial. Uma busca com tolerâncias estritas e Jacobiana
central independente não encontrou passo descendente que produzisse uma raiz.
O resíduo convergente ficou concentrado no matching dos momentos
$(p_a,p_c,p_u)$.

Portanto não foi obtida sela no ramo original.

## 4. Ampliações testadas

### 4.1 Momentos de garganta

A regularidade da garganta suave implica exatamente

$$
p_c=p_u=0.
$$

A matriz que relaciona $(p_c,p_u)$ a $(c',u')$ é não singular. Assim, liberar
esses momentos independentemente violaria a regularidade; a tentativa com
$p_c$ livre retornou numericamente a zero.

### 4.2 Rotação cohomogeneidade--1 de $J$

Foi construída uma família quase-hermitiana $J_\chi$ e derivada sua
contribuição completa à ação reduzida. Os testes variacionais de momentos e
restrição passaram. Contudo, o tensor de Nijenhuis fornece

$$
N_{J_\chi}=0
\quad\Longrightarrow\quad
\chi'=0.
$$

Logo, o modo contínuo $\chi(s)$ não pertence à geometria Hermitiana--Bismut
oficial e foi excluído antes da busca numérica.

### 4.3 Beltrami toroidal

No fator toroidal,

$$
H^{0,1}(T^{1,0}T^4)\simeq\mathbb C^4.
$$

O primeiro representante não gauge satisfaz Maurer--Cartan exatamente, mas

$$
\delta H=0,
\qquad
\Pi_\mu=0.
$$

Ele é um módulo global zero e não se acopla ao tripleto residual de matching.

### 4.4 Interface Kodaira--Spencer

A segunda variação oficial produz matching homogêneo nos momentos aumentados:

$$
[\mu]_Y=0,
\qquad
\Pi_{J,-}^{\rm aug}+\Pi_{J,+}^{\rm aug}=0.
$$

Após eliminar os bulks surge uma impedância DtN, mas sem fonte nem coeficiente
Robin livre. A auditoria confirmou também que o solver de background já usa
os momentos vinculados e não omite uma mola de interface.

## 5. Ramo integrável discreto

O segundo ramo permitido por Nijenhuis é

$$
\chi=\frac\pi2\pmod\pi,
$$

com

$$
\frac{a'}a-\frac{c'}c-\frac2c+\frac{2c}{a^2}=0.
$$

Foi construída uma DAE Hamiltoniana bordada. Sua matriz é regular:

$$
\det\mathbb M_{\rm DAE}
=\frac{20}{a^2c^2}\neq0.
$$

Os testes recuperaram velocidades e multiplicadores com erros da ordem de
$10^{-15}$. Depois de corrigir a normalização para incluir os dois colares e
o exterior, remover a redundância exata $y=z$ e fixar a liberdade auxiliar do
multiplicador, a otimização reduziu o resíduo somente pela sequência

$$
L_L\longrightarrow0,
\qquad
L_R\longrightarrow0.
$$

O melhor resíduo registrado foi

$$
\|\mathfrak F\|_\infty\simeq4{,}48\times10^{-4},
$$

dominado pelo matching de $p_u$. Não surgiu ponto crítico interior com colares
de comprimento positivo.

Assim:

$$
\boxed{
\text{não existe sela bulk--interface não degenerada nos dois ramos}
\text{ integráveis homogêneos/cohomogeneidade--1 testados.}
}
$$

Esta é evidência numérica convergente acompanhada por no-gos analíticos das
ampliações locais; não é teorema de inexistência da GDQ completa.

## 6. Portas C e D

A infraestrutura de $P^{\rm phys}$ e da Hessiana aumentada foi implementada.
Os testes algébricos deram resíduos entre $10^{-14}$ e $10^{-13}$. Entretanto,
sem sela não degenerada não existem coeficientes físicos nos quais avaliar

$$
K_*^{\rm phys}
=P^{{\rm phys}\dagger}\mathbb H_*P^{\rm phys}.
$$

Consequentemente:

- nenhum autovalor sintético foi interpretado como físico;
- estabilidade não foi demonstrada;
- gap físico não foi calculado;
- refinamento espectral da Porta D não é aplicável ao background inexistente.

## 7. Veredito científico

O loop foi concluído para toda a classe homogênea/cohomogeneidade--1
atualmente derivada. Seu resultado é negativo e forte:

$$
\boxed{
\text{a ponte global--local não fecha no ansatz homogêneo vigente.}
}
$$

Se esse ansatz for postulado como descrição exaustiva da física, os vínculos
globais e a interface são incompatíveis. A ação oficial, porém, admite campos
não homogêneos. Portanto a conclusão não pode ser promovida a inconsistência
da GDQ completa sem analisar o primeiro modo interno integrável do complexo
de Kodaira--Spencer com seu domínio elíptico de bordo.

## 8. Próxima e única rota não excluída

Derivar e resolver um background não homogêneo, começando por:

1. operador de Kodaira--Spencer no colar sobre o background warped;
2. domínio auto-adjunto/condição elíptica obtida da Hessiana oficial;
3. primeiro autovetor interno não gauge;
4. backreaction desse modo em $(g,J,f)$;
5. novo problema de sela multidomínio;
6. somente após a sela, $P^{\rm phys}$, Hessiana e gap.

Essa rota muda a classe funcional do background; não corresponde a ajustar
um parâmetro do ansatz que falhou.

## 9. Classificação

- Porta A estacionária: **fechada**;
- formulação e testes da Porta C: **fechados estruturalmente**;
- sela homogênea: **resultado numérico negativo**;
- estabilidade e gap: **abertos**, pois dependem de uma sela não homogênea;
- ponte global--local integral: **parcialmente resolvida, não fechada**.
