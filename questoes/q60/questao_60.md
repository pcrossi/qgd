# Questão 60 — Raio do próton

## 1. Enunciado

A questão pede corrigir a fórmula legada:

$$
0{,}8778\times0{,}07479\times10^{-3}\times3{,}7915
\approx
0{,}000249\,{\rm fm},
$$

não \(0{,}0369\,{\rm fm}\).

Arquivos relacionados:

1. `pt-br/35 - Anomalias Leptônicas e Estrutura Hadrônica Fina.md`;
2. `pt-br/notas/27/nota_27.4_raio_do_proton.md`;
3. `pt-br/38 - A Geometria do Atomo de Hidrogenio.md`;
4. `pt-br/27 -  O Confinamento.md`;
5. `questoes/q40/questao_40.md`;
6. `questoes/q48/associados/raio_proton_hidrogenio_muonico.md`.

---

## 2. Veredito

$$
\boxed{
\text{Q60 fechada estruturalmente como correção do raio do próton.}
}
$$

A fórmula multiplicativa do texto legado não pode ser usada para explicar a
diferença entre \(0{,}8778\,{\rm fm}\) e \(0{,}8409\,{\rm fm}\). Ela erra por
um fator numérico de aproximadamente \(148\).

O raio vigente da GDQ é o raio canônico de superfície derivado na Q40:

$$
\boxed{
r_p
=
C_r\epsilon_{\rm eff}R_B,
\qquad
C_r=
\frac18\left(1+\frac{\alpha}{4}\right),
\qquad
R_B=\frac32\Lambda_C.
}
$$

Com os valores consolidados:

$$
\epsilon_{\rm eff}=0{,}011591040463,
\qquad
\Lambda_C=386{,}159268\,{\rm fm},
$$

obtém-se:

$$
\boxed{
r_p^{\rm GDQ}
=
0{,}840778765432\,{\rm fm}.
}
$$

---

## 3. Correção aritmética

O script:

```text
questoes/q60/associados/calcular_raio_proton_q60.py
```

produziu:

```text
0.8778 * 0.07479 * 1e-3 * 3.7915 = 0.000248914485 fm
```

Logo:

$$
\boxed{
\Delta r_{\rm legado}
=
2{,}48914485\times10^{-4}\,{\rm fm}.
}
$$

O texto antigo afirmava:

$$
\Delta r_{\rm antigo}=0{,}0369\,{\rm fm}.
$$

A razão é:

$$
\frac{0{,}0369}{0{,}000248914485}
\approx
148{,}24.
$$

Portanto, a passagem antiga está descartada como derivação quantitativa.

---

## 4. O que fica aproveitável do legado

O legado contém uma ideia física válida:

$$
\text{o raio efetivo medido pode depender da sonda.}
$$

Isso é compatível com a GDQ porque o próton não é tratado como esfera rígida.
Ele é um sóliton bariônico de superfície/estômato, e a medição é uma
interação de contorno.

O que não fica aproveitável é a fórmula:

$$
\Delta r_p
=
r_p^{(e)}
\left(
\frac{\chi_{\rm Fano,n}}{\delta^2}10^{-3}
\right)
\left(
\frac{m_\mu}{m_e}
\right)^{1/4},
$$

pois ela:

1. não segue diretamente da ação oficial;
2. mistura fatores de contorno sem Hessiana explícita;
3. produz numericamente \(0{,}000249\,{\rm fm}\), não \(0{,}0369\,{\rm fm}\);
4. usa \(r_p^{(e)}\) como entrada experimental.

---

## 5. Rota correta na GDQ

A cadeia correta é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{p,*}
\to
H_p^{\rm surf}
\to
F_p(q^2)
\to
r_p^2
\to
\text{observável atômico ou de espalhamento}.
$$

O raio de carga aparece no fator de forma:

$$
F_p(q^2)
=
1-\frac{q^2r_p^2}{6}
+O(q^4).
$$

No hidrogênio, a correção de tamanho finito para estados \(ns\) é:

$$
\Delta E_{\rm fs}(ns)
=
\frac{2\pi}{3}
Z\alpha\hbar c\,r_p^2
|\psi_{ns}(0)|^2.
$$

Como:

$$
|\psi_{ns}(0)|^2
=
\frac{(Z\alpha\mu c/\hbar)^3}{\pi n^3},
$$

segue:

$$
\Delta E_{\rm fs}(ns)
\propto
\mu^3r_p^2.
$$

Isso explica por que o hidrogênio muônico é muito mais sensível ao raio do
próton do que o hidrogênio eletrônico.

---

