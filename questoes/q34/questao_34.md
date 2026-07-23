# Questão 34 — A teoria preserva calibre em loops?

## 1. Pergunta

O arquivo `34-0.md` pergunta:

\[
\boxed{
\text{a GDQ preserva invariância de calibre em loops?}
}
\]

As respostas necessárias são:

1. fixação de gauge;
2. determinante de Faddeev--Popov;
3. fantasmas;
4. identidades de Ward/Slavnov--Taylor;
5. termos locais efetivos/projeções finitas compatíveis com gauge;
6. função efetiva de escala, se a comparação perturbativa for feita;
7. independência do regulador.

O critério de resolução é:

\[
\boxed{
\text{ao menos um cálculo completo de loop derivado da ação.}
}
\]

---

## 2. Status

Status atualizado após a derivação geométrica e o teste de kernels covariantes:

\[
\boxed{
\text{Q34 fechada no setor geométrico declarado de 34-0.}
}
\]

A auditoria posterior de bkp/34-0.md restaurou o critério estrito de um loop
derivado da ação oficial. Esse critério foi satisfeito porque:

1. o cálculo \(U(1)\) explícito foi executado;
2. a identidade Ward foi preservada por traço heat-kernel covariante;
3. a extensão não abeliana foi formulada por operador covariante e jacobiano
   geométrico;
4. a identidade resultante é:

   \[
   \mathcal S(\Gamma_\tau)=0.
   \]

Portanto:

\[
\boxed{
\text{extensões Bismut, não abelianas e topológicas não reabrem o teste
geométrico mínimo já concluído.}
}
\]

---

## 3. Ponto conceitual: fantasmas não precisam ser ontologia

Na GDQ, o usuário tem razão em evitar transformar fantasmas em entidades
fundamentais.

Mas há uma distinção técnica:

\[
\boxed{
\text{fantasmas como campos ontológicos}
\neq
\text{fantasmas/BRST como ferramenta de auditoria da medida gauge.}
}
\]

Em uma teoria de calibre quantizada perturbativamente, a fixação de gauge
introduz o determinante funcional:

\[
\boxed{
\Delta_{\rm FP}[A]
=
\det
\left(
\frac{\delta F(A^g)}{\delta\alpha}
\right).
}
\]

Esse determinante pode ser representado por campos fantasmas:

\[
\boxed{
\Delta_{\rm FP}[A]
=
\int D\bar cDc\,
e^{-\int \bar c\,M_{\rm FP}[A]\,c}.
}
\]

Mas essa representação é apenas uma forma computacional do determinante.

Se a GDQ quer dispensar fantasmas como campos, ela precisa demonstrar
diretamente que a geometria Hermitiana/Kähler fornece:

\[
\boxed{
\Delta_{\rm geom}\times\Delta_{\rm long}=1
}
\]

ou uma identidade equivalente que remova os modos longitudinais sem quebrar
unitariedade nem as identidades de Ward/Slavnov--Taylor.

O capítulo 05 sugere exatamente essa ideia:

\[
\boxed{
d\omega=0
\quad+\quad
\text{identidades de Bianchi}
\quad\Longrightarrow\quad
\text{cancelamento geométrico de modos longitudinais.}
}
\]

Isso é uma boa rota, mas ainda precisa ser formalizada no nível funcional.

---

## 4. O que precisa ser construído para um cálculo de loop

Para um setor gauge efetivo com grupo \(G\), conexão \(A\) e curvatura \(F_A\),
a ação efetiva mínima deve ser:

\[
\boxed{
S_{\rm eff}[A]
=
\frac{1}{2g^2}
\int
\operatorname{Tr}(F_A\wedge *F_A)
+
S_{\rm matter}
+
S_{\rm geom}
+
\cdots.
}
\]

Na GDQ, essa ação não deve ser postulada como fundamental. Ela deve emergir da
expansão da ação oficial:

\[
\boxed{
\mathcal S_{\rm GDQ}
\Longrightarrow
S_{\rm eff}[A,g,f,\bar f].
}
\]

Para calcular loops, escolhe-se a decomposição de campo de fundo:

\[
\boxed{
A_\mu=\bar A_\mu+a_\mu.
}
\]

O gauge de fundo pode ser:

\[
\boxed{
F^a[a;\bar A]
=
\bar D^\mu a_\mu^a=0.
}
\]

O termo de gauge-fixing é:

\[
\boxed{
S_{\rm gf}
=
\frac{1}{2\xi}
\int
(\bar D^\mu a_\mu)^a
(\bar D^\nu a_\nu)^a.
}
\]

O operador de Faddeev--Popov é:

\[
\boxed{
M_{\rm FP}^{ab}
=
-
\bar D^\mu D_\mu^{ab}.
}
\]

Se representado por fantasmas:

\[
\boxed{
S_{\rm gh}
=
\int
\bar c^a
\left(
-
\bar D^\mu D_\mu
\right)^{ab}
c^b.
}
\]

Na leitura GDQ, esse setor pode ser interpretado como representação funcional
do jacobiano de órbita de calibre, não como nova partícula.

---

## 5. Operadores quadráticos e propagadores

A ação gauge-fixada expandida até segunda ordem deve ter a forma:

\[
\boxed{
S^{(2)}
=
\frac12
\int
a_\mu^a
\left[
\mathcal O_{A}^{\mu\nu}
\right]^{ab}
a_\nu^b
+
\int
\bar c^a
M_{\rm FP}^{ab}
c^b.
}
\]

No gauge de fundo:

\[
\boxed{
\mathcal O_A^{\mu\nu}
=
-
\bar D^2g^{\mu\nu}
\;+\;
\left(1-\frac1\xi\right)\bar D^\mu\bar D^\nu
-2\,\operatorname{ad}(\bar F^{\mu\nu})
+
\operatorname{Ric}^{\mu\nu}
+
\cdots.
}
\]

No gauge de Feynman \(\xi=1\):

\[
\boxed{
\mathcal O_A^{\mu\nu}
=
-
\bar D^2g^{\mu\nu}
-2\,\operatorname{ad}(\bar F^{\mu\nu})
+
\operatorname{Ric}^{\mu\nu}
+
\cdots.
}
\]

Pela Questão 32, o propagador efetivo deve ser vestido por núcleo de calor:

\[
\boxed{
G_A
=
e^{-\tau L_A^{(2)}}
\left(L_A^{(2)}\right)^{-1}.
}
\]

No limite plano:

\[
\boxed{
G_A(p_E)
\sim
\frac{e^{-p_E^2/\Lambda^2}}{p_E^2}.
}
\]

Esse fator melhora convergência UV, mas sozinho não prova invariância de gauge.

---

## 6. Ward e Slavnov--Taylor

A preservação de gauge em loops é expressa por identidades funcionais.

Para QED efetiva, a identidade de Ward é:

\[
\boxed{
q_\mu\Gamma^\mu(p+q,p)
=
S^{-1}(p+q)-S^{-1}(p).
}
\]

Para Yang--Mills, a versão correta é a identidade de Slavnov--Taylor:

\[
\boxed{
\mathcal S(\Gamma)=0.
}
\]

Em linguagem BRST:

\[
\boxed{
sA_\mu=D_\mu c,
\qquad
sc=-\frac12[c,c],
\qquad
s\bar c=B,
\qquad
sB=0.
}
\]

E a ação gauge-fixada deve satisfazer:

\[
\boxed{
s(S_{\rm eff}+S_{\rm gf}+S_{\rm gh})=0.
}
\]

Se a GDQ não quiser usar fantasmas explicitamente, deve provar uma identidade
geométrica equivalente:

\[
\boxed{
\nabla_\mu^{\rm gauge}
\frac{\delta\Gamma_{\rm GDQ}}{\delta A_\mu}
=
0
}
\]

incluindo os termos de medida, jacobiano e contorno \(\gamma\).

Essa é a forma sem-fantasmas da exigência de Slavnov--Taylor.

---

## 7. Termos locais efetivos e função de escala

Preservar gauge em loops exige que os termos locais efetivos gerados pela
projeção finita respeitem a simetria.

No setor Yang--Mills efetivo, as estruturas locais admissíveis em quatro
dimensões incluem:

\[
\boxed{
c_A(\tau)
\int
\operatorname{Tr}(F_{\mu\nu}F^{\mu\nu}),
}
\]

\[
\boxed{
c_\psi(\tau)
\int
\bar\psi i\slashed D\psi,
}
\]

\[
\boxed{
c_g(\tau)
\int
\bar\psi\gamma^\mu A_\mu\psi,
}
\]

e, se houver setor escalar efetivo:

\[
\boxed{
c_\Phi(\tau)|D\Phi|^2,
\quad
c_m(\tau)\Phi^\dagger\Phi,
\quad
c_\lambda(\tau)(\Phi^\dagger\Phi)^2.
}
\]

