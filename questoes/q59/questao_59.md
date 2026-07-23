# Questão 59 — Escala eletrofraca

## 1. Enunciado

A questão pede corrigir a alegação de que a fórmula atual produz diretamente a
escala eletrofraca \(v\simeq246\,\mathrm{GeV}\).

A fórmula criticada no manuscrito legado é

$$
v_K
=
\frac{M_e}{\alpha}
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2}.
$$

O problema é aritmético e conceitual: essa expressão não gera \(246\,\mathrm{GeV}\).
Portanto, ela não pode ser apresentada como derivação do valor esperado
eletrofraco.

## 2. Domínio e dados usados

Domínio desta resposta:

1. ação oficial da GDQ preservada;
2. Q29 como documento canônico da quebra eletrofraca geométrica;
3. Q37 como origem vigente de \(\alpha\);
4. Q40/Q29 como origem da escala bariônica usada na normalização global;
5. comparação \(W/Z\) apenas como teste fenomenológico condicional.

Dados numéricos usados no teste:

$$
\alpha^{-1}=137{,}035999177,
\qquad
M_e=0{,}00051099895069\,\mathrm{GeV},
$$

$$
M_p=0{,}93827208816\,\mathrm{GeV}.
$$

O script autocontido está em:

$$
\texttt{questoes/q59/associados/calcular\_escala\_eletrofraca\_q59.py}.
$$

A saída está em:

$$
\texttt{questoes/q59/associados/saida\_calculo\_escala\_eletrofraca\_q59.md}.
$$

## 3. Auditoria da fórmula legada

Substituindo os valores,

$$
\frac{M_e}{\alpha}
=
M_e\alpha^{-1}
\simeq
0{,}070028\,\mathrm{GeV}.
$$

O fator geométrico

$$
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2}
$$

é próximo de \(1\), não de \(10^3\). Logo,

$$
\boxed{
v_K=0{,}072847818683\,\mathrm{GeV}
=72{,}847819\,\mathrm{MeV}.
}
$$

Esse valor está distante de \(246\,\mathrm{GeV}\) por cerca de

$$
-99{,}970413\%.
$$

Portanto,

$$
\boxed{
v_K \neq 246\,\mathrm{GeV}.
}
$$

Essa fórmula deve ser removida como derivação da escala eletrofraca. Se for
mantida no manuscrito, deve ser reclassificada como escala geométrica auxiliar
ou leptônica, nunca como valor esperado eletrofraco.

## 4. Escala eletrofraca vigente na GDQ

Na Q29 consolidada, o valor esperado eletrofraco não é identificado com
\(v_K\). Ele é definido pela rigidez do modo de ordem:

$$
S_{\rm eff}(\varphi)
=
S_0
+
\frac12a_2|\varphi|^2
+
\frac14a_4|\varphi|^4
+
O(|\varphi|^6),
$$

com

$$
a_2<0,
\qquad
a_4>0.
$$

Assim,

$$
\boxed{
v^2=-\frac{2a_2}{a_4}.
}
$$

Os coeficientes adimensionais estruturais já registrados na Q29 são

$$
a_2=-0{,}253196676,
\qquad
a_4^{\rm total}=2133{,}554507>0,
$$

e

$$
\beta_*=0{,}0108937431.
$$

A normalização dimensional vigente usa a calibração geométrica bariônica

$$
\boxed{
v_{\rm GDQ}
=
M_p\frac{6\pi^5}{7}
=
246{,}111195996\,\mathrm{GeV}.
}
$$

Comparada ao valor operacional obtido de \(G_F\),
\(v=(\sqrt2G_F)^{-1/2}\simeq246{,}21965\,\mathrm{GeV}\), a diferença é

$$
-0{,}044048\%.
$$

Essa é a rota correta dentro do estado vigente da teoria: a escala não nasce
da expressão \(M_e/\alpha\), mas da combinação entre o potencial variacional
do modo eletrofraco e a normalização global herdada do setor bariônico/cosmológico.

## 5. O que fica demonstrado

A Q59 fecha os seguintes pontos:

1. a alegação legada \(v_K\simeq246\,\mathrm{GeV}\) é falsa;
2. a fórmula \(v_K\) produz \(72{,}85\,\mathrm{MeV}\);
3. a resposta canônica deve usar

   $$
   v^2=-2a_2/a_4;
   $$

4. a normalização dimensional candidata vigente é

   $$
   v_{\rm GDQ}=M_p6\pi^5/7;
   $$

5. a comparação numérica com \(G_F\) é forte, mas sua leitura metrológica
   permanece condicionada ao fechamento global da normalização.

## 6. Relação com \(W\), \(Z\), fóton e \(\theta_W\)

Na redução efetiva, a Q29 recupera

