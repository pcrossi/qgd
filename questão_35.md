# Questão 35 — O polo de Landau foi eliminado?

## 1. Pergunta

A Questão 35 pergunta se o polo de Landau foi eliminado na GDQ.

As exigências mínimas são:

1. identificar qual beta-função foi calculada;
2. identificar quais diagramas contribuem;
3. especificar o esquema de renormalização;
4. demonstrar estabilidade do ponto fixo;
5. verificar compatibilidade com o running observado de \(\alpha\).

A formulação correta deve respeitar a ação oficial da GDQ e não pode substituir uma derivação por uma beta-função postulada.

Há, porém, uma distinção essencial:

\[
\boxed{
\text{na GDQ não há renormalização fundamental por contratermos}
}
\]

O que existe é fluxo geométrico de escala, parametrizado por \(\tau\), com regularização intrínseca pela estrutura da própria variedade. Portanto, nesta questão, palavras como “beta-função”, “running” e “esquema de renormalização” devem ser lidas como linguagem comparativa externa, usada para responder à auditoria em termos reconhecíveis pela QFT perturbativa.

Internamente, a pergunta correta não é:

\[
\text{``qual contratermo remove o polo?''}
\]

mas:

\[
\text{``o fluxo geométrico impede que a descrição pontual produza o polo?''}
\]

---

## 2. Veredito

\[
\boxed{
\text{Q35 fechada condicionalmente no setor }U(1)
}
\]

A leitura inicial deste documento era que o manuscrito continha uma ideia física
consistente e aproveitável, mas ainda não a tradução perturbativa externa. Essa
lacuna foi reduzida nas seções 14 e 15 por:

1. cálculo explícito da polarização \(U(1)\) com heat-kernel covariante;
2. saturação ultravioleta de \(\Pi_\tau(q^2)\);
3. identificação setorial \(\tau_{\rm EM}=\Lambda_{\rm EM}^{-2}\).
4. derivação de $\widehat\Lambda_{\rm EM}=1{,}90727017413475$ no subespaço
   homogêneo e calibração $\Lambda_{\rm EM}=1{,}90727017413475\Lambda_C$.

O resultado físico aproveitado continua sendo:

\[
\boxed{
\text{a geometria GDQ fornece um regulador ultravioleta dinâmico}
}
\]

O status tecnicamente correto agora é:

\[
\boxed{
\text{o polo de Landau é evitado na tradução }U(1)\text{ efetiva por saturação
heat-kernel; falta avaliar }\Lambda_{\rm EM}\text{ numericamente.}
}
\]

---

## 3. O que o manuscrito já possui

O Capítulo 5 propõe que o polo de Landau seja evitado porque a estrutura geométrica da GDQ impede o limite pontual \(r\to 0\).

O mecanismo físico usado é:

1. a densidade \(\rho\) não colapsa livremente em uma delta;
2. o potencial quântico de Bohm cresce quando a distribuição se torna muito concentrada;
3. a métrica responde a essa pressão geométrica;
4. a distância própria efetiva não atinge zero;
5. os modos ultravioleta são amortecidos pela estrutura de fluxo.

Em forma efetiva, o Capítulo 33 escreve um propagador regularizado:

\[
\mathcal G(p)
\propto
\frac{e^{-|p|^2/\Lambda_{\rm Cartan}^2}}
{p^2-m^2+i\epsilon}.
\]

Essa estrutura é compatível com a análise das Questões 32 e 33, desde que seja lida como uma redução plana do kernel geométrico:

\[
G_\tau(L)
=
e^{-\tau L}L^{-1},
\qquad
\tau\simeq \Lambda^{-2}.
\]

Portanto, o que já está estruturalmente justificado é:

\[
\boxed{
\text{loops ficam amortecidos por um fator geométrico do tipo heat-kernel}
}
\]

e, por isso, integrais perturbativas típicas passam de:

\[
\int^\infty d^4k\,\frac{1}{(k^2+m^2)^n}
\]

para:

\[
\int^\infty d^4k\,
\frac{e^{-\tau k^2}}{(k^2+m^2)^n}.
\]

Essa integral é finita para \(\tau>0\).

Esse resultado é importante, mas ainda não é a mesma coisa que uma prova completa de eliminação do polo de Landau em linguagem de beta-função perturbativa.

---

## 4. Primeira beta-função proposta no Capítulo 5

