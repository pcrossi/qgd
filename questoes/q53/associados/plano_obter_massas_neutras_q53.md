# Q53 — Plano para obter as escalas inerciais neutras

## 1. Objetivo

Obter as três escalas inerciais espectrais neutras da GDQ, observadas
operacionalmente como massas de neutrinos, sem inserir dados de oscilação como
alvo.

O alvo interno não é começar por massas, mas por autovalores:

$$
D_\nu^{\rm tors}\Psi_i^{\rm neutro}
=
\lambda_i\Psi_i^{\rm neutro}.
$$

As massas físicas só aparecem depois da normalização global--local:

$$
m_i^2c^4
=
Z_\nu E_C^2\lambda_i.
$$

---

## 2. Dados já disponíveis

O canal beta neutro já foi identificado no setor do nêutron:

$$
\Psi_e^{\rm folha}
=
\psi_{\bar\nu}^{(e)}
\in
\ker D_{0,-3/2}^{(0)}.
$$

Arquivos de base:

- `questoes/q50/questao_50.md`;
- `questoes/q50/associados/decaimento_beta_livre_gdq.md`;
- `topicos/neutron_decaimento/fechamento_meia_vida_neutron_gdq.md`;
- `topicos/neutron_decaimento/taxa_decaimento_neutron_overlap_gdq.md`;
- `topicos/neutron_decaimento/fechamento_terceiros_jatos_neutron_gdq.md`;
- `topicos/neutron_decaimento/ward_noether_cirurgia_neutron.md`;
- `questoes/q53/questao_53.md`.

Isso fecha a ontologia local do neutrino:

$$
\boxed{
\nu=\text{modo neutro torsional/fase, sem estômato localizado}.
}
$$

---

## 3. Cadeia de cálculo

### Etapa 1 — Construir as três folhas neutras

Definir os transportes de Bismut entre folhas leptônicas:

$$
\Psi_\alpha^{\rm folha}
=
\mathcal P_{\alpha e}\Psi_e^{\rm folha},
\qquad
\alpha=e,\mu,\tau.
$$

com:

$$
\mathcal P_{\alpha e}
=
\operatorname{Pexp}
\left(
-\int_{\mathcal C_{\alpha e}}
\nabla_{\rm neutro}^B
\right).
$$

Saída da etapa:

$$
\mathcal H_\nu^{\rm folha}
=
\operatorname{span}
\{
\Psi_e^{\rm folha},
\Psi_\mu^{\rm folha},
\Psi_\tau^{\rm folha}
\}.
$$

Critério de sucesso: as três folhas devem ser linearmente independentes no
produto interno ponderado por $\mathcal U$.

---

### Etapa 2 — Calcular o Gram ponderado

Calcular:

$$
G_{\alpha\beta}^\nu
=
\langle
\Psi_\alpha^{\rm folha},
\Psi_\beta^{\rm folha}
\rangle_{\mathcal U}.
$$

com:

$$
\langle a,b\rangle_{\mathcal U}
=
\int_M\bar a\,b\,\mathcal U\,dV_g.
$$

Critério de sucesso:

$$
G^\nu>0.
$$

Se $G^\nu$ for singular, o ansatz de três folhas não fornece três modos
neutros independentes.

---

### Etapa 3 — Calcular o bloco neutro da Hessiana

Projetar a Hessiana física da ação oficial no espaço de folhas:

$$
K_{\alpha\beta}^\nu
=
\langle
\Psi_\alpha^{\rm folha},
K_{\rm neutro}^{\rm phys}
\Psi_\beta^{\rm folha}
\rangle_{\mathcal U}.
$$

Aqui:

$$
K_{\rm neutro}^{\rm phys}
=
P_{\ker Q,\chi_L}
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
P_{\ker Q,\chi_L}.
$$

O bloco $K^\nu$ deve conter:

1. inércia neutra diagonal de cada folha;
2. colagem torsional entre folhas;
3. fases orientadas de Bismut;
4. resposta global--local do canal sem estômato.

Critério de sucesso:

$$
K^\nu=(K^\nu)^\dagger
$$

no produto interno definido por $G^\nu$.

---

### Etapa 4 — Resolver o problema espectral generalizado

Resolver:

$$
K^\nu c_i
=
\lambda_iG^\nu c_i.
$$

Os modos próprios são:

$$
\Psi_i^{\rm neutro}
=
\sum_{\alpha=e,\mu,\tau}
c_i^\alpha\Psi_\alpha^{\rm folha}.
$$

