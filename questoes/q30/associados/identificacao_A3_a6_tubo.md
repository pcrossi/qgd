# Q30 — Correção: $A_3$ é o terceiro jato causal da Hessiana tubular

## 1. Enunciado

Determinar o coeficiente $A_3$ selecionado pelo contorno causal diretamente
da ação oficial e testar se ele pode ser identificado com um coeficiente de
Seeley--DeWitt.

## 2. Pullback correto da ação quadrática

Se $z=z_\tau$ parametriza o contorno e $\tau=\tau(z)$ em seu pullback, a
segunda variação da ação oficial pode ser escrita esquematicamente como

$$
\mathcal S^{(2)}
=
\frac{\hbar}{\Lambda_C^2}
\oint_\gamma
\frac{dz}{(4\pi z)^4}
F^{(2)}(z),
$$

onde

$$
\boxed{
F^{(2)}(z)
:=
\frac{d\tau}{dz}\frac1{\tau(z)}
\int_M e^{-\sigma(z)}
\sqrt{\det g(z)}\,
\mathcal Q^{(2)}[g(z),f(z),\bar f(z);\tau(z)],d^8x.
}
$$

$\mathcal Q^{(2)}$ é a densidade da Hessiana antes do prefator
$(4\pi z)^{-4}$. Ela deve ser obtida pela segunda variação da ação oficial,
com fixação de gauge e projeção física.

Se

$$
F^{(2)}(z)=\sum_{m\in\mathbb Z}A_mz^m,
$$

então

$$
\boxed{
\operatorname*{Res}_{z=0}
\frac{F^{(2)}(z)}{(4\pi z)^4}
=\frac{A_3}{(4\pi)^4}.
}
$$

Quando $F^{(2)}$ é holomorfo em zero,

$$
\boxed{
A_3=\frac1{3!}
\left.\frac{d^3F^{(2)}}{dz^3}\right|_{z=0}.
}
$$

Esse é o significado exato do dado que faltava: o terceiro jato causal da
forma quadrática ponderada ao longo da família de backgrounds.

## 3. Setor cinético

Na parcela da ação em que $\mathcal Q^{(2)}_{\rm kin}=\tau Q_{\rm kin}$, o
fator $\tau$ cancela o $1/\tau$ da medida de contorno. Assim,

$$
F^{(2)}_{\rm kin}(z)
=
\frac{d\tau}{dz}
\int_M e^{-\sigma(z)}\sqrt{\det g(z)}
Q_{\rm kin}[g(z),f(z),\bar f(z)],d^8x.
$$

Logo, a rigidez residual depende das derivadas até terceira ordem de:

1. $d\tau/dz$;
2. $g(z)$ e seu volume;
3. $\sigma(z)=\operatorname{Re}f(z)$;
4. os coeficientes da Hessiana física $Q_{\rm kin}(z)$.

Se o background e o pullback forem congelados em $z$, então
$F^{(2)}_{\rm kin}$ é constante, $A_3=0$ e o contorno fechado não produz
rigidez quadrática. Portanto, a rigidez deve vir da evolução causal não
trivial da família; ela não segue apenas do fator $(4\pi z)^{-4}$.

## 4. Relação com $a_6$

Para um operador de tipo Laplace $L$, existe separadamente a expansão

$$
\operatorname{Tr}e^{-zL}
\sim(4\pi z)^{-4}\sum_{j\geq0}z^j a_{2j}[L].
$$

Nessa expansão, o resíduo selecionaria $a_6[L]$. Mas a ação oficial não
contém, por definição, $\operatorname{Tr}e^{-zL}$: ela contém a densidade
$\mathcal U$ multiplicando a ação geométrica. Portanto,

$$
\boxed{A_3=a_6[L_{\rm tubo}]}
$$

não é uma identidade da GDQ. Ela só valeria após provar adicionalmente a
representação

$$
F^{(2)}(z)=\operatorname{Tr}e^{-zL_{\rm tubo}}
$$

com o mesmo operador, domínio, bordo e normalização. Essa prova não existe no
corpus. O $a_6$ da Q34 permanece uma auditoria efetiva e não resolve $A_3$.

## 5. Critério de coercividade

Com orientação positiva,

$$
\mathfrak c_1^{\rm phys}
=
\operatorname{Re}\left[
\frac{2\pi i}{(4\pi)^4}A_3
\right]
=
-\frac{2\pi}{(4\pi)^4}\operatorname{Im}A_3.
$$

Assim,

$$
\boxed{\mathfrak c_1^{\rm phys}>0
\iff\operatorname{Im}A_3<0}
$$

para essa orientação. A orientação inversa inverte a desigualdade.

## 6. Veredito

Fica resolvido o significado operacional de $A_3$ e excluída a identificação
automática com $a_6$. O valor de $A_3$ ainda não é calculável porque Q4/Q9
fixam $z_\tau=\tau+i\nu_0t$ e o princípio de Laurent, mas não fornecem a
família tubular

$$
(g(z),f(z),\bar f(z))
$$

até terceira ordem em $z$, nem um pullback fechado explícito
$(\tau(z),t(z))$.

Isso é subdeterminação de dados da teoria vigente, não dificuldade numérica.
Escolher esses jatos pelo sinal desejado seria acrescentar uma prescrição
causal não derivada.

## 7. Redução pela conservação torsional

O teorema registrado em
`questoes/q30/associados/teorema_puxamento_estomato_conservacao_torcao.md` reduz essa liberdade.
Ao deformar a garganta sem cirurgia,

$$
Q_T=\int_{\Sigma_z}H_z
$$

é conservada. No modo homogêneo, se $x(z)=\log[V(z)/V_0]$, então

$$
\mathcal E_T(z)=\mathcal E_{T,0}e^{-x(z)}
$$

e

$$
\frac{d^3\mathcal E_T}{dz^3}
=\mathcal E_T[-(x')^3+3x'x''-x'''].
$$

Logo, o módulo torsional não é mais um jato independente: ele é determinado
pelo jato da distorção. Permanece necessário resolver a equação de fluxo para
$x(z)$ e somar os blocos de curvatura e dilatão.

## 8. Classificação

- fórmula de $A_3$ como terceiro jato: derivação exata;
- $A_3=a_6$: hipótese adicional não demonstrada, agora retirada;
- background congelado implica $A_3=0$: consequência exata;
- módulo torsional sob puxamento: determinado pela carga conservada e volume;
- sinal físico total: aberto até resolver a família causal tubular vinculada;
- construção Clay: aberta.
