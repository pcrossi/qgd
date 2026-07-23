# Questão 38 — Como \(G\) é derivada?

## 1. Pergunta

A Questão 38 pergunta:

\[
\boxed{
\text{como a GDQ deriva a constante gravitacional de Newton }G?
}
\]

O arquivo `38-0.md` exige responder:

1. por que o grupo de Buckingham escolhido tem a forma proposta;
2. por que aparece \(\alpha^4\);
3. por que aparece \(e^{-1/(2\alpha)}\);
4. se o meio-instantão existe numa solução explícita;
5. por que o fator de Fano entra;
6. se a massa do próton é entrada;
7. se a correção eletromagnética foi prevista ou escolhida para eliminar o
   resíduo.

O critério de resolução é:

\[
\boxed{
\text{derivar o limite newtoniano da ação e identificar }G
\text{ no coeficiente de Einstein--Hilbert.}
}
\]

---

## 2. Veredito

\[
\boxed{
\text{a Questão 38 fica fechada estruturalmente pela extração de }C_R
}
\]

O Apêndice 2 fornece uma fórmula fenomenológica numericamente boa:

\[
\Pi_1
=
\frac{G M_p^2}{\hbar c}
=
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
\exp\!\left(-\frac{1}{2\alpha}\right),
\]

e então:

\[
G
=
\frac{\hbar c}{M_p^2}
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
\exp\!\left(-\frac{1}{2\alpha}\right).
\]

Essa expressão acerta a ordem de grandeza e chega perto do valor CODATA, mas
ela deve ser lida como avaliação fenomenológica da integral interna efetiva,
não como a derivação fundamental. A derivação fundamental vem da extração do
coeficiente \(C_R\) do termo de curvatura da ação oficial.

Portanto, o status correto é:

\[
\boxed{
\text{Buckingham valida a avaliação; }C_R\text{ vem da ação.}
}
\]

---

## 3. O caminho correto para derivar \(G\)

A derivação de \(G\) deve começar na ação oficial da GDQ, não na fórmula
dimensional.

A ação fundamental é:

\[
\mathcal{S}_{\rm GDQ}=
\int_{\gamma}\left[
\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
\]

Para obter gravidade efetiva em quatro dimensões, deve-se expandir a métrica
complexa em torno de um background estacionário:

\[
g_{\mu\bar\nu}
=
g_{\mu\bar\nu}^{(0)}
+\delta g_{\mu\bar\nu},
\]

escolher a fatia real física \(N\), integrar os graus internos e projetar o
setor métrico real \(h_{\mu\nu}\). A redução efetiva deve ter a forma:

\[
\boxed{
S_{\rm eff}[h,\cdots]
\supset
C_R
\int_N R[h]\sqrt{-h}\,d^4x.
}
\]

O coeficiente \(C_R\) é o objeto que precisa ser derivado da geometria:

\[
\boxed{
C_R
=
\mathcal C_R[
g_*,
f_*,
\bar f_*,
\mathcal U_*,
\gamma,
\Lambda_C,
\text{dados de contorno}
].
}
\]

Depois disso, \(G\) é identificado por comparação com Einstein--Hilbert:

\[
S_{\rm EH}
=
\frac{c^4}{16\pi G}
\int_N R[h]\sqrt{-h}\,d^4x.
\]

Logo:

\[
\boxed{
G
=
\frac{c^4}{16\pi C_R}.
}
\]

Em unidades naturais \(c=1\):

\[
\boxed{
G
=
\frac{1}{16\pi C_R}.
}
\]

Essa é a derivação exigida por `38-0.md`.

---

## 3.1 Extração direta de \(C_R\) da ação oficial

O termo de curvatura da ação oficial é:

\[
\mathcal S_{\mathcal R}
=
\int_\gamma
\left[
\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\tau\mathcal R\,
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]
\frac{d\tau}{\tau}.
\]

O fator \(\tau\) do termo de curvatura cancela o \(1/\tau\) da medida de
contorno. Portanto:

\[
\boxed{
\mathcal S_{\mathcal R}
=
\frac{\hbar}{\Lambda_C^2}
\int_\gamma d\tau
\int_{\mathcal M_\mathbb C}
\mathcal R\,
\mathcal U\sqrt{\det g}\,d^{2n}z.
}
\]

Agora assumimos a redução local de campo fraco:

\[
\mathcal M_\mathbb C
\simeq
N\times K,
\]

onde:

- \(N\) é a fatia real física \(4D\), com métrica \(h_{\mu\nu}(x)\);
- \(K\) é o setor interno/fibra compacta efetiva;
- o background estacionário é \((g_*,f_*,\bar f_*)\);
- \(h_{\mu\nu}\) varia lentamente em \(N\);
- os modos internos permanecem no estado fundamental.

Permitindo uma deformação conforme interna geral, escrevemos o bloco
externo como:

\[
ds^2_{\rm ext}
=
e^{2A(y,\tau)}h_{\mu\nu}(x)dx^\mu dx^\nu.
\]

Então a curvatura escalar complexa projetada contém:

\[
\mathcal R[g]
=
\eta_R\,e^{-2A(y,\tau)}R[h]
+\mathcal R_K
+\text{termos de gradiente interno}
+\text{termos de mistura}.
\]

Aqui \(\eta_R\) é o fator de normalização entre a curvatura escalar de
Kähler-Ricci usada na ação e a curvatura escalar real \(R[h]\). Com a
convenção em que a projeção real já está normalizada como Einstein-Hilbert,
\(\eta_R=1\). Se a convenção de Kähler usar
\(\mathcal R_K=g^{\mu\bar\nu}R_{\mu\bar\nu}\) como metade da curvatura real,
então \(\eta_R\) deve absorver esse fator.

A medida fatoriza como:

\[
\sqrt{\det g}
=
e^{4A(y,\tau)}
\sqrt{-h(x)}\sqrt{q_*(y,\tau)}
\]

no setor externo \(4D\). Logo, o termo proporcional a \(R[h]\) fica:

\[
\mathcal S_{\mathcal R}
\supset
\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}
\left[
\int_\gamma d\tau
\int_K
\eta_R\,e^{2A(y,\tau)}
\mathcal U_*(y,\tau)
\sqrt{q_*(y,\tau)}
d^4y
\right]
\int_N R[h]\sqrt{-h}\,d^4x.
\]

