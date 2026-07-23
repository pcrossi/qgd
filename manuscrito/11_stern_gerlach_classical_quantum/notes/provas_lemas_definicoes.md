---
title: "Provas, lemas e definições — Capítulo 11"
---

# Provas, lemas e definições — Capítulo 11

Esta nota conserva a construção técnica de Stern--Gerlach na GDQ. O
experimento é tratado como interação entre:

1. um sóliton que já possui circulação/spin;
2. um campo magnético clássico produzido por aparelho;
3. uma interface que seleciona eixo, canais e resposta;
4. uma tela que registra dois feixes separados.

A ação oficial não é modificada. O aparelho fornece fonte/contorno clássico.

## 1. Enunciado físico

Stern--Gerlach exige explicar:

1. por que aparecem dois canais;
2. por que o eixo é o do aparelho;
3. por que a população dos canais depende do ângulo de preparação;
4. por que cada canal sofre deflexão mecânica;
5. por que medições sequenciais em eixos diferentes não revelam uma tabela
   preexistente de valores.

A cadeia GDQ é

$$
J_{\rm SG}^{\rm classico}
\to
\Phi_*^{\rm SG}
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\mathsf R_{\rm SG}
\to
P_{\mathbf n}^{\pm}
\to
\Delta z_\pm
\to
\text{registro}.
$$

## 2. Spin antes da medição

O spin não é criado pelo aparelho. O objeto já possui um módulo interno de
circulação/Hopf. No setor espinorial reduzido, a orientação é representada por
um vetor unitário $\mathbf a$ e pela matriz densidade

$$
\varrho_{\mathbf a}
=
\frac12(I+\mathbf a\cdot\sigma).
$$

A função do aparelho é selecionar uma direção $\mathbf n$, não fabricar o
spin.

## 3. Fonte magnética clássica

O campo do aparelho é dado externo:

$$
\mathbf n(\mathbf x)
=
\frac{\mathbf B(\mathbf x)}{|\mathbf B(\mathbf x)|}.
$$

No regime de gradiente aproximadamente uniforme,

$$
B_z(z)
\simeq
B_0+z\,\partial_zB_z.
$$

Esse dado entra como fonte/contorno clássico:

$$
K_{\rm phys}^{\rm obj}\,\delta\Phi_{\rm SG}
=
J_{\rm SG}^{\rm classico}.
$$

Aqui $K_{\rm phys}^{\rm obj}$ é a Hessiana física projetada do objeto. A
resposta $\delta\Phi_{\rm SG}$ é calculada; não é inserida como operador
quântico manual.

## 4. Projetores de Hopf/Clifford

O eixo $\mathbf n$ define dois projetores:

$$
P_{\mathbf n}^{\pm}
=
\frac12(I\pm\mathbf n\cdot\sigma).
$$

Eles satisfazem

$$
(P_{\mathbf n}^{\pm})^2=P_{\mathbf n}^{\pm},
\qquad
P_{\mathbf n}^{+}P_{\mathbf n}^{-}=0,
\qquad
P_{\mathbf n}^{+}+P_{\mathbf n}^{-}=I.
$$

A razão geométrica é que o elo de Hopf da fatia normal possui dois autosectores
estáveis quando o aparelho quebra a isotropia por um eixo uniaxial. Em
linguagem reduzida, esses setores são os autoprojetores de
$\mathbf n\cdot\sigma$.

O script `scripts/verificar_atlas_hopf_sg.py` verifica a colagem de cartas, o
projetor e a métrica de Fubini--Study no modelo reduzido de Hopf.

## 5. Pesos angulares

Com preparação $\mathbf a$ e aparelho no eixo $\mathbf n$, Born operacional do
Capítulo 9 fornece

$$
p_\pm(\mathbf n|\mathbf a)
=
\operatorname{Tr}(\varrho_{\mathbf a}P_{\mathbf n}^{\pm}).
$$

Substituindo,

$$
p_\pm
=
\operatorname{Tr}
\left[
\frac12(I+\mathbf a\cdot\sigma)
\frac12(I\pm\mathbf n\cdot\sigma)
\right].
$$

Usando

$$
\operatorname{Tr}(\sigma_i)=0,
\qquad
\operatorname{Tr}(\sigma_i\sigma_j)=2\delta_{ij},
$$

obtemos

$$
p_\pm(\mathbf n|\mathbf a)
=
\frac{1\pm\mathbf a\cdot\mathbf n}{2}.
$$

Se $\theta$ é o ângulo entre $\mathbf a$ e $\mathbf n$,

$$
p_+=\cos^2\frac{\theta}{2},
\qquad
p_-=\sin^2\frac{\theta}{2}.
$$

