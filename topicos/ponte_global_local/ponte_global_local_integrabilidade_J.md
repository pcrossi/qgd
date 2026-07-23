# Ponte global--local — integrabilidade do candidato $J_\chi$

## 1. Pergunta

O candidato quase-hermitiano

$$
\omega_\perp(\chi)
=\cos\chi(e^{58}+e^{67})
+\sin\chi(e^{56}-e^{78})
$$

só pertence ao domínio hermitiano da ação se

$$
N_{J_\chi}=0.
$$

Esta condição deve ser testada antes da integração numérica da sela.

## 2. Brackets do frame Berger

Defina

$$
\alpha=\frac{\dot a}{a},\qquad
\gamma=\frac{\dot c}{c},\qquad
p=\frac2c,\qquad q=\frac{2c}{a^2}.
$$

No frame $(e_5,e_6,e_7,e_8)$, os brackets não nulos são

$$
[e_5,e_6]=-\alpha e_6,
\quad [e_5,e_7]=-\alpha e_7,
\quad [e_5,e_8]=-\gamma e_8,
$$

$$
[e_7,e_8]=-p e_6,
\quad [e_6,e_8]=p e_7,
\quad [e_6,e_7]=-q e_8.
$$

O cálculo usa

$$
N_J(X,Y)=[JX,JY]-J[JX,Y]-J[X,JY]-[X,Y].
$$

## 3. Primeira consequência: ausência de modo radial

Duas componentes independentes são

$$
(N_J(e_5,e_6))^6
=\dot\chi\sin\chi\cos\chi,
$$

e

$$
(N_J(e_6,e_7))^6
=-\dot\chi\sin^2\chi.
$$

Quando $\sin\chi\neq0$, elas impõem $\dot\chi=0$. Quando
$\sin\chi=0$, outra componente dá diretamente $\dot\chi=0$. Portanto

$$
\boxed{N_{J_\chi}=0\Longrightarrow\dot\chi=0.}
$$

A direção canônica $(\chi,p_\chi)$ construída no documento quase-hermitiano
não é um grau de liberdade da classe hermitiana integrável.

## 4. Classificação dos ramos constantes

### 4.1 Estrutura original

Para

$$
\chi=0\pmod\pi,
$$

o tensor de Nijenhuis se anula sem condição métrica adicional. Este é o ramo
já usado na redução oficial.

### 4.2 Estrutura quaternionicamente ortogonal

Para

$$
\chi=\frac\pi2\pmod\pi,
$$

todas as componentes se anulam se, e somente se,

$$
\boxed{
\frac{\dot a}{a}-\frac{\dot c}{c}-\frac2c+rac{2c}{a^2}=0.
}
$$

Este é um ramo discreto, não um modo dinâmico. Numa garganta mínima refletida,
$\dot a=\dot c=0$, ele exige $a=c$. Fora da seção, a equação deve valer ao
longo de todo o colo.

### 4.3 Ângulo constante genérico

Se $\sin(2\chi)\neq0$, além da condição anterior surgem

$$
\alpha=p,
\qquad
\gamma=q,
\qquad
\alpha+\gamma=0.
$$

Para $a,c>0$, $p$ e $q$ são positivos, tornando essas equações incompatíveis.
Logo não há ramo genérico.

## 5. Consequência para a Porta B

O modo $\chi(s)$ não pode ser usado para liberar $(p_c,p_u)$ mantendo a
geometria Hermitiana--Bismut oficial. O arquivo
`topicos/ponte_global_local/ponte_global_local_modo_J.md` permanece como cálculo quase-hermitiano e teste
de uma rota excluída, não como extensão admissível do solver.

O ramo $\chi=\pi/2$ pode ser avaliado separadamente se a relação métrica for
imposta, mas ele não acrescenta um par canônico nem resolve por si só a falta
de parâmetros de tiro.

## 6. Menor deformação integrável restante

Uma deformação integrável infinitesimal geral é descrita por uma forma de
Beltrami

$$
\mu\in\Omega^{0,1}(T^{1,0}M)
$$

que obedece à equação de Maurer--Cartan

$$
\boxed{
\bar\partial\mu+\frac12[\mu,\mu]=0.
}
$$

Na ordem linear,

$$
\bar\partial\mu=0,
$$

e deformações

$$
\mu=\bar\partial V^{1,0}
$$

são apenas difeomorfismos, portanto pertencem a $\operatorname{Ran}R_*$ e são
removidas por $P^{\rm phys}$.

O cálculo acima mostra que não existe representante físico puramente
cohomogeneidade--1 dentro da família homogênea natural. A menor busca legítima
deve incluir um harmônico não homogêneo de $\mu$ no
$T^3\times S^3$, resolver $\bar\partial\mu=0$ com os contornos do colo e
testar se sua classe em

$$
H^{0,1}(T^{1,0}M)
$$
é não trivial. Escolher uma função arbitrária para $\mu$ ou um potencial sem
resolver Maurer--Cartan reintroduziria o mesmo erro.

Essa rota ainda não fornece um novo background: ela define o próximo problema
espectral intrínseco, sem Robin externa e sem termo fundamental adicional.

## 7. Verificação

`derivar_nijenhuis_modo_J.py` calcula todas as componentes simbolicamente.
`teste_nijenhuis_modo_J.py` verifica os dois ramos, a relação métrica e a
ausência de $\dot\chi\neq0$.

