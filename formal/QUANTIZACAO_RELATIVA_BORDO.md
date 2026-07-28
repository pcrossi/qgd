# Formalização da quantização relativa por bordo

## Enunciado certificado

O módulo `GDQ/BoundaryPhaseQuantization.lean` formaliza a camada algébrica do
teorema condicional

$$
\text{identificação global}
+
\text{carga conservada}
+
\exp(iI_{\rm phys}/\hbar)\text{ bem definida}
\Longrightarrow
Q_S\Delta S_R\in h\mathbb Z.
$$

No setor primitivo selecionado independentemente como $Q_S=1$:

$$
\Delta S_R\in h\mathbb Z.
$$

## No-go local

O módulo distingue uma mudança constante de toda a história,

$$
S_R\longmapsto S_R+c,
$$

de uma interpolação dependente do tempo,

$$
S_R\longmapsto S_R+a(t)\Delta S_R.
$$

Para o deslocamento constante, o termo de extremidade é exatamente zero para
todo $c\in\mathbb R$. Sua ação exponenciada é, portanto, invariável sem impor
qualquer integralidade.

Para a interpolação com $a(t_1)=0$ e $a(t_2)=1$, a redução canônica produz,
sob conservação da carga,

$$
\Delta I_{\rm red}=Q_S\Delta S_R.
$$

Se os extremos são identificados fisicamente e a ação reconstruída recebe o
peso $\exp(iI_{\rm phys}/\hbar)$, Lean prova

$$
Q_S\Delta S_R=2\pi\hbar n.
$$

## Conservação

A camada algébrica da lei de Stokes também foi formalizada:

$$
Q_2-Q_1+\Phi_{\rm lateral}=0,
\qquad
\Phi_{\rm lateral}=0
\Longrightarrow
Q_2=Q_1.
$$

Quando o fluxo que sai do objeto entra no aparelho, conserva-se a soma das
cargas do sistema composto.

## Hipóteses que permanecem visíveis

O código não postula nem finge demonstrar:

1. existência das folhas físicas;
2. regularidade necessária ao teorema de Stokes no background concreto;
3. reconstrução de uma ação lorentziana real em todo contorno;
4. identificação física dos extremos;
5. discreção do reticulado de cargas;
6. seleção do setor primitivo.

Esses dados pertencem à admissibilidade global do problema. A densidade local
da ação oficial fornece a corrente contínua, mas não fabrica sozinha o
reticulado inteiro.

## Classificação formal

O módulo distingue seis classes:

1. topológica circular;
2. relativa/de bordo;
3. trivial;
4. spinorial/Hopf;
5. aberta com fuga de fluxo;
6. obstruída.

Essa classificação impede promover o resultado relativo de uma classe a todo
background da ação oficial.

## Verificação

O módulo foi incluído em `GDQ.lean` e o pacote completo foi recompilado:

```text
lake build GDQ.BoundaryPhaseQuantization GDQ
Build completed successfully (3696 jobs).
```

A fonte não contém declarações `axiom`, nem lacunas `sorry` ou `admit`.

A consulta `#print axioms` aos quatro teoremas centrais encontrou somente:

```text
propext
Classical.choice
Quot.sound
```

São princípios fundacionais padrão da Mathlib, não axiomas físicos da GDQ.
