# Plano de solução completa — Q48 Hidrogênio

## 1. Objetivo

Construir uma resposta completa da GDQ para o hidrogênio, incluindo:

1. equação espinorial correta;
2. espectro;
3. degenerescências;
4. estrutura fina;
5. estrutura hiperfina;
6. Lamb shift;
7. dependência do raio do próton;
8. comparação sem ajuste posterior.

Restrição principal:

$$
\boxed{
\text{a equação escalar radial do legado não substitui a equação espinorial.}
}
$$

Ela pode ser reaproveitada apenas como limite radial efetivo depois da projeção
espinorial correta.

---

## 2. Princípio de solução

A Q48 deve seguir a cadeia:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{p,*}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathcal D^{B}_{p,e}
\to
\mathcal D^{B}_{n\kappa}
\to
\text{espectro}
\to
\text{correções}
\to
\text{comparação}.
$$

Onde:

- $\Phi_{p,*}$ é o background protônico/bariônico da Q40;
- $\mathcal D^{B}_{p,e}$ é a redução espinorial Dirac--Bismut efetiva da
  Hessiana física da GDQ;
- $\mathcal D^{B}_{n\kappa}$ é o operador radial espinorial central;
- os potenciais, fatores de forma e impedâncias entram como projeções,
  contornos ou respostas da Hessiana, não como termos fundamentais novos.

---

## 3. Dados já disponíveis e como usá-los

### 3.1 Ação oficial

A ação oficial permanece fixa:

$$
\mathcal{S}_{\mathrm{GDQ}}
=
\int_{\gamma}
\left[
\int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(
\mathcal R
+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+
\frac{f+\bar f}{2}
-
n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]
\frac{d\tau}{\tau}.
$$

Classificação:

$$
\boxed{\text{axioma dinâmico vigente.}}
$$

### 3.2 Spin e equação espinorial

Da Q26:

$$
\psi\in\Gamma(S\otimes E),
\qquad
\{\gamma^a,\gamma^b\}=2\eta^{ab}.
$$

Uso em Q48:

1. construir o fibrado espinorial físico $S$;
2. acoplar a linha de carga $L_Q$;
3. escrever o operador espinorial efetivo;
4. só depois reduzir a equações radiais.

### 3.3 Estrutura fina

Da Q37:

$$
\alpha_{\rm lab}=\alpha_E^{\rm mean}
$$

condicionalmente ao ensemble isotrópico de Einstein e à ponte global--local.

Uso em Q48:

$$
\boxed{
\alpha\text{ entra congelada antes da comparação espectral.}
}
$$

Não usar hidrogênio para ajustar $\alpha$.

### 3.4 Próton

Da Q40:

O próton é um background bariônico composto, não uma carga pontual
fundamental. A aproximação pontual é permitida apenas como limite:

$$
r_p\to0,
\qquad
F_p(q^2)\to1.
$$

Uso em Q48:

1. começar com próton pesado e pontual para obter o limite líder;
2. depois inserir fator de forma e contorno de superfície;
3. separar hidrogênio eletrônico e muônico.

### 3.5 Momento magnético e $g=2$

Da Q43:

$$
g_0=2
$$

é a parte mínima protegida por Noether. Correções vêm da resposta transversal:

$$
\Delta\gamma_{\rm geom}
=
\frac{\langle c,H_C^{-1}m_\perp\rangle}
     {\langle c,H_C^{-1}c\rangle}.
$$

Uso em Q48:

1. estrutura hiperfina;
2. correção magnética do elétron;
3. acoplamento spin--spin elétron--próton;
4. separar termo mínimo e anomalia.

---

## 4. Extração máxima do Capítulo 38 legado

### 4.1 Bloco aproveitável A — campo fraco

O legado fornece:

$$
\frac{d^2 \mathcal R}{dr^2}
+
\frac{2}{r}\frac{d\mathcal R}{dr}
+
\left[
\frac{E^2-m_e^2c^4}{\hbar^2c^2}
+
\frac{2E\alpha}{\hbar c r}
-
\frac{\ell(\ell+1)-4\alpha^2}{r^2}
\right]\mathcal R=0.
$$

Reclassificação:

$$
\boxed{
\text{equação radial escalar efetiva spin-projetada.}
}
$$

Uso:

1. comparação com o limite espinorial;
2. auditoria do termo torsional $-4\alpha^2/r^2$;
3. ponto de partida para o limite radial se a projeção espinorial produzir o
   mesmo operador quadrado.

### 4.2 Bloco aproveitável B — Frobenius/Kummer/Whittaker

O legado já organiza:

1. comportamento no infinito;
2. equação indicial no núcleo;
3. truncamento por polinômios;
4. quantização por condição de integrabilidade.

Uso:

$$
\boxed{
\text{reaproveitar como técnica de solução radial, não como ontologia.}
}
$$

### 4.3 Bloco aproveitável C — campo próximo/Heun/Hill

O legado contém a ideia de que termos de campo próximo geram:

1. relação multi-termo;
2. determinantes de Hill;
3. quebra da degenerescência $2s_{1/2}$--$2p_{1/2}$;
4. interpretação geométrica do Lamb shift.

Uso:

$$
\boxed{
\text{transformar em problema espectral da Hessiana com domínio e contorno.}
}
$$

### 4.4 Bloco aproveitável D — hidrogênio muônico

O legado contém:

1. múon como sonda de campo próximo;
2. raio orbital reduzido;
3. acoplamento solitônico bidirecional;
4. contração efetiva do raio do próton.

Uso:

$$
\boxed{
\text{base física para dependência dinâmica do raio/fator de forma do próton.}
}
$$

---

## 5. Fase I — Construção do operador espinorial

### 5.1 Enunciado da fase

Construir a equação efetiva correta:

$$
\mathcal D_H\psi=0,
\qquad
\psi\in\Gamma(S\otimes L_Q).
$$

### 5.2 Forma esperada

No setor local físico:

$$
\mathcal D_H\psi
=
\left[
i\hbar c\,\gamma^a e_a{}^\mu
\left(
\nabla_\mu^B
+
\frac{iQ}{\hbar c}A_\mu^{(p)}
\right)
-
m_ec^2
\right]\psi.
$$

Classificação:

$$
\boxed{
\text{redução efetiva espinorial da Hessiana GDQ.}
}
$$

Não é ação fundamental nova.

### 5.3 Tarefas

1. Definir $S\otimes L_Q$ no espaço físico reconstruído.
2. Definir $\nabla^B$ com conexão de Bismut.
3. Projetar o modo eletromagnético do próton:

   $$
   A_\mu^{(p)}
   =
   \text{projeção }U(1)\text{ do background }\Phi_{p,*}.
   $$

4. Definir o produto interno:

   $$
   \langle\psi,\varphi\rangle
   =
   \int_{\Sigma}
   \psi^\dagger\varphi\,
   d\mu_{\rm phys}.
   $$

5. Definir domínio:

   $$
   \mathcal D(\mathcal D_H)
   =
   H^1_{\rm loc}(\Sigma,S\otimes L_Q)
   \cap
   \text{condições de bordo GDQ}.
   $$

6. Definir contorno curto:

   $$
   \mathsf R_p(r_p)
   \psi|_{\partial\mathcal N_p}
   +
   n^a\nabla_a^B\psi|_{\partial\mathcal N_p}
   =0.
   $$

7. Mostrar auto-adjunticidade física depois da projeção de gauge/modos nulos.

### 5.4 Produto

Criar:

$$
\texttt{questoes/q48/associados/operador_espinorial_hidrogenio.md}.
$$

---

## 6. Fase II — Redução central e espectro líder

### 6.1 Limite de Coulomb

Hipóteses:

1. próton pesado;
2. fundo local assintoticamente plano;
3. raio do próton negligenciado;
4. campo externo ausente;
5. torção residual apenas no acoplamento espinorial mínimo.

Então:

$$
A_0^{(p)}(r)
\simeq
\frac{e}{4\pi\varepsilon_0 r},
\qquad
\boldsymbol A^{(p)}\simeq0.
$$

### 6.2 Separação espinorial

Usar os harmônicos espinoriais:

$$
\Omega_{\kappa m}(\theta,\phi).
$$

Escrever:

$$
\psi_{E\kappa m}(r,\theta,\phi)
=
\frac1r
\begin{pmatrix}
G_{E\kappa}(r)\Omega_{\kappa m}\\
iF_{E\kappa}(r)\Omega_{-\kappa m}
\end{pmatrix}.
$$

Com:

$$
\kappa=
\begin{cases}
-(j+1/2), & j=\ell+1/2,\\
+(j+1/2), & j=\ell-1/2.
\end{cases}
$$

### 6.3 Sistema radial

Derivar o par de equações radiais acopladas:

$$
\frac{dG}{dr}
+
\frac{\kappa}{r}G
-
\frac{1}{\hbar c}
\left(
m_ec^2+E-V(r)
\right)F
=0,
$$

$$
\frac{dF}{dr}
-
\frac{\kappa}{r}F
+
\frac{1}{\hbar c}
\left(
m_ec^2-E+V(r)
\right)G
=0.
$$

### 6.4 Espectro líder

Obter:

$$
E_{n\kappa}
=
m_ec^2
\left[
1+
\frac{(Z\alpha)^2}
{
\left(
n-|\kappa|
+
\sqrt{\kappa^2-(Z\alpha)^2}
\right)^2
}
\right]^{-1/2}.
$$

Para hidrogênio:

$$
Z=1.
$$

### 6.5 Produto

Criar:

$$
\texttt{questoes/q48/associados/espectro_sommerfeld_dirac_gdq.md}.
$$

---

## 7. Fase III — Degenerescências e estrutura fina

### 7.1 Degenerescências

O espectro líder depende de:

$$
n,
\qquad
j=|\kappa|-\frac12,
$$

mas não de $m_j$. Logo:

$$
\deg(m_j)=2j+1.
$$

O problema escalar legado não organiza corretamente esta estrutura porque usa
$\ell$ em vez de $\kappa$.

### 7.2 Expansão fina

Expandir:

$$
E_{nj}
=
m_ec^2
-
\frac{m_ec^2\alpha^2}{2n^2}
-
\frac{m_ec^2\alpha^4}{2n^4}
\left(
\frac{n}{j+1/2}
-
\frac34
\right)
+
O(\alpha^6).
$$

Energia de ligação:

$$
\Delta E_{nj}
=
E_{nj}-m_ec^2.
$$

### 7.3 Produto

Criar:

$$
\texttt{questoes/q48/associados/degenerescencias_estrutura_fina.md}.
$$

---

## 8. Fase IV — Estrutura hiperfina

### 8.1 Origem GDQ

A estrutura hiperfina deve vir de:

1. circulação/spin do elétron;
2. circulação/spin do próton;
3. momento magnético mínimo protegido por Noether;
4. fator de forma e impedância de superfície do próton.

Não inserir o Hamiltoniano hiperfino como axioma. Ele deve surgir como
redução efetiva da resposta magnética:

$$
\Phi_p
\to
J^{\rm mag}_p
\to
\operatorname{Hess}^{-1}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm mag}^{p,e}
\to
\Delta E_{\rm hfs}.
$$

