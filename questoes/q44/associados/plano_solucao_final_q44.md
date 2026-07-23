# Q44 — Plano para solução final completa

## 1. Objetivo

Fechar a Questão 44 não apenas como explicação reduzida de Madelung, mas como
tratamento GDQ completo da dupla fenda com detector.

O alvo final é derivar, sem fator fenomenológico manual, a perda de
visibilidade:

$$
\mathcal V_{\rm GDQ}
=
\mathcal V_0 e^{-\Gamma_{\rm det}}
$$

a partir da ação oficial da GDQ e do acoplamento clássico do aparelho.

---

## 2. Estado inicial vigente

Já temos:

1. redução Madelung da GDQ;
2. domínio efetivo com duas fendas;
3. padrão de interferência por duas fontes coerentes;
4. pressão de Bohm como pressão geométrica;
5. script legado como visualização de gaussianas em fundo fixo;
6. diagnóstico de que o fator de decoerência legado é efetivo, não derivado.

Ainda falta:

1. modelar o detector como contorno/fonte física;
2. derivar a impedância $\mathsf R_{\rm det}$;
3. calcular $\Gamma_{\rm det}$;
4. executar solver com e sem detector;
5. extrair visibilidade e comparar com dados ou limites experimentais.

---

## 3. Cadeia de fechamento

A cadeia mínima deve ser:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_*=(g_*,J_*,H_*,f_*,\mathcal U_*)
\to
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
\to
\Omega_{\rm fendas}
\to
\mathsf R_{\rm det}
\to
\Gamma_{\rm det}
\to
\rho_{\rm anteparo}
\to
\mathcal V.
$$

Onde:

- $\Phi_*$ é o background estacionário admissível;
- $\Omega_{\rm fendas}$ é o domínio com barreira, aberturas e anteparo;
- $\mathsf R_{\rm det}$ é a impedância geométrica do detector;
- $\Gamma_{\rm det}$ é o funcional de decoerência;
- $\mathcal V$ é a visibilidade das franjas.

---

## 4. Fase 1 — Definir o problema reduzido correto

### 4.1 Domínio

Definir:

$$
\Omega
=
\{(x,y):y_{\rm in}<y<y_{\rm out}\}
\setminus
\text{barreira}.
$$

A barreira fica em $y=0$ e possui duas aberturas:

$$
A_1,\ A_2.
$$

### 4.2 Condições de contorno sem detector

Na parte opaca:

$$
J^n=\rho\frac{\nabla^n S_R}{m}=0.
$$

Nas fendas:

$$
J^n\big|_{A_1}+J^n\big|_{A_2}=J_{\rm in}.
$$

Para fendas idênticas:

$$
\int_{A_1}J^n\,dA
=
\int_{A_2}J^n\,dA
=
\frac12J_{\rm in}.
$$

### 4.3 Equações reduzidas

Resolver:

$$
\partial_t\rho+\nabla\cdot\left(\rho\frac{\nabla S_R}{m}\right)=0,
$$

$$
\partial_tS_R+\frac{|\nabla S_R|^2}{2m}
+V_{\rm app}
-\frac{\hbar^2}{2m}\frac{\Delta\sqrt\rho}{\sqrt\rho}=0.
$$

Status esperado da Fase 1:

$$
\boxed{
\text{solver reduzido sem detector validado contra a solução gaussiana/paraxial.}
}
$$

---

## 5. Fase 2 — Detector como contorno físico

O detector não deve ser inserido como operador quântico manual. Ele entra como
fonte clássica ou impedância de bordo.

### 5.1 Dados físicos do detector

Declarar:

1. geometria do detector;
2. posição relativa às fendas;
3. espessura efetiva $L$;
4. densidade material $\rho_{\rm det}$;
5. resposta elástica/torsional efetiva;
6. temperatura ou ruído térmico, se usado.

### 5.2 Fonte clássica

Representar o detector por:

$$
J_{\rm det}^{\rm clássico}.
$$

Esse termo não altera a ação oficial. Ele define a condição externa do
problema, como campo de aparelho.

### 5.3 Resposta induzida

Calcular:

$$
\delta\Phi_{\rm det}
=
K_{\rm phys}^{-1}J_{\rm det},
$$

onde:

$$
K_{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

### 5.4 Impedância de detector

Definir:

$$
\mathsf R_{\rm det}
=
\operatorname{DtN}_{\rm det}
$$

ou, de modo equivalente,

$$
\mathsf R_{\rm det}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Essa é a forma de Schur da eliminação dos graus internos do detector.

Status esperado da Fase 2:

$$
\boxed{
\mathsf R_{\rm det}\text{ derivada como impedância de contorno.}
}
$$

---

## 6. Fase 3 — Derivar o fator de decoerência

Com a impedância calculada, a perda de coerência deve vir de uma forma
quadrática positiva:

$$
\Gamma_{\rm det}
=
\int_{\partial\Omega_{\rm det}}
\Delta\Phi^\dagger
\mathsf R_{\rm det}
\Delta\Phi
\,d\Sigma.
$$

Ou, no volume do detector:

$$
\Gamma_{\rm det}
=
\int_{\Omega_{\rm det}}
J_{\rm det}^\dagger
K_{\rm det}^{-1}
J_{\rm det}
\,d\mu.
$$

Critério físico:

$$
\Gamma_{\rm det}=0
\quad\Longrightarrow\quad
\mathcal V=\mathcal V_0.
$$

$$
\Gamma_{\rm det}\gg1
\quad\Longrightarrow\quad
\mathcal V\to0.
$$

Status esperado da Fase 3:

$$
\boxed{
\text{fator de decoerência substituído por funcional derivado.}
}
$$

---

## 7. Fase 4 — Solver numérico mínimo

Criar um solver autocontido em:

$$
\texttt{questoes/q44/associados/}
$$

com três regimes:

1. sem detector;
2. detector fraco;
3. detector forte.

### 7.1 Saídas obrigatórias

Salvar:

1. densidade no anteparo $\rho(x,L)$;
2. fase $S_R(x,L)$;
3. potencial de Bohm $Q[\rho]$;
4. visibilidade:

$$
\mathcal V
=
\frac{I_{\max}-I_{\min}}{I_{\max}+I_{\min}};
$$

5. curva $\mathcal V(\Gamma_{\rm det})$;
6. estudo de convergência de malha.

### 7.2 Validação

Sem detector:

$$
\rho_{\rm num}
\to
\rho_{\rm gaussiana}
$$

no limite paraxial.

Com detector forte:

$$
\rho_{\rm num}
\to
\rho_1+\rho_2.
$$

Status esperado da Fase 4:

$$
\boxed{
\text{transição interferência}\to\text{mistura clássica reproduzida sem pós-ajuste.}
}
$$

---

## 8. Fase 5 — Previsão experimental distintiva

A previsão distintiva não é a existência das franjas. Isso já é comum à
mecânica ondulatória.

A previsão distintiva deve ser a lei:

$$
\mathcal V
=
\mathcal V_0
e^{-\Gamma_{\rm det}[\rho_{\rm det},L,E,T,\mathsf R_{\rm det}]}.
$$

O ponto testável é se $\Gamma_{\rm det}$ segue a impedância geométrica do
aparelho, e não apenas uma seção de choque ajustada.

### 8.1 Comparações possíveis

1. variação da distância detector--fenda;
2. variação da espessura do substrato;
3. variação de material;
4. variação de energia da partícula;
5. experimentos de apagador quântico e escolha retardada, tratados como
   mudança de contorno.

### 8.2 Critério de sucesso

A Q44 fica completa se:

$$
\Gamma_{\rm det}
$$

for calculado antes da comparação e reproduzir a curva de visibilidade sem
recalibração para cada ponto.

---

## 9. Fase 6 — Documento final

Atualizar `questoes/q44/questao_44.md` com:

1. enunciado;
2. ação oficial preservada;
3. domínio;
4. condições de contorno;
5. derivação de Madelung reduzida;
6. derivação de $\mathsf R_{\rm det}$;
7. derivação de $\Gamma_{\rm det}$;
8. resultados numéricos;
9. comparação experimental;
10. limitações.

Status final desejado:

$$
\boxed{
\text{Q44 fechada condicionalmente com detector derivado e solver validado.}
}
$$

---

## 10. Critério de parada

Não declarar Q44 fechada completa se faltar qualquer um destes itens:

1. $\mathsf R_{\rm det}$ derivada;
2. $\Gamma_{\rm det}$ derivado;
3. solver com detector;
4. convergência numérica;
5. separação explícita entre parâmetro do aparelho e constante universal;
6. comparação com dados ou ao menos protocolo experimental claro.

Se o detector não for calculado, o status correto permanece:

$$
\boxed{
\text{Q44 fechada no setor Madelung sem detector, aberta no setor decoerência.}
}
$$
