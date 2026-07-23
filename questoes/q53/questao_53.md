# Questão 53 — Neutrinos

## 1. Enunciado

A questão pede uma resposta para o setor de neutrinos da GDQ contendo:

- mecanismo de massa;
- unidades corretas;
- três massas;
- diferenças de massas quadradas;
- matriz PMNS;
- fase CP;
- hierarquia;
- efeito MSW;
- previsão independente.

O arquivo legado associado é:

```text
pt-br/Apêndice 7 - Espectro de Mésons e Oscilação Neutrina.md
```

Este documento consolida o que esse apêndice fornece, o que já está
compatível com a GDQ vigente e o que ainda não pode ser declarado como
previsão fechada.

---

## 2. Ponto de partida GDQ

Na GDQ, o neutrino não deve ser introduzido como campo fundamental externo,
nem como cópia direta do tratamento do Modelo Padrão.

O objeto correto é o setor neutro da Hessiana física da ação oficial. Em
termos operacionais, o canal de neutrino deve vir da cadeia:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_*^{\rm neutro}
\to
K_{\rm neutro}^{\rm phys}
\to
\ker Q
\to
D_{\nu}^{\rm tors}
\to
\{\lambda_i,\mathsf U_{\rm folha\text{-}modo}^{\rm GDQ}\}.
$$

Aqui:

- $\Phi_*^{\rm neutro}$ é o background admissível do setor leptônico neutro;
- $K_{\rm neutro}^{\rm phys}$ é a Hessiana física projetada;
- $\ker Q$ impõe carga elétrica nula;
- $D_{\nu}^{\rm tors}$ é o operador efetivo de propagação torsional/quiral;
- os autovalores fornecem as escalas inerciais espectrais neutras;
- os autovetores projetados nas folhas leptônicas fornecem a matriz de
  projeção folha--modo, observada externamente como PMNS.

O neutrino, portanto, é uma onda neutra de torção/fase, sem estômato
localizado. Essa identificação é consistente com o que já foi registrado no
setor de decaimento beta: o antineutrino fecha energia, momento e torção como
canal neutro propagante.

---

## 3. Acordo terminológico interno

Para evitar importar a ontologia do Modelo Padrão como se fosse fundamento,
este documento usa primeiro a terminologia da GDQ.

| Termo operacional usual | Termo GDQ usado aqui | Significado |
|---|---|---|
| neutrino de sabor | canal neutro de folha leptônica | projeção do modo neutro torsional na folha $e,\mu,\tau$ |
| estado de massa | modo próprio inercial neutro | autovetor do operador torsional neutro projetado |
| massa do neutrino | escala inercial espectral neutra | autovalor normalizado do setor neutro da Hessiana |
| mistura PMNS | matriz de projeção folha--modo | overlaps entre canais de folha e modos próprios neutros |
| fase CP | holonomia orientada neutra | fase de Bismut acumulada em ciclos de transição entre folhas |
| efeito MSW | refração torsional por meio | deformação do operador neutro por fonte clássica de matéria |

Assim, quando o texto mencionar PMNS, MSW ou massa de neutrino, esses termos
devem ser lidos como nomes operacionais externos para estruturas internas da
GDQ:

$$
\text{folhas leptônicas}
\leftrightarrow
\text{modos próprios neutros}.
$$

O objetivo da Q53 não é postular uma matriz de mistura, mas calcular a matriz
de projeção:

$$
\mathsf U_{\alpha i}^{\rm GDQ}
=
\langle
\Psi_\alpha^{\rm folha},
\Psi_i^{\rm neutro}
\rangle_{\mathcal U}.
$$

Na redução fenomenológica, essa matriz é o objeto medido como matriz PMNS.

---

## 4. Bloco já fechado pelo nêutron

Antes de construir o setor completo de oscilação, é importante registrar que a
GDQ já identificou o canal neutro no estudo do nêutron.

Arquivos consolidados usados:

- `questoes/q50/questao_50.md`;
- `questoes/q50/associados/decaimento_beta_livre_gdq.md`;
- `topicos/neutron_decaimento/fechamento_meia_vida_neutron_gdq.md`;
- `topicos/neutron_decaimento/taxa_decaimento_neutron_overlap_gdq.md`;
- `topicos/neutron_decaimento/fechamento_terceiros_jatos_neutron_gdq.md`;
- `topicos/neutron_decaimento/ward_noether_cirurgia_neutron.md`;
- `topicos/neutron_decaimento/fechamento_condicional_mecanismo_neutron.md`;
- `topicos/neutron_decaimento/mecanismo_neutron_decaimento.md`;
- `questoes/q40/questao_40.md`;
- `questoes/q40/associados/adendo_neutron_deltaB.md`;
- `questoes/q40/associados/perfil_torcional_neutron.md`.

No decaimento beta livre,

$$
n\to p+e^-+\bar\nu_e,
$$

o elétron ocupa o canal carregado localizado:

$$
m=-1,
\qquad
j=\frac12,
$$

enquanto o antineutrino ocupa o kernel neutro:

$$
\boxed{
\psi_{\bar\nu}
\in
\ker D_{0,-3/2}^{(0)}.
}
$$

No operador tangencial usado nesse fechamento,

$$
D_{m,-3/2}^{(j)}
=
\frac1r
\left(
2\boldsymbol\sigma\cdot\mathbf L
-
m\sigma_3
\right),
$$

o bloco do antineutrino é neutro, propagante e sem estômato localizado. Assim,
a identificação ontológica do neutrino não é uma falta da Q53. Ela já foi
estabelecida no setor do nêutron.

As conservações no cobordismo são:

$$
M_nc^2-M_pc^2
=
E_e+E_{\bar\nu}+E_{\rm recoil},
$$

$$
Q_T^{(n)}
=
Q_T^{(p)}
+Q_T^{(e)}
+Q_T^{(\bar\nu)}.
$$

No limite de recuo desprezível:

$$
E_{\bar\nu}
=
\Delta M-E_e.
$$

O fator contínuo do espectro beta é:

$$
I_\beta
=
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2dE_e,
\qquad
p_e=\sqrt{E_e^2-m_e^2}.
$$

Esse fator foi avaliado como:

$$
I_\beta
=
5.700456936530352\times10^{-17}\ {\rm GeV}^5.
$$

A taxa total do nêutron foi fechada pela lei GDQ de relaxamento:

$$
\tau_n
=
\frac{32}{15}
\alpha^{-11}
\frac{\hbar}{m_ec^2}
=
879.398775004012\ {\rm s}.
$$

Portanto, o bloco já demonstrado é:

$$
\boxed{
\bar\nu_e
=
\text{modo neutro torsional/fase do canal beta}.
}
$$

O que a Q53 precisa construir a mais não é a existência do neutrino, mas a sua
extensão global de oscilação.

---

## 5. Construção iniciada: do canal beta ao operador global de oscilação

O ponto de partida natural para a Q53 é promover o modo neutro local do
decaimento beta para uma família de três transportes sobre as folhas
leptônicas:

$$
\psi_{\bar\nu}^{(e)}
\in
\ker D_{0,-3/2}^{(0)}.
$$

As demais componentes de folha não devem ser postuladas como partículas novas;
devem ser obtidas por transporte geométrico do mesmo canal neutro através das
folhas/canais de geração:

$$
\psi_{\nu}^{(\alpha)}
=
\mathcal P_{\alpha e}\psi_{\bar\nu}^{(e)},
\qquad
\alpha=e,\mu,\tau.
$$

Aqui $\mathcal P_{\alpha e}$ é o transporte GDQ no fibrado neutro entre folhas
de geração. Ele deve ser induzido pela conexão de Bismut projetada:

$$
\mathcal P_{\alpha e}
=
\operatorname{Pexp}
\left(
-\int_{\mathcal C_{\alpha e}}
\nabla^B_{\rm neutro}
\right).
$$

Com isso, o espaço de folhas neutras é:

$$
\mathcal H_{\nu}^{\rm folha}
=
\operatorname{span}
\{
\psi_\nu^{(e)},
\psi_\nu^{(\mu)},
\psi_\nu^{(\tau)}
\}.
$$

