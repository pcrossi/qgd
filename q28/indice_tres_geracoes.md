# Q28 — Bloco 3 — Índice, três gerações e limite do fechamento

## 1. Objetivo

Este bloco usa a rota topológica já trabalhada na Q39 para conectar a contagem
de três gerações ao problema de índice da Q28.

É preciso separar duas afirmações:

1. a GDQ possui uma rota estrutural para três gerações;
2. ainda falta provar que o mesmo índice produz exatamente todo o espectro
   fermiônico com representações e hipercargas do Modelo Padrão.

Assim:

\[
\boxed{
\text{três gerações: estruturalmente encaminhadas;}
}
\]

\[
\boxed{
\text{espectro SM completo: ainda depende do índice refinado de }E_{\rm int}.
}
\]

---

## 2. Índice quiral relevante

O operador é:

\[
\slashed D_{B,A}^{+}:
\Gamma(S^+\otimes E_{\rm int})
\to
\Gamma(S^-\otimes E_{\rm int}).
\]

O índice é:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
\dim\ker\slashed D_{B,A}^{+}
-
\dim\ker\slashed D_{B,A}^{-}.
}
\]

Pelo teorema do índice, em uma versão compacta/regularizada:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
\int_{\mathcal I}
\widehat A(T\mathcal I)
\operatorname{ch}(E_{\rm int})
+
\eta_{\partial}.
}
\]

Aqui \(\eta_{\partial}\) é a correção de borda/APS dos estômatos.

---

## 3. Torção de Bismut e invariância do índice

A conexão de Bismut altera o operador local:

\[
\nabla^{\rm LC}\to\nabla^{\rm Bismut}.
\]

Mas, para torção totalmente antissimétrica regular e sem mudança de classe
topológica, o índice quiral é estável por deformação contínua:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A})
=
\operatorname{Ind}(\slashed D_{0,A})
+\Delta_{\partial B}.
}
\]

Se a torção é interna e não muda a condição APS na borda:

\[
\Delta_{\partial B}=0.
\]

Se há torção concentrada nas gargantas/colas, \(\Delta_{\partial B}\) deve ser
calculada como termo de borda.

---

## 4. Contagem de três gerações

A Q39 estruturou a contagem de gerações por classes topológicas:

\[
\boxed{
N_{\rm ger}
=
|h^{1,1}-h^{2,1}|
=
3.
}
\]

Essa fórmula é a parte de contagem do índice:

\[
\boxed{
\operatorname{rank}_{\rm gen}
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
3.
}
\]

Ou seja, a topologia global do setor interno seleciona três famílias estáveis.

---

## 5. Índice refinado para o espectro completo

O alvo forte da Q28 é:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
3
\left[
(3,2)_{1/6}
\oplus
(\bar3,1)_{-2/3}
\oplus
(\bar3,1)_{1/3}
\oplus
(1,2)_{-1/2}
\oplus
(1,1)_1
\right].
}
\]

O fator \(3\) está estruturalmente apoiado pela topologia de gerações.

O conteúdo entre colchetes ainda exige:

1. classes de Chern de \(E_C,E_W,L_Y\);
2. condição global de hipercarga;
3. projeção quiral \(P_L\);
4. correção APS dos estômatos;
5. identificação das representações no kernel.

---

## 6. Forma de Chern character esperada

Com:

\[
E_{\rm int}=E_C\oplus E_W\oplus L_Y,
\]

temos:

\[
\operatorname{ch}(E_{\rm int})
=
\operatorname{ch}(E_C)
+
\operatorname{ch}(E_W)
+
\operatorname{ch}(L_Y).
\]

Para a linha de hipercarga:

\[
\operatorname{ch}(L_Y^q)
=
e^{q c_1(L_Y)}.
\]

Para os setores não abelianos:

\[
c_1(E_C)=0,
\qquad
c_1(E_W)=0.
\]

Logo, as informações não abelianas entram por:

\[
c_2(E_C),\quad c_3(E_C),\quad c_2(E_W),
\]

e a hipercarga por:

\[
c_1(L_Y).
\]

---

## 7. Condição de integralidade da hipercarga

O quociente global:

\[
\frac{SU(3)\times SU(2)\times U(1)_Y}{\mathbb Z_6}
\]

impõe compatibilidade entre trialidade de \(SU(3)\), paridade de \(SU(2)\) e
peso de \(U(1)_Y\). Isso permite que \(Y\) seja fracionário em unidades locais,
mas integral no fibrado global.

A condição de fechamento é:

\[
\boxed{
e^{2\pi iY}
z_3^{t(R_3)}
z_2^{p(R_2)}
=1.
}
\]

Essa é a rota geométrica para obter:

\[
Y=
\frac16,\ -\frac23,\ \frac13,\ -\frac12,\ 1.
\]

---

## 8. Teorema estrutural condicional

Se o fibrado interno efetivo \(E_{\rm int}=E_C\oplus E_W\oplus L_Y\) possui
classes características compatíveis com o quociente
\((SU(3)\times SU(2)\times U(1))/\mathbb Z_6\), se a torção de Bismut apenas
seleciona o setor quiral sem alterar a integralidade do índice, e se a condição
APS dos estômatos fornece \(N_{\rm ger}=3\), então:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
3\,\mathcal E_{\rm gen}
\quad\Longrightarrow\quad
\text{anomalias canceladas}.
}
\]

---

## 9. O que ainda falta para teorema completo

Ainda falta calcular explicitamente:

1. as classes \(c_2(E_C),c_3(E_C),c_2(E_W),c_1(L_Y)\);
2. o termo APS \(\eta_{\partial}\);
3. a ação da torção de Bismut sobre a projeção quiral;
4. a normalização de \(Y\);
5. a igualdade:

   \[
   \operatorname{Ind}(\slashed D_{B,A}^{+})
   =
   3\,\mathcal E_{\rm gen}.
   \]

Status:

\[
\boxed{
\text{Q28 está fechada como teorema condicional; ainda não como cálculo de índice completo.}
}
