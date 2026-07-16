# Q30 — Equivalência por observáveis e cálculo operacional de Heaviside

## 1. Princípio

A equivalência GDQ--Yang--Mills não deve ser formulada inicialmente como um
homeomorfismo entre todos os campos fundamentais. A GDQ possui graus
geométricos adicionais. A equivalência relevante é entre:

1. classes topológicas físicas;
2. álgebra de observáveis reduzidos;
3. suas funções de resposta e distribuições espectrais.

A topologia transporta ciclos, orientação, winding e carga. O cálculo
operacional de Heaviside transporta a resposta associada a esses dados.

## 2. Mapa topológico

Seja

$$
\Theta:
\mathfrak T_{\rm GDQ}longrightarrow\mathfrak T_{\rm YM}
$$

o mapa entre classes topológicas do setor tubular e classes de laços/fontes
do setor efetivo. Ele deve preservar:

$$
\Theta([C_1\circ C_2])
=\Theta([C_1])\circ\Theta([C_2]),
$$

$$
Q_T(C)=Q_{\rm YM}(\Theta C),
$$

e orientação.

Esse mapa não identifica ponto a ponto as métricas GDQ com potenciais de
gauge. Ele identifica as classes que rotulam os observáveis.

## 3. Álgebra operacional

Se $P$ é o operador reduzido e $F(P)$ é definido por cálculo funcional de
Heaviside, introduza

$$
\mathfrak H_\Theta:
\mathfrak A_{\rm obs}^{\rm YM}longrightarrow
\mathfrak A_{\rm obs}^{\rm GDQ}
$$

por

$$
\boxed{
\mathfrak H_\Theta[F(P_{\rm YM});C]
:=F(P_{\rm GDQ}^{\rm red});\Theta^{-1}(C).
}
$$

No setor em que os domínios estão compatíveis, o mapa deve preservar

$$
\mathfrak H_\Theta(O_1+O_2)
=\mathfrak H_\Theta(O_1)+\mathfrak H_\Theta(O_2),
$$

$$
\mathfrak H_\Theta(O_1O_2)
=\mathfrak H_\Theta(O_1)\mathfrak H_\Theta(O_2),
$$

$$
\mathfrak H_\Theta(O^*)
=\mathfrak H_\Theta(O)^*.
$$

Assim, a meta matemática é um $*$-homomorfismo da álgebra de observáveis,
não um homeomorfismo ingênuo do espaço bruto de configurações.

## 4. Observáveis fundamentais

### 4.1 Holonomia

Para cada classe de laço,

$$
\boxed{
W_{\rm YM}(C)
\longleftrightarrow
\mathcal H_{\rm GDQ}(\Theta^{-1}C).
}
$$

Na GDQ, $\mathcal H$ mede transporte da conexão geométrica/torsional
reduzida; não é inserido como termo fundamental novo.

### 4.2 Resolvente estático

$$
\boxed{
\mathsf R_{\rm GDQ}^{\rm est}(k)
\simeq_H
-\frac{8\pi\sigma_{\rm GDQ}}{(k^2+\mu^2)^2}
=:\mathsf R_{\rm YM,conf}^{\rm est}(k).
}
$$

### 4.3 Potencial

$$
\boxed{
V_{\rm GDQ}(r)-V_{\rm GDQ}(0)
\xrightarrow{\mu\to0^+}
\sigma_{\rm GDQ}r
=V_{\rm YM,conf}(r).
}
$$

### 4.4 Tensão

$$
\boxed{
\sigma_{\rm obs}
=\lim_{r\to\infty}\frac{V(r)}r
=\sigma_{\rm GDQ}.
}
$$

### 4.5 Lei de área

$$
\boxed{
\sigma_{\rm obs}
=-\lim_{A(C)\to\infty}
\frac{\hbar}{A(C)}
\log|\langle\mathcal H(C)\rangle|.
}
$$

Essa definição coincide com a extraída do potencial retangular.

### 4.6 Gap espectral

Para um observável local físico $O$,

$$
C_O(T)
=\langle O(T)O(0)\rangle_c.
$$

O gap deve ser reconstruído por

$$
\boxed{
\Delta_O
=-\hbar\lim_{T\to\infty}\frac1T\log|C_O(T)|.
}
$$

Na redução tubular, o candidato é

