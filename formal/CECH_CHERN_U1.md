# Cociclo de Čech e primeira classe de Chern

## 1. Dados locais

Em uma interseção tripla $U_a\cap U_b\cap U_c$, as funções de transição de
um fibrado de linha hermitiano satisfazem:

$$
g_{ab}g_{bc}g_{ca}=1.
$$

Escolhendo levantamentos reais:

$$
g_{ab}=e^{i\lambda_{ab}},
\qquad
g_{bc}=e^{i\lambda_{bc}},
\qquad
g_{ca}=e^{i\lambda_{ca}},
$$

segue:

$$
\lambda_{ab}+\lambda_{bc}+\lambda_{ca}
=
2\pi n_{abc},
\qquad
n_{abc}\in\mathbb Z.
$$

## 2. Mudança dos levantamentos

Os levantamentos não são únicos:

$$
\lambda_{ab}'
=
\lambda_{ab}+2\pi k_{ab},
\qquad
k_{ab}\in\mathbb Z.
$$

Aplicando a mudança às três arestas:

$$
n_{abc}'
=
n_{abc}+k_{ab}+k_{bc}+k_{ca}.
$$

Logo:

$$
n_{abc}'-n_{abc}
=
(\delta k)_{abc}.
$$

O representante inteiro muda, mas muda por um cobordo. Portanto sua classe
em cohomologia é independente da escolha dos levantamentos:

$$
[n]\in \check H^2(M,\mathbb Z).
$$

Sob as hipóteses usuais de uma boa cobertura, essa classe é a primeira classe
de Chern:

$$
c_1(L)=[n].
$$

## 3. Conteúdo certificado em Lean

O módulo `GDQ/CechChern.lean` prova a etapa local:

1. existência do inteiro $n_{abc}$;
2. unicidade do coeficiente inteiro de $2\pi$;
3. invariância das funções de transição sob mudanças dos levantamentos por
   $2\pi k$;
4. a lei exata:

$$
n_{abc}'
=
n_{abc}+k_{ab}+k_{bc}+k_{ca};
$$

5. a diferença entre os representantes é precisamente o cobordo inteiro.

O módulo `GDQ/CechCohomology.lean` acrescenta a etapa global algébrica:

1. cochains inteiras $C^1$, $C^2$ e $C^3$ sobre um conjunto arbitrário de
   índices;
2. operadores orientados $\delta_1$ e $\delta_2$;
3. a identidade:

$$
\delta_2\delta_1=0;
$$

4. os subgrupos:

$$
Z^2=\ker\delta_2,
\qquad
B^2=\operatorname{im}\delta_1;
$$

5. o grupo quociente:

$$
\check H^2=Z^2/B^2;
$$

6. a construção do cociclo inteiro global a partir dos levantamentos
   $U(1)$;
7. a prova de que esse cociclo é fechado;
8. a definição formal de `firstChernClass` como sua classe em
   $\check H^2$;
9. a igualdade:

$$
c_1(u+2\pi k)=c_1(u).
$$

Não há `axiom`, `sorry` ou `admit`.

## 4. Limite formal atual

Os módulos formalizam a álgebra local, o complexo global sobre um índice
arbitrário e a invariância da classe. Ainda não constroem:

- uma cobertura aberta concreta da variedade GDQ;
- o nervo que elimina tuplas com interseção vazia;
- o sistema de restrições do feixe sobre as interseções;
- o isomorfismo entre cohomologia de Čech e cohomologia singular;
- a identificação de Chern--Weil:

$$
c_1(L)
=
\left[\frac{F_A}{2\pi}\right].
$$

Para uma boa cobertura e coeficientes constantes inteiros, o complexo
formalizado é exatamente o núcleo algébrico usado na construção usual. A
instanciação numa cobertura concreta e Chern--Weil são extensões; não reabrem
a quantização de circulação nem a invariância cohomológica já demonstradas.
