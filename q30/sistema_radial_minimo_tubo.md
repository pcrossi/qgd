# Q30 — Sistema radial mínimo e no-go da truncagem de uma fibra

## 1. Funcional reduzido

No teste de uma direção de Cartan, com $S=0$, o funcional radial derivado na
etapa anterior é

$$
\boxed{
\mathcal I[a,u,v]
=\int_0^\infty dr\,r e^{-u}
\left\{
\mathfrak c_1\left[
-\frac{(a')^2}{2r^2}
+(u')^2+(v')^2
+\frac{(n_C-qa)^2}{r^2}
\right]
+\mathfrak c_0(u-4)
\right\}.
}
$$

Esta é a ação reduzida estacionária na convenção escalar oficial. Não é
reinterpretada como energia positiva de Yang--Mills.

## 2. Equação da conexão

A variação em $a$ fornece

$$
\boxed{
\frac{d}{dr}
\left(
e^{-u}\frac{a'}r
\right)
=2q\,e^{-u}\frac{n_C-qa}{r}.
}
$$

As condições topológicas pretendidas são

$$
a(0)=0,
\qquad
a(\infty)=\frac{n_C}{q}.
$$

## 3. Equação da fase radial

A variação em $v$ dá uma primeira integral:

$$
\boxed{
r e^{-u}v'=J_v.
}
$$

Se não há fluxo radial de fase pelo eixo ou pelo infinito, regularidade e
energia finita fixam

$$
\boxed{J_v=0,\qquad v'=0.}
$$

## 4. Equação de $u=\operatorname{Re}f$

A equação de Euler--Lagrange de $u$ é

$$
\boxed{
\begin{aligned}
0={}&\mathfrak c_1\left[
2u''+\frac{2u'}r-(u')^2+(v')^2
+\frac{(n_C-qa)^2}{r^2}
-\frac{(a')^2}{2r^2}
\right]\\
&+\mathfrak c_0(u-5).
\end{aligned}
}
$$

O deslocamento $u-5$ resulta da variação simultânea do peso $e^{-u}$ e do
termo oficial $u-4$; ele não é um potencial acrescentado.

## 5. Vínculo de elongação nula

Da variação métrica já calculada, $S=0$ requer

$$
\boxed{
\begin{aligned}
0={}&\mathfrak c_1\left[
2u''+\frac{2u'}r-(u')^2+(v')^2
+\frac{(n_C-qa)^2}{r^2}
-\frac{3(a')^2}{2r^2}
\right]\\
&+\mathfrak c_0(u-4).
\end{aligned}
}
$$

## 6. Condição de compatibilidade

Subtraindo a equação de $u$ do vínculo de $S$, todos os perfis escalares e a
circulação cancelam. Resta a condição exata

$$
\boxed{
\frac{(a')^2}{r^2}
=\frac{\mathfrak c_0}{\mathfrak c_1}.
}
$$

Se $\mathfrak c_0/\mathfrak c_1>0$ é constante real, então

$$
a(r)=a(0)\pm\frac12
\sqrt{\frac{\mathfrak c_0}{\mathfrak c_1}}\,r^2.
$$

Essa solução não pode tender a $n_C/q$ quando $r\to\infty$. Se a razão é
negativa, não existe solução real. Se é zero, $a'=0$ e, com $a(0)=0$, não se
atinge holonomia assintótica não trivial.

Portanto:

$$
\boxed{
\text{não existe solução real, regular e assintoticamente finita com
holonomia não trivial no truncamento mínimo de uma fibra e }S=0.
}
$$

## 7. Alcance do no-go

O resultado não rejeita a hipótese física do autor nem o confinamento na GDQ.
Ele mostra que o teste abeliano de uma única fibra é pequeno demais. A
realização precisa de pelo menos uma contribuição ausente que apareça também
na equação métrica:

1. comutador genuinamente não abeliano $\mathcal A\wedge\mathcal A$;
2. curvatura dos outros planos internos;
3. fluxo harmônico/topológico de Bismut;
4. colagem em domínio compacto com fonte de bordo;
5. termos da Hessiana completa do bloco $G_C$, em vez de um único raio $S$.

Em particular, o resultado indica que reduzir primeiro a um gerador de Cartan
remove precisamente a estrutura não abeliana que pode balancear a equação de
elongação.

## 8. Decisão para a continuação

Não será executado um shooting numérico desse sistema, pois as equações já
provam que as condições de contorno desejadas são incompatíveis. O próximo
passo legítimo é manter a conexão matricial completa

$$
\mathcal A_C=a_A(r,\theta)T_A
$$

e calcular o tensor de tensão do bloco $SU(3)$ antes de impor elongação nula.

A consequência espectral dessa continuação foi estabelecida em
`q30/teorema_gap_holonomia_irredutivel.md`: numa seção compacta, holonomia
$SU(3)$ irreducível torna trivial o kernel adjunto e produz
$\lambda_{1,\mathcal A}>0$ para $D_{\mathcal A}^\dagger D_{\mathcal A}$.

## 9. Classificação

- equações radiais: derivação variacional do truncamento;
- condição de compatibilidade: identidade exata;
- inexistência: teorema condicional ao truncamento, momentos constantes e
  domínio infinito;
- exclusão do tubo $SU(3)$ completo: não demonstrada;
- saída numérica evitada: ansatz já excluído analiticamente.