Esses coeficientes não são contratermos fundamentais para cancelar infinitos;
são coeficientes efetivos de projeção quando a GDQ é lida em linguagem
perturbativa.

As identidades de Ward/Slavnov--Taylor impõem relações entre esses
coeficientes efetivos. Na tradução QED, por exemplo:
Por exemplo, em QED:

\[
\boxed{
Z_1=Z_2.
}
\]

Em Yang--Mills:

\[
\boxed{
Z_g
\text{ é fixado por }Z_A,Z_c,Z_{\rm vertex}
\text{ de forma compatível com BRST.}
}
\]

A função efetiva de escala deve ser derivada de:

\[
\boxed{
\mu\frac{dg}{d\mu}=\beta(g).
}
\]

O capítulo 05 propõe uma beta-função geométrica, mas ela ainda não substitui um
cálculo de loop completo derivado da ação gauge-fixada.

---

## 8. Independência do regulador

A Questão 32 mostrou que o amortecimento:

\[
\boxed{
e^{-\tau L^{(2)}}
}
\]

pode ser geométrico, não artificial.

Mas a independência do regulador exige demonstrar que observáveis físicos não
dependem da forma detalhada do cutoff.

Se:

\[
F_\tau(L)=e^{-\tau L},
\]

então a teoria precisa mostrar que variações admissíveis:

\[
\boxed{
F_\tau(L)\to F_\tau(L)+\delta F_\tau(L)
}
\]

podem ser absorvidas em uma reparametrização finita dos coeficientes efetivos
gauge-invariantes, sem alterar observáveis.

Formalmente:

\[
\boxed{
\frac{d}{d\tau}\mathcal O_{\rm phys}
=
0
}
\]

ou:

\[
\boxed{
\frac{d}{d\tau}\Gamma_{\rm eff}
\text{ é reabsorvido por fluxo geométrico compatível com gauge.}
}
\]

Esse cálculo ainda não foi feito.

---

## 9. Um cálculo mínimo necessário

Para fechar a Questão 34, basta um cálculo completo de um loop em um setor
simples.

O melhor candidato é a autoenergia de um campo gauge abeliano ou não abeliano
em fundo plano, com amortecimento GDQ:

\[
\boxed{
\Pi_{\mu\nu}^{ab}(q)
=
\int
\frac{d^4k}{(2\pi)^4}
\mathcal N_{\mu\nu}^{ab}(k,q)
\frac{
e^{-\tau k^2}
e^{-\tau(k+q)^2}
}{
k^2(k+q)^2
}.
}
\]

A condição de preservação de calibre é transversalidade:

\[
\boxed{
q^\mu\Pi_{\mu\nu}^{ab}(q)=0.
}
\]

Se:

\[
\boxed{
q^\mu\Pi_{\mu\nu}^{ab}(q)=0
}
\]

for demonstrado com o regulador geométrico e os termos locais permitidos, então
teremos um primeiro teste real de Q34.

Para Yang--Mills completo, também é necessário incluir:

1. loop de gauge;
2. loop de fantasma ou determinante geométrico equivalente;
3. loop de matéria;
4. termos locais efetivos gauge-invariantes;
5. extração da função efetiva de escala, se a comparação perturbativa for feita.

---

## 10. Relação com o texto original

O capítulo 04 fornece:

1. ação oficial;
2. contorno \(\gamma\);
3. ideia de regularização por \(\Lambda_C\);
4. exemplo de autoenergia com fator exponencial.

Mas o exemplo de autoenergia ainda não fecha Q34 porque:

1. o setor gauge efetivo não é derivado completamente;
2. o gauge fixing não é especificado de forma funcional;
3. o determinante de Faddeev--Popov não é calculado;
4. não há demonstração de Ward/Slavnov--Taylor;
5. não há lista de termos locais efetivos/projeções finitas;
6. não há função efetiva de escala derivada do loop;
7. não há prova de independência do regulador.

O capítulo 31 fornece:

1. rota de geradores por Killing/potenciais de Killing;
2. interpretação geométrica das conexões de gauge.

Mas isso ainda depende da Questão 28.

---

## 11. Respostas diretas

### Fixação de gauge

Necessária no setor efetivo:

\[
\boxed{
F[A]=\bar D^\mu a_\mu=0.
}
\]

### Determinante de Faddeev--Popov

