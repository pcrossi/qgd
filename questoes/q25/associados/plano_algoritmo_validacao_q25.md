# Plano Q25 — algoritmo GDQ positivo e validação experimental

## 1. Objetivo

A Questão 25 não deve ser formulada como “resolver o problema do sinal da MQ”
como ontologia externa. Na GDQ, a medida fundamental já é positiva:

$$
\rho=e^{-(f+\bar f)/2}>0,
$$

e a antissimetria fermiônica aparece como fase/holonomia:

$$
S_R(P_{ij}Z)=S_R(Z)+\pi\hbar.
$$

O problema operacional correto é:

$$
\boxed{
\text{calcular observáveis sensíveis à holonomia GDQ com erro, variância e
custo controlados.}
}
$$

O plano abaixo transforma essa afirmação em programa numérico reprodutível.

---

## 2. Separação conceitual obrigatória

### 2.1 Interno à GDQ

Deve ser derivado ou implementado a partir dos objetos GDQ:

1. medida positiva local \(\rho_a\);
2. fase \(S_{R,a}\);
3. holonomia fermiônica \(\operatorname{Hol}(P_{ij})=-1\);
4. domínios \(U_a\);
5. interfaces \(\Sigma_{ab}\);
6. matriz transmissão/reflexão \(\mathsf S_{ab}\);
7. estimadores de observáveis \(O(Z,\nabla S_R,\operatorname{Hol})\).

### 2.2 Comparação externa

Monte Carlo fermiônico, Hubbard, AFQMC, DQMC, Bethe ansatz e diagonalização
exata entram apenas como:

1. benchmarks;
2. linguagem comparativa;
3. dados experimentais ou numéricos de referência;
4. teste de escala de erro.

Eles não substituem a ação oficial da GDQ.

---

## 3. Construção algorítmica mínima

### 3.1 Decomposição de domínios

Modelar o espaço efetivo como:

$$
M^\ast=\bigcup_a U_a,
\qquad
\Sigma_{ab}=U_a\cap U_b.
$$

Em cada domínio:

$$
d\mu_a=\rho_a\,d\mu_{g,a},
\qquad
\rho_a>0.
$$

Nas interfaces:

$$
\begin{pmatrix}
\psi_a^{\rm out}\\
\psi_b^{\rm out}
\end{pmatrix}
=
\mathsf S_{ab}
\begin{pmatrix}
\psi_a^{\rm in}\\
\psi_b^{\rm in}
\end{pmatrix}.
$$

Com:

$$
\mathsf S_{ab}
=
\begin{pmatrix}
\mathsf R_a & \mathsf T_{ba}\\
\mathsf T_{ab} & \mathsf R_b
\end{pmatrix}.
$$

### 3.2 Requisitos da interface

Para setor fechado:

$$
\mathsf S_{ab}^\dagger\mathsf S_{ab}=I.
$$

Para setor aberto/dissipativo:

$$
\mathsf S_{ab}^\dagger\mathsf S_{ab}\le I.
$$

A holonomia de troca deve ser preservada:

$$
\operatorname{Hol}(P_{ij})=-1.
$$

### 3.3 Estimador

O estimador GDQ mínimo deve ter a forma:

$$
\widehat O_M
=
\frac1M
\sum_{k=1}^M
O(a_k,Z_k,\mathsf S_{\partial a_k}),
$$

com:

$$
Z_k\sim \rho_{a_k}d\mu_{g,a_k}.
$$

O fechamento algorítmico exige demonstrar:

$$
\operatorname{Var}(\widehat O_M)
\le
\frac{\operatorname{poly}(N,\beta,\varepsilon^{-1})}{M},
$$

e:

$$
\tau_{\rm mix},
\tau_{\rm corr}
\le
\operatorname{poly}(N,\beta,\varepsilon^{-1}).
$$

---

## 4. Scripts Python autocontidos

Todos os scripts devem rodar sem internet. Dados externos devem estar
congelados em arquivos locais com metadados de origem.

### 4.1 `q25_01_domain_interface.py`

Função:

1. construir uma rede pequena de domínios \(U_a\);
2. atribuir \(\rho_a>0\);
3. construir \(\mathsf S_{ab}\) unitária ou contrativa;
4. impor \(\operatorname{Hol}(P_{ij})=-1\);
5. verificar conservação de norma/fluxo.

Saídas:

1. erro de unitariedade;
2. erro de positividade;
3. holonomia de troca;
4. tabela Markdown.

### 4.2 `q25_02_estimador_holonomia.py`

Função:

1. amostrar \(Z_k\) com medida positiva;
2. calcular observáveis locais e sensíveis à holonomia;
3. separar erro estatístico de erro sistemático;
4. comparar estimador com solução exata em sistemas pequenos.

Saídas:

1. média;
2. variância;
3. intervalo de confiança;
4. erro relativo contra solução exata.

### 4.3 `q25_03_autocorrelacao_variancia.py`

Função:

1. medir autocorrelação integrada;
2. estimar tempo de mistura;
3. testar escala com \(N\), \(\beta\) e número de domínios;
4. verificar se há crescimento compatível com exponencial.

Saídas:

1. \(\tau_{\rm corr}\);
2. \(\tau_{\rm mix}\);
3. ajuste polinomial versus exponencial;
4. gráficos/tabelas.

