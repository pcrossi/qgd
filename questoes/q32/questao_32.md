# Questão 32 — De onde vem o propagador modificado?

## 1. Pergunta

O arquivo `32-0.md` pergunta:

\[
\boxed{
\text{de onde vem o propagador modificado com fator }e^{-p^2/\Lambda^2}?
}
\]

As perguntas obrigatórias são:

1. qual termo da ação gera \(e^{-p^2/\Lambda^2}\)?
2. o operador contém infinitas derivadas?
3. quais são seus polos?
4. há estados fantasma?
5. a continuação lorentziana é causal?

A resposta não aceitável é:

\[
\boxed{
\text{inserir manualmente o fator gaussiano em uma integral.}
}
\]

---

## 2. Status

A Questão 32 ainda não estava fechada no texto auditado.

O manuscrito possui a ideia física correta:

\[
\boxed{
\text{o ultravioleta é amortecido pelo fluxo de Ricci/Perelman, pela medida de
calor e pela pressão de Bohm.}
}
\]

Mas a auditoria tem razão em exigir mais:

\[
\boxed{
e^{-p^2/\Lambda^2}
\text{ deve sair de um operador ou de um semigrupo de calor derivado da ação,
não ser inserido como regulador externo.}
}
\]

Portanto, a rota correta é derivar o fator como núcleo de calor associado ao
operador quadrático da ação GDQ.

---

## 3. Qual termo da ação pode gerar o fator gaussiano?

A ação oficial contém, no integrando:

\[
\boxed{
\tau\left(
\mathcal R
+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
\mathcal U\sqrt{\det g}.
}
\]

Ao expandir em torno de um fundo estável:

\[
g=g_0+\delta g,
\qquad
f=f_0+\varphi,
\]

o setor quadrático das flutuações deve assumir a forma:

\[
\boxed{
\mathcal S^{(2)}
=
\frac12
\int
\Phi\,\mathcal O_{\rm GDQ}\,\Phi\,d\mu_{g_0}
}
\]

onde \(\Phi\) representa coletivamente as flutuações físicas:

\[
\Phi\in\{\varphi,\bar\varphi,h_{\mu\bar\nu},B,\ldots\}.
\]

O operador quadrático esperado é elíptico no setor euclidiano:

\[
\boxed{
\mathcal O_{\rm GDQ}
=
-\Delta_{B,g_0}
+
M_{\rm eff}^2
+
\mathcal R_{\rm eff}
+
\cdots.
}
\]

Aqui:

- \(\Delta_{B,g_0}\) é o Laplaciano efetivo com conexão de Bismut/Chern;
- \(M_{\rm eff}^2\) é a massa/rigidez efetiva do modo;
- \(\mathcal R_{\rm eff}\) contém termos de curvatura do fundo.

O fluxo em \(\tau\) associado a esse operador é:

\[
\boxed{
\partial_\tau\Phi
=
-
\mathcal O_{\rm GDQ}\Phi.
}
\]

Logo:

\[
\boxed{
\Phi(\tau)
=
e^{-\tau\mathcal O_{\rm GDQ}}\Phi(0).
}
\]

Em uma base espectral:

\[
\mathcal O_{\rm GDQ}\psi_n=\lambda_n\psi_n,
\]

temos:

\[
\boxed{
\Phi_n(\tau)
=
e^{-\tau\lambda_n}\Phi_n(0).
}
\]

No regime assintoticamente plano:

\[
\lambda_p\simeq p_E^2+m_{\rm eff}^2.
\]

Então:

\[
\boxed{
e^{-\tau\lambda_p}
\simeq
e^{-\tau(p_E^2+m_{\rm eff}^2)}.
}
\]

Identificando a escala:

\[
\boxed{
\tau=\Lambda^{-2},
}
\]

obtemos:

\[
\boxed{
e^{-\tau p_E^2}
=
e^{-p_E^2/\Lambda^2}.
}
\]

Portanto, o fator gaussiano deve ser entendido como:

\[
\boxed{
\text{núcleo de calor do operador quadrático GDQ.}
}
\]

Não como:

\[
\boxed{
\text{fator multiplicativo colocado manualmente no loop.}
}
\]

---

## 4. Propagador efetivo correto

Se o propagador local euclidiano sem amortecimento é:

\[
\boxed{
G_0(p_E)
=
\frac{1}{p_E^2+m^2},
}
\]

então o propagador efetivo em escala \(\tau=\Lambda^{-2}\) fica:

\[
\boxed{
G_\Lambda(p_E)
=
\frac{e^{-p_E^2/\Lambda^2}}{p_E^2+m^2}.
}
\]

Mais invariantemente:

\[
\boxed{
G_\tau
=
e^{-\tau\mathcal O_{\rm GDQ}}
\mathcal O_{\rm GDQ}^{-1}.
}
\]

Esta é a forma segura, pois deixa claro que:

1. o denominador vem do operador quadrático;
2. o numerador vem do fluxo de calor;
3. a escala de corte é \(\Lambda=\tau^{-1/2}\);
4. a construção depende do espectro de \(\mathcal O_{\rm GDQ}\).

---

## 5. O operador contém infinitas derivadas?

Há duas leituras distintas.

### 5.1 Ação fundamental

Na ação oficial, não é necessário introduzir infinitas derivadas.

A ação é local nos campos fundamentais:

\[
\boxed{
g_{\mu\bar\nu},\quad f,\quad \bar f.
}
\]

Ela contém termos de curvatura e gradientes:

\[
\boxed{
\mathcal R,
\qquad
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f.
}
\]

Portanto:

\[
\boxed{
\text{a GDQ fundamental não precisa ser escrita como teoria de infinitas
derivadas.}
}
\]

### 5.2 Ação efetiva em escala fixa

Se eliminarmos explicitamente o parâmetro de fluxo \(\tau\), podemos representar
o amortecimento por um operador não-local inteiro:

\[
\boxed{
\mathcal O_{\rm eff}
=
e^{\mathcal O_{\rm GDQ}/\Lambda^2}
\mathcal O_{\rm GDQ}.
}
\]

Nesse caso:

\[
e^{\mathcal O_{\rm GDQ}/\Lambda^2}
=
\sum_{n=0}^{\infty}
\frac{1}{n!}
\left(
\frac{\mathcal O_{\rm GDQ}}{\Lambda^2}
\right)^n.
\]

Logo, a descrição efetiva contém infinitas derivadas.

Mas isso deve ser interpretado como:

\[
\boxed{
\text{representação efetiva do semigrupo de calor, não nova ontologia
fundamental.}
}
\]

---

## 6. Quais são os polos?

Considere:

\[
\boxed{
G_\Lambda(p_E)
=
\frac{e^{-p_E^2/\Lambda^2}}{p_E^2+m^2}.
}
\]

O fator exponencial:

\[
\boxed{
e^{-p_E^2/\Lambda^2}
}
\]

é uma função inteira e nunca zera:

\[
\boxed{
e^{-z}\ne0
\quad
\forall z\in\mathbb C.
}
\]

Portanto, ele não adiciona polos.

Os polos são determinados apenas por:

\[
\boxed{
p_E^2+m^2=0.
}
\]

Após reconstrução lorentziana:

\[
\boxed{
p_h^2+m^2=0,
}
\]

onde \(p_h^2=h^{\mu\nu}p_\mu p_\nu\) é calculado com a métrica física
lorentziana constitutiva \(h\).

Assim:

\[
\boxed{
\text{o form factor gaussiano não cria novos polos.}
}
\]

Essa é a condição central para evitar fantasmas do tipo Ostrogradsky.

---

## 7. Há estados fantasma?

Se o propagador efetivo for exatamente:

\[
\boxed{
G_\Lambda(p)
=
\frac{F(p^2)}{p^2+m^2},
\qquad
F(z)=e^{-z/\Lambda^2},
}
\]

então \(F\) não cria polos adicionais.

Logo:

\[
\boxed{
\text{não há novos fantasmas apenas por causa do fator gaussiano.}
}
\]

Mas isso não encerra o problema inteiro.

Para garantir ausência de fantasmas no setor completo, ainda é necessário:

1. decompor as flutuações métricas em setores físicos e de calibre;
2. provar positividade do produto interno físico;
3. mostrar que modos longitudinais não propagam;
4. preservar identidades de Ward/Slavnov--Taylor no setor gauge efetivo;
5. garantir reflexão positiva no setor euclidiano;
6. reconstruir o Hilbert físico por Osterwalder--Schrader ou estrutura
   equivalente já usada nas Questões 7 e 20.

A prescrição de Sudarshan ajuda a selecionar polos físicos e cancelar modos
espúrios avançado-retardados, mas não deve ser usada sozinha como substituto de
positividade e reconstrução Hilbertiana.

---

## 8. A continuação lorentziana é causal?

A continuação lorentziana não deve ser feita ingenuamente por:

\[
p_E^2\mapsto -p_h^2
\]

mantendo o mesmo fator como:

\[
e^{+p_h^2/\Lambda^2}.
\]

Essa forma pode crescer exponencialmente em direções temporais e gerar
problemas de causalidade, crescimento assintótico e definição de contorno.

A rota correta da GDQ é:

\[
\boxed{
\text{definir o amortecimento no setor euclidiano/fluxo}
\quad
\Longrightarrow
\quad
\text{reconstruir a teoria lorentziana física.}
}
\]

Isto exige:

1. Schwinger functions bem definidas;
2. reflexão positiva;
3. espectro positivo;
4. prescrição de polos compatível com Sudarshan;
5. propagador retardado com suporte no cone causal de \(h\).

Na camada física:

\[
\boxed{
h_{\mu\nu}
=
q_{\mu\nu}
-
2\frac{u_\mu u_\nu}{q^{-1}(u,u)}.
}
\]

A causalidade operacional deve ser:

\[
\boxed{
\operatorname{supp}G_{\rm ret}
\subseteq
J_h^+.
}
\]

Portanto:

\[
\boxed{
\text{a causalidade é plausível se o propagador for reconstruído via fluxo
euclidiano + OS/Sudarshan;}
}
\]

mas:

\[
\boxed{
\text{não está garantida por simplesmente escrever }
e^{-p^2/\Lambda^2}
\text{ em Minkowski.}
}
\]

---

## 9. Relação com o texto original

O texto original fornece ingredientes aproveitáveis:

1. a diferença entre Feynman e Wiener;
2. a medida de calor/difusão;
3. o papel do fluxo de Ricci--Perelman;
4. a pressão de Bohm como barreira UV;
5. a prescrição causal de Sudarshan;
6. o amortecimento por núcleo de calor;
7. a ideia de que \(\tau\) atua como escala de fluxo, com:

   \[
   \tau\sim \Lambda^{-2}.
   \]

Mas a formulação auditável deve corrigir o ponto fraco:

\[
\boxed{
\text{o gaussiano precisa ser derivado do operador quadrático }
\mathcal O_{\rm GDQ}
\text{ e de seu semigrupo }e^{-\tau\mathcal O_{\rm GDQ}}.
}
\]

Não basta escrever:

\[
\boxed{
d^4p\to d^4p\,e^{-p^2/\Lambda^2}.
}
\]

---

## 10. Respostas diretas às perguntas obrigatórias

### 1. Qual termo da ação gera \(e^{-p^2/\Lambda^2}\)?

O fator deve vir do operador quadrático obtido da expansão da ação oficial:

\[
\boxed{
\tau\left(
\mathcal R
+
g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\bar f
\right)
}
\]

em torno de um fundo estável.

Esse operador gera o semigrupo:

\[
\boxed{
e^{-\tau\mathcal O_{\rm GDQ}}.
}
\]

No limite plano:

\[
\boxed{
e^{-\tau p_E^2}
=
e^{-p_E^2/\Lambda^2}.
}
\]

### 2. O operador contém infinitas derivadas?

Fundamentalmente:

\[
\boxed{
\text{não.}
}
\]

Efetivamente, se o fluxo for reescrito como operador não-local:

\[
\boxed{
\text{sim, como função inteira }e^{\mathcal O/\Lambda^2}.
}
\]

### 3. Quais são seus polos?

Se:

\[
\boxed{
G_\Lambda(p_E)
=
\frac{e^{-p_E^2/\Lambda^2}}{p_E^2+m^2},
}
\]

então os polos são apenas:

\[
\boxed{
p_E^2+m^2=0.
}
\]

O exponencial não adiciona polos.

### 4. Há estados fantasma?

O fator inteiro não cria fantasmas por si só:

\[
\boxed{
e^{-p^2/\Lambda^2}
\text{ não adiciona polos.}
}
\]

Mas a ausência completa de fantasmas exige reconstrução do espaço físico,
fixação de calibre/constraints e positividade.

### 5. A continuação lorentziana é causal?

Somente se feita por reconstrução correta:

\[
\boxed{
\text{Euclidiano/fluxo}
\longrightarrow
\text{OS}
\longrightarrow
\text{propagador retardado em }(N,h).
}
\]

Não é seguro fazer a substituição ingênua:

\[
\boxed{
e^{-p_E^2/\Lambda^2}
\to
e^{+p_h^2/\Lambda^2}.
}
\]

---

## 11. Análise do arquivo `32-1.md`

O arquivo `32-1.md` avança na direção correta, porque tenta calcular
explicitamente o operador quadrático:

\[
\mathcal O_{\rm GDQ}^{(2)}.
\]

Ele acerta quatro pontos importantes:

1. usa o espaço ponderado:

   \[
   L^2(M,e^{-f_0}dV);
   \]

2. identifica o Laplaciano com drift:

   \[
   \Delta_{f_0}=\Delta-\nabla f_0\cdot\nabla;
   \]

3. reconhece que o setor métrico deve envolver um operador tipo
   Lichnerowicz com drift;
4. mostra que, no limite plano, o núcleo de calor produz:

   \[
   e^{-\tau p_E^2}.
   \]

Portanto:

\[
\boxed{
\text{`32-1.md` fortalece a resposta da Questão 32.}
}
\]

Mas ele ainda precisa de correções antes de ser tratado como prova final.

### 11.1 Problema principal: dupla contagem de \(\tau\)

Em `32-1.md`, os operadores são escritos com um fator explícito de \(\tau\):

\[
\mathcal O_{\varphi}^{(2)}\sim 2\tau(-\Delta_{f_0}+\cdots),
\qquad
\mathcal O_h^{(2)}\sim \tau(-\Delta_{f_0}+\cdots).
\]

Depois o texto usa o semigrupo:

\[
e^{-\tau\mathcal O^{(2)}}.
\]

Se \(\mathcal O^{(2)}\) já contém \(\tau\), então no limite plano teríamos:

\[
e^{-\tau(\tau p_E^2)}
=
e^{-\tau^2p_E^2},
\]

não:

\[
e^{-\tau p_E^2}.
\]

Logo, a forma correta é separar:

\[
\boxed{
\text{Hessiana da ação}
=
\tau\,L,
}
\]

do gerador do calor:

\[
\boxed{
L
=
\frac{1}{\tau}\mathcal O_{\rm Hess}^{(2)}.
}
\]

Então:

\[
\boxed{
e^{-\tau L}
\longrightarrow
e^{-\tau p_E^2}.
}
\]

Assim, o operador que gera o núcleo de calor não deve ser a Hessiana completa
com o prefator \(\tau\), mas a Hessiana normalizada por \(\tau\), ou operador
cinético reduzido:

\[
\boxed{
L_{\rm GDQ}^{(2)}
:=
\tau^{-1}\mathcal O_{\rm Hess}^{(2)}.
}
\]

Essa correção é essencial.

### 11.2 Setor escalar: coeficiente do potencial efetivo

O cálculo de `32-1.md` para o setor escalar é útil, mas o potencial efetivo
escrito ali parece supercontado.

Partindo da simplificação:

\[
S[f]
=
\tau\int
(R_0+|\nabla f|^2)e^{-f}dV,
\qquad
f=f_0+\varphi,
\]

o termo quadrático é:

\[
\tau\int e^{-f_0}
\left[
|\nabla\varphi|^2
-2\varphi\nabla f_0\cdot\nabla\varphi
+\frac12(R_0+|\nabla f_0|^2)\varphi^2
\right]dV.
\]

Após integração por partes:

\[
\int e^{-f_0}|\nabla\varphi|^2dV
=
\int e^{-f_0}\varphi(-\Delta_{f_0}\varphi)dV,
\]

e:

\[
\int -2e^{-f_0}\varphi\nabla f_0\cdot\nabla\varphi\,dV
=
\int e^{-f_0}
(\Delta f_0-|\nabla f_0|^2)\varphi^2dV.
\]

Logo, na convenção:

\[
S_\varphi^{(2)}
=
\frac12
\int e^{-f_0}
\varphi\,\mathcal O_{\rm Hess,\varphi}^{(2)}\varphi\,dV,
\]

o operador é:

\[
\boxed{
\mathcal O_{\rm Hess,\varphi}^{(2)}
=
2\tau
\left[
-\Delta_{f_0}
+
\Delta f_0
+
\frac12R_0
-
\frac12|\nabla f_0|^2
\right].
}
\]

Assim, o gerador normalizado do calor é:

\[
\boxed{
L_\varphi
=
2
\left[
-\Delta_{f_0}
+
\Delta f_0
+
\frac12R_0
-
\frac12|\nabla f_0|^2
\right].
}
\]

O texto `32-1.md` escreve:

\[
2\tau
\left[
-\Delta_{f_0}
+R_0+2\Delta f_0-|\nabla f_0|^2
\right],
\]

que equivale a dobrar a parte potencial nessa expansão simplificada.

Além disso, na ação oficial da GDQ há termos extras:

\[
\frac{f+\bar f}{2}-n,
\qquad
\mathcal U=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n},
\]

