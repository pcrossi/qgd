# Questão 58 — Hubble, lítio, Bullet Cluster e birrefringência

## 1. Enunciado

A questão exige uma resposta cosmológica integrada. Não basta explicar
separadamente tensão de Hubble, lítio, Bullet Cluster, CMB, BAO, supernovas,
lentes, crescimento e birrefringência com fatores independentes. Um único
modelo deve calcular tudo a partir do mesmo background.

Arquivos relacionados:

- `58-0.md`;
- `pt-br/32 - Fenomenologia Astrofísica e Cosmológica da GDQ.md`;
- `pt-br/notas/31/nota_31.4_anomalia_litio.md`;
- `pt-br/notas/32/nota_32.9_rotacao_agregados.md`;
- `questoes/q54/questao_54.md`;
- `questoes/q56/questao_56.md`;
- `questoes/q57/questao_57.md`.

---

## 2. Veredito

$$
\boxed{
\text{Q58 formulada estruturalmente; fechamento metrológico conjunto em programa futuro.}
}
$$

A GDQ já possui os blocos necessários para montar um modelo único:

1. Q54: emergência macroscópica da equação métrica efetiva;
2. Q56: densidade de energia escura e contorno cosmológico;
3. Q57: escala galáctica $a_0^{\rm GDQ}=cH_0/(2\pi)$;
4. capítulo 32 legado: rotas para Hubble, lítio, birrefringência e aglomerados.

Mas a Q58 impõe uma exigência maior: esses blocos precisam ser executados em
um único solver cosmológico com um único background e um único conjunto de
contornos. Isso ainda não foi feito.

Logo:

$$
\boxed{
\text{não há falta estrutural de princípio; falta cálculo integrado.}
}
$$

---

## 3. O objeto único da Q58

O objeto que unifica o setor cosmológico é a sela global:

$$
\Phi_*^{\rm cos}
=
(g,J,H,f,\mathcal U)_{\rm cos}.
$$

A cadeia correta é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_*^{\rm cos}
\to
K_{\rm cos}^{\rm phys}
\to
\delta\Phi_{\rm cos}
\to
\text{observáveis cosmológicos}.
$$

Aqui:

- $g$ fornece a geometria macroscópica efetiva;
- $J$ define a estrutura complexa;
- $H$ é a torção de Bismut/Cartan;
- $f$ define densidade, fase e medida;
- $\mathcal U$ é a medida ponderada;
- $K_{\rm cos}^{\rm phys}$ é a Hessiana física cosmológica.

Essa formulação impede a multiplicação de explicações independentes.

---

## 4. Fundo cosmológico comum

O fundo efetivo vem da equação métrica ponderada da GDQ, não de uma ação
Einstein--Hilbert substituta. Na redução macroscópica da Q54:

$$
\operatorname{Eul}_g(\mathcal S_{\rm GDQ})=0
\quad
\Longrightarrow
\quad
\mathcal E_{\rm cos}[a,H,\rho_i,\Theta_H]=0.
$$

O observável de expansão é:

$$
H(z)=\frac{\dot a}{a}.
$$

Supernovas e BAO devem ser calculadas com esse mesmo $H(z)$:

$$
D_C(z)=c\int_0^z\frac{dz'}{H(z')},
$$

$$
D_L(z)=(1+z)D_C(z),
$$

$$
D_A(z)=\frac{D_C(z)}{1+z}.
$$

Portanto, a tensão de Hubble não pode ser tratada com um fator próprio
desacoplado. Ela deve aparecer como diferença entre:

1. contorno global cosmológico;
2. observação local;
3. cisalhamento/tensão de fundo permitidos pelo mesmo $\Phi_*^{\rm cos}$.

---

## 5. CMB, crescimento e lentes

As perturbações cosmológicas devem vir de uma única Hessiana:

$$
K_{\rm cos}^{\rm phys}
=
P_{\rm cos}^{\rm phys}
\operatorname{Hess}\mathcal S_{\rm GDQ}
P_{\rm cos}^{\rm phys}.
$$

A equação comum é:

$$
K_{\rm cos}^{\rm phys}\delta\Phi_{\rm cos}
=
J_{\rm bar}
+J_{\gamma}
+J_\nu
+J_H.
$$

O mesmo $\delta\Phi_{\rm cos}$ define:

- os potenciais escalares de lente;
- as funções de transferência da CMB;
- o crescimento de estrutura;
- a resposta torsional em aglomerados;
- correções em escalas galácticas.

Em lentes:

$$
\hat\alpha
=
\int_{\gamma_{\rm luz}}
\nabla_\perp(\Phi+\Psi)\frac{2\,dl}{c^2}.
$$

No Bullet Cluster, a interpretação GDQ correta não é “matéria escura
particulada escondida”, mas estresse geométrico residual:

$$
\Theta_{\mu\nu}^{(H)}
\sim
H_{\mu\alpha\beta}H_{\nu}^{\ \alpha\beta}
-\frac12g_{\mu\nu}|H|^2.
$$

Esse tensor deve atravessar colisões de aglomerados de modo quase sem
interação eletromagnética, enquanto o plasma bariônico sofre choque. A lente
então segue o pico geométrico, não necessariamente o gás.

