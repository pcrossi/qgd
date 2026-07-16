# Q28 — Retroação do dilatão sobre a densidade de Chern

## 1. Setor real normalizado da ação oficial

No setor estacionário relevante, escreva

$$
\rho
=\mathcal U\sqrt g,
\qquad
\int_K\rho=1.
$$

O funcional real de Perelman contido na ação oficial possui a estrutura

$$
\mathcal W[g,f]
=\int_K
\rho
\left[
\tau\left(
\mathcal R+|\nabla f|^2
\right)
+f-n
\right].
$$

Na métrica fibrada, a curvatura é

$$
\mathcal R
=\mathcal R_0
-\frac{r^2}{4}|F|^2.
$$

Assim, a densidade de Chern entra no potencial geométrico da própria ação
oficial.

## 2. Equação estacionária de $f$

Variando $f$ sob a restrição de normalização, obtém-se

$$
\boxed{
2\tau\Delta f
-\tau|\nabla f|^2
+\tau\mathcal R
+f-n
=\mu,
}
$$

onde $\mu$ é o multiplicador constante da normalização. Substituindo a
curvatura fibrada,

$$
2\tau\Delta f
-\tau|\nabla f|^2
+\tau\mathcal R_0
-\frac{\tau r^2}{4}|F|^2
+f-n
=\mu.
$$

Logo, o perfil $f_A$ responde à distribuição espacial de $|F_A|^2$; essa
resposta não deve ser omitida.

## 3. Derivada on-shell pelo teorema do envelope

Considere uma família homotética dentro dos representantes estacionários,

$$
|F_A(y)|^2=|A|\,q(y),
\qquad
q(y)\ge0.
$$

Defina o funcional já extremizado em todas as variáveis contínuas:

$$
\mathcal W_{\rm eff}(A)
=\mathcal W[g_A,f_A,F_A].
$$

Como $g_A$, $f_A$ e $F_A$ satisfazem suas equações variacionais, suas
derivadas implícitas não entram na primeira derivada on-shell. Portanto,

$$
\frac{d\mathcal W_{\rm eff}}{d|A|}
=\left.
\frac{\partial\mathcal W}{\partial|A|}
\right|_{g_A,f_A,F_A}.
$$

Para o sinal geométrico da ação oficial,

$$
\boxed{
\frac{d\mathcal W_{\rm eff}}{d|A|}
=-\frac{\tau}{4}
\int_K\rho_A r_A^2q(y)
<0
}
$$

sempre que o fluxo é não nulo.

Se a continuação euclidiana física inverter o sinal do bloco quadrático, a
mesma conta fornece

$$
\boxed{
\frac{d\mathcal W_{\rm eff}^{(+)}}{d|A|}
=+\frac{\tau}{4}
\int_K\rho_A r_A^2q(y)
>0.
}
$$

Em ambas as convenções, a derivada possui sinal definido.

## 4. Por que a redistribuição de $\rho$ não muda o sinal

O perfil $\rho_A$ pode concentrar peso onde $q(y)$ é menor ou maior, conforme
o sinal do acoplamento. Contudo,

$$
\rho_A>0,
\qquad
r_A^2>0,
\qquad
q(y)\ge0.
$$

Assim, a integral

$$
\int_K\rho_A r_A^2q(y)
$$

pode alterar a magnitude da resposta, mas não seu sinal. A entropia e a
normalização regularizam a redistribuição; não criam um zero da derivada em
$A=18$.

## 5. Alcance do teorema

O argumento vale quando os setores são comparados por uma família suave cuja
densidade quadrática de curvatura é homotética em $|A|$. Ele inclui:

1. conexões homogêneas;
2. soluções auto-duais de mesma forma e carga multiplicada;
3. perfis de dilatão e métricas que se reajustem variacionalmente;
4. pesos normalizados não homogêneos.

Ele pode falhar somente se a mudança de setor alterar qualitativamente o
domínio — por cirurgia, número de componentes, condição de bordo ou mudança
da classe de colagem — de modo que os setores não pertençam a uma única
família homotética.

## 6. Conclusão

$$
\boxed{
\text{a retroação contínua completa de }f,\mathcal U,r,G
\text{ não produz um mínimo interior em }A=18
}
$$

dentro da família fibrada suave considerada.

Portanto, três gerações só podem emergir, nessa rota, de uma seleção global
descontínua do domínio:

$$
\boxed{
\text{colagem/cirurgia/contorno global}
\Longrightarrow A=18.
}
$$

Essa condição deve ser derivada independentemente da observação de três
gerações. A ação oficial então preserva o setor e calcula sua dinâmica, mas a
cardinalidade é um dado topológico global do problema de contorno.
