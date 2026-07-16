# Q34 — Loop geométrico da fase no bulk oficial $\mathbb R^4\times T^4$

## 1. Enunciado

O objetivo é executar um loop diretamente derivado da ação oficial, sem
introduzir espinores, Grassmann, Yang--Mills fundamental ou fantasmas como
ontologia.

Usa-se o bulk local oficial

$$
M=\mathbb R^4\times T^4
$$

e o setor de fase do campo fundamental $f$.

## 2. Flutuação de fase

Escreva, em torno de um background real constante $f_*$,

$$
f=f_*+i\chi,
\qquad
\bar f=f_*-i\chi.
$$

Então

$$
\frac{f+\bar f}{2}=f_*,
\qquad
\mathcal U=\mathcal U_*,
$$

exatamente: a medida ponderada não varia com $\chi$.

Além disso,

$$
g^{MN}\partial_Mf\partial_N\bar f
=
g^{MN}\partial_M\chi\partial_N\chi.
$$

Logo, a segunda variação da ação oficial contém

$$
\boxed{
S_\chi^{(2)}
=
\frac{Z_\chi}{2}
\int_M
g^{MN}\partial_M\chi\partial_N\chi\,dV_g,
}
$$

onde $Z_\chi>0$ reúne o prefator comum, a medida estacionária e a integral no
contorno de fluxo. Sua normalização não afeta a resposta de calibre, pois
$\operatorname{Tr}\log Z_\chi$ é independente de $A$.

## 3. Conexão geométrica de um ciclo toroidal

Escolha um ciclo $S^1\subset T^4$ com coordenada periódica

$$
y\sim y+2\pi
$$

e métrica

$$
ds^2
=
h_{\mu\nu}dx^\mu dx^\nu
+R^2(dy+\kappa A_\mu dx^\mu)^2
+ds^2_{T^3}.
$$

Aqui $A_\mu$ é componente da métrica/fibração. Não é acrescentado como campo
fundamental.

Expanda a fase real:

$$
\chi(x,y)
=
\sum_{n\in\mathbb Z}\chi_n(x)e^{iny},
\qquad
\chi_{-n}=\bar\chi_n.
$$

A derivada horizontal atua como

$$
\boxed{
D_\mu^{(n)}
=
\partial_\mu-iq_nA_\mu,
\qquad
q_n=n\kappa.
}
$$

O autovalor interno é

$$
\boxed{
m_n^2=\frac{n^2}{R^2}+\lambda_\perp,
}
$$

onde $\lambda_\perp$ é o autovalor dos outros três ciclos. Para o modo
fundamental considerado, $\lambda_\perp=0$.

## 4. Hessiana física do modo

Para cada par $n,-n$, a Hessiana reduzida é

$$
\boxed{
H_n[A]
=
-(D^{(n)})^2+m_n^2.
}
$$

A integral gaussiana do campo fundamental real sobre o par conjugado produz

$$
\boxed{
\Gamma_n^{(1)}[A]
=
\operatorname{Tr}\log H_n[A].
}
$$

Essa é a mesma potência de determinante de um modo complexo, mas sua origem é
um par de modos reais da fase geométrica.

## 5. Representação de tempo próprio

Com resolução geométrica $s_0>0$,

$$
\boxed{
\Gamma_{n,s_0}^{(1)}[A]
=
-\operatorname{Tr}
\int_{s_0}^\infty\frac{ds}{s}e^{-sH_n[A]}.
}
$$

Como

$$
H_n[A+\partial\lambda]
=
e^{iq_n\lambda}H_n[A]e^{-iq_n\lambda},
$$

o traço é invariante. Portanto,

$$
\boxed{
\partial_\mu
\frac{\delta\Gamma_{n,s_0}^{(1)}}{\delta A_\mu}=0.
}
$$

## 6. Diagramas geométricos

A expansão de $|D\chi_n|^2$ contém:

1. dois vértices lineares $A\chi\partial\chi$;
2. o vértice quadrático de contato $A^2|\chi|^2$.

Na linguagem externa, são o bubble escalar e o seagull. Ambos vêm da mesma
Hessiana geométrica. O termo de contato não pode ser omitido: ele completa a
identidade de Ward.

## 7. Polarização calculada

Defina

$$
u=x(1-x),
\qquad
\eta_n=s_0m_n^2.
$$

Depois da subtração infravermelha $\Pi_n(0)=0$, a função escalar é

$$
\boxed{
\Pi_{n,s_0}(Q^2)
=
\frac{q_n^2}{16\pi^2}
\int_0^1dx\,(1-2x)^2
\left[
E_1(\eta_n)
-E_1\!\left(
s_0[m_n^2+uQ^2]
\right)
\right].
}
$$

O tensor completo é

$$
\boxed{
\Pi_{\mu\nu}^{(n)}(Q)
=
(Q_\mu Q_\nu-Q^2\delta_{\mu\nu})
\Pi_{n,s_0}(Q^2),
}
$$

e

$$
\boxed{
Q^\mu\Pi_{\mu\nu}^{(n)}=0.
}
$$

## 8. Limites

Para $s_0Q^2\ll1$:

$$
\Pi_{n,s_0}(Q^2)
\longrightarrow
\frac{q_n^2}{16\pi^2}
\int_0^1dx\,(1-2x)^2
\log\left(1+\frac{uQ^2}{m_n^2}\right).
$$

Na janela $m_n^2\ll Q^2\ll s_0^{-1}$:

$$
\boxed{
\Pi_n(Q^2)
\simeq
\frac{q_n^2}{48\pi^2}
\log\frac{Q^2}{m_n^2}
+\text{constante}.
}
$$

No ultravioleta geométrico:

$$
\boxed{
\Pi_{n,s_0}(\infty)
=
\frac{q_n^2}{48\pi^2}E_1(\eta_n)<\infty.
}
$$

## 9. Cadeia de derivação

O cálculo satisfaz:

$$
\boxed{
\mathcal S_{\rm GDQ}
\longrightarrow
S_\chi^{(2)}
\longrightarrow
H_n[A]
\longrightarrow
\Gamma_n^{(1)}[A]
\longrightarrow
\Pi_{\mu\nu}^{(n)}.
}
$$

Não foi introduzida ação de matéria externa: o modo circulante é componente
da fase do campo fundamental e a conexão é componente da métrica.

## 10. Limitações

1. o cálculo é feito no setor local $\mathbb R^4\times T^4$;
2. $q_n=n\kappa$ e $m_n=n/R$ são geométricos, mas sua conversão metrológica
   requer a normalização dos módulos toroidais;
3. o resultado testa um bloco positivo da Hessiana, não o determinante de
   todos os setores acoplados;
4. a independência quantitativa sob outros kernels covariantes permanece
   separada.

## 11. Veredito para 34-0

$$
\boxed{
\text{foi executado um loop completo de um modo geométrico derivado da ação
oficial.}
}
$$

Isso satisfaz o critério mínimo de 34-0 no setor declarado. Q34 ainda requer
o teste explícito de independência do kernel para responder toda a lista
obrigatória.

## 12. Referência externa de auditoria

D. V. Vassilevich, “Heat kernel expansion: user's manual”,
*Physics Reports* **388** (2003) 279--360,
DOI: 10.1016/j.physrep.2003.09.002,
arXiv:hep-th/0306138. A referência é usada apenas para a representação de
tempo próprio e expansão de heat kernel; o operador $H_n[A]$ foi obtido da
ação oficial.