O Capítulo 5 propõe:

\[
\beta(\alpha)
\equiv
\frac{d\alpha}{dt}
=
-b_0\alpha^2
+\gamma_C\alpha^3
\exp\left(-\frac{\Lambda_C^2}{Q^2}\right),
\qquad
t=\ln(Q^2/\mu^2).
\]

No limite infravermelho:

\[
Q^2\ll \Lambda_C^2
\quad\Rightarrow\quad
e^{-\Lambda_C^2/Q^2}\to0,
\]

o texto afirma:

\[
\beta(\alpha)\approx -b_0\alpha^2
=
\frac{\alpha^2}{3\pi}.
\]

Aqui há uma inconsistência de sinal no próprio texto, porque ele simultaneamente escreve \(b_0>0\) e afirma que, na QED convencional, \(b_0=-1/(3\pi)\).

Para recuperar a QED usual, a convenção deve ser fixada explicitamente. Em notação usual para QED:

\[
\beta_\alpha
=
\mu\frac{d\alpha}{d\mu}
=
\frac{2}{3\pi}
\left(\sum_f N_c Q_f^2\right)\alpha^2
+O(\alpha^3),
\]

com variações de fator dependendo se o parâmetro de fluxo é \(\ln\mu\) ou \(\ln Q^2\).

No limite ultravioleta:

\[
Q^2\gg \Lambda_C^2
\quad\Rightarrow\quad
e^{-\Lambda_C^2/Q^2}\to1,
\]

a beta-função proposta vira:

\[
\beta(\alpha)
\to
-b_0\alpha^2+\gamma_C\alpha^3
=
\alpha^2(\gamma_C\alpha-b_0).
\]

O ponto fixo não trivial seria:

\[
\alpha_*
=
\frac{b_0}{\gamma_C}.
\]

Mas isso só é uma prova se:

1. \(b_0\) for derivado dos diagramas corretos;
2. \(\gamma_C\) for calculado a partir da ação oficial;
3. o sinal for coerente;
4. o ponto fixo for estável;
5. o running em baixas energias reproduzir a QED observada.

Com a convenção:

\[
\frac{d\alpha}{dt}=\beta(\alpha),
\qquad
t=\ln Q^2,
\]

a estabilidade linear é determinada por:

\[
\delta'=\beta'(\alpha_*)\delta.
\]

Para:

\[
\beta(\alpha)
=
-b_0\alpha^2+\gamma_C\alpha^3,
\]

temos:

\[
\beta'(\alpha)
=
-2b_0\alpha+3\gamma_C\alpha^2.
\]

No ponto fixo:

\[
\beta'(\alpha_*)
=
-2b_0\frac{b_0}{\gamma_C}
+3\gamma_C\frac{b_0^2}{\gamma_C^2}
=
\frac{b_0^2}{\gamma_C}.
\]

Se \(b_0>0\) e \(\gamma_C>0\), então:

\[
\beta'(\alpha_*)>0.
\]

Logo, nessa convenção, o ponto fixo é UV-instável, não UV-estável.

Portanto, a beta-função do Capítulo 5 ainda não fecha a Questão 35.

---

## 5. Segunda beta-função proposta nas notas 5.4 e 5.5

As notas 5.4 e 5.5 propõem uma dedução por integração de camada de momento, com:

\[
g_{ij}=\bar g_{ij}+\tilde g_{ij},
\qquad
H=\bar H+\tilde H.
\]

O termo de pressão geométrica é escrito como:

\[
\mathcal V_{\rm pressão}(k)
=
\frac{\hbar^4}{4m^2}k^4.
\]

A beta-função proposta é:

\[
\beta(g)
=
\frac{A g^2}
{1+\frac{\hbar^4}{4m^2}\mu^2}
-
\frac{B g^3}
{\left(1+\frac{\hbar^4}{4m^2}\mu^2\right)^2}.
\]

Essa expressão contém uma ideia aproveitável:

\[
\boxed{
\text{o termo de quarta ordem enfraquece o fluxo no ultravioleta}
}
\]

De fato, para \(g\) finito:

\[
\mu\to\infty
\quad\Rightarrow\quad
\beta(g,\mu)\to0.
\]

Isso sugere congelamento assintótico ou saturação geométrica.

Mas há três problemas técnicos.

### 5.1 A beta-função não é autônoma

