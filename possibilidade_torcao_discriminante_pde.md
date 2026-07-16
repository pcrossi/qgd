# Possibilidade — torção e mudança de tipo da equação da GDQ

## 1. Ideia central

Uma equação diferencial de segunda ordem em duas variáveis,

$$
A,u_{xx}
+B,u_{xy}
+C,u_{yy}
+\text{termos de ordem inferior}
=0,
$$

é classificada pelo discriminante

$$
\Delta_{\mathrm{PDE}}=B^2-4AC.
$$

Na convenção acima:

$$
\Delta_{\mathrm{PDE}}<0
\quad\Longrightarrow\quad
\text{tipo elíptico},
$$

$$
\Delta_{\mathrm{PDE}}=0
\quad\Longrightarrow\quad
\text{tipo parabólico},
$$

$$
\Delta_{\mathrm{PDE}}>0
\quad\Longrightarrow\quad
\text{tipo hiperbólico}.
$$

A hipótese a investigar é que a torção da conexão Hermitiana da GDQ induza o
termo misto responsável por conectar esses regimes.

## 2. Relação com Wiener, Feynman e Perelman

Os três setores relevantes são:

1. problemas elípticos para configurações estacionárias e condições de
   contorno;
2. evolução parabólica para difusão e fluxo geométrico;
3. propagação hiperbólica ou dispersiva/unitária para a dinâmica física.

O formalismo de Perelman conecta naturalmente fluxo parabólico, equação do
calor conjugada e pontos críticos elípticos. A GDQ precisa ainda explicar a
passagem ao setor causal e oscilatório associado à dinâmica física.

A possibilidade proposta é:

$$
\boxed{
\text{torção}
\longrightarrow
\text{termo diferencial misto}
\longrightarrow
\text{mudança do discriminante}
\longrightarrow
\text{mudança de tipo da PDE}.
}
$$

Nesse quadro, a ligação Wiener–Feynman não seria apenas uma rotação formal de
Wick. Ela corresponderia a regimes diferentes do mesmo operador geométrico
acoplado.

## 3. Operador causal efetivo

No plano formado pelo parâmetro de fluxo $\tau$ e pelo tempo físico $t$, um
operador reduzido poderia assumir a forma

$$
\mathcal P_H
=A,\partial_\tau^2
+\mathscr B_H,\partial_\tau\partial_t
+C,\partial_t^2
+\mathcal L_{\mathrm{inferior}},
$$

onde $\mathscr B_H$ é o coeficiente misto induzido pela torção. A letra
$\mathscr B_H$ evita confusão com a 3-forma torsional $H$ ou $B$.

O discriminante seria

$$
\boxed{
\Delta_H
=\mathscr B_H^2-4AC.
}
$$

Variações do background, da torção ou da projeção causal poderiam então
selecionar regiões elípticas, parabólicas ou hiperbólicas do operador efetivo.

## 4. Limitação matemática que precisa ser enfrentada

A presença de torção não garante automaticamente a alteração do tipo da PDE.
Para um campo escalar isolado, derivadas de segunda ordem são simétricas:

$$
\partial_\mu\partial_\nu u
=\partial_\nu\partial_\mu u.
$$

Por isso, a parte antissimétrica da conexão pode desaparecer do símbolo
principal e sobreviver apenas em termos de primeira ordem. Termos de ordem
inferior não alteram a classificação elíptica, parabólica ou hiperbólica.

A hipótese só será confirmada se a torção entrar efetivamente no símbolo
principal do sistema físico acoplado.

## 5. Rota provável pela Hessiana acoplada

A GDQ não contém apenas um escalar livre. O sistema físico envolve, conforme o
setor considerado:

- perturbações métricas;
- parte real e imaginária de $f$;
- densidade e fase derivadas;
- conexão torsional;
- vínculos e condições de contorno;
- estrutura causal em $z_\tau$.

A segunda variação da ação oficial deve ser organizada em blocos. Se $q$
representa o setor métrico–dilatônico e $h$ o setor torsional, a Hessiana tem a
forma esquemática

$$
\mathbb H
=
\begin{pmatrix}
K_q & J_H \\
J_H^\dagger & K_H
\end{pmatrix}.
$$

Eliminando o setor torsional, obtém-se o complemento de Schur

$$
K_{\mathrm{eff}}
=K_q-J_HK_H^{-1}J_H^\dagger.
$$

A questão decisiva é verificar se esse operador contém, na parte principal,

$$
\mathscr B_H,\partial_\tau\partial_t.
$$

## 6. Cálculo necessário

Para testar a hipótese:

1. escolher um background estacionário admissível da ação oficial;
2. fixar difeomorfismos e remover modos de gauge;
3. calcular a Hessiana métrico–fase–torção;
4. identificar seu símbolo principal nas direções $(\tau,t)$;
5. calcular o complemento de Schur do setor torsional;
6. extrair $A$, $\mathscr B_H$ e $C$;
7. avaliar

   $$
   \Delta_H=\mathscr B_H^2-4AC;
   $$

8. determinar se o sinal muda em backgrounds ou regimes fisicamente
   admissíveis;
9. verificar bem-postura, causalidade e estabilidade em cada região;
10. comparar a continuação obtida com a prescrição de Wick e com a variável
    causal $z_\tau=\tau+i\nu_0t$.

## 7. Critério de sucesso

A hipótese será confirmada se for demonstrado que

$$
\boxed{
\mathscr B_H=\mathscr B[H,g,f]\neq0
}
$$

no símbolo principal físico e que sua contribuição permite a transição
controlada entre os tipos de equação.

Se a torção aparecer apenas em termos inferiores, a interpretação do
discriminante deverá ser rejeitada como mecanismo fundamental, embora a
torção ainda possa afetar espectro, estabilidade, spin e condições de
contorno.

## 8. Status

> Hipótese estrutural promissora, ainda não demonstrada. Sua validade depende
> de um cálculo explícito do símbolo principal da Hessiana acoplada da ação
> oficial.