## 6. Raio livre, raio de superfície e raio efetivo

Na GDQ devem ser separados três objetos:

| Objeto | Significado | Status |
| --- | --- | --- |
| \(r_p^{\rm surf}\) | raio canônico de superfície do estômato bariônico | derivado na Q40 |
| \(r_p^{\rm eff}({\rm sonda})\) | raio medido sob interação com uma sonda concreta | condicional à Hessiana de superfície e ao contorno |
| \(r_p^{\rm vol}\) | média volumétrica de modos internos do bulk | não é o raio eletromagnético observado |

O valor vigente para o raio canônico é:

$$
\boxed{
r_p^{\rm surf}=0{,}840778765432\,{\rm fm}.
}
$$

O modelo volumétrico antigo fica reclassificado como estudo de modo interno,
não como predição do raio de carga.

---

## 7. Dependência por sonda

A dependência por sonda deve ser escrita como resposta linear do background:

$$
r_p^{\rm eff}[\ell]
=
r_p^{\rm surf}
+\delta r_p[\ell],
$$

com:

$$
\delta r_p[\ell]
=
-
\left(H_p^{\rm surf}\right)^{-1}J_{p,\ell}.
$$

Aqui:

- \(H_p^{\rm surf}\) é a Hessiana física de superfície do próton;
- \(J_{p,\ell}\) é a fonte gerada pela sonda leptônica;
- o elétron produz fonte pequena;
- o múon produz fonte muito maior por contato.

Para estados \(s\), a razão das fontes é:

$$
\frac{\delta r_p[e]}{\delta r_p[\mu]}
=
\left(
\frac{\mu_{ep}}{\mu_{\mu p}}
\right)^3
=
1{,}555489846615637\times10^{-7}.
$$

Portanto, se houver uma retroação muônica na escala de \(10^{-2}\,{\rm fm}\),
a retroação eletrônica correspondente fica na escala de \(10^{-9}\,{\rm fm}\).

Isso preserva a lógica física do legado sem usar a fórmula aritmeticamente
errada.

---

## 8. Comparação

Usando o valor canônico:

$$
r_p^{\rm GDQ}=0{,}840778765432\,{\rm fm}.
$$

Comparações internas:

| Referência | Diferença |
| --- | ---: |
| \(0{,}84087\,{\rm fm}\) | \(-0{,}000091234568\,{\rm fm}\) |
| \(0{,}8778\,{\rm fm}\) | \(-0{,}037021234568\,{\rm fm}\) |
| \(0{,}8354\,{\rm fm}\) | \(+0{,}005378765432\,{\rm fm}\) |

Interpretação:

1. o valor GDQ canônico fica muito próximo da escala muônica;
2. a diferença para \(0{,}8778\,{\rm fm}\) não deve ser forçada pela fórmula
   antiga;
3. a diferença entre experimentos deve ser tratada por contorno, fator de forma
   e resposta bidirecional próton--sonda.

---

## 9. O que falta para metrologia completa

Não falta para fechar a Q60 estruturalmente.

Falta apenas para transformar a resposta estrutural em previsão metrológica
completa do puzzle. O procedimento correto é:

### 9.1 Construir o background protônico congelado

Usar o background bariônico da Q40:

$$
\Phi_{p,*}
=
(g_{p,*},f_{p,*},H_{p,*}),
$$

com raio de superfície:

$$
r_p^{\rm surf}
=
0{,}840778765432\,{\rm fm}.
$$

Esse é o objeto não perturbado. Ele não deve ser recalibrado por espectroscopia.

### 9.2 Calcular a Hessiana física de superfície

Avaliar diretamente:

$$
H_p^{\rm surf}
=
P_{\rm surf}^{\rm phys}
\operatorname{Hess}_{\Phi_{p,*}}
\mathcal S_{\rm GDQ}
P_{\rm surf}^{\rm phys}.
$$

O projetor remove:

1. modos de gauge;
2. rotação global;
3. mudança de carga total;
4. modo volumétrico que não altera o raio eletromagnético observado.

O canal relevante é o modo radial/superficial que desloca o fator de forma:

$$
F_p(q^2)
=
1-\frac{q^2r_p^2}{6}
+O(q^4).
$$

### 9.3 Calcular as fontes das sondas

Para cada sonda ligada \(\ell=e,\mu\), calcular:

$$
J_{p,\ell}
=
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}^{p+\ell}}
{\delta\Phi_p\,\delta\Phi_\ell}
\right|_{\Phi_{p,*},\Phi_{\ell,*}}.
$$

No limite atômico \(ns\), a parte de contato deve reproduzir a escala:

$$
J_{p,\ell}^{(s)}
\propto
|\psi_{ns}^{(\ell)}(0)|^2
\propto
\mu_{\ell p}^3.
$$

Por isso:

$$
\frac{J_{p,e}}{J_{p,\mu}}
=
\left(
\frac{\mu_{ep}}{\mu_{\mu p}}
\right)^3.
$$

Esse quociente já está fixado. O que falta é o coeficiente absoluto de
acoplamento, que deve sair de \(H_p^{\rm surf}\) e da fonte \(J_{p,\ell}\), não
do valor experimental do raio.

### 9.4 Obter o raio efetivo por resposta linear

Resolver:

$$
H_p^{\rm surf}\,\delta\Phi_p[\ell]
=
-J_{p,\ell}.
$$

Então extrair:

$$
\delta r_p[\ell]
=
\left\langle
\nabla_\Phi r_p,\,
\delta\Phi_p[\ell]
\right\rangle,
$$

ou, no canal reduzido:

$$
\delta r_p[\ell]
=
-
\left(H_p^{\rm surf}\right)^{-1}J_{p,\ell}.
$$

O raio usado no problema atômico passa a ser:

$$
r_p^{\rm eff}[\ell]
=
r_p^{\rm surf}
+\delta r_p[\ell].
$$

### 9.5 Inserir no operador atômico Q48

Com \(r_p^{\rm eff}[\ell]\) congelado, calcular o deslocamento de tamanho
finito:

$$
\Delta E_{\rm fs}^{(\ell)}(ns)
=
\frac{2\pi}{3}
Z\alpha\hbar c\,
\left(r_p^{\rm eff}[\ell]\right)^2
|\psi_{ns}^{(\ell)}(0)|^2.
$$

No caso muônico, a amplificação por \(\mu^3\) torna esse termo dominante na
extração espectroscópica do raio.

### 9.6 Comparação simultânea

O fechamento metrológico exige comparar, com os mesmos blocos
\(H_p^{\rm surf}\), \(J_{p,e}\) e \(J_{p,\mu}\):

1. espalhamento \(e-p\), via inclinação de \(F_p(q^2)\);
2. hidrogênio eletrônico, via Lamb shift e tamanho finito;
3. hidrogênio muônico, via Lamb shift muônico;
4. hiperfina, quando o raio de Zemach for incluído;
5. dependência de contorno/aparelho, se houver.

### 9.7 Critério de sucesso

A etapa metrológica só fica fechada se:

1. \(r_p^{\rm surf}\) permanecer o valor Q40;
2. nenhum raio experimental for usado para ajustar
   \(H_p^{\rm surf}\) ou \(J_{p,\ell}\);
3. \(r_p^{\rm eff}[e]\) e \(r_p^{\rm eff}[\mu]\) forem calculados antes da
   comparação;
4. a mesma Hessiana explicar fator de forma, Lamb shift e hidrogênio muônico;
5. os resíduos forem classificados como erro experimental, contorno/aparelho
   ou falta de bloco físico identificado.

Esses itens refinam a resposta, mas não reabilitam a fórmula legada errada.

---

## 10. Fechamento

A conclusão adequada é:

$$
\boxed{
\text{a fórmula legada de contração está descartada quantitativamente.}
}
$$

O raio GDQ vigente é:

$$
\boxed{
r_p^{\rm GDQ}
=
0{,}840778765432\,{\rm fm},
}
$$

derivado como raio de superfície do estômato bariônico:

$$
\boxed{
r_p
=
\frac18
\left(1+\frac{\alpha}{4}\right)
\epsilon_{\rm eff}
\left(\frac32\Lambda_C\right).
}
$$

A diferença entre sondas fica formulada corretamente como:

$$
\boxed{
\delta r_p[\ell]
=
-
\left(H_p^{\rm surf}\right)^{-1}J_{p,\ell}.
}
$$

Portanto, a Q60 está fechada no ponto essencial: corrige o erro, preserva o
resultado canônico da Q40 e separa o que é raio estrutural do que é raio
efetivo dependente da medição.

O fechamento metrológico posterior não muda essa conclusão. Ele apenas avalia,
para cada sonda concreta, quanto o contorno físico altera o raio efetivo:

$$
\boxed{
r_p^{\rm eff}[\ell]
=
0{,}840778765432\,{\rm fm}
-
\left(H_p^{\rm surf}\right)^{-1}J_{p,\ell}.
}
$$

Assim, a conclusão final da Q60 é:

$$
\boxed{
\text{raio estrutural fechado; puzzle experimental reduzido a resposta de contorno.}
}
$$