Portanto, obtemos explicitamente:

\[
\boxed{
C_R
=
\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}
\left[
\int_\gamma d\tau
\int_K
\eta_R\,e^{2A(y,\tau)}
\mathcal U_*(y,\tau)
\sqrt{q_*(y,\tau)}
d^4y
\right].
}
\]

Definindo o volume efetivo ponderado:

\[
\boxed{
\mathcal V_{\rm eff}^{(G)}
:=
\operatorname{Re}
\left[
\int_\gamma d\tau
\int_K
\eta_R\,e^{2A(y,\tau)}
\mathcal U_*(y,\tau)
\sqrt{q_*(y,\tau)}
d^4y
\right],
}
\]

fica:

\[
\boxed{
C_R
=
\frac{\hbar}{\Lambda_C^2}
\mathcal V_{\rm eff}^{(G)}.
}
\]

E, portanto:

\[
\boxed{
G
=
\frac{c^4\Lambda_C^2}
{16\pi\hbar\,\mathcal V_{\rm eff}^{(G)}}.
}
\]

Em unidades naturais:

\[
\boxed{
G
=
\frac{\Lambda_C^2}
{16\pi\,\mathcal V_{\rm eff}^{(G)}}.
}
\]

Essa é a forma variacional de \(G\) exigida pela questão.

### Caso sem warp

Se:

\[
A=0,
\qquad
\eta_R=1,
\]

então:

\[
\boxed{
C_R
=
\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}
\left[
\int_\gamma d\tau
\int_K
\mathcal U_*(y,\tau)\sqrt{q_*(y,\tau)}\,d^4y
\right].
}
\]

Se definirmos:

\[
\mathcal I_K
:=
\operatorname{Re}
\left[
\int_\gamma d\tau
\int_K
\mathcal U_*\sqrt{q_*}\,d^4y
\right],
\]

temos:

\[
\boxed{
C_R=\frac{\hbar}{\Lambda_C^2}\mathcal I_K,
\qquad
G=\frac{c^4\Lambda_C^2}{16\pi\hbar\,\mathcal I_K}.
}
\]