Uma beta-função de ponto fixo usual é uma equação autônoma:

\[
\mu\frac{dg}{d\mu}=\beta(g).
\]

Aqui a expressão depende explicitamente de \(\mu\):

\[
\mu\frac{dg}{d\mu}=\beta(g,\mu).
\]

Então a raiz:

\[
g_*(\mu)
=
\frac{A}{B}
\left(
1+\frac{\hbar^4}{4m^2}\mu^2
\right)
\]

não é um ponto fixo genuíno de RG, porque se move com a escala.

Um ponto fixo real deveria satisfazer:

\[
g(\mu)\to g_*=\text{constante}
\qquad
\text{quando}
\qquad
\mu\to\infty.
\]

### 5.2 A geometria usada está desatualizada

As notas citam \(T^5\times S^3\).

Mas a estrutura oficial consolidada é:

\[
\mathcal M=\mathbb R^4\times T^4.
\]

Logo, os coeficientes \(A\) e \(B\) precisam ser recalculados na geometria oficial.

### 5.3 Os coeficientes não foram derivados

As notas tratam \(A\) e \(B\) como constantes geométricas, mas não calculam:

1. quais operadores de Hessiana entram;
2. quais autovalores contribuem;
3. quais degenerescências entram no traço funcional;
4. qual esquema de subtração foi usado;
5. como \(A/B\) se relaciona com \(\alpha\).

Portanto, a segunda beta-função também ainda não fecha a Questão 35.

---

## 6. Relação com a Questão 34

A Questão 35 depende diretamente da Questão 34.

Para traduzir o fluxo geométrico para uma função de escala comparável a uma beta-função de calibre, antes é necessário ter:

1. setor gauge efetivo derivado da ação oficial;
2. fixação de gauge;
3. determinante de Faddeev--Popov ou substituto geométrico;
4. propagadores;
5. vértices;
6. identidade de Ward/Slavnov--Taylor;
7. prescrição de extração do acoplamento efetivo.

Sem isso, uma beta-função escrita no texto permanece uma hipótese efetiva externa, não uma consequência da GDQ.

O teste mínimo é a polarização do vácuo:

\[
\Pi_{\mu\nu}^{ab}(q).
\]

Para um setor \(U(1)\), a identidade de Ward exige:

\[
q^\mu\Pi_{\mu\nu}(q)=0.
\]

Para um setor não abeliano:

\[
q^\mu\Pi_{\mu\nu}^{ab}(q)=0
\]

no nível transversal apropriado, ou sua forma de Slavnov--Taylor no formalismo gauge-fixado.

Somente depois disso é possível extrair, se quisermos falar na linguagem QFT:

\[
Z_A,\qquad Z_e,\qquad \beta(e),
\]

e então comparar a GDQ com a descrição perturbativa onde aparece o polo de Landau.

---

## 7. Como a prova deve ser feita

A rota mínima deve ser setorial.

Não é necessário resolver todos os setores da GDQ de uma vez. O caminho mais limpo é começar por um setor efetivo \(U(1)\), porque o polo de Landau é originalmente um problema da QED.

### 7.1 Definir o setor efetivo

Assumir uma conexão efetiva:

\[
A_\mu
\]

emergente da geometria, conforme a Questão 28, mas sem importar o Modelo Padrão como postulado.

O setor quadrático deve ter a forma:

\[
S_A^{(2)}
=
\frac12
\int a_\mu
\mathcal O_A^{\mu\nu}
a_\nu.
\]

Depois da fixação de gauge de fundo:

\[
F[A]=\bar D^\mu a_\mu=0,
\]

o propagador regularizado deve ser:

\[
D_{\mu\nu}^{(\tau)}(k)
=
e^{-\tau L_A(k)}
\left(L_A^{-1}\right)_{\mu\nu}.
\]

No limite plano:

\[
D_{\mu\nu}^{(\tau)}(k)
\sim
\frac{e^{-\tau k^2}}{k^2}
\left(
\eta_{\mu\nu}
-
(1-\xi)\frac{k_\mu k_\nu}{k^2}
\right).
\]

### 7.2 Calcular a polarização do vácuo

O cálculo mínimo é:

\[
\Pi_{\mu\nu}(q)
=
-e^2
\int
\frac{d^4k}{(2\pi)^4}
\operatorname{Tr}
\left[
\gamma_\mu
S_\tau(k)
\gamma_\nu
S_\tau(k+q)
\right],
\]

