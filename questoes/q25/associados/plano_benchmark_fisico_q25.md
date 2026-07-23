# Plano Q25 — benchmark físico GDQ do problema do sinal

## 1. Enunciado

O objetivo não é resolver “o problema do sinal da MQ” importando a estrutura
de Monte Carlo fermiônico. O objetivo físico da Q25 é testar se a GDQ permite
calcular observáveis fermiônicos sensíveis à holonomia usando medida positiva,
com erro e custo controlados.

O benchmark deve verificar a cadeia:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf S_{ab}
\to
\widehat O
\to
\text{comparação externa}.
$$

O protótipo já mostrou que a arquitetura positiva por domínios/holonomias é
implementável. Agora falta substituir o toy por um sistema físico auditável.

---

## 2. Benchmark escolhido

### 2.1 Benchmark principal

Usar o modelo Fermi--Hubbard 2D de átomos frios como benchmark externo, porque
há dados experimentais site-resolved de correlação de spin e carga.

Na GDQ, ele entra apenas como condição experimental efetiva:

1. geometria discreta do aparelho/rede óptica;
2. densidade inicial;
3. temperatura efetiva;
4. escala de hopping externa;
5. observáveis de correlação extraídos dos experimentos.

Não entra como ação fundamental.

### 2.2 Referências externas prioritárias

1. Parsons et al. 2016 — correlações de spin site-resolved.
2. Cheuk et al. 2016 — correlações espaciais de carga e spin.
3. Mazurenko et al. 2017 — antiferromagnetismo Fermi--Hubbard.
4. Koepsell et al. 2019 — polaron magnético dopado.

Os valores numéricos devem ser extraídos localmente para:

```text
questoes/q25/dados/q25_referencias_experimentais.csv
```

Sem valores locais extraídos, não há comparação metrológica.

---

## 3. Objeto GDQ a calcular

### 3.1 Domínios

Cada configuração local da rede é tratada como domínio efetivo:

$$
M^\ast=\bigcup_a U_a.
$$

Cada domínio carrega medida positiva:

$$
d\mu_a=\rho_a\,d\mu_{g,a},
\qquad
\rho_a>0.
$$

### 3.2 Holonomia fermiônica

A troca fermiônica não entra como peso negativo. Ela entra como fase:

$$
S_R(P_{ij}Z)=S_R(Z)+\pi\hbar,
$$

logo:

$$
\operatorname{Hol}(P_{ij})=-1.
$$

### 3.3 Interfaces físicas

Entre domínios:

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

O benchmark físico exige derivar ou parametrizar conservadoramente:

$$
\mathsf S_{ab}
=
\begin{pmatrix}
\mathsf R_a & \mathsf T_{ba}\\
\mathsf T_{ab} & \mathsf R_b
\end{pmatrix}
$$

a partir da Hessiana GDQ reduzida do background do aparelho/rede, não do alvo
experimental.

---

## 4. Observáveis

### 4.1 Observável principal

Correlação spin--spin de dois pontos:

$$
C_s(r)=
\langle S^z_iS^z_{i+r}\rangle
-
\langle S^z_i\rangle\langle S^z_{i+r}\rangle.
$$

Na GDQ, isso deve ser reescrito como observável de circulação/holonomia:

$$
C_s(r)
=
\left\langle
O_s(Z_i,Z_{i+r},\nabla S_R,\operatorname{Hol})
\right\rangle_\rho.
$$

### 4.2 Observáveis secundários

1. correlação carga--carga;
2. comprimento de correlação antiferromagnética;
3. fator de estrutura de spin;
4. perfil de polaron magnético em torno do dopante.

---

## 5. Scripts físicos a criar

### 5.1 `q25_10_extract_experimental_data.py`

Função:

1. ler dados digitados/extrados em CSV;
2. validar unidades, barras de erro e metadados;
3. gerar tabela limpa por paper e observável.

Saída:

```text
questoes/q25/resultados/saida_q25_10_extract_experimental_data.md
```

### 5.2 `q25_11_build_physical_domains.py`

Função:

1. construir rede física \(L\times L\);
2. associar domínios \(U_a\) a padrões locais de ocupação/circulação;
3. impor \(\rho_a>0\);
4. inserir holonomia de troca \(-1\).

Saída:

```text
questoes/q25/resultados/saida_q25_11_build_physical_domains.md
```

### 5.3 `q25_12_derive_interface_from_hessian.py`

Função:

1. montar Hessiana reduzida GDQ no espaço de domínios;
2. separar blocos internos e de interface;
3. calcular complemento de Schur;
4. construir \(\mathsf S_{ab}\) por impedância de interface.

Critério:

$$
\mathsf S_{ab}^\dagger\mathsf S_{ab}=I
$$

no setor fechado, ou

$$
\mathsf S_{ab}^\dagger\mathsf S_{ab}\le I
$$

no setor aberto.

### 5.4 `q25_13_spin_correlations_gdq.py`

Função:

1. amostrar com \(\rho>0\);
2. calcular \(C_s(r)\);
3. medir erro estatístico;
4. comparar com solução exata em clusters pequenos.

### 5.5 `q25_14_variance_scaling_physical.py`

Função:

1. variar \(L\), temperatura efetiva e dopagem;
2. medir variância;
3. medir autocorrelação;
4. comparar ajuste polinomial e exponencial.

### 5.6 `q25_15_compare_experiment_physical.py`

Função:

1. comparar \(C_s(r)\), \(C_c(r)\), \(\xi_s\) e fator de estrutura com dados;
2. calcular \(\chi^2\);
3. registrar se os parâmetros usados foram fixados antes da comparação.

### 5.7 `q25_run_physical_benchmark.py`

Executar todos os scripts físicos e gerar:

```text
questoes/q25/resultados/saida_q25_benchmark_fisico.md
```

---

## 6. Parâmetros permitidos

### 6.1 Dados externos do experimento

São permitidos como contorno/aparelho:

1. tamanho da rede;
2. temperatura informada;
3. dopagem;
4. geometria da rede;
5. escala experimental usada para apresentar os dados;
6. barras de erro.

### 6.2 Não permitidos como ajuste

Não usar o alvo experimental para escolher:

1. fase de holonomia;
2. sinal de troca;
3. coeficientes de transmissão/reflexão;
4. escala de variância;
5. correção de borda posterior;
6. parâmetro livre para melhorar \(\chi^2\).

---

## 7. Critérios de fechamento

A Q25 pode ser promovida para “fechada computacionalmente em uma classe” se:

1. os dados experimentais forem extraídos localmente;
2. o operador GDQ físico for fixado antes da comparação;
3. \(\rho>0\) e \(\operatorname{Hol}(P_{ij})=-1\) forem preservados;
4. não houver denominador de fase exponencialmente pequeno;
5. a variância crescer no máximo polinomialmente na classe testada;
6. a autocorrelação/mistura for medida;
7. clusters pequenos concordarem com solução exata;
8. o benchmark experimental for comparado com barras de erro.

Até lá, o status permanece:

$$
\boxed{
\text{Q25: pipeline mínimo feito; benchmark físico em construção.}
}
$$

---

## 8. Ordem prática de execução

1. Extrair dados quantitativos dos papers para o CSV local.
2. Implementar rede/domínios físicos.
3. Construir \(\mathsf S_{ab}\) por Hessiana/impedância GDQ.
4. Validar em clusters pequenos.
5. Medir variância e autocorrelação.
6. Comparar com experimentos.
7. Atualizar `questao_25.md`, `faltas.md`, `memory.md` e `brain/`.