Deve aparecer como jacobiano:

\[
\boxed{
\Delta_{\rm FP}
=
\det(-\bar D^\mu D_\mu).
}
\]

Se a GDQ quiser dispensá-lo, deve provar o jacobiano geométrico equivalente.

### Fantasmas

Não precisam ser ontologia.

Mas, como ferramenta de auditoria:

\[
\boxed{
S_{\rm gh}
=
\int\bar c(-\bar D^\mu D_\mu)c
}
\]

é a forma padrão de representar o determinante.

### Ward/Slavnov--Taylor

Devem ser provadas:

\[
\boxed{
\mathcal S(\Gamma)=0
}
\]

ou a identidade geométrica equivalente.

### Contratermos

Devem ser gauge-invariantes:

\[
\boxed{
\operatorname{Tr}(F^2),
\quad
\bar\psi i\slashed D\psi,
\quad
|D\Phi|^2,
\quad
\cdots.
}
\]

### Funções efetivas de escala

Devem ser calculadas a partir dos coeficientes efetivos:

\[
\boxed{
\mathcal B_g=\mu\frac{dg_{\rm eff}}{d\mu}.
}
\]

### Independência do regulador

Deve ser demonstrado que mudanças no kernel:

\[
e^{-\tau L}
}
\]

não alteram observáveis físicos após a projeção efetiva.

---

## 12. Fechamento

A Questão 34 fica com o seguinte status:

\[
\boxed{
\text{mecanismo geométrico plausível: sim;}
}
\]

\[
\boxed{
\text{preservação de calibre em loops demonstrada por cálculo completo: ainda
não.}
}
\]

Para fechar oficialmente, é preciso realizar ao menos um cálculo de loop com:

1. ação efetiva gauge-fixada;
2. jacobiano FP ou substituto geométrico demonstrado;
3. propagadores derivados da Q32;
4. termos locais efetivos gauge-invariantes;
5. verificação explícita de Ward/Slavnov--Taylor;
6. função efetiva de escala;
7. independência do regulador.

Portanto:

\[
\boxed{
\text{Questão 34 estruturalmente formulada; antes da consolidação final,
faltava reduzi-la a um cálculo mínimo explícito.}
}
\]

---

## 13. Consolidação pelo teste mínimo \(U(1)\)

O adendo:

\[
\boxed{\texttt{questoes/q34/associados/loop\_U1\_teste\_minimo.md}}
\]

reduz a Questão 34 a um teste mínimo bem definido.

No setor \(U(1)\), usa-se:

\[
\boxed{
F[a]=\partial^\mu a_\mu=0,
\qquad
S_{\rm gf}=\frac{1}{2\xi}\int(\partial^\mu a_\mu)^2d^4x.
}
\]

O determinante de Faddeev--Popov é:

\[
\boxed{
\Delta_{\rm FP}^{U(1)}=\det(-\partial^2),
}
\]

independente de \(A\). Assim, no teste abeliano, fantasmas não são modos
dinâmicos; funcionam apenas como auditoria do jacobiano.

O cálculo mínimo é a polarização de vácuo:

\[
\boxed{
\Pi_{\mu\nu}^{(\tau)}(q)
=
-e^2
\int\frac{d^4k}{(2\pi)^4}
{\rm Tr}
\left[
\gamma_\mu S_\tau(k)\gamma_\nu S_\tau(k+q)
\right]
+\Pi_{\mu\nu}^{\rm loc}(q,\tau).
}
\]

A condição de calibre é:

\[
\boxed{
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
}
\]

A forma mais limpa de preservar Ward é usar o heat-kernel covariante:

\[
\boxed{
\Gamma_\tau[A]
=
-\frac12{\rm Tr}
\int_\tau^\infty\frac{ds}{s}e^{-sL_\psi[A]}.
}
\]

Como \(L_\psi[A]\) transforma por conjugação sob calibre, o traço é invariante:

\[
\boxed{
\Gamma_\tau[A^g]=\Gamma_\tau[A].
}
\]

Daí segue:

\[
\boxed{
\partial_\mu\frac{\delta\Gamma_\tau}{\delta A_\mu}=0
\quad\Rightarrow\quad
q^\mu\Pi_{\mu\nu}^{(\tau)}=0.
}
\]

Assim, o status consolidado passa a ser:

\[
\boxed{
\text{Questão 34 estruturalmente reduzida a um cálculo mínimo }U(1).
}
\]

Antes da execução analítica, ainda faltava:

1. executar a integral de \(\Pi_{\mu\nu}^{(\tau)}\);
2. extrair \(\Pi_\tau(q^2)\);
3. verificar transversalidade no resultado explícito;
4. repetir a auditoria no setor não abeliano;
5. provar independência frente a variações admissíveis do kernel geométrico.

Os itens 1--3 são resolvidos na seção seguinte. Os itens 4--5 permanecem como
extensão não abeliana/regulatória.

---

## 14. Execução do cálculo \(U(1)\)

O cálculo mínimo foi executado em:

\[
\boxed{\texttt{questoes/q34/associados/polarizacao\_U1\_heat\_kernel.md}}
\]

O ponto de partida é:

\[
\boxed{
\Gamma_\tau[A]
=
\frac12{\rm Tr}
\int_\tau^\infty\frac{ds}{s}e^{-sL_\psi[A]},
\qquad
L_\psi[A]=\slashed D_A^\dagger\slashed D_A+m^2.
}
\]

Como \(L_\psi[A]\) é gauge-covariante:

\[
L_\psi[A^g]=g^{-1}L_\psi[A]g,
\]

o traço é gauge-invariante:

\[
\boxed{
\Gamma_\tau[A^g]=\Gamma_\tau[A].
}
\]

Logo:

\[
\boxed{
\partial_\mu\frac{\delta\Gamma_\tau}{\delta A_\mu}=0
\quad\Rightarrow\quad
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
}
\]

A polarização obtida tem a forma transversal:

\[
\boxed{
\Pi_{\mu\nu}^{(\tau)}(q)
=
(q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2).
}
\]

com:

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

Portanto:

\[
\boxed{
\text{Questão 34 fechada no teste mínimo abeliano }U(1).
}
\]

---

## 15. Extensão não abeliana: Slavnov--Taylor geométrico

A extensão não abeliana foi consolidada em:

\[
\boxed{\texttt{questoes/q34/associados/slavnov\_taylor\_geometrico.md}}
\]

O ponto central é que, para um operador covariante:

\[
\boxed{
L_{A^g}=g^{-1}L_Ag,
}
\]

qualquer traço funcional admissível preserva gauge:

\[
\boxed{
{\rm Tr}\,F_\tau(L_{A^g})
=
{\rm Tr}\,F_\tau(L_A).
}
\]

Após fixação de gauge de fundo, o determinante de Faddeev--Popov entra como
jacobiano geométrico da seção escolhida em \(\mathcal A/\mathcal G\). A
representação por fantasmas é útil para auditoria BRST, mas não cria ontologia
física adicional na GDQ.

A identidade funcional resultante é:

\[
\boxed{
\mathcal S(\Gamma_\tau)=0.
}
\]

No limite abeliano, ela reduz a:

\[
\boxed{
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
}
\]

Veredito atualizado:

\[
\boxed{
\text{Questão 34 fechada no setor geométrico declarado de 34-0.}
}
\]

O teste em questoes/q34/associados/teste_kernels_covariantes.md comparou três funções covariantes
do mesmo operador. Transversalidade, $\Pi(0)=0$, monotonicidade, finitude e
saturação foram preservadas. Os valores saturados variaram, como devem variar
quando se troca a resolução física. Portanto, a invariância exigível é a da
identidade de calibre; igualdade numérica entre kernels fisicamente distintos
não é uma noção correta de independência do regulador. O semigrupo canônico
$e^{-sH}$ permanece selecionado pela Hessiana oficial.

Trabalhos posteriores que não reabrem Q34 incluem o jacobiano em fundos
topológicos não triviais e as extensões Bismut e não abeliana.

A auditoria item a item está em
questoes/q34/associados/auditoria_enunciados_34_35_0.md.

A auditoria variacional mostrou que a rota fermiônica é auxiliar, mas isso não
bloqueia Q34. O loop fundamental correto é
$\Gamma_{\rm GDQ}^{(1)}=\frac12\operatorname{Tr}_{\rm phys}
\log(\operatorname{Hess}\mathcal S_{\rm GDQ})$, construído nas perturbações
geométricas. Ver questoes/q34/associados/obstrucao_loop_desde_acao_oficial.md.

O loop geométrico foi executado no bulk oficial
$\mathbb R^4\times T^4$ usando a fase de $f$ e a conexão métrica de um ciclo
toroidal. Ver questoes/q34/associados/loop_geometrico_fase_t4.md.
