# Plano de fechamento — Q24: assintoticidade da medição

## 1. Enunciado preciso

Resolver a pendência remanescente da Questão 24:

$$
\boxed{
\text{conectar a dominância espectral da difusão GDQ aos registros
macroscópicos }R_i.
}
$$

A prova já existente no manuscrito legado mostra dominância de modo
fundamental para um operador efetivo:

$$
\mathcal H\psi_n=\lambda_n\psi_n,
\qquad
0<\lambda_0<\lambda_1<\cdots,
$$

$$
\rho(\tau)
=
\sum_n c_ne^{-\lambda_n\tau}\psi_n
\xrightarrow{\tau\to\infty}
c_0e^{-\lambda_0\tau}\psi_0.
$$

O que ainda falta é transformar esse fato espectral em um teorema de medição
GDQ:

$$
\text{operador de aparelho}
\to
\text{setores }R_i
\to
\text{gap}
\to
\text{supressão de coerências}
\to
\text{registro estável}.
$$

---

## 2. Dados do problema

### 2.1 Dados fornecidos

1. Ação oficial da GDQ.
2. Densidade:

   $$
   \rho=e^{-(f+\bar f)/2}.
   $$

3. Medida:

   $$
   \mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
   $$

4. Modelo estrutural de medição:

   $$
   S+A+E.
   $$

5. Regra de Born operacional já tratada na Q22:

   $$
   P(i)=\operatorname{Tr}(\rho_SP_i).
   $$

### 2.2 Dados que pertencem ao aparelho

Para uma medição concreta, o aparelho fornece:

1. domínio espacial/geométrico \(\Omega_{\rm app}\);
2. janela causal de interação;
3. fonte clássica \(J_{\rm app}\);
4. impedância ou contorno \(\mathsf R_{\rm app}\);
5. resolução macroscópica que define registros distinguíveis \(R_i\).

Esses dados não são novos termos fundamentais da ação; são condições de
contorno/fonte do problema experimental.

---

## 3. Construção matemática a executar

### Etapa 1 — Definir o operador de medição GDQ

Construir, a partir da Hessiana física da ação oficial no background
aparelho+sistema, o operador setorial:

$$
\mathcal H_{\rm meas}
=
P^{\rm phys}
\operatorname{Hess}\mathcal S_{\rm GDQ}
P^{\rm phys}.
$$

No limite difusivo da densidade, ele deve reduzir ao operador tipo calor
conjugado:

$$
\partial_\tau\rho
=
-\mathcal H_{\rm meas}\rho.
$$

Produto desta etapa:

$$
\boxed{
\mathcal H_{\rm meas},\quad
\mathcal D(\mathcal H_{\rm meas}),\quad
\text{produto interno ponderado por }\mathcal U.
}
$$

Critério de aprovação:

1. operador simétrico ou auto-adjunto no domínio declarado;
2. sinais compatíveis com decaimento;
3. contornos do aparelho explícitos.

---

### Etapa 2 — Definir registros como setores espectrais/bacias

Cada registro macroscópico deve ser definido por um subdomínio ou setor
estável:

$$
R_i
\leftrightarrow
\Omega_i
\leftrightarrow
\Pi_i.
$$

Aqui \(\Pi_i\) é o projetor espectral ou quase-projetor associado ao setor de
ponteiro.

Produto desta etapa:

$$
\boxed{
\Pi_i\Pi_j\simeq\delta_{ij}\Pi_i,
\qquad
\sum_i\Pi_i\simeq I_{\rm reg}.
}
$$

Critério de aprovação:

1. registros distinguíveis por suporte, contorno ou atrator;
2. quase-ortogonalidade macroscópica;
3. estabilidade sob pequenas perturbações do aparelho.

---

### Etapa 3 — Provar gap setorial

Para cada setor \(R_i\), provar que o operador restrito possui modo dominante:

$$
\mathcal H_i
=
\Pi_i\mathcal H_{\rm meas}\Pi_i,
$$

$$
0\le\lambda_{i,0}<\lambda_{i,1},
\qquad
\Delta_i=\lambda_{i,1}-\lambda_{i,0}>0.
$$

Produto desta etapa:

$$
\boxed{
\Delta_{\rm meas}
=
\min_i\Delta_i>0.
}
$$

Critério de aprovação:

1. espectro discreto ou gap efetivo no setor macroscópico;
2. estimativa inferior de \(\Delta_i\);
3. tratamento de modos zero/gauge.

---

### Etapa 4 — Provar supressão dos termos fora da diagonal

No estado correlacionado:

$$
|\Psi_{SAE}\rangle
=
\sum_i c_i|s_i\rangle|A_i\rangle|E_i\rangle,
$$

os termos cruzados são controlados pelos overlaps:

$$
\Gamma_{ij}(\tau)
=
\langle A_j(\tau),E_j(\tau)|A_i(\tau),E_i(\tau)\rangle.
$$

O objetivo é obter:

$$
|\Gamma_{ij}(\tau)|
\le
C_{ij}e^{-\Delta_{ij}\tau},
\qquad
i\ne j.
$$

Então:

$$
\rho_{SA}(\tau)
\to
\sum_i |c_i|^2
|s_i,A_i\rangle\langle s_i,A_i|.
$$

Produto desta etapa:

$$
\boxed{
\text{taxa de decoerência } \Delta_{ij}
\text{ derivada do operador de medição.}
}
$$

Critério de aprovação:

1. taxa positiva;
2. dependência explícita do contorno/aparelho;
3. nenhuma inserção manual de pesos Born.

---

### Etapa 5 — Relacionar Born, bacias e repetibilidade

Born não deve ser derivado por inserir \(|c_i|^2\) na partição. A Q22 fornece:

$$
P(i)=\operatorname{Tr}(\rho_SP_i).
$$

Na Q24, devemos mostrar que a medição implementa fisicamente os \(P_i\) como
setores de bacia:

$$
P_i
\longleftrightarrow
\Pi_i
\longleftrightarrow
R_i.
$$

Depois do registro:

$$
\rho_{S|i}
=
\frac{P_i\rho_SP_i}{\operatorname{Tr}(\rho_SP_i)},
$$

e a repetibilidade exige:

$$
\operatorname{Tr}(\rho_{S|i}P_i)=1.
$$

Produto desta etapa:

$$
\boxed{
\text{medição implementa Born; não postula Born.}
}
$$

Critério de aprovação:

1. projetores \(P_i\) ligados ao domínio físico do aparelho;
2. repetibilidade demonstrada;
3. separação clara entre probabilidade operacional e seleção ontológica de
   bacia.

---

### Etapa 6 — Resultado único como hipótese dinâmica controlada

A Q24 atual reconhece que decoerência sozinha produz mistura imprópria. Para
resultado único, formalizar a hipótese GDQ:

$$
\boxed{
\text{a microgeometria real do aparelho/ambiente seleciona uma bacia }R_i.
}
$$

Para elevar isso de hipótese a teorema, será necessário provar:

1. existência de trajetória dinâmica condicionada para uma bacia;
2. estabilidade do atrator selecionado;
3. ausência de sinalização superluminal;
4. compatibilidade com unitariedade global no setor fechado.

Produto desta etapa:

$$
\boxed{
\text{status explícito: teorema, teorema condicional ou hipótese ontológica.}
}
$$

Critério de aprovação:

Não chamar resultado único de provado se apenas houver decoerência.

---

## 4. Ordem prática de execução

1. Criar adendo:

   `questoes/q24/associados/operador_medicao_gdq.md`

   com a definição de \(\mathcal H_{\rm meas}\), domínio e contornos.

2. Criar adendo:

   `questoes/q24/associados/setores_registro_bacias.md`

   com \(R_i,\Omega_i,\Pi_i\).

3. Criar adendo:

   `questoes/q24/associados/gap_decoerencia_assintotica.md`

   com a prova:

   $$
   |\Gamma_{ij}(\tau)|
   \le
   C_{ij}e^{-\Delta_{ij}\tau}.
   $$

4. Atualizar `questoes/q24/questao_24.md`, seção 15.5, incorporando o teorema
   como fechamento da ponte entre dominância espectral e registros.

5. Atualizar `faltas.md`, `memory.md` e `brain/conditional-results/q24-measurement-model/index.md`.

---

## 5. Critério de fechamento da Q24

A Q24 poderá ser reclassificada de:

$$
\boxed{
\text{fechada estruturalmente com ressalva}
}
$$

para:

$$
\boxed{
\text{fechada condicionalmente como teorema assintótico de registros}
}
$$

quando estiver demonstrado:

1. \(\mathcal H_{\rm meas}\) vem da Hessiana física GDQ com contorno de
   aparelho;
2. \(R_i\) são setores/projetores estáveis;
3. existe gap setorial \(\Delta_{\rm meas}>0\);
4. os termos fora da diagonal decaem exponencialmente;
5. Born entra apenas como regra operacional já derivada na Q22;
6. a repetibilidade segue da estabilidade do setor;
7. o resultado único permanece claramente classificado como dinâmica
   condicionada ou hipótese ontológica, conforme a prova disponível.

---

## 6. Próxima ação recomendada

Começar pela Etapa 1:

$$
\boxed{
\text{definir } \mathcal H_{\rm meas}
\text{ diretamente da Hessiana física com contorno do aparelho.}
}
$$

Sem esse operador, não há como provar gap, taxa de decoerência ou estabilidade
dos registros.
