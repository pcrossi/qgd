# Q38 — Warp térmico do espaço de Einstein

## 1. Objetivo

Este documento continua a avaliação direta de:

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

Depois de tratar \(\eta_R\) como fator de convenção tensorial, o próximo
objeto físico é:

\[
\boxed{e^{2A(y,\tau)}}
\]

isto é, o warp que comunica o fundo cosmológico \(T^5\times S^3\) com o setor
gravitacional observado localmente.

---

## 2. Princípio físico

O fundo de Einstein não é equivalente ao plano.

\[
\boxed{
T^5\times S^3
=
\text{tecido cosmológico térmico/global},
\qquad
T^4\times\mathbb R^4
=
\text{aproximação local plana.}
}
\]

Portanto, a calibração de \(G\) deve usar o volume efetivo do fundo global,
não o volume plano local.

O plano só aparece depois, como limite de leitura observacional. Usar o plano
para determinar \(G\) seria trocar o problema real por sua aproximação
tangente.

---

## 3. Onde a temperatura entra

Na ação oficial, a densidade ponderada é:

\[
\mathcal U_*
=
\frac{\rho_*}{(4\pi z_\tau)^4},
\qquad
\rho_*
=
e^{-(f_*+\bar f_*)/2}.
\]

O parâmetro \(z_\tau\) atua como escala térmica/tempo de difusão do fluxo de
Perelman. Assim, no fundo estacionário:

\[
\mathcal U_*\sqrt{q_*}
\]

não é apenas volume geométrico; é volume térmico ponderado.

O fator que entra em \(C_R\) é:

\[
I_G(y,\tau)
=
\eta_R e^{2A(y,\tau)}
\frac{\rho_*(y,\tau)}{(4\pi z_\tau)^4}
\sqrt{q_*(y,\tau)}.
\]

Logo:

\[
\boxed{
\mathcal V_{\rm eff}^{(G)}
=
\operatorname{Re}
\int_\gamma d\tau
\int_K I_G(y,\tau)\,d^4y.
}
\]

Esse é o lugar matemático onde a temperatura cosmológica entra.

---

## 4. Interpretação do warp \(A\)

O warp \(A(y,\tau)\) mede a diferença entre:

1. a escala de curvatura real do tecido cosmológico;
2. a escala local usada pelo observador quase plano.

Uma decomposição útil é:

\[
A(y,\tau)
=
A_{\rm Ein}(y)
+A_{\rm th}(\tau)
+A_{\rm bdy}(y,\tau).
\]

com:

1. \(A_{\rm Ein}\): curvatura global de \(S^3\) e ciclos internos;
2. \(A_{\rm th}\): peso térmico do fluxo/tempo \(z_\tau\);
3. \(A_{\rm bdy}\): impedância de fronteira/estômato.

Então:

\[
e^{2A}
=
e^{2A_{\rm Ein}}
e^{2A_{\rm th}}
e^{2A_{\rm bdy}}.
\]

Essa separação evita misturar:

1. geometria cosmológica;
2. temperatura de Perelman;
3. correção de contorno.

---

## 5. Relação com o potencial cotangente

No fundo global \(S^3\), o potencial geométrico não é exatamente \(1/r\). A
forma natural é:

\[
V_{S^3}(r)
\propto
\frac1R\cot(r/R).
\]

O potencial de laboratório é apenas o limite:

\[
\frac1R\cot(r/R)
=
\frac1r
-\frac{r}{3R^2}
+O(r^3/R^4).
\]

Portanto:

\[
\boxed{
\text{a calibração global de massas e de }G\text{ deve usar a forma cotangente;}
}
\]

\[
\boxed{
\text{o potencial }1/r\text{ é a leitura plana local.}
}
\]

Isso é a mesma distinção que aparece em Q39: o espectro global usa \(S^3\);
o estômato/plano produz deslocamentos locais de contorno.

---

## 6. Interpretação da planificação estereográfica

Nos scripts atuais de Q38 aparece um fator:

\[
\sqrt{\pi}.
\]

Ele foi usado como “planificação estereográfica”:

\[
\Pi_{1,\rm obs}
=
\frac{\Pi_{1,\rm bulk}}{\sqrt{\pi}}.
\]

Status correto:

\[
\boxed{
\sqrt{\pi}\text{ é uma hipótese efetiva de projeção, ainda não uma derivação.}
}
\]

Para fechar a Q38, esse fator deve sair de um mapa explícito:

\[
\mathcal P_{\rm flat}:
T^5\times S^3
\longrightarrow
\mathbb R^3_{\rm local}
\]

com jacobiano:

\[
J_{\rm flat}
=
\left|
\frac{\partial \mathrm{vol}_{\rm local}}
{\partial \mathrm{vol}_{S^3}}
\right|.
\]

O fator observacional deve ser:

\[
\Pi_{1,\rm obs}
=
J_{\rm flat}^{-1}
\Pi_{1,\rm bulk}.
\]

Se:

\[
J_{\rm flat}=\sqrt{\pi},
\]

