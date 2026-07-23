# Q28 — Bloco 2 — Espectro fermiônico, hipercarga e anomalias

## 1. Objetivo

O grupo efetivo só é fisicamente relevante se atuar no espectro correto. A Q28
não fecha apenas com:

\[
SU(3)_C\times SU(2)_L\times U(1)_Y.
\]

É necessário obter os modos fermiônicos, suas hipercargas, sua quiralidade e o
cancelamento de anomalias.

O alvo de uma geração, escrito com campos de Weyl à esquerda, é:

\[
\boxed{
\mathcal E_{\rm gen}
=
(3,2)_{1/6}
\oplus
(\bar3,1)_{-2/3}
\oplus
(\bar3,1)_{1/3}
\oplus
(1,2)_{-1/2}
\oplus
(1,1)_{1}.
}
\]

Opcionalmente:

\[
(1,1)_0
\]

para \(\nu_R^c\).

---

## 2. Operador espectral

O espectro deve vir do operador de Dirac--Bismut acoplado:

\[
\boxed{
\slashed D_{B,A}
=
\gamma^\mu
\left(
\nabla_\mu^{\rm LC}
+
\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iA_\mu
\right).
}
\]

Com:

\[
A_\mu
=
G_\mu^aT_a
+
W_\mu^it_i
+
B_\mu Y.
\]

A decomposição quiral é:

\[
\slashed D_{B,A}^{+}:
\Gamma(S^+\otimes E_{\rm int})
\to
\Gamma(S^-\otimes E_{\rm int}).
\]

O espectro quiral líquido é:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
\ker\slashed D_{B,A}^{+}
-
\ker\slashed D_{B,A}^{-}.
}
\]

---

## 3. Postulado geométrico mínimo a demonstrar

Para fechar a Q28 como teorema, a GDQ deve provar:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
3\,\mathcal E_{\rm gen}
}
\]

para três gerações, ou:

\[
\boxed{
\operatorname{Ind}_{\rm local}
=
\mathcal E_{\rm gen}
}
\]

por célula geracional.

Na fase atual, este bloco formula a condição exata de fechamento. A prova
completa depende da aplicação de índice/APS/Atiyah--Singer ao fibrado interno
efetivo da GDQ.

---

## 4. Origem geométrica das representações

### 4.1 Cor

Os estados coloridos são seções que transformam em \(E_C\simeq\mathbb C^3\):

\[
3.
\]

Estados anticoloridos aparecem no dual:

\[
E_C^*\simeq\bar3.
\]

Estados leptônicos são singletos:

\[
1.
\]

### 4.2 Fraco quiral

Os dubletos esquerdos são seções de \(P_LE_W\):

\[
2.
\]

Os singletos direitos conjugados são seções que não carregam \(E_W\):

\[
1.
\]

Logo:

\[
Q_L,L_L\sim2,
\qquad
u_R^c,d_R^c,e_R^c\sim1.
\]

### 4.3 Hipercarga

A hipercarga é peso da linha \(L_Y\). Se \(L_Y^q\) denota a potência racional
compatível com o quociente global, então:

\[
Y=q.
\]

A presença do quociente \(\Gamma\subseteq\mathbb Z_6\) permite pesos
fracionários consistentes.

---

## 5. Condição global de hipercarga

Para o grupo global:

\[
G_{\rm SM}^{\rm global}
=
\frac{
SU(3)\times SU(2)\times U(1)_Y
}{
\mathbb Z_6
},
\]

uma representação \((R_3,R_2)_Y\) é bem definida se o centro combinado atua
trivialmente.

Se:

\[
z_3=e^{2\pi i/3}\in Z(SU(3)),
\]

\[
z_2=-1\in Z(SU(2)),
\]

e:

\[
e^{i\theta_Y}\in U(1)_Y,
\]

então a condição global impõe uma congruência entre trialidade de cor,
paridade fraca e hipercarga.

Essa congruência fixa a quantização fracionária de \(Y\). Assim, as frações:

\[
\frac16,\quad -\frac23,\quad \frac13,\quad -\frac12,\quad 1
\]

não são escolhas independentes: elas são pesos compatíveis com o quociente
global e com a exigência:

\[
\boxed{
Q=T_3+Y
}
\]

produzir cargas elétricas inteiras para observáveis compostos.

