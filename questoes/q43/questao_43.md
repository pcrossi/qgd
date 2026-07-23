# Questão 43 — Efeito Zeeman e \(g-2\)

## 1. Enunciado

A questão pergunta:

1. \(g=2\) é derivado ou assumido?
2. A correção de Schwinger é calculada?
3. Qual diagrama ou operador produz a anomalia?
4. O resultado depende da escala?

O objetivo não é reescrever a GDQ como QED. Na GDQ, o efeito Zeeman deve ser
obtido como resposta geométrica de um sóliton com circulação conservada a um
campo magnético externo tratado como fonte ou dado de contorno do aparelho.

---

## 2. Fontes usadas

1. `pt-br/19 - Efeito Zeeman.md`;
2. `pt-br/35 - Anomalias Leptônicas e Estrutura Hadrônica Fina.md`;
3. `topicos/medida_interface/teorema_noether_zeeman_gdq.md`;
4. `topicos/geometria_torcao_hopf/projecao_hessiana_noether_g2.md`;
5. `questoes/q42/questao_42.md`;
6. `brain/future/muon-g2-meson-anomalies/index.md`;
7. `memory.md`.

---

## 3. Dados e domínio

O campo magnético externo não é campo fundamental novo da ação oficial. Ele é
um dado externo do aparelho ou da fonte clássica. O objeto físico é um defeito
GDQ com circulação interna protegida por Noether.

O setor analisado é:

\[
\text{sóliton estacionário}
+\text{fluxo de Noether conservado}
+\text{campo magnético externo fraco}
+\text{resposta linear da Hessiana física}.
\]

O campo externo seleciona um eixo, mas não cria o spin nem a circulação. A
parte fundamental vem da ação oficial da GDQ; a linguagem Zeeman é a redução
efetiva no setor magnético.

---

## 4. Forma Zeeman pela simetria de Noether

A ação oficial é invariante sob deslocamento constante da fase:

\[
f\mapsto f+i\varepsilon,
\qquad
\bar f\mapsto\bar f-i\varepsilon.
\]

Essa simetria produz uma corrente de Noether conservada. No setor rotacional
do defeito, a projeção Hopf dessa corrente define uma circulação vetorial:

\[
\boldsymbol{\mathcal C}[\Phi]
=\int_\Sigma \boldsymbol J_{\rm N}\cdot d\boldsymbol\Sigma.
\]

No setor fermiônico elementar:

\[
\boldsymbol C_\pm
=\pm\frac{\hbar}{2}\boldsymbol n.
\]

Antes da aplicação do campo, a isotropia impede a escolha de um eixo
preferencial. Com uma fonte magnética externa fraca \(\boldsymbol B\), o único
escalar linear compatível com isotropia é:

\[
\boldsymbol C\cdot\boldsymbol B.
\]

Logo, a energia reduzida tem a forma:

\[
E(\boldsymbol C,\boldsymbol B)
=E_0(C^2)-\gamma_{\rm eff}\boldsymbol C\cdot\boldsymbol B+O(B^2).
\]

Essa é a forma Zeeman. Ela não é postulada como Hamiltoniano fundamental; ela
é a única resposta linear permitida pela simetria de rotação, pela conservação
de Noether e pelo acoplamento externo ao fluxo.

A condição estacionária angular é:

\[
\delta\boldsymbol C
=\delta\boldsymbol\theta\times\boldsymbol C,
\]

\[
\delta E
=-\gamma_{\rm eff}\delta\boldsymbol\theta\cdot
(\boldsymbol C\times\boldsymbol B).
\]

Portanto:

\[
\boldsymbol C\times\boldsymbol B=0.
\]

No setor elementar:

\[
\boldsymbol C_\pm
=\pm\frac{\hbar}{2}
\frac{\boldsymbol B}{|\boldsymbol B|},
\]

e:

\[
E_\pm
=E_0\mp\gamma_{\rm eff}\frac{\hbar}{2}|\boldsymbol B|.
\]

Para campo inomogêneo:

\[
\boldsymbol F_\pm
=\pm\gamma_{\rm eff}\frac{\hbar}{2}\nabla|\boldsymbol B|.
\]

Esse é o conteúdo geométrico do efeito Zeeman e é o mesmo mecanismo que a Q42
usa para Stern--Gerlach.

---

## 5. \(g=2\): derivado ou assumido?

Na normalização magnética mínima:

\[
\boldsymbol\mu
=\gamma_{\rm eff}\boldsymbol C
=g\frac{q}{2mc}\boldsymbol C.
\]

A parte protegida por Noether identifica o momento magnético mínimo com o
mesmo fluxo conservado:

\[
M_{\boldsymbol n}
=\gamma_0\mathcal C_{\boldsymbol n}.
\]

Com:

\[
\gamma_0=\frac{q}{mc},
\]

segue:

\[
g_0=\frac{2mc}{q}\gamma_0=2.
\]

Portanto, no estado atual da GDQ:

\[
\boxed{
g=2\ \text{é derivado como termo mínimo protegido por Noether,}
}
\]

desde que se aceite a normalização eletromagnética já usada nos setores de
carga e circulação. Ele não é assumido como postulado de Pauli ou Dirac.

O que Noether fixa é apenas a parte mínima:

\[
\boxed{Z_{\rm N}=1.}
\]

Noether não fixa sozinho o momento magnético total, porque o campo pode
deformar modos internos do mesmo sóliton sem alterar a carga conservada.

---

## 6. Resposta geométrica e anomalia

Decomponha o diferencial magnético em:

\[
m=\gamma_0c+m_\perp,
\]

onde:

- \(c=\delta\mathcal C/\delta\Phi\) é o modo protegido de Noether;
- \(m_\perp\) é a resposta interna que não muda a carga de Noether.

