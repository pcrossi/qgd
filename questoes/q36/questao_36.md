# Questão 36 — De onde vem a escala dimensional?

## 1. Pergunta

A Questão 36 pergunta de onde vêm as unidades físicas da teoria.

As perguntas obrigatórias são:

1. qual comprimento ou energia fundamental é assumido;
2. se essa escala é derivada ou medida;
3. como autovalores adimensionais se tornam MeV ou GeV;
4. se a escala é universal.

O critério de resolução é direto:

\[
\boxed{
\text{se uma massa experimental fixa a escala, as demais massas são razões previstas}
}
\]

e não massas absolutas derivadas inteiramente ab initio.

---

## 2. Veredito

\[
\boxed{
\text{a Questão 36 está fechada no sentido metrológico por calibração}
}
\]

O manuscrito possui uma estrutura coerente para gerar razões espectrais:

\[
\frac{M_i}{M_j}
=
\frac{\sqrt{\hat\lambda_i}}{\sqrt{\hat\lambda_j}},
\]

onde \(\hat\lambda_i\) são autovalores adimensionais de operadores geométricos.

Mas a conversão desses autovalores para unidades físicas exige uma escala dimensional:

\[
E_0
=
\frac{\hbar c}{\ell_0}.
\]

Isso não é uma deficiência por si só. Nenhuma teoria física determina o
significado operacional de “MeV”, “GeV”, “metro” ou “segundo” sem uma
convenção metrológica. O que uma teoria fundamental deve prever são razões
adimensionais. A unidade física é fixada por calibração.

Assim, se o elétron é tomado como padrão metrológico,

\[
E_0=M_ec^2,
\]

então a GDQ deve prever razões como:

\[
\frac{M_\mu}{M_e},
\qquad
\frac{M_p}{M_e},
\qquad
\frac{\Lambda_C}{M_ec^2}.
\]

Portanto, o status correto é:

\[
\boxed{
\text{a escala absoluta é uma calibração; a exigência física é prever razões}
}
\]

---

## 3. O ponto dimensional básico

Um operador espectral geométrico pode ser escrito como:

\[
L\phi_n=\lambda_n\phi_n.
\]

Se a variedade for escrita em coordenadas físicas, então:

\[
[\lambda_n]=L^{-2}.
\]

Nesse caso:

\[
M_n c^2
=
\hbar c\sqrt{\lambda_n}.
\]

Mas se a geometria interna for normalizada com raio unitário, o operador fornece autovalores adimensionais:

\[
\hat L\phi_n=\hat\lambda_n\phi_n,
\qquad
[\hat\lambda_n]=1.
\]

Para obter energia física é necessário introduzir um comprimento:

\[
\lambda_n
=
\frac{\hat\lambda_n}{\ell_0^2}.
\]

Então:

\[
M_n c^2
=
\frac{\hbar c}{\ell_0}\sqrt{\hat\lambda_n}.
\]

Definindo:

\[
E_0:=\frac{\hbar c}{\ell_0},
\]

temos:

\[
\boxed{
M_n c^2=E_0\sqrt{\hat\lambda_n}.
}
\]

Logo:

\[
\boxed{
\text{autovalores adimensionais só viram MeV ou GeV depois que }E_0\text{ é fixado}
}
\]

---

## 4. Qual escala dimensional aparece na ação oficial?

A ação oficial da GDQ contém:

\[
\frac{\hbar}{\Lambda_C^2}.
\]

Portanto, a candidata natural a escala dimensional fundamental da camada efetiva é:

\[
\boxed{
\Lambda_C
}
\]

ou, equivalentemente:

\[
\boxed{
\ell_C=\frac{\hbar c}{\Lambda_C}.
}
\]

Essa escala não deve ser confundida com:

1. massa do elétron;
2. escala hadrônica;
3. escala eletrofraca;
4. escala de Planck;
5. parâmetro de resolução \(\Lambda(\tau)=\tau^{-1/2}\).

Conforme já separado na Questão 33:

\[
\boxed{
\Lambda_C\neq \Lambda(\tau)\neq m_i.
}
\]

Portanto, a resposta formal é:

\[
\boxed{
\text{a escala dimensional candidata da GDQ é }\Lambda_C\text{ ou }\ell_C
}
\]

mas o valor numérico dessa escala ainda precisa ser derivado.

---

## 5. O que o Capítulo 24 realmente demonstra?

O Capítulo 24 propõe:

\[
M_n c^2=\hbar\sqrt{\lambda_n}.
\]

Essa fórmula está correta apenas se \(\lambda_n\) já possuir dimensão física.

Se \(\lambda_n\) for obtido de uma geometria normalizada, a fórmula correta deve ser:

\[
M_n c^2
=
E_0\sqrt{\hat\lambda_n}
=
\frac{\hbar c}{\ell_0}\sqrt{\hat\lambda_n}.
\]

O Capítulo 24 calcula principalmente razões entre léptons. Por exemplo:

\[
M_\mu
=
M_e
\left(
\frac{3}{2}\alpha^{-1}
+\sqrt2\chi_{\rm Fano}
+2\alpha
\right).
\]

Essa fórmula usa \(M_e\) como escala de entrada.

Logo, a conclusão tecnicamente correta é:

\[
\boxed{
\text{o capítulo prevê }M_\mu/M_e\text{, não }M_\mu\text{ absoluto}
}
\]

Da mesma forma, a massa do tau via Koide usa \(M_e\) e \(M_\mu\):

\[
\frac{M_e+M_\mu+M_\tau}
{(\sqrt{M_e}+\sqrt{M_\mu}+\sqrt{M_\tau})^2}
=
\frac23.
\]

Se \(M_e\) e \(M_\mu\) já entraram em MeV, então \(M_\tau\) sai em MeV.

Portanto:

\[
\boxed{
\text{Koide fixa uma relação geométrica de massas, não a unidade absoluta de massa}
}
\]

---

## 6. O que o Apêndice 1 realmente demonstra?

O Apêndice 1 deriva quantidades como:

\[
V_0=\frac{\pi^2}{2},
\]

\[
\Delta V_{\rm top}
=
\frac{3}{4\pi^2},
\]

\[
\delta_{\rm bare}
=
\ln(2\pi^2),
\]

\[
\chi_{\rm Fano}
=
\frac{3\sqrt2}{5},
\]

\[
\delta_{\rm efetivo}
=
\ln(2\pi^2)\frac{3\sqrt2}{5}
\approx2{,}530827.
\]

Esses são números adimensionais.

O próprio texto compara:

\[
\delta_{\rm efetivo}
\approx
\frac{M_n-M_p}{M_e}.
\]

Essa é uma comparação de razão.

Para obter:

\[
M_n-M_p
\]

em MeV, é necessário multiplicar por:

\[
M_e.
\]

Portanto:

\[
\boxed{
\delta_{\rm efetivo}
\text{ pode ser uma previsão geométrica de razão, mas não fixa sozinho a escala MeV}
}
\]

Isso é uma força do texto se for apresentado corretamente: a GDQ prevê números puros, e a escala absoluta é uma calibração separada.

---

## 7. Como autovalores se tornam MeV ou GeV?

A conversão correta é:

\[
\boxed{
E_n=E_0\,\varepsilon_n
}
\]

onde:

\[
\varepsilon_n:=\sqrt{\hat\lambda_n}
\]

é adimensional.

Existem três possibilidades.

### 7.1 Escala medida

Escolhe-se uma massa observada, por exemplo:

\[
E_0
=
\frac{M_e c^2}{\varepsilon_e}.
\]

Se a normalização escolher \(\varepsilon_e=1\), então:

\[
E_0=M_ec^2.
\]

Nesse caso:

\[
M_n
=
M_e
\frac{\varepsilon_n}{\varepsilon_e}.
\]

Essa rota é fenomenologicamente válida, mas deve ser descrita como:

\[
\boxed{
\text{predição de razões após calibração por }M_e
}
\]

### 7.2 Escala geométrica derivada

Deriva-se \(\ell_0\) de uma condição interna:

\[
\ell_0
=
\ell_C
=
\text{funcional de }(g_{\mu\bar\nu},f,\bar f,\gamma).
\]

Então:

\[
E_0=\frac{\hbar c}{\ell_C}.
\]

Essa seria a versão ab initio forte.

Mas ela ainda não foi demonstrada numericamente de modo fechado.

### 7.3 Escala setorial

Cada setor pode possuir uma escala própria:

\[
E_0^{(s)}
=
\frac{\hbar c}{\ell_s},
\]

com:

\[
s=e,\mu,\tau,\text{had},\text{EW},\text{grav},\ldots
\]

Nesse caso:

\[
M_n^{(s)}c^2
=
E_0^{(s)}\varepsilon_n^{(s)}.
\]

Essa possibilidade é compatível com a Questão 33, mas exige cuidado: se cada setor recebe uma escala experimental própria, a teoria perde poder preditivo absoluto e passa a prever apenas razões internas.

---

## 8. A escala é universal?

Atualmente, o texto não demonstra uma escala universal única.

A hipótese universal seria:

\[
E_0=\Lambda_C
\quad
\text{para todos os setores.}
\]

Mas isso enfrentaria problemas já apontados na Questão 33:

1. \(0{,}511\,{\rm MeV}\) não pode ser corte universal;
2. \(1\,{\rm GeV}\) não pode ser corte universal sem conflito com escalas de colisores;
3. \(246\,{\rm GeV}\) não foi derivado corretamente pela fórmula \(M_e/\alpha\);
4. diferentes setores parecem usar escalas distintas.

Portanto, a resposta mais segura é:

\[
\boxed{
\text{a escala absoluta ainda não está provada universal}
}
\]

O que há é uma estrutura de escalas:

\[
\boxed{
E_0^{(s)}
\text{ pode ser setorial, enquanto as razões }\varepsilon_i^{(s)}/\varepsilon_j^{(s)}
\text{ são geométricas}
}
\]

---

## 9. Respostas obrigatórias

### 9.1 Qual comprimento ou energia fundamental é assumido?

A candidata formal é:

\[
\ell_C=\frac{\hbar c}{\Lambda_C},
\qquad
E_C=\Lambda_C.
\]

Mas, em vários cálculos concretos do manuscrito, a escala prática usada é:

\[
M_e c^2.
\]

Logo, há duas leituras:

\[
\boxed{
\Lambda_C\text{ é a escala formal da ação}
}
\]

e:

\[
\boxed{
M_e\text{ é frequentemente usado como calibração fenomenológica}
}
\]

Essas duas coisas não podem ser confundidas.

### 9.2 Ele é derivado ou medido?

No estado atual:

\[
\boxed{
M_e\text{ é medido}
}
\]

e:

\[
\boxed{
\Lambda_C\text{ ainda precisa ser derivado numericamente}
}
\]

O manuscrito possui tentativas de derivar constantes adimensionais, como \(\alpha\), \(\chi\), \(\delta_{\rm efetivo}\), fatores de Fano e razões espectrais.

Mas a escala absoluta em MeV/GeV ainda não está fechada de modo independente.

### 9.3 Como autovalores adimensionais se tornam MeV ou GeV?

Por multiplicação por uma escala:

\[
M_n c^2
=
E_0\sqrt{\hat\lambda_n}.
\]

Se \(E_0\) é fixado por \(M_e\), então:

\[
M_n
=
M_e
\sqrt{\frac{\hat\lambda_n}{\hat\lambda_e}}.
\]

Se \(E_0\) é derivado de \(\ell_C\), então:

\[
M_n c^2
=
\frac{\hbar c}{\ell_C}\sqrt{\hat\lambda_n}.
\]

### 9.4 A escala é universal?

Ainda não foi provado.

O texto deve assumir uma destas posições:

1. escala universal \(\Lambda_C\), derivada uma vez para todos os setores;
2. escalas setoriais \(E_0^{(s)}\), cada uma derivada por operador setorial;
3. uma escala medida, por exemplo \(M_e\), usada como calibração, com o restante tratado como razão prevista.

A opção mais honesta agora é a terceira, com abertura para a segunda.

---

## 10. Correção conceitual necessária

Sempre que o texto escrever:

\[
\text{``massa calculada ab initio''}
\]

mas usar \(M_e\), \(M_p\), \(M_n\), \(v\), \(f_B\), \(\Lambda_{\rm QCD}\) ou qualquer massa experimental como entrada, deve substituir por:

\[
\boxed{
\text{massa obtida como razão geométrica após calibração de escala}
}
\]

Exemplo:

\[
M_\mu
=
M_e R_\mu^{\rm GDQ}.
\]

Então a predição real é:

\[
\boxed{
R_\mu^{\rm GDQ}
=
\frac{M_\mu}{M_e}
}
\]

não \(M_\mu\) absoluto.

---

## 11. O que falta para fechar a questão

Para fechar a Questão 36 em sentido forte, é necessário provar uma das seguintes teses.

### Tese A — escala universal

Derivar:

\[
\Lambda_C
=
F[g_{\mu\bar\nu},f,\bar f,\gamma]
\]

da ação oficial e das condições de contorno, sem usar uma massa experimental.

Depois mostrar que:

\[
M_n c^2
=
\Lambda_C\,\varepsilon_n.
\]

### Tese B — escala setorial derivada

Para cada setor \(s\), derivar:

\[
E_0^{(s)}
=
\frac{\hbar c}{\ell_s}
\]

como autovalor fundamental de um operador:

\[
L_s\phi_n^{(s)}
=
\lambda_n^{(s)}\phi_n^{(s)}.
\]

Depois mostrar:

\[
M_n^{(s)}c^2
=
E_0^{(s)}\varepsilon_n^{(s)}.
\]

### Tese C — calibração fenomenológica

Assumir explicitamente uma escala de referência metrológica:

\[
E_0=M_ec^2
\]

ou outra escala medida.

Então declarar:

\[
\boxed{
\text{a teoria prevê razões adimensionais; a unidade MeV é fixada por calibração}
}
\]

Essa tese é suficiente para fechar a questão dimensional no sentido físico
usual. O ponto que permanece matematicamente exigente não é derivar a unidade
“MeV” do nada, mas demonstrar que as razões usadas pela teoria são
geométricas e não entradas experimentais disfarçadas.

Em particular, se a escala de Cartan for ligada ao raio de estômato
\(r_c\),

\[
\Lambda_C\simeq \frac{\hbar c}{r_c},
\]

então a razão relevante é:

\[
\boxed{
\theta_C
:=
\frac{\Lambda_C}{M_ec^2}
=
\frac{\lambda_e}{r_c},
}
\]

com

\[
\lambda_e=\frac{\hbar}{M_ec}.
\]

Logo, a questão fica fechada se \(r_c/\lambda_e\), ou
equivalentemente \(\theta_C\), for derivado da geometria de Kähler,
do empacotamento do bulk e das condições de contorno, sem inserir o valor
experimental de \(r_c\) como postulado.

---

## 12. Conclusão final

A Questão 36 fica classificada como:

\[
\boxed{
\text{fechada por calibração metrológica}
}
\]

com a seguinte leitura:

\[
\boxed{
\text{a GDQ deve prever razões geométricas; a escala MeV é uma escolha de unidade}
}
\]

O manuscrito deve apresentar massas, cortes e constantes dimensionais como
resultados espectrais relativos após uma calibração explícita, por exemplo
por \(M_e\). A pendência remanescente é verificar, caso a caso, que razões
como \(\Lambda_C/(M_ec^2)\), \(M_\mu/M_e\), \(M_p/M_e\) e \(M_n/M_e\) são
realmente deduzidas da geometria, e não ajustadas por valores experimentais.