que também contribuem para a Hessiana escalar. Portanto, a fórmula acima é
apenas a versão reduzida do setor \((R+|\nabla f|^2)e^{-f}\), não a Hessiana
oficial completa.

### 11.3 Setor métrico: correto como esquema, incompleto como Hessiana total

O operador de Lichnerowicz com drift:

\[
\left(L_hh\right)_{ij}
=
-\Delta_{f_0}h_{ij}
-2R_{ikjl}h^{kl}
+R_{ik}h^k{}_j
+R_{jk}h^k{}_i
\]

é a estrutura esperada para flutuações métricas em gauge apropriado.

Mas, para a GDQ oficial, ainda falta:

1. trabalhar no setor Hermitiano \(h_{\mu\bar\nu}\), não apenas em tensores
   reais \(h_{ij}\);
2. incluir a variação da medida \(\mathcal U\sqrt{\det g}\);
3. separar traço, difeomorfismos e modos físicos;
4. especificar o gauge de DeTurck usado;
5. tratar o acoplamento entre flutuações de \(g\) e de \(f,\bar f\).

Logo:

\[
\boxed{
\text{o Lichnerowicz com drift é o símbolo principal correto, mas não é ainda
a Hessiana GDQ completa.}
}
\]

### 11.4 Setor vetorial: depende da Questão 28