No background vinculado, com Hessiana física \(H_C\), a resposta do
multiplicador fornece:

\[
\gamma_{\rm eff}
=-\left.\frac{\partial\lambda}{\partial B}\right|_{B=0}
=
\frac{\langle c,H_C^{-1}m\rangle}
     {\langle c,H_C^{-1}c\rangle}.
\]

Logo:

\[
\gamma_{\rm eff}
=\gamma_0+\Delta\gamma_{\rm geom},
\]

\[
\Delta\gamma_{\rm geom}
=
\frac{\langle c,H_C^{-1}m_\perp\rangle}
     {\langle c,H_C^{-1}c\rangle}.
\]

Assim:

\[
g_{\rm GDQ}
=2\left(1+a_{\rm geom}\right),
\]

\[
a_{\rm geom}
=\frac{\Delta\gamma_{\rm geom}}{\gamma_0}.
\]

Esse é o operador geométrico que substitui, na ontologia da GDQ, a linguagem
de diagramas da QED:

\[
\boxed{
H_C^{-1}m_\perp
}
\]

ou seja, a anomalia é a resposta transversal do background, propagada pela
Hessiana física da ação oficial no setor de circulação fixada.

---

## 7. Origem do fator \(1/(2\pi)\)

No ciclo elementar \(S^1\), com \(\vartheta\in[0,2\pi)\), o modo físico não é
o modo zero escalar, mas a 1-forma harmônica normalizada:

\[
h=\frac{d\vartheta}{2\pi},
\qquad
\oint_{S^1}h=1.
\]

Sua norma é:

\[
\langle h,h\rangle
=\int_0^{2\pi}\frac{d\vartheta}{(2\pi)^2}
=\frac{1}{2\pi}.
\]

Uma circulação \(C\) tem componente harmônica:

\[
a_C=Ch.
\]

Logo:

\[
\|a_C\|^2
=\frac{C^2}{2\pi}.
\]

Essa é a projeção angular do termo quadrático em \(|dS_R|^2\) da ação oficial.
Como a carga usa a primeira potência,

\[
\int_0^{2\pi}\varrho_Cd\vartheta=C,
\]

mas o vestido elástico usa a segunda,

\[
\int_0^{2\pi}\varrho_C^2d\vartheta
=\frac{C^2}{2\pi},
\]

surge o fator angular:

\[
\boxed{
\frac{1}{2\pi}.
}
\]

Consequentemente, se a intensidade eletrogeométrica elementar é \(\alpha\),
o primeiro vestido geométrico é:

\[
a_{\rm geom}^{(1)}
=\frac{\alpha}{2\pi}.
\]

---

## 8. Correção de Schwinger

A GDQ reproduz a forma líder:

\[
\boxed{
a_{\rm geom}^{(1)}
=\frac{\alpha}{2\pi}.
}
\]

Portanto:

\[
\boxed{
g_{\rm GDQ}^{(1)}
=2\left(1+\frac{\alpha}{2\pi}\right).
}
\]

Usando \(\alpha^{-1}=137.035999177\):

\[
a_{\rm geom}^{(1)}
=0.001161409732098,
\]

\[
g_{\rm GDQ}^{(1)}
=2.002322819464196.
\]

Esse valor tem o sinal e a escala corretos do primeiro excesso magnético. Ele
fica acima do valor eletrônico medido por cerca de \(3.5\times10^{-6}\) em
\(g\), isto é, aproximadamente \(1.76\) ppm.

Logo:

\[
\boxed{
\text{a correção de Schwinger está derivada estruturalmente na ordem líder.}
}
\]

Mas:

\[
\boxed{
\text{a predição metrológica completa de }g_e
\text{ ainda exige os termos superiores de }H_C^{-1}m_\perp.
}
\]

---

## 9. Qual operador produz a anomalia?

Na QED, a resposta seria descrita por diagramas de vértice. Na GDQ, a
linguagem correta é a resposta da Hessiana física:

\[
\Delta\gamma_{\rm geom}
=
\frac{\langle c,H_C^{-1}m_\perp\rangle}
     {\langle c,H_C^{-1}c\rangle}.
\]

Portanto, o objeto que produz a anomalia é:

\[
\boxed{
H_C^{-1}m_\perp,
}
\]

com \(H_C\) sendo a Hessiana física da ação oficial no background com
circulação fixada.

Em termos de cálculo:

1. fixa-se a carga/circulação de Noether;
2. projeta-se a fonte magnética;
3. separa-se a parte mínima \(\gamma_0c\);
4. calcula-se a resposta transversal \(m_\perp\);
5. avalia-se a contração pela pseudoinversa física de \(H_C\), removendo
   modos de gauge, fase comum e modos de Noether.

Essa é a versão GDQ do cálculo de anomalia magnética. Não se deve chamá-la de
diagrama fundamental.

O desenvolvimento formal dos termos superiores está registrado em
`associados/expansao_hessiana_g2.md`. Em resumo, escrevendo:

\[
H_C
=H_0+\alpha H_1+\alpha^2H_2+\cdots,
\]

\[
m_\perp
=\alpha m_1+\alpha^2m_2+\cdots,
\]

os coeficientes superiores são obtidos pela expansão da pseudoinversa física
de \(H_C\), e não por importação da série perturbativa da QED.

---

## 10. Dependência de escala

Há três escalas que não devem ser misturadas:

1. a escala do campo/aparelho externo;
2. a escala interna do sóliton;
3. a normalização eletrogeométrica \(\alpha\).

O termo mínimo \(g_0=2\) é protegido por Noether e pela normalização da
circulação. Ele não depende da escala do aparelho no regime de campo fraco.

A correção líder:

\[
\frac{\alpha}{2\pi}
\]

depende da normalização eletrogeométrica \(\alpha\). Se \(\alpha\) for tomada
como a constante global herdada do setor eletromagnético/cosmológico, então o
resultado líder é universal. Se for avaliada por um background local
específico, a universalidade depende da ponte global--local desse setor.

Os termos superiores dependem do espectro de \(H_C\), do domínio, do contorno e
do background. Portanto, a predição metrológica completa é sensível ao operador
físico e à normalização setorial, mas não deve depender de ajuste posterior ao
valor experimental.

---

## 11. Auditoria do capítulo legado 35 sobre \(g_\mu-2\)

O capítulo legado 35 propõe para o múon uma fórmula com fatores de Fano,
impedância torsional, \(\delta_{\rm efetivo}\) e potências de \(\alpha\). No
estado atual da teoria, esse bloco deve ser classificado como:

\[
\boxed{
\text{fenomenologia futura, não prova vigente.}
}
\]

Motivo:

1. os coeficientes \(\chi_{\rm Fano}\) e \(\delta_{\rm efetivo}\) precisam ser
   derivados da Hessiana oficial do background leptônico;
2. a fórmula não identifica diretamente o operador físico \(H_C^{-1}m_\perp\);
3. a comparação numérica não pode ser usada como derivação;
4. o status experimental de \(g_\mu-2\) deve ser reavaliado com dados
   atualizados antes de qualquer alegação forte.

Assim, a Q43 não deve declarar resolvido o \(g_\mu-2\) completo. Ela deve
declarar resolvida a estrutura do operador que calcularia a anomalia.

---

## 12. Relação com a hierarquia leptônica

A hierarquia leptônica não deriva o efeito Zeeman. Ela fornece os backgrounds
nos quais a resposta magnética deve ser avaliada.

Para cada lépton carregado:

\[
\ell\in\{e,\mu,\tau\},
\]

o problema correto é:

\[
\text{Q39}
\longrightarrow
\Phi_\ell
\longrightarrow
H_{C,\ell}^{-1}m_{\perp,\ell}
\longrightarrow
a_\ell.
\]

Logo:

\[
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{-1}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{-1}c_\ell\rangle
}.
\]

Isso explica por que \(g_\mu-2\) não deve ser calculado com uma fórmula isolada
sem antes construir o background do múon. A massa/hierarquia entra na Hessiana
e no modo transversal do lépton, não na forma Zeeman mínima.

---

## 13. Verificação numérica líder

O script `associados/calcular_g2_lider_q43.py` calcula apenas o termo líder:

\[
a^{(1)}
=\frac{\alpha}{2\pi},
\qquad
g^{(1)}
=2\left(1+\frac{\alpha}{2\pi}\right).
\]

A saída está em `associados/saida_g2_lider_q43.md`.

Usando \(\alpha^{-1}=137.035999177\):

\[
g_{\rm lider}=2.002322819464196.
\]

Comparado ao valor eletrônico de referência usado localmente:

\[
g_e\simeq2.00231930436092,
\]

o resíduo é:

\[
g_e-g_{\rm lider}
\simeq
-3.5151\times10^{-6}.
\]

Esse resíduo é exatamente o que deve ser produzido pelas ordens superiores da
resposta:

\[
H_C^{-1}m_\perp.
\]

Portanto, o teste numérico confirma o fechamento do termo líder e delimita o
tamanho do problema restante, mas não fecha a metrologia completa.

---

## 14. Resíduos superiores diagnosticados

O script `associados/calcular_residuos_superiores_q43.py` calcula o que falta
após subtrair o termo líder:

\[
a_1=\frac{\alpha}{2\pi}.
\]

Usando \(\alpha^{-1}=137.035999177\), obtém-se:

| caso | \(a_{\rm obs}-a_1\) | coeficiente agregado em \((\alpha/\pi)^2\) |
|---|---:|---:|
| elétron | \(-1.7575515\times10^{-6}\) | \(-0.3257445\) |
| múon, média mundial 2023 | \(4.5108579\times10^{-6}\) | \(0.8360423\) |

Esse cálculo mostra duas coisas:

1. o elétron requer uma correção superior pequena e negativa;
2. o múon requer uma resposta superior diferente, portanto não se deve usar o
   mesmo background do elétron.

O coeficiente agregado não é derivação. Ele apenas mede o tamanho que a
contração

\[
H_{C,\ell}^{-1}m_{\perp,\ell}
\]

deve produzir.

---

## 15. Avaliador espectral de Hessiana

Foi criado o script `associados/avaliar_hessiana_q43.py`.

Entrada esperada:

1. matriz física \(H_C\);
2. vetor \(c\);
3. vetor \(m_\perp\);
4. normalização \(\gamma_0\).

O script calcula:

\[
a_{\rm geom}
=
\frac{1}{\gamma_0}
\frac{\langle c,H_C^+m_\perp\rangle}
{\langle c,H_C^+c\rangle},
\]

onde \(H_C^+\) é a pseudoinversa após remoção dos modos nulos.

Uma fixture sintética foi executada apenas para validar a álgebra do código.
Ela reproduz o termo líder, mas não representa um background físico.

## 16. Teste reduzido Q39→Q43

Foi criado o script `associados/modelo_reduzido_q39_q43.py` para testar uma
pergunta específica:

\[
\text{a hierarquia leptônica Q39, sozinha, já explica os resíduos superiores de }g-2?
\]

A resposta é não.

O script foi atualizado para usar a hierarquia intrínseca vigente da Q39, não
o benchmark Rosen--Morse:

\[
R_e=1,
\qquad
R_\mu=
\frac{3}{2\alpha}
+\frac65
+2\alpha,
\]

