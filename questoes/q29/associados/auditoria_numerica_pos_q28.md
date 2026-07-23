# Q29 — Auditoria numérica após o fechamento da Q28

## 1. Entradas que podem ser usadas

A Q28 fornece, no ponto geométrico comum,

$$
\sin^2\theta_W=\frac38,
$$

$$
g=0{,}494506,
\qquad
g'=0{,}383043.
$$

Esses valores substituem as normas arbitrárias usadas nos scripts antigos.

## 2. Scripts antigos não constituem derivação

Os códigos anteriores usam pelo menos uma destas entradas não derivadas:

1. $a_2=-8000\,\mathrm{GeV}^2$ e $a_4=0{,}5$;
2. perfis de Killing escolhidos manualmente;
3. $\sin^2\theta_W=2/9$;
4. a escala $v=m_p(6\pi^5)/7$ sem obtê-la como quarta variação;
5. um potencial de Landau--Ginzburg introduzido diretamente.

Eles devem permanecer como histórico numérico, não como prova da Q29.

## 3. Teste do candidato de escala existente

Mantendo somente como candidato metrológico

$$
v_{\rm cand}=m_p\frac{6\pi^5}{7},
$$

e usando os acoplamentos da Q28, calculamos

$$
m_W=\frac{gv_{\rm cand}}2,
$$

$$
m_Z=\frac{v_{\rm cand}}2\sqrt{g^2+g'^2}.
$$

O teste é honesto: nenhuma massa de bóson é usada como entrada. A execução
numérica está em `numerico/q29_eletrofraco_auditado.py`.

## 4. Incompatibilidade variacional atual

O background $C_3$ gaussiano da Q28 possui

$$
\mathbb H_{\rm phys}^{(3)}>0.
$$

Entretanto, a quebra eletrofraca exige que o background **simétrico anterior à
quebra** tenha um modo

$$
\Phi_{\rm EW}\sim(1,2)_{1/2}
$$

com

$$
a_2
=\langle\Phi_{\rm EW},\mathbb H_{\rm sym}\Phi_{\rm EW}\rangle<0.
$$

Logo, $\mathbb H_{\rm sym}$ não pode ser identificada com a Hessiana estável
pós-quebra calculada na Q28. São dois backgrounds distintos:

$$
\mathfrak B_{\rm sym}
\longrightarrow
\mathfrak B_{C_3,\rm quebrado}.
$$

## 5. Cálculo que realmente falta

É necessário construir $\mathfrak B_{\rm sym}$ e calcular

$$
a_2
=\delta^2\mathcal S_{\rm GDQ}
[\Phi_{\rm EW},\bar\Phi_{\rm EW}],
$$

$$
a_4
=\delta^4\mathcal S_{\rm GDQ}
[\Phi_{\rm EW},\Phi_{\rm EW},
\bar\Phi_{\rm EW},\bar\Phi_{\rm EW}].
$$

Somente então

$$
v^2=-\frac{2a_2}{a_4}
$$

é uma previsão. O quociente $m_p6\pi^5/7$ pode coincidir numericamente com
$v$, mas ainda precisa ser demonstrado como o mesmo quociente variacional.

## 6. Veredito

A Q29 permanece estruturalmente formulada, porém não está numericamente
fechada. O obstáculo não é computacional: falta especificar o background
simétrico pré-quebra e seu modo eletrofraco normalizado. Inserir $a_2$, $a_4$
ou $v$ manualmente ocultaria exatamente a dedução pedida em `29-0.md`.