Status: mecanismo estrutural. Falta simulação cosmológica/lenteamento conjunta.

---

## 6. BBN e lítio

A BBN deve usar o mesmo fundo:

$$
T(z)=T_0(1+z),
\qquad
H(z)=H_{\rm GDQ}(z).
$$

As taxas nucleares recebem correções de barreira Bohm--Cartan:

$$
\Gamma_{ij}^{\rm GDQ}(T)
=
\Gamma_{ij}^{\rm nuc}(T)
+\Delta\Gamma_{ij}^{\rm Bohm-Cartan}(T,\Phi_*^{\rm cos}).
$$

O problema do lítio só fica resolvido se a mesma correção:

1. reduzir efetivamente $^7{\rm Be}/^7{\rm Li}$;
2. preservar deutério;
3. preservar hélio;
4. preservar a razão bárion-fóton;
5. usar o mesmo $H(z)$ do CMB/BAO/SN.

Portanto o fator legado de redução do lítio é uma pista útil, mas não fecha
a Q58 sozinho.

---

## 7. Birrefringência

No capítulo legado, a birrefringência aparece como rotação acumulada de
polarização por torção residual:

$$
\Delta\Psi
\sim
\frac{\alpha}{\pi}
\left(
1-\frac{3}{4\pi^2}
\right).
$$

Na formulação GDQ mais limpa, esse ângulo deve ser calculado como holonomia do
canal fotônico sobre a conexão de Bismut cosmológica:

$$
\Delta\Psi_{\rm GDQ}
=
\frac12
\int_{\gamma_{\rm CMB}}
\omega_{\rm pol}^{B}.
$$

A exigência da Q58 é que $\omega_{\rm pol}^{B}$ venha do mesmo
$\Phi_*^{\rm cos}$ que produz $H(z)$, lentes, CMB e crescimento.

Status: rota estrutural; falta cálculo metrológico no background integrado.

---

## 8. O que já está resolvido por questões anteriores

### 8.1 Energia escura

Da Q56:

$$
\rho_{\Lambda}^{\rm GDQ}
=
\alpha^2N_{\rm Cartan}\rho_{\rm UV}
\frac{r_p}{R_H}\frac1{c^2}.
$$

Essa estrutura fornece:

- escala de densidade de fundo;
- diluição global--local;
- equação de estado $w=-1$ no background homogêneo;
- ponto de partida para perturbações cosmológicas.

### 8.2 Aceleração galáctica

Da Q57:

$$
a_0^{\rm GDQ}
=
\frac{c^2}{2\pi R_H}
=
\frac{cH_0}{2\pi}.
$$

Isso dá a redução galáctica:

$$
v^4\simeq GM_ba_0^{\rm GDQ}.
$$

Mas lentes e aglomerados exigem o setor geométrico escuro/torsional
$\Theta_{\mu\nu}^{(H)}$, não apenas MOND escalar.

### 8.3 Gravidade macroscópica

Da Q54, a equação de Einstein é limite macroscópico efetivo da equação métrica
ponderada, sob média torsional e fechamento hidrodinâmico. Logo, usar
distâncias cosmológicas, lenteamento e expansão FLRW é legítimo como redução
efetiva, desde que não se substitua a ação oficial por Einstein--Hilbert como
fundamento.

---

## 9. Plano de fechamento metrológico

O plano executável está em:

```text
questoes/q58/associados/plano_solver_cosmologico_integrado_q58.md
```

Critério de sucesso:

1. congelar um único $\mathcal P_{\rm cos}$ antes da comparação;
2. calcular $H(z)$, SN, BAO e CMB com o mesmo fundo;
3. calcular BBN e lítio com o mesmo $H(z)$;
4. calcular lentes, Bullet Cluster e crescimento com o mesmo
   $K_{\rm cos}^{\rm phys}$;
5. calcular birrefringência com a mesma conexão de Bismut cosmológica;
6. não introduzir fator separado por anomalia.

---

## 10. Conclusão

A Q58 não invalida as respostas anteriores; ela organiza o nível superior de
consistência cosmológica.

O resultado atual é:

$$
\boxed{
\text{há uma arquitetura cosmológica GDQ única; o solver conjunto é extensão metrológica.}
}
$$

Portanto, a Q58 deve ser classificada como:

$$
\boxed{
\text{fechada estruturalmente como formulação; metrologia integrada em aberto.}
}
$$

---

## 11. Fechamento da questão

A pergunta foi respondida no nível correto. A Q58 exigia decidir se a GDQ
possui uma arquitetura cosmológica única ou apenas explicações isoladas. A
arquitetura única foi explicitada:

$$
\Phi_*^{\rm cos}
\longrightarrow
K_{\rm cos}^{\rm phys}
\longrightarrow
\delta\Phi_{\rm cos}
\longrightarrow
\left\{
H(z),
\mathrm{CMB},
\mathrm{BAO},
\mathrm{SN},
\mathrm{BBN},
\mathrm{lentes},
\mathrm{crescimento},
\mathrm{birrefringência}
\right\}.
$$

O solver cosmológico integrado fica como refinamento metrológico posterior,
não como falta estrutural da resposta.

Classificação final:

$$
\boxed{
\text{Q58 fechada estruturalmente; solver cosmológico integrado como extensão metrológica.}
}
$$
