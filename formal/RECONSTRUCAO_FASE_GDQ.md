# Reconstrução constitutiva da fase e quantização

## 1. Enunciado certificado

O módulo `GDQ/PhaseReconstruction.lean` formaliza a cadeia:

$$
f
\longrightarrow
\rho(f)
\quad\text{e}\quad
e^{i\operatorname{Im}f}
\longrightarrow
\Psi(f)
\longrightarrow
\text{laço admissível em }U(1)
\longrightarrow
\Delta S_R=nh.
$$

O resultado não substitui a ação oficial e não introduz uma função de onda
fundamental. O estado complexo é reconstruído de `f`.

## 2. Relações constitutivas

Lean usa:

$$
\rho(f)=e^{-\operatorname{Re}f},
$$

$$
u(f)=e^{i\operatorname{Im}f},
$$

e:

$$
\Psi(f)=\sqrt{\rho(f)}\,u(f).
$$

Foram provadas exatamente:

$$
|u(f)|=1,
$$

$$
|\Psi(f)|^2=\rho(f),
$$

e:

$$
\Psi(f)\ne0
$$

para todo potencial complexo finito.

Para uma configuração oficial, no locus regular:

$$
|\Psi_\Phi(x)|^2=\rho_\Phi(x).
$$

## 3. Simetria de fase

Para:

$$
f_c=f+ic,
$$

Lean prova:

$$
\operatorname{Re}f_c=\operatorname{Re}f,
$$

$$
\operatorname{Im}f_c=\operatorname{Im}f+c,
$$

$$
\rho(f_c)=\rho(f),
$$

e:

$$
u(f_c)=u(f)e^{ic}.
$$

Em particular, para $k\in\mathbb Z$:

$$
u(f+2\pi k i)=u(f),
$$

$$
\Psi(f+2\pi k i)=\Psi(f).
$$

Isso certifica a identificação periódica dos levantamentos locais.

## 4. Relação com a ação oficial

Também foi provado que, mantendo explícitos os dados geométricos:

1. o termo real não derivativo do colchete oficial é invariável sob
   $f\mapsto f+ic$;
2. o kernel oficial construído de $\rho$ é invariável;
3. a densidade pontual oficial é invariável quando o quadrado do gradiente é
   mantido — como deve ocorrer após diferenciar um deslocamento constante.

Esse último enunciado é pontual. A formalização diferencial completa da
igualdade:

$$
d(f+ic)=df
$$

será incorporada quando a camada de campos suaves for ligada ao atlas
concreto. Não foi fingida como já disponível.

## 5. Laço do próprio potencial

Foi criado o tipo `PotentialPhaseLoop`. Ele contém:

- um caminho contínuo $f:[0,1]\to\mathbb C$;
- a condição global:

$$
e^{i\operatorname{Im}f(1)}
=
e^{i\operatorname{Im}f(0)}.
$$

Lean deduz, sem linearizar o caminho:

$$
\hbar
\left[
\operatorname{Im}f(1)-\operatorname{Im}f(0)
\right]
=
n\,2\pi\hbar.
$$

Definindo:

$$
h=2\pi\hbar,
$$

obtemos:

$$
\Delta S_R=nh.
$$

## 6. Classificação científica

O resultado é um teorema estrutural da GDQ sob sua admissibilidade global:

$$
\text{potencial oficial}
+
\text{reconstrução constitutiva}
+
\text{fechamento global }U(1)
\Longrightarrow
\text{circulação inteira}.
$$

Não se afirma que a integral pontual da ação determine sozinha a topologia do
domínio. Domínio, cobertura e condições globais pertencem à definição do
problema variacional. Tampouco se introduz um axioma independente de
“circulação quantizada”: depois que a admissibilidade global é dada, a
integralidade é demonstrada.

## 7. Integração com os demais módulos

- `GDQ/PhaseQuantization.lean`: levantamento de caminhos e circulação;
- `GDQ/PhaseReconstruction.lean`: origem constitutiva da fase em `f`;
- `GDQ/CechChern.lean`: inteiros nas interseções triplas;
- `GDQ/CechCohomology.lean`: cociclo global, quociente e classe de Chern.

Nenhum desses módulos contém `axiom`, `sorry` ou `admit`.

## 8. Verificação executada

O pacote completo foi recompilado:

```text
lake build GDQ
Build completed successfully (3694 jobs).
```

Uma consulta `#print axioms` aos teoremas finais encontrou somente:

```text
propext
Classical.choice
Quot.sound
```

Esses são princípios fundacionais padrão usados pela Mathlib, não axiomas
físicos acrescentados à GDQ. A varredura dos fontes não encontrou `axiom`,
`sorry` ou `admit`.

O teste independente do pente regularizado foi reexecutado. O erro absoluto
máximo entre a série de Fourier amortecida e o trem gaussiano foi:

$$
1.780\times10^{-15}.
$$

Esse número é teste de consistência da identidade de Poisson, não evidência
experimental nem origem da quantização.