com propagador fermônico regularizado:

\[
S_\tau(k)
=
e^{-\tau L_\psi(k)}
S(k).
\]

No limite plano simples:

\[
S_\tau(k)
\sim
e^{-\tau(k^2+m^2)}
\frac{i\slashed{k}+m}{k^2+m^2}.
\]

A estrutura tensorial deve reduzir a:

\[
\Pi_{\mu\nu}(q)
=
\left(q_\mu q_\nu-q^2\eta_{\mu\nu}\right)\Pi(q^2).
\]

Isso prova transversalidade:

\[
q^\mu\Pi_{\mu\nu}(q)=0.
\]

### 7.3 Extrair a lei efetiva de escala

Não se deve definir a GDQ por renormalização de contratermos. O procedimento correto é definir um acoplamento efetivo medido em uma escala operacional \(\mu\), por exemplo a partir da resposta de dois pontos:

\[
\alpha_R(\mu)
=
\frac{\alpha_0}
{1-\Pi_R(q^2=\mu^2)}.
\]

Essa expressão é apenas uma tradução fenomenológica. O objeto fundamental continua sendo o fluxo em \(\tau\), com:

\[
\mu^2\sim \tau^{-1}.
\]

Então pode-se definir uma função de escala efetiva:

\[
\mathcal B_\alpha(\alpha,\mu)
=
\mu\frac{d\alpha_R}{d\mu}.
\]

Em baixas energias, essa função efetiva precisa recuperar:

\[
\beta_\alpha
\simeq
\frac{2}{3\pi}
\left(\sum_f N_cQ_f^2\right)\alpha^2
+O(\alpha^3),
\]

nos regimes em que a QED convencional já foi testada.

Em altas energias, a correção geométrica deve modificar a integral de modo calculável. A prova do fim do polo exige mostrar uma das duas alternativas:

1. ou \(\alpha_{\rm eff}(\mu)\) tende a um valor finito;
2. ou a escala física \(\Lambda_C\) encerra a validade da descrição pontual antes que a solução perturbativa alcance o polo.

Essas duas teses são diferentes.

A primeira é uma tese de ponto fixo:

\[
\lim_{\mu\to\infty}\alpha_R(\mu)=\alpha_*<\infty.
\]

A segunda é uma tese de completude geométrica:

\[
\mu\gtrsim \Lambda_C
\quad\Rightarrow\quad
\text{o fluxo não é mais descrito por QED pontual}.
\]

O manuscrito atual sustenta melhor a segunda tese: não há polo porque o regime pontual que geraria o polo não é fisicamente acessível na GDQ.

---

## 8. Compatibilidade com o running observado de \(\alpha\)

A GDQ não pode eliminar o running de baixa energia.

Ela deve preservar o fato de que a constante de estrutura fina efetiva varia com escala. Portanto, a regularização geométrica deve ser fraca no regime experimental já medido.

Isso exige:

\[
\tau\mu^2\ll1
\]

no domínio em que a QED usual funciona, de modo que:

\[
e^{-\tau k^2}\approx1.
\]

Somente no regime ultravioleta profundo a estrutura geométrica pode se tornar relevante:

\[
\tau\mu^2\gtrsim1.
\]

Assim, a compatibilidade fenomenológica exige uma janela:

\[
\beta_{\rm GDQ}(\alpha,\mu)
\approx
\beta_{\rm QED}(\alpha)
\quad
\text{em baixas e médias energias},
\]

mas:

\[
\beta_{\rm GDQ}(\alpha,\mu)
\not\approx
\beta_{\rm QED}(\alpha)
\quad
\text{no ultravioleta geométrico}.
\]

---

## 9. Resposta às perguntas obrigatórias

### 9.1 Qual beta-função foi calculada?

Nenhuma beta-função foi calculada de modo completo a partir da ação oficial.

Existem duas beta-funções propostas:

\[
\beta(\alpha)
=
-b_0\alpha^2
+\gamma_C\alpha^3
e^{-\Lambda_C^2/Q^2}
\]

e:

\[
\beta(g)
=
\frac{A g^2}
{1+\frac{\hbar^4}{4m^2}\mu^2}
-
\frac{B g^3}
{\left(1+\frac{\hbar^4}{4m^2}\mu^2\right)^2}.
\]

