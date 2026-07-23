# Ponte global--local — Jacobiana variacional da colagem

## 1. Motivo

O solver de duas interfaces possui dez parâmetros e dez resíduos. Uma
Jacobiana por diferenças finitas exige, em cada iteração, múltiplas
integrações completas dos dois colares e do exterior. Além do custo, a
subtração entre trajetórias próximas amplifica o erro de tiro.

A alternativa canônica é transportar a derivada do fluxo juntamente com a
solução.

## 2. Equação variacional

Para um sistema

$$
\frac{dY}{ds}=F(Y,\theta),
$$

defina

$$
S(s)=\frac{\partial Y(s)}{\partial\theta}.
$$

Então

$$
\boxed{
\frac{dS}{ds}
=D_YF(Y,\theta)S+D_\theta F(Y,\theta).
}
$$

A condição inicial dependente dos parâmetros fornece

$$
S(0)=D_\theta Y_0(\theta).
$$

## 3. Domínios normalizados

Cada região é parametrizada por $t\in[0,1]$:

$$
s=\ell t.
$$

A equação torna-se

$$
\frac{dY}{dt}=\ell F(Y,\theta),
$$

e

$$
\frac{dS}{dt}
=\ell D_YF\,S
+\ell D_\theta F
+(D_\theta\ell)F.
$$

Assim, a sensibilidade aos comprimentos dos colares é incluída sem deslocar
numericamente a extremidade de integração.

## 4. Propagação em cascata

### 4.1 Colar esquerdo

Integram-se

$$
(Y_-,S_-)
$$

da garganta até $Y_-$.

### 4.2 Adaptador

O estado exterior inicial é

$$
Y_+^0=\mathcal A(Y_-;p_x),
$$

com

$$
p_y=a\Pi_a,
\qquad
p_z=c\Pi_c.
$$

Sua sensibilidade é obtida exatamente pela regra da cadeia:

$$
S_+^0
=D_Y\mathcal A\,S_-
+D_\theta\mathcal A.
$$

### 4.3 Exterior

Integram-se

$$
(Y_+,S_+)
$$

entre as duas interfaces.

### 4.4 Colar direito

O segundo colar é integrado independentemente, produzindo

$$
(Y_R,S_R).
$$

## 5. Jacobiana do resíduo

Se

$$
\mathfrak F(\theta)
$$

é o vetor de dez resíduos, então

$$
\boxed{
D_\theta\mathfrak F
=D_{Y_+}\mathfrak F\,S_+
+D_{Y_R}\mathfrak F\,S_R
+\partial_\theta\mathfrak F.
}
$$

As derivadas do adaptador e dos resíduos de traço/momento são algébricas.

## 6. Derivadas dos campos vetoriais

As Jacobianas $D_YF$ devem ser obtidas por uma destas rotas:

1. diferenciação simbólica das expressões já derivadas;
2. passo complexo local, usado dentro de uma única integração aumentada.

O passo complexo é aceitável para validar a implementação porque não subtrai
duas soluções globais. A versão final deve preservar as expressões simbólicas
ou testes cruzados com elas.

## 7. Critérios de aceitação

Uma candidata só será aceita se:

1. $\|\mathfrak F\|<10^{-8}$ em integração precisa;
2. as três restrições do lapse permanecerem abaixo de $10^{-9}$;
3. o posto numérico de $D\mathfrak F$ for dez, salvo zero mode identificado;
4. o candidato for reproduzido por pelo menos duas sementes;
5. refinamento de tolerância alterar os parâmetros menos que a incerteza
   declarada;
6. os parâmetros não estiverem presos aos limites artificiais.

## 8. Papel da colocação multidomínio

Depois de obter uma raiz pelo tiro variacional, ela deve servir de chute para
um solver de colocação com três subdomínios. A concordância entre os métodos
será um teste de discretização, não uma nova hipótese física.

## 9. Status

$$
\boxed{
\text{método variacional especificado; implementação do fluxo aumentado é o
próximo passo numérico.}
}
$$

## 10. Implementação e diagnóstico

O fluxo aumentado foi implementado em
`ponte_global_local_busca_jacobiana_variacional.py`. O resultado está em
`topicos/ponte_global_local/ponte_global_local_jacobiana_variacional_resultado.md`. A Jacobiana possui
posto oito: os dois resíduos de fase são triviais no setor $p_v=0$ e devem ser
substituídos pelos vínculos cosmológicos de raio e energia.