---

## 6. Espectro de uma geração

A célula geracional mínima é:

| Campo | Origem geométrica | Rep. efetiva | \(Y\) |
|---|---|---:|---:|
| \(Q_L=(u_L,d_L)\) | \(E_C\otimes P_LE_W\) | \((3,2)\) | \(1/6\) |
| \(u_R^c\) | \(E_C^*\) com orientação \(u\) | \((\bar3,1)\) | \(-2/3\) |
| \(d_R^c\) | \(E_C^*\) com orientação \(d\) | \((\bar3,1)\) | \(1/3\) |
| \(L_L=(\nu_L,e_L)\) | \(P_LE_W\) sem cor | \((1,2)\) | \(-1/2\) |
| \(e_R^c\) | linha singlete conjugada | \((1,1)\) | \(1\) |
| \(\nu_R^c\) | singlete neutro opcional | \((1,1)\) | \(0\) |

Status:

\[
\boxed{
\text{tabela-alvo formulada geometricamente; índice ainda precisa derivá-la.}
}
\]

---

## 7. Cancelamento de anomalias

Uma vez obtido o espectro acima, o cancelamento é automático por identidade
algébrica. A Q28 precisa demonstrar essas somas.

### 7.1 \([SU(3)]^2U(1)_Y\)

\[
2\left(\frac16\right)T(3)
+
\left(-\frac23\right)T(\bar3)
+
\left(\frac13\right)T(\bar3)=0.
\]

Como:

\[
T(3)=T(\bar3)=\frac12,
\]

temos:

\[
\frac16-\frac13+\frac16=0.
\]

### 7.2 \([SU(2)]^2U(1)_Y\)

\[
3\left(\frac16\right)T(2)
+
\left(-\frac12\right)T(2)=0.
\]

Como:

\[
T(2)=\frac12,
\]

temos:

\[
\frac14-\frac14=0.
\]

### 7.3 Gravitacional--\(U(1)_Y\)

\[
6\left(\frac16\right)
+3\left(-\frac23\right)
+3\left(\frac13\right)
+2\left(-\frac12\right)
+1=0.
\]

Isto dá:

\[
1-2+1-1+1=0.
\]

### 7.4 \([U(1)_Y]^3\)

\[
6\left(\frac16\right)^3
+3\left(-\frac23\right)^3
+3\left(\frac13\right)^3
+2\left(-\frac12\right)^3
+1^3=0.
\]

Explicitamente:

\[
\frac1{36}
-\frac89
+\frac19
-\frac14
+1=0.
\]

### 7.5 Anomalia global de Witten

O número de dubletos \(SU(2)\) por geração é:

\[
3+1=4.
\]

Como é par:

\[
\boxed{
\text{não há anomalia global de Witten.}
}
\]

---

## 8. Interpretação GDQ

Na GDQ, o cancelamento de anomalias deve ser lido como consistência global da
cola geométrica:

\[
\boxed{
\text{anomalia}=
\text{falha de colagem quântica da medida/fase.}
}
\]

Portanto, o cancelamento significa:

\[
\boxed{
\text{a medida quântica e a holonomia interna são globalmente bem definidas.}
}
\]

Isso é compatível com a filosofia da GDQ: a consistência do espectro não é
apenas algébrica, mas topológica.

---

## 9. O que este bloco resolve

Este bloco fornece:

1. o operador espectral que deve gerar os férmions;
2. a tabela-alvo de uma geração escrita geometricamente;
3. a origem das representações em \(E_C\), \(E_W\), \(L_Y\);
4. o papel do quociente global \(\mathbb Z_6\);
5. o cancelamento explícito das anomalias para o espectro obtido.

---

## 10. O que ainda falta

Para fechar Q28 como teorema forte, ainda falta provar:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
3\,\mathcal E_{\rm gen}.
}
\]

Isto exige:

1. caracterizar as classes de Chern do fibrado interno;
2. aplicar índice de Atiyah--Singer/APS ao domínio com estômatos;
3. mostrar que a torção de Bismut não altera o índice, ou calcular sua
   correção de borda;
4. demonstrar que há exatamente três gerações;
5. fixar a normalização global de \(Y\).

Status:

\[
\boxed{
\text{Bloco 2 reduz a Q28 ao teorema de índice do fibrado interno.}
}
