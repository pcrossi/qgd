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
\text{a identificação variacional de }G\text{ está resolvida; a previsão numérica ab initio permanece aberta.}
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
\mathfrak C_\gamma\!\left[
\int_K
\eta_R\,e^{2A(y,\tau)}
\mathcal U_*(y,\tau)
\sqrt{q_*(y,\tau)}
d^4y
\right]
\int_N R[h]\sqrt{-h}\,d^4x.
\]

Aqui \(\mathfrak C_\gamma\) é a prescrição causal real definida pelo
contorno da ação. Sua normalização, orientação e fatores de \(i\) e \(2\pi\)
precisam ser fixados pela dinâmica causal; ela não pode ser substituída sem
justificativa por \(\operatorname{Re}\oint_\gamma\).

Portanto:

\[
\boxed{
C_R
=
\frac{\hbar}{\Lambda_C^2}
\mathfrak C_\gamma\!\left[
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
\mathfrak C_\gamma\!\left[
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
\mathfrak C_\gamma\!\left[
\int_K
\mathcal U_*(y,\tau)\sqrt{q_*(y,\tau)}\,d^4y
\right].
}
\]

Se definirmos:

\[
\mathcal I_K
:=
\mathfrak C_\gamma\!\left[
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
\mathfrak C_\gamma\!\left[
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

## 6. O que falta após a identificação estrutural

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
\mathfrak C_\gamma\!\left[
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

5. definir a prescrição causal real do contorno \(\gamma\), incluindo seus
   fatores de \(i\) e \(2\pi\);
6. derivar da ação oficial, e não acrescentar separadamente, o funcional
   instantônico de Pontryagin;
7. calcular os operadores \(K_H\), \(K_T\) e \(J\) do complemento de Schur.

## 7. Respostas diretas às perguntas obrigatórias

1. **Por que o grupo de Buckingham tem essa forma?**

   Porque \(G\), \(M_p\), \(\hbar\) e \(c\) formam o acoplamento gravitacional adimensional do próton:
   \[
   \Pi_1=\frac{G M_p^2}{\hbar c}.
   \]
   Isso expressa o acoplamento gravitacional macroscópico medido no laboratório.

2. **Por que aparece \(\alpha^4\)?**

   A estrutura hermitiana-torsional sugere essa potência, mas a redução da
   ação oficial ainda precisa demonstrar por que aparece exatamente
   \(\alpha^4\).

3. **Por que aparece \(e^{-1/(2\alpha)}\)?**

   Ele resulta condicionalmente de
   \(S_E/\hbar=Q_{\rm rel}/\alpha\) e \(Q_{\rm rel}=1/2\). Ainda falta
   derivar esse funcional topológico da ação oficial e avaliar o termo de
   bordo da calota.

4. **O meio-instantão existe numa solução explícita?**

   Ainda não em sentido forte. Existe um ansatz topológico de sela autodual,
   mas falta uma solução local explícita que satisfaça as equações e as
   condições de bordo derivadas da ação oficial.

5. **Por que o fator de Fano entra?**

   A contagem \(N_H=3\), \(N_T=5\) e os ramos conjugados motivam
   \(3\sqrt2/5\). A derivação rigorosa ainda requer os operadores explícitos
   do complemento de Schur e seus espectros.

6. **A massa do próton é entrada?**

   Na fórmula fenomenológica original sim, mas na derivação fundamental de primeiros princípios a massa do próton é substituída por \(M_p = M_e R_p^{\rm GDQ}\), onde \(R_p^{\rm GDQ}\) é a razão de escalas bariônica obtida geometricamente.

7. **A correção eletromagnética foi prevista ou escolhida para eliminar o resíduo?**

   No estado atual ela é uma correção fenomenológica externa. Não integra a
   derivação fundamental até ser obtida do setor local da GDQ antes da
   comparação com o valor observado.

---

## 8. Conclusão final

A Questão 38 fica classificada como:
\[
\boxed{
\text{identificação formal de }G\text{ resolvida; avaliação preditiva ab initio aberta}
}
\]
O documento [resolucao_completa_q38.md](file:///home/pedro/Dropbox/obs/todo/q38/resolucao_completa_q38.md)
registra a parte demonstrada e o programa matemático necessário para o
fechamento forte.

---

## 9. Atualização após a auditoria dimensional e algébrica

As correções estabelecem:

1. **Geometria 8D:** a decomposição radial coerente é
   \(N_4\times I_r\times S^3\). O ansatz anterior com um \(S^1\) adicional
   possuía nove dimensões.
2. **Normalização:** o vínculo global restringe o diláton, mas não determina
   sozinho o perfil local ou a unicidade do background.
3. **Polo e warp:** o perfil
   \(e^{2A}\sim\phi_0/(\tau-\tau_*)\) é uma condição candidata a ser
   demonstrada pela solução das EDPs, não um resultado já obtido.
4. **Contorno causal:** para um resíduo real,
   \(\operatorname{Re}\oint F\,d\tau=0\); a ação deve especificar a operação
   causal que produz um coeficiente real.

---

## 10. Status do meio-instantão, impedância de Fano e planificação

O estado correto dessas construções é:

* **Sela de meio-instantão:** condicional à derivação do funcional de
  Pontryagin a partir da ação oficial e à avaliação do termo de
  Chern--Simons de bordo.
* **Complemento de Schur e Fano:** estruturalmente formulado, mas ainda sem
  os operadores e espectros necessários para calcular \(3\sqrt2/5\).
* **Planificação:** \(J_{\rm flat}^{(0)}=1\) é uma hipótese consistente para
  o modo zero normalizado, devendo ser confirmada na mesma redução espectral.

A fórmula fenomenológica candidata para o acoplamento adimensional é:
\[
\boxed{
\Pi_1^{\rm GDQ} = \frac{G M_p^2}{\hbar c} = \frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}^{\rm bulk}} \exp\!\left(-\frac{1}{2\alpha}\right).
}
\]

Ela implica necessariamente

\[
\boxed{
C_R=\frac{c^3M_p^2}{16\pi\hbar}
\frac{\chi_{\rm Fano}^{\rm bulk}}{\alpha^4(1+\alpha)}
\exp\!\left(\frac1{2\alpha}\right),
}
\]

pois \(C_R=c^4/(16\pi G)\). Essa relação inversa deve ser preservada em
qualquer futura avaliação do resíduo.

---

## 11. Resultado da execução dos quatro blocos

A execução conjunta está documentada em
[derivacao_quatro_blocos_q38.md](file:///home/pedro/Dropbox/obs/todo/q38/derivacao_quatro_blocos_q38.md).
Os resultados são:

1. **Background 8D:** foram obtidas as equações reduzidas de \(A,R,\sigma\)
   para \(N_4\times I_r\times S^3\), incluindo o vínculo radial. A ação não
   seleciona uma solução única sem condições de contorno, fluxo e torção.
2. **Resíduo:** para o ansatz
   \(e^{2A}\sim w^{-p}\), \(R\sim w^q\) e
   \(e^{-\sigma}\sim w^s\), existe polo simples exatamente quando
   \(-p+3q+s=-1\), com coeficiente finito e não nulo. A ação ainda precisa
   selecionar esses expoentes e fixar \(\mathfrak C_\gamma\).
3. **Meio-instantão:** foi provada a implicação
   \(Q_{\rm rel}=1/2\Rightarrow S_{\rm inst}/\hbar=1/(2\alpha)\), condicionada
   à localização do escalar de Bismut no funcional topológico. Essa
   localização não decorre automaticamente da ação escrita.
4. **Fano:** o complemento de Schur é exato, mas seu valor depende dos
   elementos de matriz de \(J\) e dos autovalores de \(K_T\). A simples
   contagem de três e cinco canais não deriva \(3\sqrt2/5\).

Assim, a obstrução restante não é algébrica: faltam as condições de contorno
que selecionam o background, a identidade de localização do setor
instantônico e os operadores espectrais da colagem. Sem esses três dados, a
ação oficial não determina numericamente \(G\).

---

## 12. Avaliação direta dos três dados restantes

O cálculo completo está em
[fechamento_tres_dados_q38.md](file:///home/pedro/Dropbox/obs/todo/q38/fechamento_tres_dados_q38.md).
Ele produz os seguintes resultados:

1. **Contorno:** sem um funcional de bordo, a variação métrica admite
   naturalmente Dirichlet. Regularidade em \(I_r\times S^3\) seleciona
   \(R(0)=0\), \(R'(0)=1\), \(A'(0)=\sigma'(0)=0\); com fluxo de torção
   \(k\ne0\), a finitude exige uma garganta \(R_c>0\), cujo raio precisa ser
   fornecido como dado de bordo. O bulk não seleciona o polo meromorfo.
2. **Localização:** \(\mathcal R_B\) é linear na curvatura, enquanto
   \(\operatorname{Tr}(\mathcal F_B\wedge\mathcal F_B)\) é quadrático. Uma
   reescala da curvatura prova que não existe identidade universal que
   transforme o primeiro no segundo. O meio-instantão requer um determinante
   efetivo ou termo adicional já pertencente à GDQ.
3. **Espectro:** na redução 8D, a fronteira é
   \(N_4\times S^3\), não \(S^3\times T^5\). No background produto a Hessiana
   é bloco-diagonal e \(J=0\). Para um setor toroidal separado foram escritos
   \(K_H\), \(K_T\), seus espectros e a soma exata do complemento de Schur;
   seu valor depende da kernel de colagem, não apenas de contar canais.

Consequentemente, os três dados desejados não são derivados pela ação oficial
bulk em sua forma atual. O fechamento numérico de Q38 exige localizar no
manuscrito um funcional de bordo/Hessiana já pertencente à GDQ ou assumir
explicitamente condições causais e de colagem como novos axiomas
constitutivos, antes de calcular \(G\).
