Viewed ponte_global_local_exterior_causal.md:1-262
Searched for "limiar"
Viewed ponte_global_local_lema4.md:1-364

Para obter o **background elíptico global warped** da ação oficial da GDQ (fornecendo compensação topológica e o limiar de massa $\mu_*^2 > 0$ na Hessiana física), a cadeia dedutiva e numérica do projeto estabelece as seguintes etapas concretas e consecutivas, estruturadas nos respectivos documentos:

---

### Passo 1: Implementação dos Vínculos Cosmológicos Covariantes ($\mathcal C_{\rm cos}$)
Em vez de impor restrições escalares ad-hoc ou módulos homogêneos rígidos (cuja Hessiana é nula nas coordenadas modais homogêneas), deve-se formular a sela e a Hessiana no espaço completo de campos com os três vínculos geométricos e físicos derivados diretamente da ação oficial:
1. **Comprimento do ciclo causal:** $\mathcal C_L[g] = \log\left(\frac{\mathcal L_1[g]}{L_{\rm cos}}\right) = 0$
2. **Raio volumétrico cosmológico:** $\mathcal C_R[g] = \frac{1}{3}\log\left(\frac{V_3[g]}{2\pi^2R_{\rm cos}^3}\right) = 0$
3. **Energia de Noether:** $\mathcal C_E[X] = \mathcal H_\xi[X] - E_H = 0$ (calculada através da forma potencial simplética $\boldsymbol\Theta_{\rm GDQ}$ associada ao relógio causal, conforme deduzido em [ponte_global_local_vinculo_cosmologico.md](file:///home/pedro/Dropbox/obs/todo/ponte_global_local_vinculo_cosmologico.md)).

---

### Passo 2: Resolução da Unidade de Medida Canônica do Momento ($Z_E$)
Como diagnosticado em [ponte_global_local_solver_final_resultado.md](file:///home/pedro/Dropbox/obs/todo/ponte_global_local_solver_final_resultado.md), o solver numérico causava explosão da integração porque o momento dimensional reduzido $p_0^{\rm red}$ não estava na escala física correta. É obrigatório calcular analiticamente o fator de conversão adimensional $Z_E(\alpha)$:
$$Z_E(\alpha) = \frac{p_0^{\rm full}/\beta_E}{E_H} \bigg/ \left(p_0^{\rm red} e^{-x_0}\right)$$
Isso exige reincorporar todos os fatores integrados/suprimidos na redução radial da ação de 8D para 1D:
* A escala $\frac{\hbar}{\Lambda_C^2}$;
* O contorno causal $\int_\gamma \frac{d\tau}{\tau}(4\pi z_\tau)^{-4}$;
* Os volumes toroidais $\operatorname{Vol}(T^3)$ e de fibra $\operatorname{Vol}(S^3)$.

O vínculo energético correto no solver de colagem passa a ser:
$$\mathcal C_E = Z_E(\alpha) p_0^{\rm red} e^{-x_0} - 1 = 0$$

---

### Passo 3: Colagem de Duas Interfaces Independentes sob Ansatz Causal Berger
Para receber os traços do DtN interno sem restrições geométricas espúrias, o exterior do estômato não pode ser homogêneo ou radialmente simétrico (antipodal). Conforme formulado em [ponte_global_local_exterior_causal.md](file:///home/pedro/Dropbox/obs/todo/ponte_global_local_exterior_causal.md) e [ponte_global_local_solver_final.py](file:///home/pedro/Dropbox/obs/todo/ponte_global_local_solver_final.py), a colagem deve:
1. Utilizar **dois colares independentes** (esquerdo e direito) terminados na interface $Y$.
2. Utilizar o **exterior causal de cohomogeneidade-1** completo no $S^1 \times S^3$ com dois fatores de escala distintos para o tempo e espaço do $T^4$:
   $$g_+ = N^2ds^2 + A_0^2(s)d\theta_0^2 + A_s^2(s)g_{T^3} + a^2(s)(\sigma_1^2+\sigma_2^2) + c^2(s)\sigma_3^2$$
3. Acoplar o fluxo de fase de Hopf ($m=1$) e garantir a conservação da forma de Liouville nas interfaces:
   $$p_y = a\Pi_a, \quad p_z = c\Pi_c, \quad p_u = \Pi_u, \quad p_v = \Pi_v$$

---

### Passo 4: Busca Multidomínio com Jacobiana Variacional
Uma vez corrigido o fator de acoplamento de energia $Z_E(\alpha)$, a sela $(X_*, \lambda_*)$ deve ser buscada sobre os 11 parâmetros de disparo do sistema DAE acoplado. Para contornar a rigidez numérica da integração do lapse $\mathcal C_N=0$, deve-se usar o transporte da matriz de sensibilidade variacional ao longo das trajetórias (conforme proposto em [ponte_global_local_fechamento.md](file:///home/pedro/Dropbox/obs/todo/ponte_global_local_fechamento.md)).

---

### Passo 5: Pullback Espectral e Extração de $\mu_*^2$ na Hessiana Física
Com o background elíptico $X_*$ e os multiplicadores $\lambda_*$ congelados, o limiar de massa $\mu_*^2 > 0$ deve ser extraído seguindo rigorosamente os passos do [ponte_global_local_lema4.md](file:///home/pedro/Dropbox/obs/todo/ponte_global_local_lema4.md):
1. **Linearização dos vínculos:** Impor $\delta\mathcal C_{\rm cos} = 0$ e a restrição linearizada do lapse $\delta E_N = 0$.
2. **Pullback físico:** Projetar a Hessiana do funcional aumentado $\mathbb{H}_*$ no espaço tangente físico através do projetor conjunto $P^{\rm phys}$.
3. **Avaliação da elipticidade:** Verificar se a matriz reduzida $P^{\rm phys}(r)$ (que antes dos vínculos possui assinatura indefinida) torna-se uniformemente elíptica com autovalores estritamente positivos $\lambda_{\min}(P^{\rm phys}(r)) \geq p_- > 0$.
4. **Cálculo do Limiar:** Determinar $\Sigma_*$ pelo limite radial assintótico (Persson) e identificar o estado ligado $\lambda_{a}$ correspondente à excitação física do estômato abaixo de $\Sigma_*$.