### 4.4 `q25_04_referencias_experimentais.py`

Função:

1. ler arquivos locais em `questoes/q25/dados/`;
2. validar esquema dos dados extraídos de papers;
3. salvar uma tabela normalizada de observáveis.

Formato mínimo:

```csv
paper_id,observable,U_over_t,T_over_t,doping,site_distance,value,error,figure,notes
```

### 4.5 `q25_05_compare_experiment.py`

Função:

1. comparar predições do algoritmo GDQ com dados experimentais;
2. calcular \(\chi^2\), erro relativo e cobertura por barras de erro;
3. separar comparação qualitativa, semi-quantitativa e quantitativa.

### 4.6 `q25_run_all.py`

Função:

1. executar todos os scripts;
2. gerar `saida_q25_validacao.md`;
3. registrar parâmetros, seeds e versões.

---

## 5. Referências experimentais prioritárias

As referências abaixo devem ser usadas para comparação experimental, não como
ontologia da GDQ.

### 5.1 Correlações de spin site-resolved

Parsons et al. medem diretamente a função de correlação de spin no modelo
Fermi--Hubbard 2D com microscopia de gás quântico.

Referência:

M. F. Parsons, A. Mazurenko, C. S. Chiu, G. Ji, D. Greif, M. Greiner,
“Site-resolved measurement of the spin-correlation function in the
Fermi-Hubbard model,” *Science* **353**, 1253--1256 (2016).

DOI:

$$
10.1126/science.aag1430
$$

Dados a extrair:

1. correlações \(C(r)\);
2. dependência com distância;
3. temperatura estimada;
4. \(U/t\);
5. incertezas.

### 5.2 Correlações espaciais de carga e spin

Cheuk et al. medem correlações espaciais de carga e spin no Fermi--Hubbard 2D.

Referência:

L. W. Cheuk, M. A. Nichols, K. R. Lawrence, M. Okan, H. Zhang, E. Khatami,
N. Trivedi, T. Paiva, M. Rigol, M. W. Zwierlein, “Observation of spatial
charge and spin correlations in the 2D Fermi-Hubbard model,” *Science*
**353**, 1260--1264 (2016).

DOI:

$$
10.1126/science.aag3349
$$

Dados a extrair:

1. correlação spin--spin;
2. correlação carga--carga;
3. dependência com doping;
4. regime de temperatura;
5. comparação com cálculos numéricos publicados.

### 5.3 Antiferromagneto cold-atom Hubbard

Mazurenko et al. observam antiferromagnetismo de longo alcance em sistema
Fermi--Hubbard 2D e testam dopagem.

Referência:

A. Mazurenko, C. S. Chiu, G. Ji, M. F. Parsons, M. Kanász-Nagy, R. Schmidt,
F. Grusdt, E. Demler, D. Greif, M. Greiner, “A cold-atom Fermi-Hubbard
antiferromagnet,” *Nature* **545**, 462--466 (2017).

DOI:

$$
10.1038/nature22362
$$

Dados a extrair:

1. comprimento de correlação;
2. fator de estrutura de spin;
3. magnetização escalonada;
4. dopagem até \(\sim15\%\);
5. temperatura em unidades de \(t\).

### 5.4 Polaron magnético em Hubbard dopado

Koepsell et al. fornecem dados de um dopante em background magnético.

Referência:

J. Koepsell, J. Vijayan, P. Sompet, F. Grusdt, T. A. Hilker, E. Demler,
G. Salomon, I. Bloch, C. Gross, “Imaging magnetic polarons in the doped
Fermi-Hubbard model,” *Nature* **572**, 358--362 (2019).

DOI:

$$
10.1038/s41586-019-1463-1
$$

Dados a extrair:

1. perfil de correlações ao redor do dopante;
2. distorção magnética local;
3. escala espacial do polaron;
4. dependência com dopagem/temperatura.

---

## 6. Referência de restrição computacional

Esta referência não é experimental. Ela serve como auditoria de complexidade,
para evitar declarar solução genérica indevida.

M. Troyer, U.-J. Wiese, “Computational Complexity and Fundamental Limitations
to Fermionic Quantum Monte Carlo Simulations,” *Physical Review Letters*
**94**, 170201 (2005).

DOI:

$$
10.1103/PhysRevLett.94.170201
$$

Uso correto:

1. não afirmar solução geral para todos os hamiltonianos fermiônicos;
2. declarar a classe GDQ/domínios em que a variância é testada;
3. demonstrar, se possível, que a GDQ evita a hipótese do teorema por mudar a
   representação geométrica, não por resolver genericamente QMC.

---

## 7. Critério de sucesso

A Q25 poderá ser promovida de “fechada estruturalmente” para “fechada
computacionalmente em uma classe” se houver:

1. operador/domínio GDQ explícito;
2. algoritmo autocontido;
3. estimador com variância medida;
4. autocorrelação medida;
5. estudo de escala;
6. comparação com solução exata em sistemas pequenos;
7. comparação com dados experimentais extraídos dos papers acima;
8. documentação de falhas e regimes onde a GDQ não melhora o custo.

Até lá, o status correto é:

$$
\boxed{
\text{Q25 fechada estruturalmente na GDQ; aberta como validação algorítmica e
experimental.}
}
$$