\[
\frac{1+R_\mu+R_\tau}
{(1+\sqrt{R_\mu}+\sqrt{R_\tau})^2}
=\frac23.
\]

Obtém:

| lépton | papel Q39 | \(R_\ell=M_\ell/M_e\) |
|---|---|---:|
| elétron | torção primária | \(1\) |
| múon | torção transversal/biespacial | \(206.768593470628673\) |
| tau | saturação tridimensional | \(3477.446405098381092\) |

Esse bloco confirma que a Q39 fornece os backgrounds leptônicos reduzidos
vigentes. Em seguida, testa-se a hipótese mínima de que o resíduo superior de
\(g-2\) escale apenas com a susceptibilidade escalar:

\[
\chi_\ell\propto\frac{1}{R_\ell}.
\]

Normalizando no elétron, o resíduo previsto para o múon seria:

\[
\mathcal R_\mu^{(\chi)}
\simeq
-8.50\times10^{-9}.
\]

O resíduo observado após subtrair o termo líder é:

\[
\mathcal R_\mu^{(\mathrm{obs})}
\simeq
4.51\times10^{-6}.
\]

Portanto, a hipótese escalar reduzida falha por sinal e por escala:

\[
\frac{\mathcal R_\mu^{(\chi)}}{\mathcal R_\mu^{(\mathrm{obs})}}
\simeq
-1.884\times10^{-3}.
\]

Conclusão:

\[
\boxed{
\text{a Q39 fornece o background, mas não substitui o cálculo Zeeman/anomalia.}
}
\]

O que falta para uma previsão metrológica não é a hierarquia de massas, mas o
operador transversal:

\[
\boxed{
H_{C,\ell}^{+}m_{\perp,\ell}.
}
\]

Em outras palavras, para cada lépton carregado deve-se construir diretamente:

1. o background leptônico \(\Phi_\ell\);
2. a Hessiana física com circulação fixada \(H_{C,\ell}\);
3. o modo protegido \(c_\ell\);
4. a fonte magnética transversal \(m_{\perp,\ell}\);
5. a contração:

\[
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle
}.
\]

O arquivo de saída é
`associados/saida_modelo_reduzido_q39_q43.md`.

## 17. Construção operacional de \(H_C,c,m_\perp\)

A construção operacional foi registrada em
`associados/hessiana_operacional_q43.md`.

O funcional vinculado usado é:

\[
\mathscr I[\Phi,\lambda;B]
=
\mathcal S_{\rm GDQ}[\Phi]
-B\,M[\Phi]
-\lambda\left(\mathcal C[\Phi]-C_\ell\right).
\]

No background \(\Phi_\ell\), lineariza-se:

\[
\mathcal C[\Phi_\ell+\eta]
=
C_\ell+\langle c_\ell,\eta\rangle+O(\eta^2),
\]

\[
M[\Phi_\ell+\eta]
=
M[\Phi_\ell]+\langle m_\ell,\eta\rangle+O(\eta^2).
\]

Com:

\[
m_\ell=\gamma_{0,\ell}c_\ell+m_{\perp,\ell},
\]

o observável é:

\[
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle
}.
\]

### 17.1 Bloco líder sem alvo experimental

Foi implementado o bloco matricial:

\[
H_{\rm lead}
=
\begin{pmatrix}
1 & -1\\
-1 & 2\pi/\alpha
\end{pmatrix},
\qquad
c=
\begin{pmatrix}
1\\0
\end{pmatrix},
\qquad
m_\perp=
\begin{pmatrix}
0\\1
\end{pmatrix}.
\]

Ele satisfaz:

\[
\frac{\langle c,H_{\rm lead}^{-1}m_\perp\rangle}
{\langle c,H_{\rm lead}^{-1}c\rangle}
=
\frac{\alpha}{2\pi}.
\]

O script `associados/construir_blocos_hessiana_q43.py` gerou
`associados/hessiana_lider_q43.npz`, e o avaliador independente
`associados/avaliar_hessiana_q43.py` confirmou:

\[
a_{\rm lead}=1.161409732097665\times10^{-3},
\]

\[
g_{\rm lead}=2.002322819464196.
\]

Esse é o fechamento computável do termo líder.

### 17.2 Blocos superiores `required`

Para medir o tamanho da resposta transversal faltante, foi criado o bloco:

\[
H_{\rm req}
=
\begin{pmatrix}
1 & -1 & -J_2\\
-1 & K_1 & 0\\
-J_2 & 0 & K_{2,\ell}
\end{pmatrix}.
\]

Aqui:

\[
K_1=\frac{2\pi}{\alpha}.
\]

O canal superior usa amplitude \(\mu_{2,\ell}\) escolhida para reconstruir o
valor observado. Por isso, esses blocos são diagnóstico inverso, não previsão.

Resultados:

| caso | \(\mu_{2,\ell}^{\rm required}\) | \(a_{\rm reconstruído}\) | classificação |
|---|---:|---:|---|
| elétron | \(-1.5132915275\times10^{-3}\) | \(1.159652180590110\times10^{-3}\) | diagnóstico inverso |
| múon | \(8.0307612309\times10^{-1}\) | \(1.165920590000000\times10^{-3}\) | diagnóstico inverso |

Arquivos gerados:

1. `associados/hessiana_required_e_q43.npz`;
2. `associados/hessiana_required_mu_q43.npz`;
3. `associados/saida_avaliacao_hessiana_required_e_q43.md`;
4. `associados/saida_avaliacao_hessiana_required_mu_q43.md`.

Esses números transformam a pendência em uma quantidade objetiva:

\[
\boxed{
\text{derivar da ação oficial o canal que substituirá }
\mu_{2,\ell}^{\rm required}.
}
\]

