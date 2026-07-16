# Q30 — Ansatz de torção sem elongação

## 1. Hipótese proposta

A sugestão do autor é formalizada como:

$$
\boxed{
\text{modos de elongação congelados; modos de torção/conexão permitidos.}
}
$$

No setor interno de cor, isso significa preservar a métrica Hermitiana e o
volume das três câmaras,

$$
\delta G_C=0,
\qquad
\delta\det G_C=0,
$$

permitindo rotações locais de frame

$$
\mathcal A_C\in\Omega^1(N,\mathfrak{su}(3)).
$$

Essa condição é compatível com a origem de $SU(3)$ na Q28: transformações
unitárias que preservam o volume complexo. Ela ainda deve ser verificada como
truncagem consistente da ação, não adotada silenciosamente como novo axioma.

## 2. Coframe torcido

Seja $e^a$ um coframe ortonormal do subfibrado $E_C$. A deformação permitida é
uma rotação de frame,

$$
De^a
=de^a+(\mathcal A_C)^a{}_b\wedge e^b,
$$

com

$$
\mathcal A_C^\dagger=-\mathcal A_C,
\qquad
\operatorname{tr}\mathcal A_C=0.
$$

A curvatura é

$$
\boxed{
\mathcal F_C
=d\mathcal A_C+\mathcal A_C\wedge\mathcal A_C.
}
$$

Na linguagem fundamental, $\mathcal A_C$ é uma componente da conexão
Hermitiana/Bismut projetada em $E_C$. A notação coincide com Yang--Mills, mas
a origem é geométrica GDQ.

## 3. Separação entre elongação e torção

Escreva localmente a variação do coframe como

$$
\delta e=M e,
\qquad
M=S+K,
\qquad
S^\dagger=S,
\qquad
K^\dagger=-K.
$$

Então:

1. $S$ altera comprimentos e ângulos métricos: é o setor de elongação;
2. $K$ gira o frame preservando a métrica: é o setor torsional/conexão;
3. $\operatorname{tr}S$ altera o volume;
4. $K\in\mathfrak{su}(3)$ preserva métrica, orientação e volume complexo.

A hipótese do autor equivale a

$$
\boxed{S=0,\qquad K\ne0.}
$$

## 4. Por que o no-go diagonal é evitado

No ansatz diagonal anterior, toda torção vinha de derivadas radiais dos
fatores de escala $W,P,Q$. Congelar elongações força essas derivadas a zero,
mas não força $\mathcal A_C$ nem $\mathcal F_C$ a zero.

Assim,

$$
W'=P'=Q'=0
$$

elimina a torção diagonal logarítmica, enquanto

$$
\mathcal F_C\ne0
$$

pode sustentar holonomia não trivial. O mecanismo deixa de depender de
esticar o toro ou as câmaras internas.

## 5. Teste de truncagem consistente

Congelar $S$ é legítimo somente se a equação de Euler--Lagrange desse setor
for satisfeita quando $S=0$:

$$
\boxed{
\left.
\frac{\delta\mathcal S_{\rm GDQ}}{\delta S}
\right|_{S=0,\,K\ne0}=0.
}
$$

Em geral, a energia de $\mathcal F_C$ produz tensão métrica e pode sourcear
elongação. Portanto, “elongações não são permitidas” não segue apenas da
cinemática unitária; é necessário que:

1. um vínculo de volume/rigidez já presente imponha $S=0$; ou
2. a tensão de $K$ seja balanceada por $u=\operatorname{Re}f$, curvatura e
   medida ponderada; ou
3. $S$ seja pesado e possa ser integrado, produzindo uma redução efetiva.

Sem uma dessas verificações, $S=0$ seria uma restrição externa.

## 6. Forma quadrática esperada da conexão

A redução de uma curvatura geométrica em um fibrado com métrica interna fixa
tem, no nível quadrático, a estrutura

$$
\mathcal R_8
=\mathcal R_{\rm base}+\mathcal R_{\rm int}
-\frac14\langle\mathcal F_C,\mathcal F_C\rangle_{G_C}
+\text{divergências e termos de torção}.
$$

Esse é um resultado de redução da curvatura, não a inserção de uma ação de
Yang--Mills. Contudo, o sinal da **energia física transversal** não pode ser
lido isoladamente do sinal de $\mathcal R$ na ação euclidiana, dos termos de
bordo e da subtração do background. A positividade de $\sigma$ ainda deve ser
obtida da forma quadrática física completa.

## 7. Modelo axisimétrico mínimo da holonomia

Escolha um gerador Cartan normalizado $T\in\mathfrak{su}(3)$ e

$$
\mathcal A_C=a(r)T\,d\theta.
$$

Como $[T,T]=0$ nesse subansatz,

$$
\boxed{
\mathcal F_C=a'(r)T\,dr\wedge d\theta.
}
$$

A holonomia em um círculo de raio $r$ é

$$
\operatorname{Hol}_r
=\exp\left(2\pi a(r)T\right).
$$

Condições naturais são

$$
a(0)=0,
\qquad
a(\infty)=a_\infty,
$$

onde $a_\infty$ é fixado pela classe de holonomia e não ajustado por uma
tensão alvo.

## 8. Resultado desta etapa

A proposta “torção permitida, elongação não” resolve a direção arquitetural:

$$
\boxed{
\text{Q30 deve ser calculada no setor de conexão unitária com módulos
internos congelados, sujeito ao teste dinâmico de consistência.}
}
$$

O próximo cálculo é inserir $\mathcal A_C=a(r)T d\theta$ na curvatura da
métrica/conexão Bismut, extrair o coeficiente radial de $(a')^2$ e calcular a
equação do setor de elongação em $S=0$. Isso decidirá se o chute é uma solução
da GDQ ou apenas uma restrição cinemática.

Esse teste foi executado em `q30/teste_variacional_sem_elongacao.md`. O
resultado é que $S=0$ não é automático, mas é consistente quando $u,v,a$
satisfazem o vínculo de balanço derivado da própria ação.

## 9. Classificação

- decomposição $M=S+K$: identidade linear algébrica;
- preservação métrica por $K\in\mathfrak{su}(3)$: exata;
- congelamento $S=0$: hipótese do autor em auditoria;
- forma $\mathcal F_C=d\mathcal A_C+\mathcal A_C^2$: derivação geométrica;
- consistência dinâmica e valor de $\sigma$: pendentes.
