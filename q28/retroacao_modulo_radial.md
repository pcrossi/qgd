# Q28 — Retroação do módulo radial na ação oficial

## 1. Normalização da medida

No ansatz homogêneo, o volume da fibra satisfaz

$$
\operatorname{Vol}(S^3_r)=2\pi^2r^3.
$$

A medida oficial é

$$
\mathcal U
=\frac{e^{-\sigma}}{(4\pi z_\tau)^4},
\qquad
\sigma=\frac{f+\bar f}{2},
$$

e obedece a

$$
\int_K\mathcal U\,dV_g=1.
$$

Mantidos fixos o volume toroidal e $z_\tau$, essa condição impõe

$$
\sigma(r)=\sigma_0+3\log r.
$$

Portanto, o fator $r^3$ da integração não pode ser contado como um potencial
independente: ele é absorvido pela normalização, enquanto o termo explícito
$\sigma-n$ conserva a contribuição logarítmica.

## 2. Funcional radial reduzido

Para uma conexão estacionária no setor $A$, escreva

$$
\frac14\left\langle F^a_{ij}F_a^{ij}\right\rangle
=q|A|,
\qquad
q>0,
$$

onde $q$ contém a métrica do toro e a normalização da solução de curvatura
constante. A redução da ação oficial produz, a uma constante independente de
$r$,

$$
\boxed{
W_-(r,A)
=\tau\left(
\frac6{r^2}-q|A|r^2
\right)
+3\log r+C_0.
}
$$

O sinal negativo é o sinal geométrico que aparece na fórmula de O'Neill para
o escalar de curvatura. Como controle da convenção euclidiana estável,
consideramos também

$$
W_+(r,A)
=\tau\left(
\frac6{r^2}+q|A|r^2
\right)
+3\log r+C_0.
$$

As duas convenções levam ao mesmo diagnóstico sobre a ausência de um mínimo
interior universal em $A$.

## 3. Equação estacionária radial

Para o sinal geométrico oficial,

$$
\frac{\partial W_-}{\partial r}
=-\frac{12\tau}{r^3}
-2q\tau|A|r
+\frac3r.
$$

Definindo

$$
x=r^2,
$$

a equação estacionária é

$$
\boxed{
2q\tau|A|x^2-3x+12\tau=0.
}
$$

Seu discriminante é

$$
\Delta_A
=9-96q\tau^2|A|.
$$

Logo, uma solução radial real exige

$$
|A|
\le
\frac{3}{32q\tau^2}.
$$

Esse limite depende de $q\tau^2$; ele não seleciona universalmente o inteiro
dezoito.

Para o sinal positivo de controle,

$$
2q\tau|A|x^2+3x-12\tau=0,
$$

que possui uma única raiz positiva para todo $A>0$, mas também não distingue
o número dezoito.

## 4. Teorema de monotonicidade on-shell

Se $r_A$ resolve a equação radial, o teorema do envelope dá

$$
\frac{dW_\pm^{\rm on\mbox{-}shell}}{d|A|}
=\left.
\frac{\partial W_\pm}{\partial|A|}
\right|_{r=r_A}.
$$

Portanto,

$$
\boxed{
\frac{dW_-^{\rm on\mbox{-}shell}}{d|A|}
=-q\tau r_A^2<0,
}
$$

e

$$
\boxed{
\frac{dW_+^{\rm on\mbox{-}shell}}{d|A|}
=+q\tau r_A^2>0.
}
$$

Assim, mesmo depois da retroação do raio:

1. com o sinal geométrico, a ação decresce até o limite de existência ou até
   uma instabilidade;
2. com a forma quadrática positiva, a ação cresce e seleciona o menor setor.

Nenhuma delas possui um mínimo interior em

$$
A=18.
$$

## 5. Consequência

A retroação de $r$ e a normalização do dilatão não fecham a contagem de três
gerações. Para que a ação oficial selecione um inteiro interior, é necessário
um termo adicional que já resulte das variáveis oficiais, como:

1. retroação anisotrópica da métrica $G_{ij}$;
2. dependência não homogênea de $f$ correlacionada com $F\wedge F$;
3. condições de colagem que tornem o conjunto admissível finito e tenham
   $18$ como extremidade;
4. decomposição obrigatória em três componentes de carga mínima seis.

Sem uma dessas estruturas, escolher $A=18$ continua sendo uma condição de
contorno, não uma consequência variacional.

## 6. Status

Foi avaliada diretamente a primeira retroação exigida pela ação oficial. O
resultado é um teorema negativo útil:

$$
\boxed{
\text{raio de }S^3
+\text{ normalização de }\mathcal U
+\text{ curvatura homogênea}
\not\Rightarrow A=18.
}
$$

O próximo setor genuinamente novo é a retroação anisotrópica de $G_{ij}$ e a
possível correlação espacial entre $f$ e a densidade de Chern.