Portanto, a cadeia operacional está construída; a parte metrológica permanece
condicionada à derivação física do canal transversal superior.

---

## 18. Respostas diretas às perguntas obrigatórias

### 18.1 \(g=2\) é derivado ou assumido?

Derivado no setor mínimo protegido por Noether:

\[
g_0=2.
\]

A derivação depende da identificação do momento magnético mínimo com a mesma
circulação conservada:

\[
\gamma_0=\frac{q}{mc}.
\]

Essa identificação pertence ao dicionário eletromagnético GDQ já usado nos
setores de carga, não à álgebra de Pauli postulada.

### 18.2 A correção de Schwinger é calculada?

Sim, no nível estrutural/líder:

\[
a^{(1)}=\frac{\alpha}{2\pi}.
\]

Mas a predição metrológica completa de \(g_e\), \(g_\mu\) ou \(g_\tau\) exige
calcular as ordens superiores pela resposta da Hessiana.

### 18.3 Qual diagrama ou operador produz a anomalia?

Não há diagrama fundamental de QED na ontologia da GDQ. O operador é:

\[
H_C^{-1}m_\perp.
\]

Ele representa a resposta interna transversal do background ao campo
magnético, com circulação de Noether mantida fixa.

### 18.4 O resultado depende da escala?

O termo mínimo \(g=2\) não depende da escala no regime fraco. O primeiro
vestido depende apenas de \(\alpha\). As correções superiores dependem do
background, do domínio, do contorno e da normalização eletromagnética setorial.

---

## 19. Status da Questão 43

\[
\boxed{
\text{Questão 43 fechada estrutural e operacionalmente.}
}
\]

Fechada estrutural e operacionalmente porque:

1. a forma Zeeman foi derivada por Noether e isotropia;
2. \(g=2\) foi identificado como parte mínima protegida;
3. o fator \(1/(2\pi)\) foi obtido pela norma da 1-forma harmônica;
4. a correção líder de Schwinger foi reproduzida como
   \(\alpha/(2\pi)\);
5. o operador GDQ responsável pela anomalia foi identificado como
   \(H_C^{-1}m_\perp\);
6. o bloco computável \(H_C,c,m_\perp\) foi construído para o termo líder;
7. o avaliador numérico foi executado e validado.

Não está fechada preditivamente/metrologicamente porque:

1. as ordens superiores de \(g_e\) não foram calculadas da Hessiana completa;
2. o \(g_\mu-2\) legado permanece fenomenologia futura;
3. a dependência de massa/família exige o background leptônico completo;
4. a comparação com dados experimentais atuais deve ser feita posteriormente.

Comparação líder:

\[
g_{\rm lead}=2.002322819464196,
\]

\[
g_e^{\rm exp}=2.002319304361180,
\]

\[
g_{\rm lead}-g_e^{\rm exp}
=3.5151030\times10^{-6}.
\]

Em termos de anomalia:

\[
a_e^{\rm exp}-a_{\rm lead}
=-1.7575515\times10^{-6},
\]

\[
a_\mu^{\rm exp}-a_{\rm lead}
=4.5108579\times10^{-6}.
\]

Os blocos `required` reproduzem esses resíduos por construção; eles são
diagnóstico inverso do canal transversal superior, não previsão cega.

Os itens 1--5 do refinamento foram tratados assim:

| Item | Resultado |
|---|---|
| 1. Termos superiores | fórmula por expansão de \(H_C^{-1}\) em `associados/expansao_hessiana_g2.md` |
| 2. \(H_C^{-1}m_\perp\) | operador definido como resposta transversal no setor de circulação fixa |
| 3. elétron/múon/tau | dependência passa por \(\Phi_\ell,H_{C,\ell},m_{\perp,\ell}\), herdados da Q39 |
| 4. comparação experimental | mantida como comparação local; \(g_\mu-2\) atual exige auditoria futura |
| 5. teste numérico | script líder criado e executado; resíduo isolado como problema das ordens superiores |

Complementação posterior:

| Cálculo | Resultado |
|---|---|
| resíduos superiores | elétron e múon avaliados como diagnóstico metrológico |
| avaliador de Hessiana | script genérico criado; depende de \(H_C,c,m_\perp\) físicos |
| fixture | valida álgebra da pseudoinversa, não é background físico |
| modelo reduzido Q39→Q43 | mostra que a hierarquia fornece background, mas não fecha \(g-2\) sem \(m_{\perp,\ell}\) |
| blocos operacionais \(H_C,c,m_\perp\) | bloco líder físico fecha \(\alpha/(2\pi)\); blocos superiores são diagnóstico inverso |

Auditoria final do canal superior:

| Bloco | Resultado |
|---|---|
| derivação formal | \(K_{2,\ell}\), \(J_{2,\ell}\) e \(\mu_{2,\ell}\) são projeções de \(H_{C,\ell}\) e \(m_{\perp,\ell}\) no primeiro modo transversal superior |
| teste de não-unicidade | várias triplas \((J_2,K_2,\mu_2)\) reproduzem o mesmo \(a_{\rm obs}\) |
| veredito | \(\mu_{2,\ell}^{\rm required}\) não pode ser promovido a previsão sem calcular \(J_{2,\ell}\) e \(K_{2,\ell}\) pela Hessiana oficial |

Assim, o fechamento metrológico completo fica bloqueado por um único cálculo
bem definido:

\[
\boxed{
\text{construir o modo transversal }e_{2,\ell}\text{ e avaliar }
\langle e_{2,\ell},H_{C,\ell}e_{2,\ell}\rangle,\,
\langle e_{0,\ell},H_{C,\ell}e_{2,\ell}\rangle,\,
\langle e_{2,\ell},m_{\perp,\ell}\rangle.
}
\]

Arquivos:

1. `associados/canal_superior_formal_q43.md`;
2. `associados/extrair_canal_superior_q43.py`;
3. `associados/saida_extracao_canais_lider_q43.md`;
4. `associados/saida_extracao_canais_required_e_q43.md`;
5. `associados/saida_extracao_canais_required_mu_q43.md`;
6. `associados/auditar_nao_unicidade_canal_superior_q43.py`;
7. `associados/saida_nao_unicidade_canal_superior_q43.md`.

Extração nos blocos disponíveis:

| entrada | \(K_2\) | \(J_2\) | \(\mu_2\) | classificação |
|---|---:|---:|---:|---|
| `hessiana_required_e_q43.npz` | \(8.6102257658\times10^2\) | \(1\) | \(-1.5132915275\times10^{-3}\) | diagnóstico inverso; degenerado com o canal líder |
| `hessiana_required_mu_q43.npz` | \(1.7803179361\times10^5\) | \(1\) | \(8.0307612309\times10^{-1}\) | diagnóstico inverso |

O extrator resolve a parte algébrica. Para transformar esses números em
previsão, a entrada deve ser a Hessiana oficial \(H_{C,\ell}\) do background
leptônico \(\Phi_\ell\), não um bloco `required`.

Execução dos sete passos em Galerkin oficial reduzido:

| Passo | Resultado |
|---|---|
| background \(\Phi_\ell\) | truncagem \(x_*=(1,0,0,0,0)\), usada apenas como teste |
| flutuações | modos de fase, densidade e métrica conformal |
| ação | integrando oficial reduzido com \(\mathcal U=e^{-(f+\bar f)/2}\) |
| Hessiana | calculada por diferenças finitas |
| circulação | \(c=(1,0,0,0,0)\) |
| fonte magnética nua | \(m_\perp^{\rm naked}=0\) |
| extração | \(K_i,J_i,\mu_i\) calculados pelo extrator |

O teste mostrou que a ação oficial reduzida fornece \(H\) e \(c\), mas não
fornece \(m_\perp\) sem o mapa externo \(M[\Phi;B]\). Também mostrou que a
truncagem usada ainda não é uma sela estável, pois possui modos negativos.

Arquivos:

1. `associados/sete_passos_hessiana_oficial_q43.md`;
2. `associados/hessiana_oficial_galerkin_q43.py`;
3. `associados/saida_hessiana_oficial_galerkin_q43.md`;
4. `associados/saida_extracao_hessiana_oficial_galerkin_nua_q43.md`;
5. `associados/saida_extracao_hessiana_oficial_galerkin_lider_q43.md`.

Construção posterior do background leptônico estável reduzido e do mapa
magnético:

O script `associados/construir_background_fonte_q43.py` executou a próxima
etapa em duas camadas.

Primeiro, tentou-se obter uma sela diretamente na truncagem Galerkin oficial
simples, com circulação fixa. O melhor candidato encontrado ainda possui modo
negativo na Hessiana transversal. Portanto:

\[
\boxed{
\text{a truncagem Galerkin simples não é a sela leptônica física.}
}
\]

Esse resultado não invalida a Q43; ele apenas mostra que o background físico
exige o projetor físico/bulk completo ou uma truncagem mais rica.

Segundo, foi construído um background leptônico efetivo estável mínimo,
compatível com a Q39 e com a resposta líder de Noether. O mapa físico de fonte
magnética fraca foi escrito como:

\[
M[\Phi;B]
=
B\left(\gamma_0\mathcal C[\Phi]+M_\perp[\Phi]\right).
\]

A parte mínima é:

\[
M_{\rm min}[\Phi;B]
=
B\gamma_0\mathcal C[\Phi],
\]

e fornece \(g_0=2\). A parte transversal líder é a projeção harmônica no ciclo
de fase:

\[
M_\perp^{(1)}[\Phi;B]
=
B A_h[\Phi],
\qquad
\langle h,h\rangle=\frac{1}{2\pi}.
\]

Na representação matricial estável, usa-se:

\[
K_1=\frac{2\pi}{\alpha},
\qquad
m_\perp=(0,1,0),
\]

de modo que o fator \(\alpha/(2\pi)\) surge da contração com \(H^{-1}\), não de
um ajuste posterior.

Os blocos efetivos foram regenerados usando os papéis intrínsecos da Q39:

| lépton | papel Q39 vigente | \(M_\ell/M_e\) | \(K_2\) estável | \(a_{\rm líder}\) |
|---|---|---:|---:|---:|
| \(e\) | torção primária | \(1\) | \(8.6102257658\times10^2\) | \(1.1614097321\times10^{-3}\) |
| \(\mu\) | torção transversal/biespacial | \(206.7685934706\) | \(1.7803242711\times10^5\) | \(1.1614097321\times10^{-3}\) |
| \(\tau\) | saturação tridimensional | \(3477.4464050984\) | \(2.9941598636\times10^6\) | \(1.1614097321\times10^{-3}\) |

Os valores antigos de \(K_2\) associados a \(n=0,1,17\) ficam preservados
apenas em saídas históricas/diagnósticas, não como canal físico canônico da
Q43.

As extrações confirmam:

1. o canal líder tem \(K_1=2\pi/\alpha\), \(J_1=1\), \(\mu_1=1\);
2. o canal superior de massa \(K_2\) foi incluído de forma positiva e estável;
3. como \(\mu_2=0\) nesses blocos, eles ainda não produzem resíduos
   metrológicos superiores.

Logo, a construção atual fecha o background efetivo mínimo e o mapa magnético
linear, mas não fecha o canal superior metrológico:

\[
\boxed{
\text{falta derivar }M_\perp^{(2)}[\Phi;B]\text{ ou o modo superior acoplado }
\mu_{2,\ell}\text{ pela Hessiana oficial completa.}
}
\]