### Interpretação

O acoplamento gravitacional não vem de um número escolhido
posteriormente. Ele é o inverso do volume efetivo ponderado do setor interno
sob a medida de Perelman-GDQ.

Quanto maior:

\[
\mathcal V_{\rm eff}^{(G)},
\]

menor é \(G\). Isso é fisicamente coerente: a gravidade macroscópica fica
fraca porque a curvatura local é diluída por um volume interno/contorno
geométrico muito grande na medida efetiva.

---

## 3.2 Relação com a fórmula de Buckingham

A fórmula fenomenológica do Apêndice 2 pode agora ser reinterpretada como
uma avaliação aproximada de \(\mathcal V_{\rm eff}^{(G)}\), não como ponto
de partida.

Como:

\[
G
=
\frac{\hbar c}{M_p^2}
\Pi_1,
\qquad
\Pi_1
=
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
e^{-1/(2\alpha)},
\]

então:

\[
C_R
=
\frac{c^4}{16\pi G}
=
\frac{c^3M_p^2}{16\pi\hbar\,\Pi_1}.
\]

Logo:

\[
\boxed{
C_R^{\rm Buck}
=
\frac{c^3M_p^2}{16\pi\hbar}
\frac{\chi_{\rm Fano}}
{\alpha^4(1+\alpha)}
e^{1/(2\alpha)}.
}
\]

Comparando com a expressão variacional:

\[
C_R
=
\frac{\hbar}{\Lambda_C^2}
\mathcal V_{\rm eff}^{(G)},
\]

obtemos a condição de fechamento:

\[
\boxed{
\mathcal V_{\rm eff}^{(G)}
=
\frac{\Lambda_C^2c^3M_p^2}{16\pi\hbar^2}
\frac{\chi_{\rm Fano}}
{\alpha^4(1+\alpha)}
e^{1/(2\alpha)}.
}
\]

Na forma calibrada por \(M_e\), usando:

\[
M_p=M_eR_p^{\rm GDQ},
\]

fica:

\[
\boxed{
\mathcal V_{\rm eff}^{(G)}
=
\frac{\Lambda_C^2c^3M_e^2}{16\pi\hbar^2}
\left(R_p^{\rm GDQ}\right)^2
\frac{\chi_{\rm Fano}}
{\alpha^4(1+\alpha)}
e^{1/(2\alpha)}.
}
\]

Essa equação mostra exatamente onde os fatores do Apêndice 2 devem entrar:
eles não definem \(G\) diretamente; eles devem emergir da integral interna
ponderada \(\mathcal V_{\rm eff}^{(G)}\).

---

## 3.3 Status após a extração de \(C_R\)

A parte variacional da Questão 38 fica fechada no seguinte sentido:

\[
\boxed{
C_R
=
\frac{\hbar}{\Lambda_C^2}
\mathcal V_{\rm eff}^{(G)}
}
\]

com:

\[
\boxed{
\mathcal V_{\rm eff}^{(G)}
=
\operatorname{Re}
\left[
\int_\gamma d\tau
\int_K
\eta_R e^{2A}
\mathcal U_*
\sqrt{q_*}\,d^4y
\right].
}
\]

O que ainda não está fechado é a avaliação numérica dessa integral no
background estacionário real da GDQ. Essa avaliação deve demonstrar,
sem pós-ajuste, que:

\[
\mathcal V_{\rm eff}^{(G)}
\sim
\frac{\chi_{\rm Fano}}{\alpha^4(1+\alpha)}
e^{1/(2\alpha)}
\times
\text{escala de massa/calibração}.
\]

Portanto:

\[
\boxed{
\text{Q38 fica fechada estruturalmente; o valor numérico de }G
\text{ depende da avaliação de }\mathcal V_{\rm eff}^{(G)}.
}
\]

---

## 4. Limite newtoniano

Uma vez obtido:

\[
S_{\rm eff}
=
C_R\int R[h]\sqrt{-h}\,d^4x
+S_{\rm mat}[h,\Phi],
\]

a variação em \(h^{\mu\nu}\) fornece:

\[
C_R\,G_{\mu\nu}
=
\frac12 T_{\mu\nu}.
\]

Comparando com:

\[
G_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu},
\]

temos novamente:

\[
C_R=\frac{c^4}{16\pi G}.
\]

No regime de campo fraco:

\[
h_{00}
=
-\left(1+\frac{2\Phi}{c^2}\right),
\qquad
|\Phi|/c^2\ll1,
\]

e para matéria lenta:

\[
T_{00}\simeq \rho c^2.
\]

Então a equação de Einstein reduz-se a:

\[
\nabla^2\Phi
=
4\pi G\rho.
\]

Portanto, a GDQ só deriva \(G\) em sentido forte se a redução da ação
oficial produzir o coeficiente \(C_R\) e, em seguida, reproduzir essa equação
de Poisson com o mesmo \(G\).

---

## 5. Auditoria da fórmula atual do Apêndice 2

### 5.1 Grupo de Buckingham

O grupo:

\[
\Pi_1=\frac{G M_p^2}{\hbar c}
\]

é dimensionalmente correto. Ele é o análogo gravitacional da constante de
estrutura fina para duas massas \(M_p\):

\[
\alpha_G(M_p)
=
\frac{G M_p^2}{\hbar c}.
\]

Mas essa escolha já usa \(M_p\) como escala de massa. Portanto, ela não
deriva \(G\) sozinha. Ela reescreve \(G\) como:

\[
G=\frac{\hbar c}{M_p^2}\Pi_1.
\]

Assim, para a fórmula ser preditiva, a GDQ deve derivar simultaneamente:

\[
\Pi_1^{\rm GDQ}
\qquad\text{e}\qquad
\frac{M_p}{M_e}
\]

como razões geométricas, com \(M_e\) servindo apenas como calibração
metrológica, conforme a Questão 36.

### 5.2 Origem de \(\alpha^4\)

O Apêndice 2 justifica \(\alpha^4\) pela estrutura Kähler de dimensão
complexa \(2\), usando a forma:

\[
\frac12\Omega\wedge\Omega.
\]

A ideia é plausível como contagem geométrica: uma \((2,2)\)-forma envolve
dois pares de acoplamentos, sugerindo:

\[
\alpha^2\times\alpha^2=\alpha^4.
\]

Mas isso ainda não foi derivado variacionalmente da ação oficial. Falta
mostrar que a redução do termo de curvatura ou do determinante efetivo gera
exatamente essa quarta potência, e não \(\alpha^2\), \(\alpha^3\) ou uma
função mais geral.

Status:

\[
\boxed{
\alpha^4\text{ é uma hipótese geométrica plausível, não um teorema fechado.}
}
\]

### 5.3 Origem de \(e^{-1/(2\alpha)}\)

O fator:

\[
\exp\!\left(-\frac{1}{2\alpha}\right)
\]

é interpretado como tunelamento instantônico quiral ou meio-instantão.

Para ser derivação, é necessário exibir uma solução de sela \(\phi_{\rm inst}\)
da ação euclidiana efetiva tal que:

\[
S_E[\phi_{\rm inst}]
=
\frac{\hbar}{2\alpha}.
\]

Então:

\[
e^{-S_E/\hbar}
=
e^{-1/(2\alpha)}.
\]

No estado atual, o Apêndice 2 não fornece essa solução explícita, nem calcula
sua ação euclidiana. Portanto:

\[
\boxed{
e^{-1/(2\alpha)}\text{ é uma estrutura instantônica postulada, ainda não provada.}
}
\]

### 5.4 Fator de Fano

O fator:

\[
\chi_{\rm Fano}
=
\frac{3\sqrt2}{5}
\approx0.848528
\]

entra como admitância/impedância da fronteira:

\[
Z_{\rm vac}=\frac{1}{\chi_{\rm Fano}}.
\]

Essa interpretação é compatível com a linguagem de ressonância, canais de
interferência e impedância geométrica já usada no manuscrito. Porém, para
fechar a Q38, é necessário demonstrar que esse mesmo \(\chi_{\rm Fano}\)
aparece no coeficiente \(C_R\) do termo \(R[h]\), e não apenas em uma fórmula
de ajuste para \(\Pi_1\).

Status:

\[
\boxed{
\chi_{\rm Fano}\text{ é aproveitável, mas precisa ser conectado ao coeficiente }C_R.
}
\]

### 5.5 Massa do próton

