# Ponte global--local — resultado do ciclo agentivo causal

## 1. Objetivo

O ciclo procurou completar, em sequência:

$$
\text{imersão causal}
\to
\mathcal H_\xi
\to
\mathcal C_E
\to
\text{posto 10}
\to
\text{sela}
\to
P^{\rm phys}
\to
\text{gap}.
$$

## 2. Resultado dedutivo novo

Foi construída uma imersão causal local compatível com a Questão 2,
selecionando $S^1_{\theta_0}\subset T^4$ como círculo-relógio. Isso exige
separar o warp toroidal em $A_0$ e $A_s$. A redução completa está em
`topicos/ponte_global_local/ponte_global_local_exterior_causal.md`.

Foram derivados diretamente da ação oficial:

1. a torção $H=d_J^c\omega$ no ansatz causal;
2. $|H|^2$;
3. o escalar de Levi--Civita;
4. o funcional de primeira ordem;
5. a restrição do lapse;
6. os momentos e sua inversão exata;
7. a energia relativa reduzida como resposta on shell ao período causal.

A energia reduzida é

$$
\mathcal H_\xi^{\rm red}
=\frac{p_0^{\rm full}-p_{0,\rm ref}^{\rm full}}{\beta_E}.
$$

Ela contém a torção dentro do ansatz porque $p_0$ é derivado depois da
substituição constitutiva $H=d_J^c\omega$. Não é o Hamiltoniano radial.

## 3. Verificações

O teste simbólico obteve

$$
\det M_C=32,
$$

recuperou exatamente o exterior Berger anterior quando $A_0=A_s$ e confirmou
o momento conjugado a $x_0=\log A_0$.

O teste de integração preservou a restrição do lapse com erro máximo

$$
2{,}665\times10^{-15}.
$$

Esses resultados são testes de consistência da redução, não uma sela física.

## 4. Normalização global adotada

Por instrução explícita do autor, a normalização energética não é um novo dado
independente: ela é definida no universo global de Einstein e vinculada à
estrutura fina. Escolhendo $R_H$ como unidade de comprimento,

$$
\widehat R_H=1,
$$

as relações globais já estabelecidas fornecem

$$
\widehat\beta_E=2\pi,
$$

$$
\widehat R_{\rm cos}=\pi^2\sqrt\alpha,
$$

quando $R_{\rm cos}$ é a fibra $R$ da colagem da Q38, e a unidade energética
de horizonte

$$
E_0=\frac{c^4R_H}{2G}
$$

fornece

$$
\widehat E_H=\frac{E_H}{E_0}=1.
$$

Assim, a escala absoluta não participa da determinação da forma adimensional
da sela. Ela retorna apenas na conversão metrológica final.

O setor causal global ainda deve ser realizado por uma das construções
equivalentes:

1. o recobrimento universal do círculo-relógio; ou
2. a continuação OS do gerador euclidiano.

Para a energia relativa, o background de referência natural é o background
homogêneo de Einstein com a mesma métrica induzida e sem defeito. Nesse setor,
as derivadas normais desaparecem e $p_{0,\rm ref}=0$. Essa referência deve ser
mantida congelada durante a busca.

## 5. Estado preciso

$$
\boxed{
\begin{aligned}
&\mathcal C_R:\ \text{derivado, implementado e posto }8\to9;\\
&\mathcal C_E^{\rm red}:\ \text{derivado condicionalmente no ansatz causal};\\
&\text{sela física}:\ \text{aguarda inserir a normalização global no solver};\\
&P^{\rm phys}\text{ e gap}:\ \text{aguardam a sela.}
\end{aligned}
}
$$

Mesmo depois da sela reduzida, o gap físico integral exigirá incluir
$\delta J$, modos tensoriais e harmônicos não homogêneos. A matriz
$D\mathfrak F^TD\mathfrak F$ do tiro não deve ser confundida com a Hessiana
física do funcional aumentado.

## 6. Próxima execução

Não faltam novos parâmetros físicos. Deve-se agora inserir no solver:

1. $\widehat R_{\rm cos}=\pi^2\sqrt\alpha$;
2. $\widehat\beta_E=2\pi$;
3. $\widehat E_H=1$;
4. $p_{0,\rm ref}=0$ no background homogêneo de Einstein;
5. o prefator reduzido expresso na mesma unidade $E_0$.

Com essa normalização, o próximo script terá onze parâmetros e onze resíduos: a
separação $A_0/A_s$ adiciona um parâmetro e uma condição de interface, enquanto
$\mathcal C_R$ e $\mathcal C_E$ substituem as duas linhas triviais de fase.

## 7. Atualização após a execução

O sistema $11\times11$ foi montado e executado em
`ponte_global_local_solver_final.py`. A execução foi negativa e está auditada
em `topicos/ponte_global_local/ponte_global_local_solver_final_resultado.md`. Ela demonstrou que a
normalização global por $\alpha$ não pode ser aplicada ao momento reduzido por
$p_0=1$ nem por $p_0=\Pi_G$ sem calcular o jacobiano $Z_E(\alpha)$ dos fatores
suprimidos na redução. As equações causais e $\mathcal C_R$ continuam
validados; a sela, o posto final e o gap permanecem não avaliados.