O operador global de oscilação deve então ser escrito como:

$$
D_\nu^{\rm tors}
=
D_{\beta,0}
+\mathcal T_{\rm folhas},
$$

onde:

- $D_{\beta,0}$ é o bloco neutro herdado do decaimento beta;
- $\mathcal T_{\rm folhas}$ é o acoplamento torsional entre folhas de geração;
- ambos devem vir da Hessiana física da ação oficial, não de uma matriz de
  massa inserida manualmente.

Em forma projetada:

$$
D_\nu^{\rm tors}
=
P_{\mathcal H_\nu^{\rm folha}}
K_{\rm neutro}^{\rm phys}
P_{\mathcal H_\nu^{\rm folha}}.
$$

O problema espectral fica:

$$
D_\nu^{\rm tors}\psi_i
=
\lambda_i\psi_i,
\qquad
i=1,2,3.
$$

As escalas inerciais espectrais físicas exigem a normalização:

$$
m_i^2c^4
=
Z_\nu E_C^2\lambda_i.
$$

A matriz de projeção folha--modo da GDQ passa a ser:

$$
\mathsf U_{\alpha i}^{\rm GDQ}
=
\langle
\psi_\nu^{(\alpha)},
\psi_i
\rangle_{\mathcal U}.
$$

Na linguagem operacional de oscilação:

$$
U_{\rm PMNS}
=
\mathsf U^{\rm GDQ}
\quad
\text{na redução assintótica de laboratório}.
$$

E a fase CP é a holonomia orientada dos ciclos de geração:

$$
\delta_{\rm CP}
=
\arg
\operatorname{Hol}_{\mathcal C}
(\nabla^B_{\rm neutro}).
$$

Essa seção inicia a construção correta: o neutrino local já está identificado
pelo nêutron; a oscilação é o problema global de transporte, overlap e
diagonalização desse setor neutro.

---

## 6. Mecanismo de escala inercial neutra

O apêndice legado propõe uma massa efetiva associada à curvatura global:

$$
m_\nu
\approx
\frac{\hbar^2\mathcal R_g}{2\mu\,d_{\rm universo}^2}.
$$

Essa expressão captura uma intuição correta: o neutrino é muito leve porque
seu modo não fica preso a um núcleo estomatal local; ele sente uma escala
global muito maior que a escala de partículas carregadas.

Mas, na forma escrita, ela não é ainda uma derivação fechada da ação oficial.
O problema é que a expressão mistura uma escala global, uma massa reduzida
$\mu$ e um comprimento cosmológico sem demonstrar o operador, o domínio, a
normalização e as unidades restauradas.

A formulação correta pela GDQ deve ser escrita como problema espectral neutro:

$$
D_{\nu}^{\rm tors}\psi_i
=
\lambda_i\psi_i,
$$

com

$$
D_{\nu}^{\rm tors}
=
P_{\ker Q,\chi_L}\,
K_{\rm neutro}^{\rm phys}\,
P_{\ker Q,\chi_L}.
$$

O projetor $P_{\ker Q,\chi_L}$ seleciona simultaneamente:

1. carga elétrica nula;
2. canal quiral físico;
3. ausência de estômato localizado;
4. propagação torsional coerente.

Assim, a massa de neutrino é um autovalor pequeno do operador neutro projetado,
após restauração de unidades. Em terminologia GDQ, ela é uma escala inercial
espectral neutra, não um parâmetro de Higgs inserido manualmente.

---

## 7. Unidades corretas

O operador que governa oscilação deve fornecer diferenças de massa ao quadrado:

$$
\Delta m_{ij}^2=m_i^2-m_j^2.
$$

Em unidades físicas, essas quantidades são medidas em ${\rm eV}^2$. Na GDQ,
isso exige uma restauração clara:

$$
m_i^2c^4
=
Z_\nu E_C^2\,\lambda_i,
$$

onde:

- $\lambda_i$ é autovalor adimensional do operador geométrico projetado;
- $E_C$ é a escala física de Cartan usada na restauração de unidades;
- $Z_\nu$ é a normalização do canal neutro obtida por fluxo global--local;
- $m_i$ é a massa física do modo.