O setor vetorial de `32-1.md` introduz:

\[
S_a^{(2)}
=
\frac{\tau}{2g_{\rm eff}^2}
\int
\operatorname{Tr}(F_a\wedge *F_a)
+\text{gauge fixing}.
\]

Esse é o setor Yang--Mills efetivo.

Mas, pelas Questões 28 e 30, ainda não se deve tratá-lo como derivado
diretamente da ação oficial. Ele é admissível como setor efetivo condicional.

O operador correto sobre 1-formas deve ter a forma esquemática:

\[
\boxed{
L_a
=
d_{A,f_0}^{\dagger}d_A
+d_A d_{A,f_0}^{\dagger}
+\operatorname{ad}(F_{\bar A})
+\operatorname{Ric}_{f_0}
}
\]

ou, no caso abeliano/plano:

\[
\boxed{
L_a\to-\Delta_{f_0}+\operatorname{Ric}.
}
\]

Portanto, `32-1.md` acerta o símbolo principal, mas falta justificar:

1. a origem de \(A_\mu\);
2. a origem de \(g_{\rm eff}\);
3. o fibrado principal;
4. o gauge fixing;
5. as identidades de Ward/Slavnov--Taylor.

### 11.5 Correção recomendada para `32-1.md`

Para tornar `32-1.md` compatível com a Questão 32, a conclusão deve trocar:

\[
\Phi(p_E,\tau)
=
e^{-\tau\mathcal O^{(2)}}\Phi(p_E,0)
\]

por:

\[
\boxed{
\Phi(p_E,\tau)
=
e^{-\tau L^{(2)}}\Phi(p_E,0),
\qquad
L^{(2)}
=
\tau^{-1}\mathcal O_{\rm Hess}^{(2)}.
}
\]

Então, no limite plano:

\[
\boxed{
L^{(2)}\to p_E^2+m_{\rm eff}^2,
}
\]

e:

\[
\boxed{
e^{-\tau L^{(2)}}
\to
e^{-\tau(p_E^2+m_{\rm eff}^2)}.
}
\]

Com:

\[
\boxed{
\tau=\Lambda^{-2},
}
\]

obtém-se:

\[
\boxed{
G_\Lambda(p_E)
=
\frac{e^{-p_E^2/\Lambda^2}}{p_E^2+m^2}.
}
\]

---

## 12. Status após `32-1.md`

`32-1.md` resolve a principal lacuna conceitual da Questão 32:

\[
\boxed{
\text{o gaussiano pode vir do núcleo de calor do operador quadrático.}
}
\]

Após a correção de `32-1.md`, os dois problemas técnicos imediatos foram
resolvidos:

1. a dupla contagem de \(\tau\) foi removida pela distinção:

   \[
   \mathcal O_{\rm Hess}^{(2)}=\tau L^{(2)};
   \]