Na fórmula atual:

\[
G
=
\frac{\hbar c}{M_p^2}\Pi_1,
\]

\(M_p\) é uma entrada se o valor experimental do próton for usado.

Isso não invalida automaticamente a rota, desde que a tese metrológica da
Questão 36 seja respeitada. O correto é escrever:

\[
M_p=M_e\,R_p^{\rm GDQ},
\]

com:

\[
R_p^{\rm GDQ}
=
\frac{M_p}{M_e}
\]

derivado geometricamente.

Então:

\[
G
=
\frac{\hbar c}{M_e^2}
\frac{\Pi_1^{\rm GDQ}}{(R_p^{\rm GDQ})^2}.
\]

Nessa forma, \(M_e\) fixa a unidade metrológica e a GDQ prevê a razão
gravitacional:

\[
\boxed{
\frac{G M_e^2}{\hbar c}
=
\frac{\Pi_1^{\rm GDQ}}{(R_p^{\rm GDQ})^2}.
}
\]

Essa é a maneira correta de compatibilizar a Q38 com a Q36.

### 5.6 Correção eletromagnética residual

O Apêndice 2 introduz uma correção radiativa de \(1\)-loop para remover o
resíduo de aproximadamente \(-0.26\%\). Isso é problemático por dois motivos:

1. a GDQ não toma renormalização por contratermos como fundamento;
2. a correção usa massas eletrofracas/protônicas externas e parece escolhida
   após a comparação numérica.

Portanto, essa correção deve ser reclassificada como comparação efetiva
externa, não como parte da derivação fundamental de \(G\).

Status:

\[
\boxed{
\text{a correção eletromagnética ainda parece pós-ajuste; precisa ser prevista antes.}
}
\]

---

## 6. O que falta após o fechamento estrutural

A cadeia variacional principal agora está definida:

\[
\mathcal S_{\rm GDQ}
\longrightarrow
C_R
=
\frac{\hbar}{\Lambda_C^2}
\mathcal V_{\rm eff}^{(G)}
\longrightarrow
G
=
\frac{c^4\Lambda_C^2}
{16\pi\hbar\,\mathcal V_{\rm eff}^{(G)}}.
\]

O que falta não é mais identificar \(C_R\), mas avaliar a integral:

\[
\mathcal V_{\rm eff}^{(G)}
=
\operatorname{Re}
\left[
\int_\gamma d\tau
\int_K
\eta_R e^{2A}
\mathcal U_*
\sqrt{q_*}\,d^4y
\right].
\]

As pendências restantes são:

1. fixar \(\eta_R\), isto é, a normalização entre \(\mathcal R\) da ação
   Kähler-Ricci e \(R[h]\) real;
2. determinar o warp \(A(y,\tau)\) no background estacionário;
3. avaliar a integral interna com a medida oficial:

   \[
   \mathcal U_*
   =
   \frac{e^{-(f_*+\bar f_*)/2}}
   {(4\pi z_\tau)^4};
   \]

4. provar que a avaliação direta reproduz os fatores fenomenológicos do
   Apêndice 2, se eles forem mantidos:

   \[
   \alpha^{-4},
   \qquad
   \chi_{\rm Fano},
   \qquad
   e^{1/(2\alpha)};
   \]

5. recuperar explicitamente o limite de Poisson:

   \[
   \nabla^2\Phi=4\pi G\rho.
   \]

Depois disso, a combinação:

\[
\frac{G M_p^2}{\hbar c}
\]

deve ser usada apenas como verificação adimensional da avaliação de
\(\mathcal V_{\rm eff}^{(G)}\).

---

## 7. Respostas diretas às perguntas obrigatórias

1. **Por que o grupo de Buckingham tem essa forma?**

   Porque \(G\), \(M_p\), \(\hbar\) e \(c\) formam o acoplamento
   gravitacional adimensional do próton:

   \[
   \Pi_1=\frac{G M_p^2}{\hbar c}.
   \]

   Isso é dimensionalmente correto, mas não deriva \(G\).

2. **Por que aparece \(\alpha^4\)?**

   A justificativa atual é a estrutura \((2,2)\) da forma de volume Kähler.
   É plausível, mas ainda precisa ser derivada da redução da ação.