O script `scripts/calcular_pesos_sg.py` preserva essa conta e gera a tabela de
pesos angulares.

## 6. Força e deflexão no canal fixo

No canal adiabático fixo, a energia de interface reduzida é

$$
E_\pm(z)
=
\mp\mu B_z(z).
$$

A força é

$$
F_z^\pm
=
-\partial_zE_\pm
=
\pm\mu\,\partial_zB_z.
$$

Se a partícula atravessa uma região de comprimento $L$ com velocidade
longitudinal $v_y$, o tempo de interação é

$$
t_{\rm int}=\frac{L}{v_y}.
$$

A deflexão durante a região de campo é

$$
\Delta z_\pm
=
\frac12\frac{F_z^\pm}{m}t_{\rm int}^2.
$$

Portanto

$$
\Delta z_\pm
=
\pm
\frac{\mu L^2}{2mv_y^2}
\partial_zB_z.
$$

Depois da região de campo, um trecho livre adicional soma deslocamento por
velocidade transversal adquirida. O script `scripts/simular_deflexao_sg.py`
implementa a versão reduzida.

## 7. Medições sequenciais

Se dois aparelhos medem eixos $\mathbf n$ e $\mathbf m$, os projetores
geralmente não comutam:

$$
[P_{\mathbf n}^{+},P_{\mathbf m}^{+}]
\ne0
\quad
\text{se}
\quad
\mathbf n\times\mathbf m\ne0.
$$

Logo uma sequência $z\to x\to z$ não mede a mesma decomposição duas vezes. O
aparelho intermediário redefine a decomposição estável. Para eixos
ortogonais, após selecionar $z+$ e medir $x$, a nova medição de $z$ volta a
dar

$$
p(z+)=p(z-)=\frac12.
$$

Os scripts `scripts/testar_sequencias_sg.py` e
`scripts/simular_sequencias_sg.py` verificam esse comportamento operacional.

## 8. Condição adiabática

A prova de dois canais limpos assume que o eixo efetivo muda lentamente na
escala do gap entre canais. Em forma reduzida,

$$
\frac{|\langle -|\dot H|+\rangle|}
{\Delta E^2}
\ll1.
$$

Se essa condição falha, transições não adiabáticas aparecem. A população deixa
de ser martingal QND simples e a dinâmica completa de interface deve ser
resolvida. Isso delimita o alcance da prova, não a contradiz.

O script `scripts/simular_nao_adiabatico_sg.py` preserva esse limite por um
teste Landau--Zener reduzido.

## 9. Aparelho magnético como Schur/DtN

Para metrologia fina, a impedância do aparelho é

$$
\mathsf R_{\rm SG}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

O bloco $Y$ representa a interface medida; o bloco $I$ representa graus
internos não monitorados. A forma é equivalente a um operador
Dirichlet--to--Neumann: dado o traço na interface, resolve-se o interior e
retorna-se o momento normal conjugado.

Essa expressão define como calcular $\kappa_H^{\rm SG}$, $\Gamma_{\rm SG}$ e
perdas de um aparelho real. Sem geometria/material/perfil de campo reais, não
há número metrológico universal.

## 10. Resultados numéricos preservados

Os scripts do capítulo são classificados em três grupos:

| Grupo | Exemplos | Uso |
|---|---|---|
| Identidades estruturais | `calcular_pesos_sg.py`, `verificar_atlas_hopf_sg.py`, `testar_sequencias_sg.py` | Preservam projetores, pesos e composição. |
| Reduções de aparelho | `simular_deflexao_sg.py`, `simular_feixe_sg_completo.py`, `resolver_dtn_hopf_cilindrico_sg.py` | Verificam fórmulas reduzidas. |
| Diagnósticos/limites | `simular_nao_adiabatico_sg.py`, `testar_zh_gaussiano_sg.py`, `testar_pipeline_background_sg.py` | Delimitam alcance; não são previsão física final. |

Scripts marcados como fixture, teste de método ou diagnóstico negativo não
devem ser citados como validação metrológica da GDQ.

## 11. Status

| Item | Status | Limite |
|---|---|---|
| Spin/circulação antes da medição | Fechado estruturalmente | Vem do Capítulo 10. |
| Eixo do aparelho | Fechado | É fonte/contorno clássico. |
| Dois canais | Fechado estruturalmente | Projetores Hopf/Clifford. |
| Pesos angulares | Fechados operacionalmente | Born do Capítulo 9. |
| Deflexão | Fechada no canal reduzido | Usa campo clássico dado. |
| Sequências incompatíveis | Fechadas operacionalmente | Projetores não comutam. |
| $\mathsf R_{\rm SG}$ real | Programa metrológico | Exige aparelho/material reais. |