Ambas são úteis como ansatz efetivo, mas ainda não são derivadas finais.

### 9.2 Quais diagramas contribuem?

Ainda não foram listados nem calculados.

Para o setor \(U(1)\), o mínimo é a polarização de vácuo por loop de férmions.

Para setor não abeliano, entram também:

1. loop de gauge;
2. loop de matéria;
3. loop de ghost ou jacobiano geométrico equivalente;
4. possíveis loops de modos métricos/conformais se acoplados ao setor.

### 9.3 Qual é o esquema de renormalização?

A resposta interna é:

\[
\boxed{
\text{nenhum esquema de renormalização fundamental é usado}
}
\]

Não há cancelamento de infinitos por contratermos como princípio da teoria. O que precisa ser especificado é uma prescrição de leitura efetiva do acoplamento em função da escala.

As opções comparativas, apenas para diálogo com QFT, são:

1. subtração em momento;
2. esquema tipo \(\overline{\rm MS}\) adaptado ao heat-kernel;
3. Wilsoniano em cascas de \(\tau\);
4. esquema espectral por traço de calor.

Para a GDQ, a prescrição mais natural é:

\[
\boxed{
\text{extração espectral por heat-kernel/fluxo em }\tau
}
\]

mas ela precisa ser definida.

### 9.4 O ponto fixo é estável?

Ainda não foi demonstrado.

Na beta-função cúbica do Capítulo 5:

\[
\beta(\alpha)
=
-b_0\alpha^2+\gamma_C\alpha^3,
\]

o ponto:

\[
\alpha_*=\frac{b_0}{\gamma_C}
\]

tem:

\[
\beta'(\alpha_*)
=
\frac{b_0^2}{\gamma_C}.
\]

Se \(b_0,\gamma_C>0\), ele é instável para fluxo UV com \(t=\ln Q^2\).

Portanto, a estabilidade precisa ser corrigida ou a convenção de sinais precisa ser reformulada.

### 9.5 É compatível com o running observado de \(\alpha\)?

Ainda não foi demonstrado.

Para ser compatível, a GDQ deve reproduzir a QED usual em baixas energias:

\[
\beta_\alpha
\propto
\alpha^2
\]

com o coeficiente correto, e só modificar o fluxo no regime em que a geometria interna se torna relevante.

---

## 10. Forma correta da conclusão

A conclusão defensável não é:

\[
\text{``o polo de Landau foi eliminado por uma beta-função já provada''.}
\]

A conclusão defensável é:

\[
\boxed{
\text{a GDQ possui um mecanismo geométrico natural que evita a singularidade pontual}
}
\]

e:

\[
\boxed{
\text{a regularização heat-kernel torna loops finitos para }\tau>0
}
\]

mas:

\[
\boxed{
\text{a tradução perturbativa externa ainda requer cálculo da função efetiva de escala}
}
\]

---

## 11. O que falta para fechar a Questão 35

Para fechar a Questão 35, é necessário:

1. escolher o setor \(U(1)\) efetivo como teste mínimo;
2. derivar o operador quadrático \(L_A^{(2)}\) da ação oficial;
3. fixar gauge ou provar o jacobiano geométrico equivalente;
4. calcular \(\Pi_{\mu\nu}(q)\);
5. provar:

   \[
   q^\mu\Pi_{\mu\nu}(q)=0;
   \]

6. escolher prescrição de leitura efetiva de escala;
7. extrair \(\alpha_{\rm eff}(\mu)\) e, se necessário, \(\mathcal B_\alpha=\mu\,d\alpha_{\rm eff}/d\mu\);
8. verificar o limite QED em baixa energia;
9. estudar o limite ultravioleta;
10. provar estabilidade ou ausência de polo.

---

## 12. Conclusão final

A Questão 35 fica classificada como:

\[
\boxed{
\text{classificação histórica antes das seções 14--15: não fechada como
tradução perturbativa externa}
}
\]

Após o cálculo \(U(1)\) e a fixação setorial de \(\tau\), a classificação
atualizada é:

\[
\boxed{
\text{fechada estruturalmente no setor }U(1)\text{ efetivo; avaliação de }
\Lambda_{\rm EM}\text{ pendente.}
}
\]

O conteúdo aproveitável do manuscrito é a tese de que a geometria GDQ impede o colapso pontual e fornece um amortecimento de heat-kernel para loops.