3. **Por que aparece \(e^{-1/(2\alpha)}\)?**

   Deve vir de uma sela euclidiana com:

   \[
   S_E/\hbar=1/(2\alpha).
   \]

   Essa sela ainda não foi exibida.

4. **O meio-instantão existe numa solução explícita?**

   Ainda não. Falta escrever a solução, seu domínio, suas condições de
   contorno e calcular sua ação.

5. **Por que o fator de Fano entra?**

   Ele pode representar admitância/impedância de fronteira. Após a extração
   de \(C_R\), a exigência precisa é mostrar que \(\chi_{\rm Fano}\) emerge
   da integral \(\mathcal V_{\rm eff}^{(G)}\), e não de um ajuste posterior.

6. **A massa do próton é entrada?**

   Sim, se for usado \(M_p\) experimental. Para evitar isso, deve-se usar:

   \[
   M_p=M_eR_p^{\rm GDQ},
   \]

   com \(R_p^{\rm GDQ}\) derivado geometricamente.

7. **A correção eletromagnética foi prevista ou escolhida para eliminar o
   resíduo?**

   No texto atual, ela parece pós-ajuste. Deve ser tratada como correção
   efetiva externa até que seja prevista antes da comparação com CODATA.

---

## 8. Conclusão final

A Questão 38 fica classificada como:

\[
\boxed{
\text{fechada estruturalmente como derivação variacional de }G
}
\]

mas:

\[
\boxed{
\text{a avaliação numérica de }\mathcal V_{\rm eff}^{(G)}
\text{ ainda precisa ser feita.}
}
\]

A rota correta é:

\[
\boxed{
\mathcal S_{\rm GDQ}
\longrightarrow
C_R\int R[h]\sqrt{-h}
\longrightarrow
G=\frac{c^4}{16\pi C_R}
\longrightarrow
\nabla^2\Phi=4\pi G\rho.
}
\]

O Apêndice 2 deve ser preservado como validação numérica e inspiração
estrutural. Com a extração de \(C_R\), ele passa a ser interpretado como uma
proposta de avaliação aproximada da integral interna
\(\mathcal V_{\rm eff}^{(G)}\), ainda pendente de cálculo direto no
background estacionário.

---

## 9. Atualização após a auditoria instantônica e espectral

Os desenvolvimentos posteriores estão consolidados em
`questoes/q38/associados/retroacao_e_determinante_espectral_q38.md`. Foram obtidos:

1. um background assintótico steady de Einstein--Bismut em
   \((S^3\times S^1)\times T^4\);
2. a classe relativa autodual com \(Q_{\rm rel}=1/2\);
3. a equação elíptica da retroação geométrica;
4. o operador relativo cujo determinante fornece o prefator semiclassico.

O fechamento numérico ainda não foi executado porque falta reduzir a ação
oficial no setor \(Q_{\rm rel}=1/2\) e variá-la com respeito ao módulo
instantônico \(\rho_0/R\), à cola de borda e aos modos zero. Essas quantidades
não são entradas adicionais: devem ser saídas da ação oficial. Como alteram o
determinante, não podem ser escolhidas usando o resíduo de \(0.2668\%\).

Status atualizado:

\[
\boxed{
\text{Q38 aberta na derivação do setor instantônico a partir da ação oficial.}
}
\]

A auditoria final em questoes/q38/associados/auditoria_final_acao_instanton_q38.md identificou que
o completamento BPS usado para obter
\(S_{\rm inst}/\hbar=1/(2\alpha)\) pressupõe um funcional quadrático em
\(\mathcal F_B\), enquanto a ação oficial exibida é linear em
\(\mathcal R_B\). Sem demonstrar a equivalência no setor reduzido, o
determinante BPST não é o determinante da ação oficial.

### 9.1 Correção ontológica

A rota instantônica/Yang--Mills não pertence à resposta oficial da GDQ e foi
retirada da cadeia dedutiva. A correção está consolidada em
questoes/q38/associados/correcao_rota_gdq_pura.md.

O exponencial deve vir da medida oficial
\[
\mathcal U=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n},
\]
isto é,
\[
\frac{f_*+\bar f_*}{2}=\frac1{2\alpha},
\]
caso a equação estacionária produza esse valor. A derivação permanece
\[
\mathcal S_{\rm GDQ}\longrightarrow C_R^{\rm GDQ}
\longrightarrow G=\frac{c^4}{16\pi C_R^{\rm GDQ}},
\]
sem introduzir uma ação de Yang--Mills.