Sem calcular $Z_\nu$ pela Hessiana e pelo transporte global--local, qualquer
valor absoluto de massa deve ser classificado como reconstrução experimental
ou comparação fenomenológica.

---

## 8. Três escalas inerciais e hierarquia

O apêndice legado fala em três folhas associadas a $e,\mu,\tau$. Isso é
compatível com a estrutura já trabalhada nas questões de gerações e hierarquia:
as três gerações fornecem três canais de projeção para o setor leptônico.

O fechamento formal em terminologia GDQ é:

$$
D_{\nu}^{\rm tors}\psi_i=\lambda_i\psi_i,
\qquad i=1,2,3.
$$

Depois da normalização $Z_\nu E_C^2$, esses três autovalores geram as três
escalas inerciais observadas como massas. Se o operador neutro tiver espectro
simples e ordenado, a hierarquia normal é:

$$
m_1<m_2<m_3.
$$

A hierarquia invertida corresponderia a outro ramo espectral:

$$
m_3<m_1<m_2.
$$

Dados atuais de oscilação ainda não eliminam completamente a ambiguidade de
ordenação; portanto a GDQ só pode declarar uma hierarquia como previsão
quando o sinal do ramo espectral for obtido sem usar o alvo experimental.

Como auditoria numérica, usando as diferenças quadradas observacionais NuFIT
6.0 e $m_1=0$ apenas como reconstrução mínima normal, obtemos:

$$
m_1=0,
\qquad
m_2=8.654478609368\times10^{-3}\ {\rm eV},
\qquad
m_3=5.033885179461\times10^{-2}\ {\rm eV}.
$$

Essa conta está em:

```text
questoes/q53/associados/saida_auditoria_neutrinos_q53.md
```

Ela não é previsão GDQ; é referência observacional mínima.

---

## 9. Diferenças de escalas inerciais quadradas

O que deve ser previsto pela GDQ é a diferença entre escalas inerciais
espectrais neutras. Na linguagem operacional, essas diferenças são medidas
como diferenças de massas quadradas:

$$
\Delta m_{21}^2
=
Z_\nu E_C^2(\lambda_2-\lambda_1),
$$

$$
\Delta m_{31}^2
=
Z_\nu E_C^2(\lambda_3-\lambda_1).
$$

O apêndice legado não calcula esses autovalores diretamente. Ele descreve o
mecanismo geométrico, mas não diagonaliza o operador neutro físico.

Portanto:

$$
\boxed{
\text{as diferenças quadradas ainda não estão previstas diretamente pela GDQ.}
}
$$

Elas ficam como alvo do fechamento metrológico do setor neutro.

---

## 10. Matriz de projeção neutra, ou PMNS operacional

A matriz física interna deve surgir como matriz de overlaps entre canais
neutros de folha e modos próprios inerciais neutros:

$$
\mathsf U_{\alpha i}^{\rm GDQ}
=
\langle
\Psi_\alpha^{\rm folha},
\Psi_i^{\rm neutro}
\rangle_{\mathcal U},
\qquad
\alpha=e,\mu,\tau.
$$

Na redução de laboratório:

$$
U_{\rm PMNS}
=
\mathsf U^{\rm GDQ}.
$$

O produto interno correto é ponderado pela medida GDQ:

$$
\langle a,b\rangle_{\mathcal U}
=
\int_M \bar a\,b\,\mathcal U\,dV_g.
$$

O apêndice legado propõe expressões geométricas cruas:

$$
\theta_{12}
=
\arctan\left(\frac1{\sqrt2}\right)
=
35.264389683^\circ,
$$

$$
\theta_{23}
=
45^\circ,
$$

$$
\theta_{13}
=
\arcsin\left(\frac{0.48e^{-\alpha/4}}{\pi}\right)
=
8.772427998^\circ.
$$

Comparadas a NuFIT 6.0, essas expressões ficam próximas, mas não fecham a
metrologia:

| parâmetro | GDQ cru legado | NuFIT 6.0 NO | diferença |
|---|---:|---:|---:|
| $\theta_{12}$ | $35.264389683^\circ$ | $33.680000000^\circ$ | $+1.584389683^\circ$ |
| $\theta_{23}$ | $45.000000000^\circ$ | $48.500000000^\circ$ | $-3.500000000^\circ$ |
| $\theta_{13}$ | $8.772427998^\circ$ | $8.520000000^\circ$ | $+0.252427998^\circ$ |

Classificação: comparação fenomenológica promissora, não previsão fechada.

---

## 11. Tabela comparativa atual

Esta tabela resume os valores disponíveis no estado atual da Q53. A coluna GDQ
crua vem das expressões geométricas legadas; a coluna observacional usa NuFIT
6.0 apenas como referência externa de comparação.

| Quantidade        |   Valor GDQ cru/legado |                    Referência NuFIT 6.0 |             Diferença | Classificação             |
| ----------------- | ---------------------: | --------------------------------------: | --------------------: | ------------------------- |
| $\theta_{12}$     |   $35.264389683^\circ$ |                    $33.680000000^\circ$ |  $+1.584389683^\circ$ | comparação fenomenológica |
| $\theta_{23}$     |   $45.000000000^\circ$ |                    $48.500000000^\circ$ |  $-3.500000000^\circ$ | comparação fenomenológica |
| $\theta_{13}$     |    $8.772427998^\circ$ |                     $8.520000000^\circ$ |  $+0.252427998^\circ$ | comparação fenomenológica |
| $\delta_{\rm CP}$ |  $220.015793330^\circ$ |                   $177.000000000^\circ$ | $+43.015793330^\circ$ | proposta/entrada legada   |
| $\Delta m_{21}^2$ | não calculado pela GDQ |         $7.49\times10^{-5}\ {\rm eV}^2$ |                     — | pendente                  |
| $\Delta m_{31}^2$ | não calculado pela GDQ |        $2.534\times10^{-3}\ {\rm eV}^2$ |                     — | pendente                  |
| $m_1$ mínimo NO   | não calculado pela GDQ |                                     $0$ |                     — | reconstrução experimental |
| $m_2$ mínimo NO   | não calculado pela GDQ | $8.654478609368\times10^{-3}\ {\rm eV}$ |                     — | reconstrução experimental |
| $m_3$ mínimo NO   | não calculado pela GDQ | $5.033885179461\times10^{-2}\ {\rm eV}$ |                     — | reconstrução experimental |

A matriz de probabilidades associada às expressões geométricas cruas é:

$$
|\mathsf U_{\rm GDQ}^{\rm cru}|^2
=
\begin{pmatrix}
0.651160413 & 0.325580207 & 0.023259380\\
0.119358514 & 0.392271176 & 0.488370310\\
0.229481072 & 0.282148617 & 0.488370310
\end{pmatrix}.
$$

A matriz observacional de referência usada na auditoria é:

$$
|U_{\rm NuFIT}|^2
=
\begin{pmatrix}
0.677270303 & 0.300779901 & 0.021949796\\
0.075785348 & 0.375592381 & 0.548622270\\
0.246944348 & 0.323627718 & 0.429427934
\end{pmatrix}.
$$

Leitura correta:

$$
\boxed{
\text{ângulos crus próximos; escala inercial neutra e holonomia CP ainda não derivadas.}
}
$$

---

## 12. Holonomia orientada neutra, ou fase CP operacional

O código legado usa:

$$
\delta_{\rm CP}=3.84\ {\rm rad}
=220.015793330^\circ.
$$

Isso não está derivado no apêndice. A forma correta de obter a fase CP na GDQ
é pela holonomia da conexão efetiva no fibrado neutro:

$$
\delta_{\rm CP}
=
\arg
\operatorname{Hol}_{\mathcal C}
(\nabla^{B}_{\rm neutro}),
$$

onde $\nabla^B_{\rm neutro}$ é a conexão de Bismut projetada no setor neutro
e $\mathcal C$ é o ciclo físico de transição entre folhas de geração.

Enquanto esse ciclo e sua holonomia não forem calculados diretamente:

$$
\boxed{
\delta_{\rm CP}
\text{ permanece proposta geométrica, não previsão.}
}
$$

---

## 13. Refração torsional por meio, ou MSW operacional

O efeito MSW não deve ser importado como postulado do Modelo Padrão. Na GDQ, a
matéria do meio entra como fonte clássica/aparelho/contorno que deforma o
background:

$$
J_{\rm meio}^{\rm clássico}
\to
\delta\Phi_{\rm meio}
\to
K_{\rm neutro}^{\rm phys}
\to
\delta D_{\nu}^{\rm tors}.
$$

Na redução efetiva de baixa energia, essa deformação deve assumir a forma de
um potencial de refração:

$$
H_{\rm eff}^{\rm matéria}
=
\frac{1}{2E}
U
\operatorname{diag}(m_1^2,m_2^2,m_3^2)
U^\dagger
+V_{\rm GDQ}(n_e).
$$

O limite conhecido é:

$$
V_{\rm GDQ}(n_e)
\longrightarrow
\operatorname{diag}(\sqrt2G_Fn_e,0,0).
$$

Na GDQ, porém, $G_F$ e o potencial devem ser lidos como constantes efetivas da
ponte global--local e da impedância fraca de contorno, não como acoplamentos
fundamentais independentes.

Assim, o MSW está fechado estruturalmente como refração geométrica por fonte
de matéria, mas sua previsão metrológica exige calcular o bloco de Schur do
meio:

$$
\mathsf R_{\rm meio}
=
K_{YY}^{\rm meio}
-K_{YI}^{\rm meio}(K_{II}^{\rm meio})^{-1}K_{IY}^{\rm meio}.
$$

---

## 14. Previsão independente

O setor de neutrinos ainda não possui previsão independente completa.

O que existe:

1. identificação estrutural do neutrino como onda neutra torsional;
2. mecanismo de oscilação como overlap entre folhas leptônicas e modos
   próprios neutros;
3. fórmulas geométricas cruas para a matriz operacional PMNS próximas dos
   dados;
4. rota GDQ para MSW como refração torsional por fonte clássica de matéria;
5. compatibilidade com o papel do antineutrino no decaimento beta.

O que falta para previsão independente:

1. construir $\Phi_*^{\rm neutro}$;
2. calcular $K_{\rm neutro}^{\rm phys}$;
3. diagonalizar $D_\nu^{\rm tors}$;
4. obter $Z_\nu$ por fluxo global--local;
5. calcular $\Delta m_{21}^2$ e $\Delta m_{31}^2$ sem dados de oscilação;
6. calcular $\delta_{\rm CP}$ como holonomia de Bismut;
7. calcular $V_{\rm GDQ}(n_e)$ para MSW sem inserir $G_F$ como entrada.

---

## 15. Construção GDQ mínima a executar

O próximo cálculo deve evitar começar por uma matriz PMNS. A matriz aparece
apenas no fim. A construção interna é:

$$
\text{canal beta neutro}
\to
\text{três folhas leptônicas}
\to
\text{Gram GDQ}
\to
\text{operador torsional neutro}
\to
\text{modos próprios}
\to
\text{matriz operacional}.
$$

### 15.1 Base de folhas neutras

Partimos do modo já obtido no nêutron:

$$
\Psi_e^{\rm folha}
=
\psi_{\bar\nu}^{(e)}
\in
\ker D_{0,-3/2}^{(0)}.
$$

As demais folhas são transportes de Bismut:

$$
\Psi_\mu^{\rm folha}
=
\mathcal P_{\mu e}\Psi_e^{\rm folha},
\qquad
\Psi_\tau^{\rm folha}
=
\mathcal P_{\tau e}\Psi_e^{\rm folha}.
$$

O primeiro objeto a calcular é o Gram ponderado:

$$
G_{\alpha\beta}^{\nu}
=
\langle
\Psi_\alpha^{\rm folha},
\Psi_\beta^{\rm folha}
\rangle_{\mathcal U}.
$$

Se a base de folhas não for ortonormal, a diagonalização correta é
generalizada, não ordinária.

### 15.2 Operador de colagem torsional entre folhas