$$
m_W=\frac{gv}{2},
\qquad
m_Z=\frac v2\sqrt{g^2+g'^2},
\qquad
m_\gamma=0.
$$

O ponto geométrico comum da Q28 fornece

$$
\sin^2\theta_W=\frac38.
$$

Para o background operacional eletrofraco, a rota promissora registrada na Q29
é

$$
\sin^2\theta_W=\frac29,
$$

com transporte diferencial das normas fracas exigindo

$$
\frac{Z_W}{Z_Y}=\frac{10}{21}.
$$

Usando ainda a resposta de superfície condicional

$$
\alpha_{\rm EW}^{-1}=132{,}457669129,
$$

o teste numérico dá

$$
m_W=80{,}403325181\,\mathrm{GeV},
\qquad
m_Z=91{,}168801291\,\mathrm{GeV}.
$$

Comparado aos valores de referência usados no script,

$$
m_W^{\rm ref}=80{,}3692\,\mathrm{GeV},
\qquad
m_Z^{\rm ref}=91{,}1876\,\mathrm{GeV},
$$

os erros são

$$
\Delta_W=+0{,}042461\%,
\qquad
\Delta_Z=-0{,}020615\%.
$$

Classificação desse bloco: comparação fenomenológica condicional. O cálculo
não deve ser chamado de previsão final enquanto a identidade de Schur
eletromagnética e o transporte \(Z_W/Z_Y\) não forem avaliados diretamente no
background global quebrado.

## 7. Status lógico

A Q59 fica classificada como:

$$
\boxed{
\text{fechada estruturalmente e condicionalmente.}
}
$$

Fechada estruturalmente porque a contradição aritmética foi removida e a rota
correta da escala eletrofraca foi identificada.

Condicional porque a metrologia final de \(v\), \(m_W\) e \(m_Z\) ainda depende
de:

1. verificar diretamente a normalização cinética \(Z_\beta\) no background 8D;
2. avaliar a identidade de Schur eletromagnética;
3. derivar o transporte diferencial \(Z_W/Z_Y=10/21\) sem usar \(m_W\) ou
   \(m_Z\) como alvo.

Essas limitações não reabrem a correção principal da Q59: a fórmula \(v_K\)
não é a escala eletrofraca.

## 8. Correção recomendada no manuscrito legado

Substituir qualquer passagem do tipo:

$$
v_K
=
\frac{M_e}{\alpha}
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2}
\approx246\,\mathrm{GeV}
$$

por:

$$
v_K
=
\frac{M_e}{\alpha}
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2}
\approx72{,}85\,\mathrm{MeV}.
$$

E acrescentar:

$$
\boxed{
v_{\rm EW}\neq v_K.
}
$$

A escala eletrofraca na GDQ deve ser tratada por:

$$
v^2=-2a_2/a_4,
\qquad
v_{\rm GDQ}=M_p6\pi^5/7
$$

com o status de normalização geométrica global condicional.

## 9. O que deve ser feito para o fechamento metrológico

O estado atual está suficiente para corrigir o erro conceitual da escala
eletrofraca e preservar a Q29 como fechamento estrutural. Para transformar a
comparação \(W/Z\) em previsão metrológica forte, faltam três cálculos diretos.

### 9.1 Normalização cinética do modo de ordem

Deve-se calcular diretamente, no background 8D quebrado,

$$
Z_\beta
=
\left.
\frac{\partial^2\mathcal S_{\rm GDQ}}
{\partial\dot\beta^2}
\right|_{\Phi_{\rm EW,*}},
$$

ou a forma equivalente obtida pelo pullback causal. O objetivo é verificar se
a normalização adimensional

$$
\beta_*=0{,}0108937431
$$

é transportada para a escala física

$$
v=246{,}111195996\,\mathrm{GeV}
$$

sem usar \(G_F\) como entrada.

Critério de fechamento:

$$
\boxed{
Z_\beta\beta_*^2=v_{\rm GDQ}^2
}
$$

deve sair da ação oficial e das condições globais, não de calibração posterior.

### 9.2 Identidade de Schur eletromagnética

O segundo cálculo é avaliar o complemento de Schur da interface eletromagnética
no setor quebrado:

$$
K_{Q}^{\rm eff}
=
K_Q
-
J_{Q\partial}
H_{\partial}^{-1}
J_{\partial Q}.
$$

A hipótese operacional usada na comparação é

$$
K_{\rm EM}^{\rm eff}
=
\frac{K_{\rm EM}^{(0)}}{1+\mathcal S_\partial},
$$

com

$$
\mathcal S_\partial
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
$$

Critério de fechamento:

$$
\boxed{
\alpha_{\rm EW}^{-1}=132{,}457669129
}
$$

deve ser obtido do bloco real da Hessiana de contorno, não de Chern--Simons
topológico isolado nem de ajuste em \(m_W,m_Z\).

### 9.3 Transporte diferencial \(W/Y\)

O terceiro cálculo é demonstrar que o transporte global entre o ponto geométrico
comum e o background eletrofraco operacional altera as normas dos canais \(W\)
e \(Y\) por

$$
\frac1{g_{\rm EW}^2}
=
Z_W\frac1{g_{\rm match}^2},
\qquad
\frac1{g_{\rm EW}'{}^2}
=
Z_Y\frac1{g_{\rm match}'{}^2},
$$

com

$$
\boxed{
\frac{Z_W}{Z_Y}=\frac{10}{21}.
}
$$

Esse resultado transporta

$$
\sin^2\theta_W=\frac38
$$

do ponto geométrico comum para

$$
\sin^2\theta_W=\frac29
$$

no background operacional. A derivação deve vir de perfis, holonomias ou
projetores globais em \(T^5\times S^3\), não da escolha direta do valor
fenomenológico.

### 9.4 Resultado esperado após os três fechamentos

Se os três cálculos acima forem demonstrados, a cadeia metrológica ficará:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{\rm EW,*}
\to
a_2,a_4,Z_\beta
\to
v
\to
K_Q^{\rm eff},Z_W/Z_Y
\to
g,g'
\to
m_W,m_Z.
$$

Nesse caso, a Q59 deixará de ser apenas estrutural/condicional e poderá ser
promovida a fechamento metrológico do setor eletrofraco.

Até lá, o status correto permanece:

$$
\boxed{
\text{correção da escala fechada; metrologia }W/Z\text{ em refinamento.}
}
$$