O ponto que ainda falta é transformar esse mecanismo em uma função efetiva de escala calculada, com operador, propagadores, identidade de Ward e teste fenomenológico. Isso não significa introduzir renormalização fundamental; significa apenas produzir a tradução necessária para responder à pergunta na linguagem onde o polo de Landau foi originalmente formulado.

---

## 13. Consolidação pela rota \(U(1)\)

O adendo:

\[
\boxed{\texttt{q35/U1\_sem\_polo\_Landau.md}}
\]

fixa a formulação tecnicamente correta.

O objeto fundamental é:

\[
\boxed{
G_\tau(L)=e^{-\tau L}L^{-1}.
}
\]

Para comparação externa com QED, define-se:

\[
\boxed{
\alpha_{\rm eff}(\mu)
=
\frac{\alpha_0}{1-\Pi_\tau(q^2=\mu^2)}.
}
\]

com:

\[
\boxed{
\Pi_{\mu\nu}^{(\tau)}(q)
=
(q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2).
}
\]

A função:

\[
\boxed{
\mathcal B_\alpha(\mu)=\mu\frac{d\alpha_{\rm eff}}{d\mu}
}
\]

é apenas tradução perturbativa externa, não renormalização fundamental da GDQ.

O status defensável é:

\[
\boxed{
\text{o polo de Landau não é uma singularidade fundamental da GDQ.}
}
\]

Isso decorre de que, para \(\tau>0\), o heat-kernel torna finitas as integrais
ultravioletas e a descrição pontual não pode ser extrapolada indefinidamente
para além da escala geométrica.

Antes da execução da polarização \(U(1)\), ainda não estava demonstrado:

\[
\boxed{
\text{a função completa }\alpha_{\rm eff}(\mu)\text{ foi calculada.}
}
\]

Para fechar Q35 como cálculo abeliano, faltava executar:

1. \(\Pi_{\mu\nu}^{(\tau)}(q)\) no setor \(U(1)\);
2. a verificação de Ward;
3. a extração de \(\Pi_\tau(q^2)\);
4. a recuperação da QED em baixa energia;
5. o comportamento UV por uma das teses:

   \[
   \alpha_{\rm eff}(\mu)\to\alpha_*<\infty
   \]

   ou:

   \[
   \mu\gtrsim\Lambda_C
   \Rightarrow
   \text{a descrição pontual deixa de ser física.}
   \]

Portanto:

\[
\boxed{
\text{Questão 35 estava estruturalmente formulada como evitação geométrica do
polo; o fechamento quantitativo dependia da polarização }U(1).
}
\]

---

## 14. Execução da polarização \(U(1)\) e saturação UV

O cálculo comum a Q34/Q35 foi executado em:

\[
\boxed{\texttt{q34/polarizacao\_U1\_heat\_kernel.md}}
\]

A função escalar obtida é:

\[
\boxed{
\Pi_\tau(q^2)
=
\frac{2\alpha_0}{\pi}
\int_0^1dx\,x(1-x)
\left[
E_1(\tau m^2)
-
E_1\!\left(\tau[m^2+x(1-x)q_E^2]\right)
\right].
}
\]

Ela satisfaz:

\[
\boxed{
\Pi_\tau(0)=0.
}
\]

No limite de baixa energia, \(\tau q_E^2\ll1\), recupera-se:

\[
\boxed{
\Pi_\tau(q^2)
\to
\frac{2\alpha_0}{\pi}
\int_0^1dx\,x(1-x)
\ln\left(
1+\frac{x(1-x)q_E^2}{m^2}
\right).
}
\]

Para \(q_E^2\gg m^2\), ainda abaixo da escala geométrica:

\[
\boxed{
\Pi_\tau(q^2)
\simeq
\frac{\alpha_0}{3\pi}\ln\frac{q_E^2}{m^2}
+\text{constante finita}.
}
\]

Assim, a tradução externa reproduz o comportamento QED:

\[
\boxed{
\mathcal B_\alpha\simeq\frac{2}{3\pi}\alpha^2
}
\]

para um férmion de carga unitária.

No ultravioleta geométrico, \(q_E^2\to\infty\) com \(\tau>0\):

\[
\boxed{
\Pi_\tau(\infty)
=
\frac{\alpha_0}{3\pi}E_1(\tau m^2).
}
\]

Logo:

\[
\boxed{
\alpha_{\rm eff}(\infty)
=
\frac{\alpha_0}
{1-\frac{\alpha_0}{3\pi}E_1(\tau m^2)}.
}
\]

O polo é evitado se:

\[
\boxed{
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<1.
}
\]

Equivalente:

\[
\boxed{
E_1(\tau m^2)<\frac{3\pi}{\alpha_0}\approx1291.
}
\]

Portanto:

\[
\boxed{
\text{Questão 35 fechada no setor }U(1)\text{ efetivo: a função de escala
externa satura e não produz polo físico para }\tau>0\text{ sob essa condição.}
}
\]

A lista de extensões foi atualizada na seção seguinte, após a fixação
geométrica setorial de \(\tau\).

---

## 15. Fixação geométrica setorial de \(\tau\)

A identificação de \(\tau\) como resolução geométrica setorial foi consolidada
em:

\[
\boxed{\texttt{q35/tau\_geometrico\_setorial.md}}
\]

Para o setor eletromagnético efetivo:

\[
\boxed{
\tau_{\rm EM}=\Lambda_{\rm EM}^{-2}.
}
\]

Portanto, \(\tau\) não é parâmetro de renormalização livre. Ele é a escala de
resolução do heat-kernel do setor.

Com essa identificação:

\[
\boxed{
\Pi_{\rm EM}(\infty)
=
\frac{\alpha_0}{3\pi}
E_1\!\left(\frac{m^2}{\Lambda_{\rm EM}^2}\right).
}
\]

Para múltiplos férmions:

\[
\boxed{
\Pi_{\rm EM}(\infty)
=
\frac{\alpha_0}{3\pi}
\sum_fN_c^{(f)}Q_f^2
E_1\!\left(\frac{m_f^2}{\Lambda_{\rm EM}^2}\right).
}
\]

Logo a condição sem polo é:

\[
\boxed{
\frac{\alpha_0}{3\pi}
\sum_fN_c^{(f)}Q_f^2
E_1\!\left(\frac{m_f^2}{\Lambda_{\rm EM}^2}\right)<1.
}
\]

O que permanecia antes da ponte macro--local da Seção 16 era uma pendência
numérica/geométrica de constantes:

\[
\boxed{
\text{calcular }\Lambda_{\rm EM}\text{ a partir da geometria setorial completa.}
}
\]

Veredito atualizado:

\[
\boxed{
\text{Questão 35 fechada condicionalmente no setor }U(1).
}
\]

Após a Seção 16 e os adendos espectral/metrológico, a lista posterior que não
reabre Q35 é:

1. calibrar o parâmetro dimensional $\Lambda_C$ da ação em uma unidade
   metrológica, se for desejado expressar a transição em GeV;
2. estender o raciocínio para setores não abelianos, onde a questão central
   passa a ser Slavnov--Taylor, confinamento e gap;
3. resolver independentemente a equação de gap Dirac--Bismut como teste da
   ponte constitutiva.

Por decisão explícita do usuário em 2026-07-12, o transporte até $1/128$ não
integra o programa atual e não é condição de fechamento adotada para Q35.

A auditoria item a item está em
q34/auditoria_enunciados_34_35_0.md.

---

## 16. Fechamento macro--local por torção e Reynolds geométrico

A conservação local $dB=0$, a carga quantizada $n_B$ e o equilíbrio radial
foram combinados com a definição constitutiva

\[
\operatorname{Re}_{\rm Q}
=
\frac{E_{\rm tor}}{E_{\rm el}}
=\alpha.
\]

O resultado é

\[
R^2=\frac{|n_B|}{\sqrt{12}\pi\sqrt\alpha},
\qquad
\tau_{\rm EM}^{\rm dimless}
=
\frac{R^6}{4R^4-n_B^2/\pi^2}>0
\]

para $\alpha<1/3$. A resolução relativa fica determinada e a conversão em
unidades físicas pertence à calibração metrológica da Q36. A derivação,
hipóteses e limites estão em q35/fechamento_torcao_reynolds.md.

Essa ponte fecha a origem estrutural de $\tau_{\rm EM}>0$ sem identificar
$\Lambda_{\rm EM}$ com a massa do fóton ou importar um corte artificial. A
igualdade $\operatorname{Re}_{\rm Q}=\alpha$ é um princípio constitutivo
macro--local explicitamente declarado; não é apresentada como consequência
já demonstrada da ação oficial.