O acoplamento entre folhas deve ser extraído da Hessiana neutra:

$$
K_{\alpha\beta}^{\nu}
=
\langle
\Psi_\alpha^{\rm folha},
K_{\rm neutro}^{\rm phys}
\Psi_\beta^{\rm folha}
\rangle_{\mathcal U}.
$$

Esse bloco é a versão GDQ do que, operacionalmente, aparece como matriz de
oscilação. Ele contém:

- termos diagonais de inércia neutra de cada folha;
- termos fora da diagonal de colagem torsional;
- fases orientadas acumuladas por transporte de Bismut.

O problema espectral correto é:

$$
K^\nu c_i
=
\lambda_i G^\nu c_i.
$$

Os modos próprios neutros são:

$$
\Psi_i^{\rm neutro}
=
\sum_{\alpha=e,\mu,\tau}
c_i^\alpha\Psi_\alpha^{\rm folha}.
$$

### 15.3 Tradução para observáveis de oscilação

Depois da diagonalização:

$$
\Delta m_{ij}^2
=
Z_\nu E_C^2(\lambda_i-\lambda_j),
$$

e:

$$
\mathsf U_{\alpha i}^{\rm GDQ}
=
\frac{
\langle
\Psi_\alpha^{\rm folha},
\Psi_i^{\rm neutro}
\rangle_{\mathcal U}
}{
\sqrt{
\langle\Psi_\alpha^{\rm folha},\Psi_\alpha^{\rm folha}\rangle_{\mathcal U}
\langle\Psi_i^{\rm neutro},\Psi_i^{\rm neutro}\rangle_{\mathcal U}
}
}.
$$

Somente nessa etapa se traduz:

$$
\mathsf U^{\rm GDQ}
\mapsto
U_{\rm PMNS}.
$$

### 15.4 Refração em meio

Para matéria, não se adiciona um potencial MSW como axioma. O meio altera a
impedância do canal neutro:

$$
J_{\rm meio}^{\rm clássico}
\to
\delta\Phi_{\rm meio}
\to
\Delta K_\nu^{\rm meio}.
$$

No bloco de folhas:

$$
\Delta K_{\alpha\beta}^{\nu,{\rm meio}}
=
\langle
\Psi_\alpha^{\rm folha},
\Delta K_\nu^{\rm meio}
\Psi_\beta^{\rm folha}
\rangle_{\mathcal U}.
$$

O limite operacional MSW é recuperado quando esse bloco se reduz a uma
correção dominante na folha eletrônica. Em linguagem GDQ:

$$
\text{refração por matéria}
=
\text{mudança de impedância torsional da folha eletrônica}.
$$

O plano operacional detalhado para obter as escalas inerciais neutras está em:

```text
questoes/q53/associados/plano_obter_massas_neutras_q53.md
```

Uma primeira execução reduzida/candidata foi realizada em:

```text
questoes/q53/associados/executar_massas_neutras_q53.py
```

com saída em:

```text
questoes/q53/associados/saida_execucao_massas_neutras_q53.md
```

Essa execução usou a escala beta neutra:

$$
S_\nu
=
\alpha^7Q_\beta^2
=
6.744367477916\times10^{-4}\ {\rm eV}^2,
$$

e o espectro reduzido candidato:

$$
\lambda
=
\left(
0,
\frac{\chi_\nu^2}{2},
\frac{6\pi}{5}
\right),
\qquad
\chi_\nu=0.48e^{-\alpha/4}.
$$

Resultado:

| quantidade | GDQ reduzido candidato | NuFIT 6.0 NO | erro relativo |
|---|---:|---:|---:|
| $\Delta m_{21}^2$ | $7.741214557111\times10^{-5}\ {\rm eV}^2$ | $7.49\times10^{-5}\ {\rm eV}^2$ | $+3.353999\%$ |
| $\Delta m_{31}^2$ | $2.542566638608\times10^{-3}\ {\rm eV}^2$ | $2.534\times10^{-3}\ {\rm eV}^2$ | $+0.338068\%$ |

As escalas inerciais reduzidas resultantes, para ramo normal com
$\lambda_1=0$, são:

$$
m_1=0,
$$

$$
m_2=8.798417219655\times10^{-3}\ {\rm eV},
$$

$$
m_3=5.042386973059\times10^{-2}\ {\rm eV}.
$$

Leitura correta:

$$
\boxed{
\text{resultado numérico forte como candidato reduzido; ainda condicional como previsão.}
}
$$

O ponto pendente é derivar diretamente da Hessiana neutra oficial os dois
números geométricos:

$$
\frac{\chi_\nu^2}{2},
\qquad
\frac{6\pi}{5}.
$$

A derivação reduzida condicional desses coeficientes foi registrada em:

```text
questoes/q53/associados/derivacao_condicional_coeficientes_neutros_q53.md
```

Ela propõe:

$$
S_\nu=\alpha^7Q_\beta^2,
$$

como escala de vazamento torsional neutro do canal beta através de sete filtros
de fluxo, e:

$$
\chi_\nu=\frac{12}{25}e^{-\alpha/4},
$$

como impedância bicanal reduzida entre folhas neutras. O modo superior é lido
como circulação neutra das três folhas sobre os cinco ciclos axiais do espaço
cosmológico de Einstein:

$$
\lambda_3=3\frac{2\pi}{5}=\frac{6\pi}{5}.
$$

Foi executado também um teste de sensibilidade em:

```text
questoes/q53/associados/testar_sensibilidade_coeficientes_q53.py
```

com saída em:

```text
questoes/q53/associados/saida_sensibilidade_coeficientes_q53.md
```

Resumo dos coeficientes:

| coeficiente | requerido pela comparação NuFIT | GDQ reduzido | erro relativo |
|---|---:|---:|---:|
| $\lambda_2$ | $1.110556330824\times10^{-1}$ | $1.147804383800\times10^{-1}$ | $+3.353999\%$ |
| $\chi_\nu$ | $4.712868194260\times10^{-1}$ | $4.791251159771\times10^{-1}$ | — |
| $\lambda_3/(2\pi)$ | $5.979784273551\times10^{-1}$ | $6.000000000000\times10^{-1}$ | — |
| $\lambda_3$ | $3.757209268768$ | $3.769911184308$ | $+0.338068\%$ |

Leitura conservadora: o modo superior está quase inteiramente explicado pela
estrutura $3/5$ do transporte global; o gargalo quantitativo principal está no
bloco bicanal de interface que determina $\lambda_2$.

Enquanto isso não for feito, a execução não deve ser chamada de fechamento
metrológico final.

O refinamento metrológico correspondente foi separado em:

```text
questoes/q53/associados/refinamento_metrologico_hessiana_neutra_q53.md
```

Esse refinamento não reabre a Q53 estrutural. Ele define a etapa futura para
elevar o candidato reduzido a previsão metrológica direta pela Hessiana neutra
8D.

---

## 16. Veredito

A Questão 53 fica classificada como:

$$
\boxed{
\text{fechada estruturalmente; candidato reduzido forte; metrologia final em refinamento.}
}
$$

A ontologia GDQ está clara: neutrinos são modos neutros de torção/fase, não
sólitons carregados com estômato. A oscilação é uma interferência/propagação
entre canais de geração. O MSW é uma refração geométrica por fonte clássica de
matéria.

As escalas inerciais reduzidas já formam um candidato quantitativo forte. O
fechamento metrológico máximo — fase CP operacional, potencial de meio e
derivação direta dos coeficientes espectrais — exige a Hessiana neutra oficial.
Portanto não é correto declarar a Q53 como fechada no sentido preditivo forte,
mas é correto tratá-la como fechada estruturalmente.

---

## 17. Fontes externas usadas para comparação

- NuFIT 6.0: Esteban, González-García, Maltoni, Martinez-Soler, Pinheiro e
  Schwetz, “NuFit-6.0: updated global analysis of three-flavor neutrino
  oscillations”, JHEP 12 (2024) 216.
  <https://link.springer.com/article/10.1007/JHEP12(2024)216>

Essa fonte foi usada apenas para referência experimental de comparação, não
como premissa da GDQ.