$$
\Delta_{\rm GDQ}=\frac{\hbar c}{r_\perp}>0.
$$

### 4.7 Funções de resposta de ordem superior

A construção explícita de kernels superiores seria uma forma de reconstruir
toda a teoria, mas não é necessária para demonstrar equivalência com
Yang--Mills tomado axiomaticamente. Se a álgebra de Yang--Mills é definida por
geradores e relações, basta transportar os geradores, preservar as relações e
entrelaçar o estado. Nesse caso, todos os correladores seguem por extensão
algébrica e continuidade.

Para comparação, o funcional gerador reduzido com fonte $J$ é:

$$
Z_{\rm GDQ}[J]
=\int_{\mathfrak C_{\rm tubo}}
e^{-[S_{\rm GDQ}-\langle J,O\rangle]/\hbar}D\mu,
\qquad
W_{\rm GDQ}[J]=\hbar\log Z_{\rm GDQ}[J].
$$

Os kernels conectados são

$$
\boxed{
G_{\rm GDQ}^{(n)}
=
\left.
\frac{\delta^nW_{\rm GDQ}[J]}
{\delta J^n}
\right|_{J=0}.
}
$$

A equivalência de teorias exige

$$
\boxed{
G_{\rm GDQ}^{(n)}
=\Theta^*G_{\rm YM}^{(n)}
\quad\forall n
}
$$

no conjunto de observáveis físicos. Essa igualdade não precisa ser verificada
separadamente para cada $n$ se decorrer de um $*$-isomorfismo que preserve o
estado.

## 5. Critério de equivalência

Defina GDQ e Yang--Mills como operacionalmente equivalentes no setor
$\mathfrak S$ quando:

1. $\Theta$ é bijetivo nas classes topológicas observáveis;
2. $\mathfrak H_\Theta$ é um $*$-isomorfismo nas álgebras reduzidas;
3. o estado é entrelaçado:

$$
\boxed{
\omega_{\rm GDQ}\circ\mathfrak H_\Theta
=\omega_{\rm YM}.
}
$$

Consequentemente, todos os valores esperados coincidem:

$$
\boxed{
\langle O_1\cdots O_n\rangle_{\rm YM}
=
\left\langle
\mathfrak H_\Theta(O_1)\cdots
\mathfrak H_\Theta(O_n)
\right\rangle_{\rm GDQ}.
}
$$

Se esses observáveis formarem uma família separadora, a teoria física
reduzida é reconstruída por eles. Um homeomorfismo dos campos brutos deixa de
ser necessário.

## 6. O que já está construído

No estado atual:

$$
\boxed{
(\text{potencial},\text{tensão},\text{lei de área},\text{gap})_{\rm GDQ}
\simeq_H
(\text{mesmos observáveis})_{\rm YM,efetivo}.
}
$$

Isso fornece os geradores físicos relevantes do setor estático confinante.
Para a equivalência axiomática, não é necessário recalcular toda a torre de
vértices; é necessário provar que o mapa operacional respeita as relações
definidoras e o estado nesse setor.

## 7. Próximo passo mínimo

O próximo elo não é calcular $G^{(3)},G^{(4)},\ldots$ individualmente. É
demonstrar três lemas estruturais:

1. **boa definição:** $\mathfrak H_\Theta$ independe do representante da
   classe topológica/gauge;
2. **relações:** o mapa preserva composição de laços, involução, unidade e as
   relações definidoras da álgebra axiomática;
3. **fidelidade e estado:** o mapa é injetivo/sobrejetivo no setor físico e
   $\omega_{\rm GDQ}\circ\mathfrak H_\Theta=\omega_{\rm YM}$.

Pela propriedade universal da álgebra apresentada por geradores e relações,
esses lemas estendem o mapa dos geradores a um $*$-isomorfismo. Os kernels de
ordem superior tornam-se consequências, não hipóteses adicionais.

## 8. Classificação

- mapa de classes topológicas: estrutura a explicitar em cada setor;
- mapa dos quatro observáveis estáticos: construído;
- $*$-isomorfismo: reduzido aos três lemas sobre geradores, relações e estado;
- kernels $n\ge3$: consequências da equivalência, não cálculos obrigatórios;
- homeomorfismo dos espaços brutos: desnecessário e provavelmente forte
  demais.