### 9.2 Resultado da variação GDQ normalizada

A variação correta inclui o multiplicador da condição
\(\int\mathcal U\,dV=1\). Ela não fixa localmente
\((f_*+\bar f_*)/2=1/(2\alpha)\). Para um modo constante, o exponencial é
fixado pelo volume e cancelado na integral normalizada.

Além disso, \(T^5\) plano com dilaton constante não satisfaz a equação
shrinking em \(\tau<\infty\). O resultado completo está em
questoes/q38/associados/fechamento_gdq_pura.md.

### 9.3 Fechamento topológico do ansatz shrinking

A tentativa de reparar o produto plano por um warp suave também foi
auditada. A obstrução é global: um sóliton gradiente shrinking compacto tem
grupo fundamental finito, enquanto

\[
\pi_1(T^5\times S^3)=\mathbb Z^5.
\]

Logo, nenhuma métrica warped que preserve essa topologia resolve a equação
shrinking ordinária da ação oficial. A demonstração está em
questoes/q38/associados/fechamento_topologico_q38.md.

Isso encerra a procura por um warp nesse ansatz. Permanece válida a extração
formal

\[
G=\frac{c^4}{16\pi C_R^{\rm GDQ}},
\]

mas o valor numérico de \(C_R^{\rm GDQ}\) exige uma sela admissível distinta
ou a formulação variacional explícita do setor steady de Bismut.

\[
\boxed{
\text{Q38: diagnóstico estrutural fechado; previsão numérica de }G\text{ aberta.}
}

### 9.4 Teste do setor steady de Bismut no contorno oficial

O background homogêneo de Hopf--Bismut satisfaz condicionalmente as equações
steady quando \(\mathcal R\) é interpretada como
\(R_{LC}-|H|^2/12\), com \(H=d^c\omega(g,J)\). Contudo, isso não basta para
gerar gravidade. Definindo

\[
F_R(\tau)=\int_K\eta_R e^{2A}\mathcal U\,dV_K,
\]

o termo de curvatura da ação dá

\[
C_R^{\rm GDQ}
=\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}\oint_\gamma F_R(\tau)d\tau.
\]

No modo steady homogêneo e normalizado, \(F_R=\eta_R\) é constante; logo a
integral fechada é zero. Um coeficiente gravitacional não nulo exige polo,
corte ou monodromia causal em \(\tau\). No caso meromorfo,

\[
C_R^{\rm GDQ}
=\frac{2\pi\hbar}{\Lambda_C^2}
\operatorname{Re}\left[i\sum_k\operatorname{Res}_{\tau_k}F_R\right].
\]

O critério e sua condição de realidade estão demonstrados em
questoes/q38/associados/criterio_residuo_contorno_gdq.md. Portanto, o problema numérico restante
é calcular esse resíduo diretamente de uma solução causal da GDQ, sem usar
Yang--Mills e sem calibrá-lo por \(G\).

### 9.5 Avaliação direta do resíduo causal

A evolução conjugada conservativa dá, para uma inserção geométrica suave,

\[
F_R(z)=\langle e^{zL}\Phi_R,\mathcal U_0\rangle
=a_0+a_1z+a_2z^2+\cdots.
\]

O aparente polo \((4\pi z)^{-n}\) do kernel é cancelado pela integração
gaussiana e pela normalização. Assim,

\[
\boxed{\operatorname{Res}_{z=0}F_R=0,
\qquad C_R^{\rm GDQ}=0}
\]

no setor suave, normalizado e sem defeitos. A combinação causal simétrica
retardada--avançada não cria um termo \(z^{-1}\) ausente em ambos os ramos.
A prova está em questoes/q38/associados/derivacao_causal_residuo_q38.md.

Consequentemente, a fórmula atual não prevê um \(G\) não nulo. Para fazê-lo,
a GDQ precisa derivar geometricamente um defeito, salto, fonte singular ou
monodromia que invalide uma hipótese do teorema de anulação; seu coeficiente
não pode ser calibrado por \(G\).
\]