Arquivos:

1. `associados/construir_background_fonte_q43.py`;
2. `associados/saida_background_fonte_q43.md`;
3. `associados/background_leptonico_estavel_e_q43.npz`;
4. `associados/background_leptonico_estavel_mu_q43.npz`;
5. `associados/background_leptonico_estavel_tau_q43.npz`;
6. `associados/saida_extracao_background_estavel_e_q43.md`;
7. `associados/saida_extracao_background_estavel_mu_q43.md`;
8. `associados/saida_extracao_background_estavel_tau_q43.md`.

Derivação do canal superior físico direto:

O script `associados/derivar_canal_superior_fisico_q43.py` avaliou se o
primeiro canal superior pode ser uma nova fonte linear direta
\(M_\perp^{(2)}[\Phi;B]\) para campo magnético uniforme.

No ciclo de Noether, a componente que acopla a um campo uniforme é a forma
harmônica:

\[
h=\frac{d\vartheta}{2\pi}.
\]

Os modos superiores locais são exatos:

\[
e_k\propto d\sin(k\vartheta),
\qquad
k\ge1.
\]

Pela decomposição de Hodge no ciclo:

\[
\langle h,e_k\rangle=0.
\]

Numericamente, o teste encontrou:

\[
\langle h,e_1\rangle\simeq -4.36\times10^{-17},
\qquad
\langle h,e_2\rangle\simeq -2.72\times10^{-17}.
\]

Portanto:

\[
\boxed{
\mu_{2,\ell}^{\rm direto}=0
}
\]

para campo magnético uniforme.

Essa é uma conclusão importante: os blocos `required` não podem ser
substituídos por uma fonte linear direta universal \(M_\perp^{(2)}\), porque a
simetria elimina esse acoplamento. Assim, o resíduo metrológico superior deve
vir de outro elo interno:

1. correções da Hessiana física,

\[
H_C=H_0+\alpha H_1+\alpha^2H_2+\cdots;
\]

2. mistura Hessiana entre o canal líder e modos superiores;
3. mapa eletrogeométrico interno não uniforme derivado do bulk;
4. ou fonte de aparelho não uniforme, que seria experimental e não universal.

Para a anomalia universal de campo uniforme, a rota correta restante é a
correção de Hessiana, não uma nova \(\mu_2\) direta.

Arquivos:

1. `associados/derivar_canal_superior_fisico_q43.py`;
2. `associados/saida_canal_superior_fisico_q43.md`;
3. `associados/saida_extracao_selecao_e_q43.md`;
4. `associados/saida_extracao_selecao_mu_q43.md`;
5. `associados/saida_extracao_selecao_tau_q43.md`.

Derivação reduzida de \(H_1\) por mistura harmônica:

O script `associados/derivar_h1_mistura_q43.py` testou a primeira rota
permitida após a regra de seleção da fonte direta. A não-linearidade
geométrica do modo líder permite:

\[
\cos^2\vartheta
=
\frac12(1+\cos2\vartheta).
\]

Removido o modo constante de normalização, sobra uma componente no primeiro
harmônico superior. O overlap normalizado calculado foi:

\[
\beta_{12}
=
\left\langle u_2,u_1^2-\langle u_1^2\rangle\right\rangle
\simeq
2.8209479177\times10^{-1}.
\]

Os overlaps com os modos 1 e 3 são nulos dentro da precisão numérica:

\[
\beta_{11}\simeq -2.72\times10^{-17},
\qquad
\beta_{13}\simeq -3.81\times10^{-17}.
\]

O bloco reduzido usado foi:

\[
H_C
=
H_0+\alpha H_1,
\]

com:

\[
(H_1)_{12}=(H_1)_{21}
=
\beta_{12}\sqrt{K_1K_2}.
\]

Esse termo é permitido pela simetria e permanece estável nos três backgrounds
efetivos. O resultado numérico foi:

| lépton | \(K_2\) | \(H_{1,12}\) | \(a\) obtido |
|---|---:|---:|---:|
| \(e\) | \(8.6102257658\times10^2\) | \(2.4288998445\times10^2\) | \(1.1614146537\times10^{-3}\) |
| \(\mu\) | \(1.7803179361\times10^5\) | \(3.4926182674\times10^3\) | \(1.1614146537\times10^{-3}\) |
| \(\tau\) | \(2.9939016515\times10^6\) | \(1.4322574912\times10^4\) | \(1.1614146537\times10^{-3}\) |

Conclusão: a rota de mistura Hessiana existe, mas a mistura angular mínima
sozinha não fecha o resíduo metrológico. Ela gera uma correção pequena e
universal. Para obter o coeficiente físico superior é necessário avaliar a
terceira/quarta variação da ação oficial no background 8D, incluindo os
fatores tensoriais, diagonais e normalizações de \(\mathcal U\sqrt g\).

Arquivos:

1. `associados/derivar_h1_mistura_q43.py`;
2. `associados/saida_h1_mistura_q43.md`;
3. `associados/saida_extracao_h1mix_e_q43.md`;
4. `associados/saida_extracao_h1mix_mu_q43.md`;
5. `associados/saida_extracao_h1mix_tau_q43.md`.

Variações superiores da ação reduzida:

Para verificar se a própria ação reduzida fornece um canal superior local, foi
calculada a expansão cúbica/quártica da truncagem Galerkin em torno do ponto
simétrico:

$$
x_*=(1,0,0,0,0).
$$

A Hessiana local ainda possui modos negativos, confirmando que essa truncagem
não é a sela leptônica física. Mesmo assim, a expansão informa a regra de
seleção variacional.

O acoplamento direto:

$$
T_{112}
=
\frac{\partial^3 S_{\rm red}}{\partial x_1^2\partial x_2}(x_*)
$$

saiu no nível de ruído numérico:

$$
T_{112}\simeq -2.66\times10^{-6}.
$$

Logo, a seleção harmônica \(\beta_{12}\) não se transforma automaticamente
numa fonte variacional direta líder\(^2\to\)superior. O termo robusto foi:

$$
T_{123}
=
\frac{\partial^3 S_{\rm red}}{\partial x_1\partial x_2\partial x_3}(x_*)
\simeq
-6.2831748693
\simeq
-2\pi.
$$

Aqui \(x_1\) é o harmônico líder, \(x_2\) o harmônico superior e \(x_3\) a
flutuação de densidade em \(\operatorname{Re}f\). A leitura correta é:

$$
\boxed{
\text{o canal superior existe como mistura mediada pela densidade, não como
fonte linear direta universal.}
}
$$

Isso reforça a pendência metrológica em vez de eliminá-la: para prever
\(g_e\) e \(g_\mu-2\), é necessário avaliar esses tensores na sela leptônica 8D
estável e contrair com o mapa magnético de contorno \(M[\Phi;B]\).

Arquivos:

1. `associados/calcular_variacoes_superiores_gdq_q43.py`;
2. `associados/saida_variacoes_superiores_gdq_q43.md`.

Contração do canal mediado pela densidade:

O termo robusto \(T_{123}\) foi então convertido em um operador condicional
para os backgrounds leptônicos efetivos. Se a sela física tiver uma amplitude
estacionária \(\eta_\ell\) no modo de densidade, a Hessiana efetiva recebe:

$$
\Delta H_{12}
=
\eta_\ell T_{123}.
$$

A amplitude foi calculada diretamente na sela angular reduzida, com duas
correções necessárias: a derivada da fase com monodromia foi tomada como
conexão globalmente definida e a normalização de
\(\mathcal U\sqrt g\) foi imposta antes da variação. A execução canônica usa
\(\eta_\ell=0\), pois essa é a única raiz estacionária normalizada encontrada.
O resultado foi:

| lépton | \(a_0\) | \(a_{\rm eff}\) | \(\Delta a\) |
|---|---:|---:|---:|
| \(e\) | \(1.1614097321\times10^{-3}\) | \(1.1614097321\times10^{-3}\) | \(0\) |
| \(\mu\) | \(1.1614097321\times10^{-3}\) | \(1.1614097321\times10^{-3}\) | \(0\) |
| \(\tau\) | \(1.1614097321\times10^{-3}\) | \(1.1614097321\times10^{-3}\) | \(0\) |

O refinamento de malha \(N=1024,2048,4096,8192\) mantém
\(|\eta_\ell|<3{,}5\times10^{-9}\). A solução não normalizada
\(|\eta|\simeq1{,}064\) é excluída do domínio variacional: ela modifica a
norma de \(\mathcal U\sqrt g\). A Hessiana da raiz homogênea ainda possui um
autovalor negativo, aproximadamente \(-6{,}247\times10^{-2}\); portanto ela é
uma sela reduzida, não o background físico 8D estável.

Isso fixa o próximo dado que realmente falta:

$$
\boxed{
\eta_\ell
\text{ ou o perfil completo de }
\operatorname{Re}f
\text{ na sela leptônica 8D.}
}
$$

Portanto, a metrologia superior de Q43 não deve ser obtida por
\(\mu_{2,\ell}^{\rm required}\), mas pelo perfil de densidade da sela física
contraído com \(T_{123}\) e com o mapa magnético de contorno.

Arquivos:

1. `associados/contrair_canal_densidade_q43.py`;
2. `associados/saida_contracao_canal_densidade_q43.md`;
3. `associados/calcular_eta_pela_sela_q43.py`;
4. `associados/saida_eta_pela_sela_q43.md`.

## 21. Papel da temperatura e fechamento conservador

A temperatura é relevante para correções finas, mas ela não muda a conclusão
estrutural da Q43. Na GDQ, temperatura pode entrar de duas formas
compatíveis com a ação oficial:

1. como dado global de contorno do espaço cosmológico de Einstein;
2. como dado físico do aparelho, por exemplo temperatura efetiva da armadilha,
   detector, cavidade ou anel de armazenamento.

Em ambos os casos, a temperatura não é novo termo fundamental. Ela deforma a
sela ou o mapa de fonte:

$$
\delta_T\Phi_\ell
=
-H_{\ell,\rm phys}^{+}J_\ell^{(\beta)},
\qquad
\beta=(k_BT)^{-1}.
$$

Com essa deformação, a anomalia deve ser reavaliada por:

$$
a_\ell(T)
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}(T)^{+}m_{\perp,\ell}(T)\rangle
}{
\langle c_\ell,H_{C,\ell}(T)^{+}c_\ell\rangle
}.
$$

Isso define uma hipótese de melhoria metrológica bem controlada:

$$
\text{temperatura}
\to
J_\ell^{(\beta)}
\to
\delta_T\Phi_\ell
\to
\delta_T H_C,\delta_T m_\perp
\to
\delta_T a_\ell.
$$

A sela angular homogênea normalizada já foi testada e não produz correção
superior: \(\eta_\ell=0\). Portanto, qualquer correção fina universal deve vir
de uma sela 8D não homogênea, warped ou mista, ou de um dado térmico global
que modifique fisicamente essa sela. Correções de aparelho são permitidas,
mas são dependentes do experimento.

Conclusão conservadora:

$$
\boxed{
\text{Q43 está fechada como problema de princípio e de operador.}
}
$$

$$
\boxed{
\text{a temperatura é rota de refinamento metrológico, não reabertura da Q43.}
}
$$