2. o potencial efetivo escalar reduzido foi corrigido para:

   \[
   V_{\rm eff}
   =
   \Delta f_0+\frac12R_0-\frac12|\nabla f_0|^2.
   \]

Após o cálculo adicional da Hessiana escalar oficial em `32-1.md`, também ficou
incluída a contribuição de:

1. \(\mathcal U=e^{-(f+\bar f)/2}/(4\pi z_\tau)^n\);
2. \((f+\bar f)/2-n\);
3. a mistura entre \(\varphi\) e \(\bar\varphi\) no bloco escalar.

A parte quadrática escalar oficial ficou:

\[
\boxed{
\mathcal S_{\rm esc}^{(2)}
=
\int_\gamma\frac{d\tau}{\tau}
\int d\mu_{\sigma_0}
\left[
\tau K_2
-
\tau sK_1
+
\left(
\frac{B_0}{2}-1
\right)s^2
\right],
}
\]

com:

\[
\sigma_0=\frac{f_0+\bar f_0}{2},
\qquad
s=\frac{\varphi+\bar\varphi}{2}.
\]

Além disso, `32-1.md` passou a registrar a Hessiana oficial em blocos:

\[
\boxed{
\mathcal S_{\rm GDQ}^{(2)}
=
\int_\gamma\frac{d\tau}{\tau}
\int d\mu_{\sigma_0,g_0}
\left[
Q_{ss}+Q_{gs}+Q_{gg}
\right].
}
\]