então a planificação usada no script fica justificada. Até lá, ela é hipótese
efetiva bem-sucedida, não prova.

---

## 7. Relação com o meio-instantão

O solver V2 impõe:

\[
S_{\rm inst}
=
\frac1{2\alpha}.
\]

Na integral efetiva, isso corresponde a:

\[
\rho_*
\sim
e^{-S_{\rm inst}}
=
e^{-1/(2\alpha)}.
\]

Como \(G\propto 1/\mathcal V_{\rm eff}^{(G)}\), a estrutura esperada é:

\[
\mathcal V_{\rm eff}^{(G)}
\sim
e^{1/(2\alpha)},
\qquad
G
\sim
e^{-1/(2\alpha)}.
\]

Pendência real:

\[
\boxed{
\text{não basta impor }S_{\rm inst}=1/(2\alpha);
\text{ é preciso obter essa ação da sela da GDQ.}
}
\]

O warp térmico deve ajudar nessa derivação: a sela instantônica é solução do
setor térmico/compacto, não constante externa.

---

## 8. Auditoria do solver V2

O script:

\[
\texttt{numerico/q38\_gravidade/solve\_gravity\_q38\_v2.py}
\]

tem valor como teste exploratório, mas possui três pontos a corrigir antes de
ser usado como evidência forte.

### 8.1 Condição de contorno

O comentário do script diz que o BVP usa Neumann, mas o código impõe:

\[
f(\epsilon)=S_{\rm inst},
\qquad
f(\pi-\epsilon)=S_{\rm inst}.
\]

Isso é Dirichlet, não Neumann.

Correção necessária:

1. ou corrigir o texto do relatório para Dirichlet;
2. ou reexecutar com condição Neumann real:

   \[
   f'(\epsilon)=0,
   \qquad
   f'(\pi-\epsilon)=0.
   \]

Fisicamente, a escolha importa:

1. Dirichlet fixa a ação instantônica na borda;
2. Neumann impõe regularidade/fluxo nulo;
3. Robin representaria impedância térmica do estômato.

Para Q38, Robin ou Neumann regular parecem mais naturais que Dirichlet fixo,
a menos que o contorno instantônico seja justificado topologicamente.

### 8.2 Fano numérico

O script usa:

\[
\chi_{\rm Fano}=0.4791.
\]

Mas outros trechos usam:

\[
\chi_{\rm Fano}=\frac{3\sqrt2}{5}\approx0.848528.
\]

Isso é uma inconsistência objetiva.

Antes de usar o resultado de \(0,34\%\), é necessário decidir qual objeto está
sendo chamado de \(\chi_{\rm Fano}\):

1. admitância \(\chi\);
2. impedância \(1/\chi\);
3. fator projetado já combinado com planificação;
4. outro coeficiente de transmissão.

### 8.3 Planificação

A divisão por \(\sqrt{\pi}\) é aplicada após o cálculo:

\[
\Pi_{1,\rm obs}
=
\Pi_{1,\rm bulk}/\sqrt{\pi}.
\]

Ela deve ser derivada como jacobiano de leitura local:

\[
J_{\rm flat}
=
\sqrt{\pi}.
\]

Enquanto isso não for feito, o solver V2 deve ser classificado como hipótese
efetiva promissora.

---

## 9. Forma mínima do cálculo correto

O cálculo correto deve avaliar:

\[
\mathcal V_{\rm eff}^{(G)}
=
\operatorname{Re}
\int_\gamma d\tau
\int_K
\eta_R
e^{2A_{\rm Ein}(y)}
e^{2A_{\rm th}(\tau)}
e^{2A_{\rm bdy}(y,\tau)}
\frac{\rho_*(y,\tau)}{(4\pi z_\tau)^4}
\sqrt{q_*(y,\tau)}
d^4y.
\]

Depois:

\[
G_{\rm bulk}
=
\frac{c^4\Lambda_C^2}
{16\pi\hbar\,\mathcal V_{\rm eff}^{(G)}}.
\]

E somente depois:

\[
G_{\rm obs}
=
\mathcal P_{\rm flat}[G_{\rm bulk}].
\]

Essa sequência impede circularidade:

\[
\boxed{
\text{primeiro fundo cosmológico; depois leitura plana local.}
}
\]

---

## 10. Próximo passo

O próximo documento deve atacar o fator de planificação:

\[
\boxed{
\texttt{questoes/q38/associados/planificacao\_estereografica.md}
}
\]

Objetivo:

1. definir o mapa \(S^3\to\mathbb R^3\);
2. calcular o jacobiano de volume;
3. verificar se a média/projeção relevante produz \(\sqrt{\pi}\);
4. separar o que é projeção geométrica do que é ajuste fenomenológico.

Continuação criada:

\[
\boxed{
\texttt{questoes/q38/associados/planificacao\_estereografica.md}
}
\]

Conclusão provisória: o jacobiano estereográfico puro não é constante; logo
\(\sqrt{\pi}\) deve vir de uma média ponderada, norma de modo gravitacional ou
combinação com impedância de contorno.

