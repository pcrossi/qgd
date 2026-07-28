---
title: "Reconstrução OS: quociente nulo, completamento e evolução"
status: "teorema condicional setorial"
---

# Reconstrução OS: quociente nulo, completamento e evolução

## 1. Enunciado

Se um setor euclidiano admissível da GDQ fornece um domínio
$\mathcal D_+$, uma reflexão $\Theta$ e um pareamento para os quais

$$
(F,G)_{\rm OS}
=
\langle\Theta F\,G\rangle_E
$$

é sesquilinear, Hermitiano e positivo semidefinido, então:

1. os funcionais de seminorma nula formam um subespaço;
2. o pareamento desce ao quociente por esse subespaço;
3. o quociente separado possui produto interno definido positivo;
4. seu completamento é um espaço de Hilbert complexo;
5. gauges que sejam nulos para o pareamento desaparecem no mesmo quociente.

Esse resultado reconstrói a camada operacional. Ele não afirma que a ação
oficial seja substituída por uma ação euclidiana diferente.

## 2. Hipótese de positividade por reflexão

Defina

$$
\|F\|_{\rm OS}^2
=
(F,F)_{\rm OS}
=
\langle\Theta F\,F\rangle_E.
$$

A hipótese central é

$$
\|F\|_{\rm OS}^2\geq0
\qquad
\forall F\in\mathcal D_+.
$$

No formalismo Lean, essa hipótese não é escondida num nome. O domínio
$\mathcal D_+$ deve receber a estrutura de espaço com produto interno
possivelmente semidefinido induzida pelo pareamento refletido, e exige-se
explicitamente:

$$
\langle\Theta F\,G\rangle_E
=
\langle F,G\rangle_{\rm OS}.
$$

Da positividade geral do produto interno segue imediatamente

$$
0\leq
\operatorname{Re}
\langle\Theta F\,F\rangle_E.
$$

## 3. Núcleo nulo

O subespaço nulo é

$$
\mathcal N
=
\{F\in\mathcal D_+:\|F\|_{\rm OS}=0\}.
$$

Pela desigualdade de Cauchy--Schwarz semidefinida, se $N\in\mathcal N$,
então

$$
|(N,G)_{\rm OS}|^2
\leq
(N,N)_{\rm OS}(G,G)_{\rm OS}
=0.
$$

Logo

$$
(N,G)_{\rm OS}=0
$$

para todo $G$. Portanto a expressão

$$
\langle[F],[G]\rangle_{\rm sep}
:=
(F,G)_{\rm OS}
$$

não depende dos representantes.

## 4. Gauge

Se o subespaço de gauge $\mathcal G$ satisfaz

$$
\mathcal G\subseteq\mathcal N,
$$

então

$$
\mathcal N+\mathcal G=\mathcal N.
$$

Consequentemente, todo $G\in\mathcal G$ representa o vetor zero no quociente.
Essa é a situação diretamente certificada.

Se $\mathcal G$ não for nulo para a forma OS, não é correto escrever
automaticamente $\mathcal D_+/(\mathcal N+\mathcal G)$. Deve-se provar que o
pareamento é bem definido num quociente gauge-invariante, ou escolher uma
seção física ortogonal antes da reconstrução. Essa alternativa é compatível
com o projetor físico construído no Capítulo 6.

## 5. Quociente e completamento

Defina o espaço separado:

$$
\mathcal D_{\rm sep}
=
\mathcal D_+/\mathcal N.
$$

Se $[F]=0$, então $\|F\|_{\rm OS}=0$. Reciprocamente, toda seminorma nula é
identificada ao zero. Portanto a norma induzida em
$\mathcal D_{\rm sep}$ é definida positiva.

O espaço de Hilbert físico é o completamento:

$$
\boxed{
\mathcal H_{\rm phys}
=
\overline{\mathcal D_{\rm sep}}.
}
$$

A inclusão canônica preserva o pareamento:

$$
\langle\iota[F],\iota[G]\rangle_{\mathcal H_{\rm phys}}
=
\langle\Theta F\,G\rangle_E,
$$

e preserva a norma:

$$
\|\iota[F]\|_{\mathcal H_{\rm phys}}
=
\|F\|_{\rm OS}.
$$

## 6. Semigrupo euclidiano e tempo físico

Quando as translações temporais positivas preservam o domínio, o núcleo nulo
e o pareamento, elas descem ao quociente e ao completamento. O setor deve
então fornecer um semigrupo contrativo:

$$
T_E(a+b)=T_E(a)T_E(b),
\qquad
\|T_E(a)\Psi\|\leq\|\Psi\|,
\qquad
a,b\geq0.
$$

O teorema OS funcional completo, sob continuidade forte, simetria e as demais
hipóteses espectrais, produz um gerador autoadjunto não negativo $H$:

$$
T_E(a)=e^{-aH/\hbar},
\qquad
H=H^\dagger,
\qquad
H\geq0.
$$

Modo a modo, para $E\geq0$, $\hbar>0$ e $a\geq0$,

$$
0<
e^{-aE/\hbar}
\leq1.
$$

No tempo físico,

$$
U(t)=e^{-itH/\hbar},
$$

e cada peso espectral satisfaz

$$
\left|e^{-itE/\hbar}\right|=1.
$$

Portanto, a contração do semigrupo euclidiano não é perda de probabilidade no
tempo físico.

## 7. Conteúdo formalizado

O módulo
[OSReconstruction.lean](../../../formal/GDQ/OSReconstruction.lean)
certifica:

- positividade por reflexão a partir do pareamento OS declarado;
- $\mathcal N+\mathcal G=\mathcal N$ quando
  $\mathcal G\subseteq\mathcal N$;
- quociente separado por normas nulas;
- produto interno e norma independentes do representante;
- anulação de gauges nulos;
- densidade da imagem canônica de $\mathcal D_+$ no completamento;
- completamento complexo e completude.

O módulo
[OSReconstructedEvolution.lean](../../../formal/GDQ/OSReconstructedEvolution.lean)
certifica:

- a interface abstrata de um semigrupo contrativo;
- a interface abstrata de um grupo linear isométrico;
- positividade e contração dos pesos $e^{-aE/\hbar}$;
- lei de semigrupo;
- módulo unitário e lei de grupo dos pesos $e^{-itE/\hbar}$.

## 8. Limite lógico

Ainda não foi demonstrado que todo background admissível da GDQ satisfaz
positividade OS. Para uma aplicação concreta continuam necessárias:

1. regularidade das funções de Schwinger;
2. reflexão compatível com o setor;
3. positividade do pareamento;
4. invariância do núcleo nulo pelas translações;
5. continuidade forte do semigrupo;
6. construção do gerador autoadjunto;
7. propriedade de cluster quando necessária.

Assim, o resultado é um teorema funcional condicional, não um novo axioma e
não uma afirmação automática sobre toda solução da ação oficial.