Assim, o cálculo da Hessiana oficial já está disponível em forma variacional
por blocos. Ainda não há derivação final em forma espectral/gauge-fixada porque
faltam:

1. reduzir \(Q_{gg}\) a um operador Hermitiano de Lichnerowicz--drift
   totalmente gauge-fixado;
2. reduzir \(Q_{gs}\) aos operadores mistos explícitos;
3. separar modos físicos, traço, difeomorfismos e gauge;
4. tratar o caráter efetivo condicional do setor vetorial;
5. provar reflexão positiva e reconstrução lorentziana causal.

Assim, o status correto passa a ser:

\[
\boxed{
\text{Questão 32 fechada estruturalmente: `32-1.md` corrigido fornece o
gerador de calor e a Hessiana oficial em blocos; falta a redução
gauge-fixada/espectral.}
}
\]

---

## 13. Fechamento

A Questão 32 fica respondida estruturalmente assim:

\[
\boxed{
\text{o propagador modificado deve ser o propagador do operador quadrático GDQ
vestido pelo semigrupo de calor do fluxo de Perelman.}
}
\]

A forma correta é:

\[
\boxed{
G_\tau
=
e^{-\tau L_{\rm GDQ}^{(2)}}
\left(L_{\rm GDQ}^{(2)}\right)^{-1}.
}
\]

No regime plano:

\[
\boxed{
G_\Lambda(p_E)
=
\frac{e^{-p_E^2/\Lambda^2}}{p_E^2+m^2}.
}
\]

Com isso:

1. o fator gaussiano não é inserido manualmente;
2. ele vem do fluxo de calor;
3. não cria polos novos;
4. não cria fantasmas por si só;
5. a causalidade lorentziana depende de reconstrução OS/Sudarshan e do cone
   físico \(h\).

Portanto:

\[
\boxed{
\text{Questão 32 fechada em nível estrutural; `32-1.md` corrigido fornece a
rota para }L_{\rm GDQ}^{(2)}\text{ e calcula a Hessiana oficial em blocos,
restando a redução gauge-fixada e a análise espectral.}
}
\]

---

## 14. Consolidação após redução gauge-fixada

O adendo técnico:

\[
\boxed{\texttt{questoes/q32/associados/reducao\_hessiana\_gauge\_fixada.md}}
\]

fixa a forma final da resposta estrutural.

O ponto central é a separação:

\[
\boxed{
\mathcal O_{\rm Hess}^{(2)}=\tau L_{\rm GDQ}^{(2)}.
}
\]

Logo, o gerador do heat-kernel é:

\[
\boxed{
L_{\rm GDQ}^{(2)}=\tau^{-1}\mathcal O_{\rm Hess}^{(2)},
}
\]

e não a Hessiana com o fator \(\tau\) contado novamente.

Com isso:

\[
\boxed{
G_\tau=e^{-\tau L_{\rm GDQ}^{(2)}}(L_{\rm GDQ}^{(2)})^{-1}.
}
\]

No limite plano:

\[
\boxed{
G_\Lambda(p_E)=\frac{e^{-p_E^2/\Lambda^2}}{p_E^2+m^2}.
}
\]

O adendo também especifica:

1. o bloco escalar reduzido;
2. o símbolo principal Lichnerowicz--drift no setor Hermitiano;
3. o gauge Hermitiano-DeTurck;
4. a estrutura matricial dos blocos mistos;
5. a condição correta de causalidade via OS/Sudarshan;
6. a razão pela qual o fator inteiro não introduz polos nem fantasmas novos.

Portanto, o status consolidado é:

\[
\boxed{
\text{Questão 32 fechada estruturalmente.}
}
\]

Permanecem como cálculo posterior:

1. coeficientes completos dos blocos mistos em fundo geral;
2. prova completa de reflexão positiva para todos os setores;
3. reconstrução explícita de \(G_{\rm ret}\) em fundo não plano;
4. verificação das identidades de Ward/Slavnov--Taylor no setor gauge efetivo.
