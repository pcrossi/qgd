# Aplicação metodológica — Q44, dupla fenda com detector

## 1. Status

Esta nota registra a Q44 como aplicação do pipeline metodológico reutilizável
da GDQ.

$$
\boxed{
\text{Q44 fechada condicionalmente no setor Madelung com detector linear reduzido.}
}
$$

O fechamento é estrutural. Ele não é uma previsão metrológica para um material
real específico.

---

## 2. Classificação dos elementos

| Elemento | Classificação | Observação |
|---|---|---|
| Ação oficial | axioma dinâmico | preservada; não é alterada pelo detector |
| Setor Madelung | redução efetiva | usado em fundo fixo/plano |
| Barreira de duas fendas | contorno clássico | dado externo do aparelho |
| Detector | fonte/contorno clássico | entra por impedância de interface |
| $K_{\rm det}$ | Hessiana efetiva reduzida | canal material linear mínimo |
| $\mathsf R_{\rm det}$ | DtN/Schur | resposta de contorno do detector |
| $\Gamma_{\rm det}$ | forma quadrática de resposta | custo de distinguir caminhos |
| $e^{-\Gamma_{\rm det}}$ | observável reduzido | coeficiente do termo de coerência |
| $\lambda_{\rm det},L,\zeta_{\rm det}$ | parâmetros de aparelho | devem vir do material real em aplicação metrológica |

---

## 3. Pipeline aplicado

O pipeline geral:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_*
\to
P_{\rm phys}
\to
K_{\rm phys}
\to
J_{\rm app}
\to
\delta\Phi
\to
\mathsf R_{\rm app}
\to
\mathcal O_{\rm obs}
$$

fica, na Q44 reduzida:

$$
\mathcal S_{\rm GDQ}
\to
(\rho,S_R)_{\rm Madelung}
\to
\text{fundo plano}
\to
K_{\rm det}
\to
\Delta\Phi_\partial
\to
\mathsf R_{\rm det}
\to
\Gamma_{\rm det}
\to
\rho_{\rm anteparo}.
$$

Neste fechamento, $P_{\rm phys}$ e $K_{\rm phys}$ completos do bulk não são
calculados. Eles são substituídos pelo setor físico reduzido de Madelung e
pelo canal linear do detector. Por isso o status é condicional.

---

## 4. Equação resolvida

A dupla fenda sem detector é tratada pela redução Madelung:

$$
\partial_t\rho+\nabla\cdot\left(\rho\frac{\nabla S_R}{m}\right)=0,
$$

$$
\partial_tS_R+\frac{|\nabla S_R|^2}{2m}
+V_{\rm app}
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}=0.
$$

O potencial $V_{\rm app}$ representa o contorno clássico da barreira e das
fendas. Ele não é termo novo da ação oficial.

---

## 5. Background e domínio

O domínio reduzido é uma seção plana:

$$
\Omega\subset\mathbb R^2_{x,y}.
$$

A barreira fica em $y=0$ e possui duas aberturas centradas em:

$$
x=\pm\frac d2.
$$

A métrica é mantida fixa:

$$
g_{ij}\simeq\delta_{ij}.
$$

Portanto, a Q44 não afirma evolução completa de $(g,J,H,f,\mathcal U)$ pela
ação oficial. Ela afirma a solução do setor hidrodinâmico reduzido em fundo
estacionário.

---

## 6. Detector como DtN/Schur

O canal material linear reduzido é:

$$
s\in[0,L],
$$

com Hessiana:

$$
K_{\rm det}
=
-\partial_s^2+\lambda_{\rm det}^2.
$$

O funcional quadrático é:

$$
S_{\rm det}^{(2)}[\varphi]
=
\frac12
\int_0^L
\left[
(\partial_s\varphi)^2+\lambda_{\rm det}^2\varphi^2
\right]ds.
$$

Com:

$$
\varphi(0)=\varphi_0,
\qquad
\varphi(L)=0,
$$

a solução interna fornece:

$$
\mathsf R_{\rm det}
=
\lambda_{\rm det}\coth(\lambda_{\rm det}L).
$$

Equivalentemente, discretizando graus internos:

$$
\mathsf R_{\rm det}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Essa é a parte reutilizável: o detector atua por eliminação de graus internos,
não por colapso postulado.

---

## 7. Fator de decoerência

A diferença de marcação entre os caminhos é:

$$
\Delta\Phi_\partial
=
\zeta_{\rm det}(w_1-w_2),
$$

com:

$$
\int_{\partial\Omega}(w_1-w_2)^2d\Sigma=C_{\rm path}.
$$

O custo quadrático é:

$$
\Gamma_{\rm det}
=
\frac12
\int_{\partial\Omega}
\Delta\Phi_\partial
\mathsf R_{\rm det}
\Delta\Phi_\partial
d\Sigma.
$$

Logo:

$$
\boxed{
\Gamma_{\rm det}
=
\frac12
\zeta_{\rm det}^2
C_{\rm path}
\lambda_{\rm det}\coth(\lambda_{\rm det}L).
}
$$

A densidade no anteparo é:

$$
\boxed{
\rho_{\rm det}
=
I_1+I_2
+2e^{-\Gamma_{\rm det}}\sqrt{I_1I_2}\cos\Delta\phi.
}
$$

O observável direto de coerência é:

$$
\boxed{
\mathcal C=e^{-\Gamma_{\rm det}}.
}
$$

---

## 8. Interpretação física

Sem detector:

$$
\Gamma_{\rm det}=0
\quad\Rightarrow\quad
\text{franjas coerentes.}
$$

Com detector forte:

$$
\Gamma_{\rm det}\gg1
\quad\Rightarrow\quad
\rho_{\rm det}\simeq I_1+I_2.
$$

Fisicamente, o detector não “observa” adicionando um postulado quântico. Ele
altera o problema de contorno. Se os dois caminhos deixam marcas de interface
distinguíveis, a forma quadrática de impedância cobra energia livre para manter
a coerência cruzada; o termo de interferência é amortecido por
$e^{-\Gamma_{\rm det}}$.

---

## 9. O que distingue GDQ neste nível

O padrão sem detector não distingue a GDQ da superposição usual de gaussianas.
A distinção deste fechamento reduzido é:

$$
\boxed{
\text{a perda de visibilidade é escrita como resposta de contorno DtN/Schur.}
}
$$

Assim, a assinatura não é simplesmente “há interferência”. A assinatura é a
dependência da visibilidade com a impedância física do aparelho:

$$
\mathcal V
=
\mathcal V_0e^{-\Gamma_{\rm det}}.
$$

Para material real, a previsão metrológica exige calcular ou medir:

1. $\lambda_{\rm det}$;
2. $L$;
3. $\zeta_{\rm det}$;
4. $C_{\rm path}$;
5. energia e coerência da fonte;
6. geometria real das fendas e do detector.

---

## 10. Validação numérica atual

O script canônico é:

- `questoes/q44/associados/resolver_dupla_fenda_detector_q44.py`.

A saída principal é:

- `questoes/q44/associados/saida_solver_detector_q44.md`;
- `questoes/q44/associados/saida_solver_detector_q44.csv`.

Com:

$$
\lambda_{\rm det}=1{,}1,
\qquad
L=1,
\qquad
C_{\rm path}=1,
$$

foi obtido:

$$
\mathsf R_{\rm det}=1{,}37414284103.
$$

O caso forte $\zeta_{\rm det}=2{,}5$ fornece:

$$
\Gamma_{\rm det}=4{,}294196378,
\qquad
e^{-\Gamma_{\rm det}}=0{,}013647535.
$$

Isto confirma numericamente a supressão forte do termo cruzado de coerência.

---

## 11. Critério de uso futuro

Ao aplicar esta estrutura a um experimento real, não ajustar
$\lambda_{\rm det}$, $L$ e $\zeta_{\rm det}$ usando a visibilidade alvo. O
procedimento correto é:

$$
\text{material e geometria do aparelho}
\to
(\lambda_{\rm det},L,\zeta_{\rm det},C_{\rm path})
\to
\Gamma_{\rm det}
\to
\mathcal V.
$$

Se os parâmetros forem inferidos da própria curva de visibilidade, o resultado
deve ser classificado como calibração ou comparação fenomenológica, não como
previsão cega.