Critério de sucesso:

1. três autovalores reais;
2. autovetores $G^\nu$-ortonormais;
3. ordenação espectral estável sob pequenas variações de contorno;
4. gap suficiente para definir três canais de oscilação.

---

### Etapa 5 — Obter a normalização absoluta $Z_\nu$

Os autovalores $\lambda_i$ são geométricos/adimensionais. Para convertê-los em
unidades físicas:

$$
m_i^2c^4
=
Z_\nu E_C^2\lambda_i.
$$

O fator $Z_\nu$ deve vir do fluxo global--local do canal neutro:

$$
Z_\nu
=
\frac{
\text{fluxo inercial neutro físico}
}{
\text{fluxo geométrico normalizado}
}.
$$

Rota preferida:

$$
Z_\nu
\leftarrow
\text{corrente simplética ponderada}
\to
\text{normalização do modo beta}
\to
\text{transporte para folhas}.
$$

Critério de sucesso: $Z_\nu$ não pode ser escolhido para bater
$\Delta m^2$; deve ser calculado antes da comparação.

---

### Etapa 6 — Calcular diferenças quadradas e massas

Depois de $Z_\nu$:

$$
\Delta m_{ij}^2
=
\frac{Z_\nu E_C^2}{c^4}
(\lambda_i-\lambda_j).
$$

Para massas absolutas, há duas possibilidades:

1. se o menor autovalor for fixado geometricamente:

$$
m_i^2
=
\frac{Z_\nu E_C^2}{c^4}
\lambda_i;
$$

2. se só as diferenças forem fixadas pelo setor oscilatório:

$$
m_i^2=m_0^2+\Delta_i,
$$

com $m_0$ determinado por condição global cosmológica, não por oscilação.

Critério de fechamento forte: a GDQ deve decidir entre essas duas rotas por
estrutura, não por ajuste.

---

### Etapa 7 — Calcular a matriz de projeção folha--modo

Calcular:

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

Na redução operacional:

$$
\mathsf U^{\rm GDQ}
\mapsto
U_{\rm PMNS}.
$$

Critério de sucesso: a matriz deve ser unitária no produto interno físico
após ortonormalização por $G^\nu$.

---

### Etapa 8 — Comparar sem reajuste

Somente depois de congelar:

$$
G^\nu,
\qquad
K^\nu,
\qquad
Z_\nu,
\qquad
\mathsf U^{\rm GDQ},
$$

comparar com:

$$
\Delta m_{21}^2,
\qquad
\Delta m_{31}^2,
\qquad
\theta_{12},
\qquad
\theta_{23},
\qquad
\theta_{13}.
$$

Classificação possível:

| Resultado | Classificação |
|---|---|
| $K^\nu$ e $G^\nu$ derivados, mas $Z_\nu$ ausente | fechamento estrutural |
| $\Delta m^2$ obtidos sem dados de oscilação | previsão forte de oscilação |
| massas absolutas obtidas sem entrada cosmológica | previsão metrológica absoluta |
| só massas relativas obtidas | fechamento oscilatório, não cosmológico |
| coeficiente escolhido para bater NuFIT | engenharia inversa |

---

## 4. Plano numérico mínimo

Criar um script em três camadas:

1. `construir_base_folhas_q53.py`;
2. `calcular_gram_hessiana_neutra_q53.py`;
3. `diagonalizar_modos_neutros_q53.py`.

O primeiro mock permitido deve ser classificado apenas como teste estrutural:

$$
G^\nu_{\rm mock},
\qquad
K^\nu_{\rm mock}.
$$

Ele serve para validar:

- diagonalização generalizada;
- normalização dos autovetores;
- extração de $\mathsf U^{\rm GDQ}$;
- sensibilidade a termos fora da diagonal;
- convenção de ordenação dos modos.

Não deve ser usado como previsão.

---

## 5. Critério de fechamento da Q53 para massas

A parte de massas da Q53 estará fortemente fechada quando existir:

$$
\boxed{
\mathcal S_{\rm GDQ}
\to
\Phi_*^{\rm neutro}
\to
G^\nu,K^\nu
\to
K^\nu c_i=\lambda_iG^\nu c_i
\to
Z_\nu
\to
m_i^2
}
$$

com:

1. nenhum dado de oscilação usado na construção;
2. unidades restauradas explicitamente;
3. três autovalores estáveis;
4. comparação posterior com NuFIT;
5. sensibilidade a contorno documentada.