### 8.2 Forma efetiva esperada

No limite pontual:

$$
\Delta E_{\rm hfs}
\propto
\boldsymbol\mu_e\cdot\boldsymbol\mu_p
\,|\psi_{n0}(0)|^2
$$

para estados $s$.

A fórmula efetiva final deve ser escrita com:

1. massa reduzida;
2. $g_e$ mínimo mais correção geométrica;
3. $g_p$ ou momento magnético protônico herdado da Q40;
4. fator de forma $F_p(q^2)$;
5. correção de recuo.

### 8.3 Produto

Criar:

$$
\texttt{questoes/q48/associados/estrutura_hiperfina_gdq.md}.
$$

---

## 9. Fase V — Lamb shift

### 9.1 O que não fazer

Não declarar Lamb shift resolvido apenas porque o legado possui um termo
proporcional a:

$$
\frac{\chi_3}{r^3}.
$$

Isso é sugestivo, mas não é ainda a correção espectral completa.

### 9.2 Rota GDQ correta

Construir o operador de campo próximo:

$$
\mathcal D_H
=
\mathcal D_{\rm Coul}
+
\delta\mathcal D_{\rm near}.
$$

A perturbação $\delta\mathcal D_{\rm near}$ deve vir de:

1. expansão do background protônico;
2. torção de Bismut;
3. fator de forma/projeção de superfície;
4. DtN/Schur da região interna;
5. domínio auto-adjunto.

### 9.3 Observável

Calcular:

$$
\Delta E_{\rm Lamb}
=
E(2s_{1/2})-E(2p_{1/2}).
$$

No primeiro nível:

$$
\Delta E_{\rm Lamb}
=
\langle 2s_{1/2}|
\delta H_{\rm near}
|2s_{1/2}\rangle
-
\langle 2p_{1/2}|
\delta H_{\rm near}
|2p_{1/2}\rangle.
$$

No nível completo:

$$
\det H_{\rm Hill}(E)=0
$$

ou forma equivalente por operador radial discretizado/convergente.

### 9.4 Produto

Criar:

$$
\texttt{questoes/q48/associados/lamb_shift_hill_heun_gdq.md}.
$$

---

## 10. Fase VI — Raio do próton e hidrogênio muônico

### 10.1 Raio como contorno/fator de forma

O raio do próton entra por:

$$
F_p(q^2),
\qquad
\mathsf R_p(r_p),
\qquad
\partial\mathcal N_p.
$$

Não deve ser um número livre ajustado em Q48. Deve vir de Q40 ou ser declarado
como dado experimental de comparação.

### 10.2 Correção líder de tamanho finito

No limite efetivo:

$$
\Delta E_{\rm fs}(ns)
\simeq
\frac{2}{3}
(Z\alpha)^4
\mu^3
r_p^2
\frac{1}{n^3}
$$

em unidades naturais, com $\mu$ massa reduzida.

Na redação final, a fórmula deve ser escrita com unidades restauradas e
normalização consistente.

### 10.3 Hidrogênio muônico

Para o múon:

$$
a_{\mu p}
\sim
\frac{a_0}{m_\mu/m_e}.
$$

Logo o campo próximo pesa muito mais. A Q48 deve separar:

1. raio livre do próton;
2. raio efetivo sob sonda muônica;
3. contração solitônica bidirecional;
4. comparação com Lamb shift muônico.

### 10.4 Produto

Criar:

$$
\texttt{questoes/q48/associados/raio_proton_hidrogenio_muonico.md}.
$$

---

## 11. Fase VII — Comparação sem ajuste posterior

### 11.1 Parâmetros congelados

Antes de comparar, congelar:

1. $\alpha$ da Q37;
2. $m_e$ por calibração metrológica;
3. $m_p$ da Q40/metrologia;
4. $r_p$ ou $F_p$ da Q40;
5. $g_e$ mínimo da Q43 e, se usado, correção geométrica declarada;
6. momento magnético do próton da Q40/Q43;
7. domínio e contorno do operador.

### 11.2 Observáveis mínimos

Comparar:

1. níveis Dirac para $1s$, $2s$, $2p_{1/2}$, $2p_{3/2}$;
2. estrutura fina $2p_{3/2}-2p_{1/2}$;
3. hiperfina $1s$;
4. Lamb shift $2s_{1/2}-2p_{1/2}$;
5. deslocamento de tamanho finito;
6. hidrogênio muônico.

### 11.3 Classificação numérica

Cada comparação deve indicar:

| Resultado | Classificação possível |
|---|---|
| Espectro Dirac líder | derivação/redução efetiva |
| Estrutura fina | derivação efetiva |
| Hiperfina com $\mu_p$ experimental | comparação fenomenológica |
| Hiperfina com $\mu_p$ GDQ | previsão condicional |
| Lamb shift por operador de campo próximo | previsão condicional se sem ajuste |
| Raio do próton inserido por dado externo | comparação/calibração |
| Raio do próton vindo de Q40 | previsão condicional |

### 11.4 Produto

Criar:

$$
\texttt{questoes/q48/associados/comparacao_metrologica_hidrogenio.md}.
$$

---

## 12. Fase VIII — Scripts numéricos

### 12.1 Script 1 — espectro Dirac líder

Arquivo:

$$
\texttt{questoes/q48/associados/calcular_espectro_dirac_hidrogenio_q48.py}.
$$

Função:

1. calcular $E_{n\kappa}$;
2. listar degenerescências;
3. comparar com valores de referência.

Classificação:

$$
\boxed{\text{avaliação direta de fórmula derivada.}}
$$

### 12.2 Script 2 — expansão fina

Arquivo:

$$
\texttt{questoes/q48/associados/calcular_estrutura_fina_q48.py}.
$$

Função:

1. comparar fórmula exata e expansão em $\alpha$;
2. medir erro da expansão.

Classificação:

$$
\boxed{\text{teste de consistência.}}
$$

### 12.3 Script 3 — tamanho finito

Arquivo:

$$
\texttt{questoes/q48/associados/calcular_tamanho_finito_q48.py}.
$$

Função:

1. calcular sensibilidade a $r_p$;
2. comparar eletrônico e muônico;
3. separar dado externo de valor GDQ.

Classificação:

$$
\boxed{\text{comparação fenomenológica ou previsão condicional, conforme entrada.}}
$$

### 12.4 Script 4 — operador radial discretizado

Arquivo:

$$
\texttt{questoes/q48/associados/solver_radial_dirac_bismut_q48.py}.
$$

Função:

1. montar operador radial;
2. impor contornos;
3. verificar convergência de malha;
4. reproduzir espectro líder;
5. depois ativar campo próximo.

Classificação inicial:

$$
\boxed{\text{teste de convergência e consistência.}}
$$

### 12.5 Script 5 — Lamb/Hill

Arquivo:

$$
\texttt{questoes/q48/associados/solver_lamb_hill_q48.py}.
$$

Função:

1. montar matriz multi-termo;
2. resolver determinante de Hill truncado;
3. estudar convergência do truncamento;
4. comparar $2s_{1/2}$ e $2p_{1/2}$.

Classificação:

$$
\boxed{\text{previsão condicional se os coeficientes vierem da Hessiana.}}
$$

---

## 13. Critérios de fechamento

A Q48 só deve ser declarada fechada se todos os itens abaixo estiverem
cumpridos.

### 13.1 Fechamento estrutural

1. operador espinorial Dirac--Bismut derivado como redução da Hessiana;
2. domínio e contornos definidos;
3. limite Coulomb obtido;
4. espectro $E_{n\kappa}$ derivado;
5. degenerescências corretas demonstradas;
6. equação escalar legada reclassificada como limite radial.

Status possível:

$$
\boxed{\text{fechada estruturalmente.}}
$$

### 13.2 Fechamento físico-metrológico

Além do fechamento estrutural:

1. hiperfina calculada com momento protônico definido;
2. Lamb shift calculado por Hessiana/campo próximo;
3. raio do próton/fator de forma herdado de Q40 ou declarado;
4. comparação experimental sem pós-ajuste;
5. estudo de sensibilidade e convergência.

Status possível:

$$
\boxed{\text{fechada condicionalmente ou fechada, conforme hipóteses restantes.}}
$$

---

## 14. Ordem prática recomendada

Executar nesta ordem:

1. `operador_espinorial_hidrogenio.md`;
2. `espectro_sommerfeld_dirac_gdq.md`;
3. `degenerescencias_estrutura_fina.md`;
4. `calcular_espectro_dirac_hidrogenio_q48.py`;
5. `calcular_estrutura_fina_q48.py`;
6. `estrutura_hiperfina_gdq.md`;
7. `raio_proton_hidrogenio_muonico.md`;
8. `calcular_tamanho_finito_q48.py`;
9. `lamb_shift_hill_heun_gdq.md`;
10. `solver_radial_dirac_bismut_q48.py`;
11. `solver_lamb_hill_q48.py`;
12. `comparacao_metrologica_hidrogenio.md`;
13. consolidar `questao_48.md`.

---

## 15. Pontos de atenção

1. Não chamar a equação radial escalar de equação fundamental do hidrogênio.
2. Não usar $\alpha$ ajustado pelo hidrogênio.
3. Não usar raio do próton experimental como previsão GDQ sem declarar.
4. Não misturar QED ontológica com GDQ; QED serve como comparação/redução.
5. Não declarar Lamb shift fechado sem operador, domínio e coeficientes.
6. Não declarar hiperfina fechada se o momento magnético do próton for dado
   externo.
7. Não ocultar o uso de massa reduzida.
8. Separar hidrogênio eletrônico, deutério se aparecer, e hidrogênio muônico.

---

## 16. Veredito do plano

Este plano deve permitir extrair todo o material aproveitável do legado e
resolver a Q48 sem reduzir a GDQ à mecânica quântica padrão.

O primeiro fechamento esperado é estrutural:

$$
\boxed{
\text{GDQ} \to \text{Dirac--Bismut efetivo} \to
\text{Sommerfeld--Dirac com degenerescências corretas.}
}
$$

O fechamento completo exige depois:

$$
\boxed{
\text{hiperfina + Lamb shift + raio do próton + comparação sem ajuste.}
}
$$
