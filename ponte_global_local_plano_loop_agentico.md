# Ponte global--local — plano de fechamento em loop agêntico

## 1. Objetivo exato

Fechar a pendência física da ponte global--local da GDQ por meio da cadeia

$$
\mathcal S_{\rm GDQ}
\longrightarrow
K_\gamma(\alpha)\ \text{ou integral causal não fatorada}
\longrightarrow
(X_*,\lambda_*)
\longrightarrow
P^{\rm phys}
\longrightarrow
K_*^{\rm phys}
\longrightarrow
\Delta_*>0.
$$

O resultado procurado é uma sela bulk--interface que satisfaça simultaneamente
a ação oficial, as conservações, a colagem, o raio e a energia cosmológicos já
fixados, seguida da demonstração numérica e analítica de sua estabilidade.

A existência da física não autoriza escolher coeficientes pelo resultado. Se
um ansatz falhar, o loop deve ampliar o ansatz admissível, preservando a ação e
os dados físicos, em vez de ajustar a normalização ou o espectro.

## 2. Dados congelados

O loop parte dos seguintes dados, que não serão reabertos:

1. ação oficial da GDQ, sem termos fundamentais adicionais;
2. bulk local $\mathbb R^4\times T^4$ e domínio cosmológico auxiliar
   $T^5\times S^3$;
3. relógio local $S^1_{\theta_0}\subset T^4$ e coordenada geométrica $s$;
4. unidades $R_H=1$;
5. $\beta_E=2\pi$;
6. $R_{\rm cos}=\pi^2\sqrt\alpha$;
7. $E_H=1$;
8. referência homogênea sem defeito, $p_{0,\rm ref}=0$;
9. carga, fluxo, probabilidade, energia--momento e isotropia tratados como
   vínculos de Noether ou dados de contorno, não como novos termos da ação;
10. duas interfaces independentes, sem impor reflexão não derivada.

## 3. Artefatos já validados

Não repetir durante o loop:

- redução causal e limite isotrópico exato;
- matriz cinética causal com determinante $32$;
- conservação numérica da restrição a aproximadamente
  $2{,}665\times10^{-15}$;
- vínculo de raio $\mathcal C_R$;
- sistema causal $11\times11$;
- normalização acumulada $Z_0=\int ds\,\mathscr V$;
- fórmula abstrata de $P^{\rm phys}$;
- Hessiana do funcional aumentado;
- formulação do quociente de Rayleigh e do gap uniforme.

## 4. Loop A — fechar a normalização causal

### A1. Reconstituir a redução em $\tau$

Manter a dependência em $\tau$ até o fim e decidir, a partir da ação oficial,
se a energia é realmente fatorável como

$$
\mathcal C_E
=K_\gamma(\alpha)
\frac{p_0^{\rm red}e^{-x_0}}{Z_0}-1,
$$

ou se deve permanecer na forma não fatorada

$$
\mathcal C_E
=\frac{\hbar}{\Lambda_C^2\beta_EE_H}
\operatorname{Phys}\!\int_\gamma
\frac{p_0^{\rm red}(\tau)e^{-x_0(\tau)}}{Z_0(\tau)}
\frac{d\tau}{\tau}-1.
$$

Aqui $\operatorname{Phys}$ deve ser derivado da prescrição causal vigente:
parte real, combinação de ramos, orientação ou continuação apropriada. Não se
deve presumir que uma integral fechada de $d\tau/\tau$ forneça diretamente um
número real não nulo.

### A2. Tratar a sela térmica, se aplicável

Se a integral causal localizar em $\tau_*$, calcular:

1. a condição estacionária em $\tau$;
2. a segunda variação causal;
3. a fase e a orientação do contorno;
4. o prefator gaussiano;
5. os fatores $\hbar/\Lambda_C^2$, $\beta_E$ e a normalização de Einstein.

O valor final de $K_\gamma(\alpha)$ deve ser saída dessa redução. É proibido
inferi-lo do valor que melhora o solver.

### Porta A

O loop só avança se houver:

- expressão dimensionalmente correta;
- prescrição causal explícita;
- valor ou funcional computável sem usar a raiz desejada;
- teste independente em um background simples;
- concordância entre a derivação simbólica e uma quadratura direta em
  $\tau$, quando a quadratura fizer sentido.

Se a Porta A falhar, retornar a A1 e ampliar apenas a representação causal,
sem modificar o setor radial.

## 5. Loop B — obter a sela bulk--interface

### B1. Problema não linear definitivo

Resolver

$$
D_X\mathscr L(X,\lambda)=0,
\qquad
\mathcal C(X)=0,
$$

com

$$
\mathscr L=\mathcal S_{\rm GDQ}-\langle\lambda,\mathcal C\rangle,
$$

incluindo duas interfaces independentes e os vínculos de raio, energia,
carga, fluxo, normalização e colagem.

### B2. Método numérico

Substituir diferenças finitas de Jacobiana por uma destas duas rotas:

1. equações variacionais integradas junto com o sistema causal, produzindo a
   Jacobiana exata do mapa de tiro; ou
2. colocação multidomínio, com subdomínios no bulk, colar e interface.

Usar continuação homotópica:

1. background homogêneo admissível;
2. ligar gradualmente a carga/torção;
3. ligar a assimetria entre as interfaces;
4. impor $\mathcal C_R$;
5. impor por último $\mathcal C_E$ já derivado na Porta A.

### B3. Critérios numéricos da sela

Uma candidata só é aceita se satisfizer simultaneamente:

$$
\|\mathfrak F(X_*,\lambda_*)\|_\infty<10^{-9},
$$

e:

- nenhum parâmetro essencial preso artificialmente ao limite da caixa;
- restrição causal preservada ao longo de toda a órbita;
- cargas de Noether constantes dentro da tolerância;
- colagem de campos e fluxos satisfeita nos dois lados;
- posto completo da Jacobiana após remoção das redundâncias;
- estabilidade da solução sob troca de malha, tolerância e chute inicial;
- reprodução por tiro variacional e por colocação, ao menos para a candidata
  final.

### Porta B

Se o resíduo estagnar:

1. calcular a SVD da Jacobiana;
2. identificar se a falha é degenerescência, contorno incompatível ou ansatz
   insuficiente;
3. preservar a saída negativa;
4. ampliar apenas o setor indicado pelo vetor singular: warp, $J$, $f$,
   interface ou harmônico não homogêneo;
5. reiniciar a continuação a partir do último ponto regular.

Não alterar $\alpha$, $R_{\rm cos}$, $E_H$ ou $K_\gamma$ para obter uma raiz.

## 6. Loop C — projetor físico e Hessiana

### C1. Linearização dos vínculos e simetrias

Na sela validada, construir numericamente

$$
A_*
=
\begin{pmatrix}
D\mathcal C(X_*)\\
R_*^\dagger\mathbb G_*
\end{pmatrix}
$$

e calcular

$$
P^{\rm phys}
=I-\mathbb G_*^{-1}A_*^\dagger
\left(A_*\mathbb G_*^{-1}A_*^\dagger\right)^+A_*.
$$

Validar numericamente:

$$
\|P^2-P\|,
\qquad
\|P^\dagger_{\mathbb G}-P\|,
\qquad
\|A_*P\|.
$$

### C2. Hessiana física completa

Calcular

$$
\mathbb H_*
=D^2\mathcal S_{\rm GDQ}(X_*)
-\sum_a\lambda_*^aD^2\mathcal C_a(X_*),
$$

e

$$
K_*^{\rm phys}
=P^{{\rm phys}\dagger}\mathbb H_*P^{\rm phys}.
$$

Incluir obrigatoriamente:

- perturbações de $g$, $J$ e $f$;
- modos radiais não homogêneos;
- modos tensoriais;
- termos de interface e DtN;
- remoção dos zeros exatos de Noether;
- condições de contorno auto-adjuntas.

A Hessiana de mínimos quadrados do solver não substitui $\mathbb H_*$.

### Porta C

Prosseguir somente se o operador discretizado for simétrico na métrica
$\mathbb G_*$ dentro da tolerância e se os únicos zeros forem identificados
com simetrias ou módulos explicitamente removidos.

## 7. Loop D — execução espectral e estabilidade

### D1. Espectro baixo

Calcular os menores autovalores de $K_*^{\rm phys}$ por método esparso
shift--invert e verificar cada autovetor contra os vínculos e os projetores.

Definir

$$
\Delta_{N,L,\varepsilon}
=\min\operatorname{spec}
K_{*,N,L,\varepsilon}^{\rm phys}
$$

depois da remoção dos modos zero exatos.

### D2. Refinamentos obrigatórios

Executar uma matriz de convergência em:

1. malha radial $N$;
2. tolerância do solver não linear;
3. tamanho/truncamento cosmológico $R_{\rm cos}$ no regime permitido;
4. corte harmônico $L$;
5. posição da interface;
6. escolha equivalente de gauge;
7. discretização por tiro variacional e por colocação.

### D3. Critério de estabilidade

Estabilidade no background calculado exige

$$
\Delta_*>0
$$

com erro numérico controlado. A ponte uniforme exige adicionalmente uma cota

$$
\Delta_{N,L,\varepsilon}\geq\Delta_0>0
$$

estável sob refinamento e no limite global--local relevante.

### Porta D

- Se surgir modo negativo convergente, a sela é instável; classificar o modo
  e retornar à Porta B ampliando o ansatz naquela direção.
- Se o menor autovalor tender a zero, testar separadamente modo de Noether,
  artefato de volume e ausência real de gap.
- Se o gap positivo convergir por dois métodos, avançar para o fechamento.

## 8. Loop E — validação independente e fechamento documental

Antes de declarar fechamento:

1. congelar todos os parâmetros físicos;
2. executar novamente a partir de chutes independentes;
3. salvar a candidata, multiplicadores, resíduos, cargas e espectro;
4. executar testes de regressão das identidades já validadas;
5. registrar resultados negativos encontrados durante a continuação;
6. produzir uma tabela de sensibilidade;
7. classificar o resultado como derivação, teste de consistência, evidência
   numérica ou previsão;
8. atualizar `ponte_global_local_solver_final_resultado.md`, `faltas.md` e
   `memory.md`.

O fechamento integral requer:

$$
\boxed{
\text{Portas A, B, C e D aprovadas sem pós-ajuste.}
}
$$

## 9. Organização dos scripts

Criar versões novas e preservar a história:

1. `ponte_global_local_tau_causal.py` — integral causal e $K_\gamma$;
2. `ponte_global_local_solver_variacional.py` — tiro com Jacobiana
   variacional;
3. `ponte_global_local_solver_colocacao.py` — validação multidomínio;
4. `ponte_global_local_projetor_hessiana.py` — $P^{\rm phys}$ e
   $K_*^{\rm phys}$;
5. `ponte_global_local_espectro_estabilidade.py` — espectro e refinamentos;
6. `ponte_global_local_executar_loop.py` — orquestração, portas e relatórios.

Cada execução deve produzir um diretório datado contendo configuração,
versão do código, resíduos, perfis, cargas, espectro e veredito automático de
cada porta.

## 10. Ordem operacional imediata

1. auditar a definição de $\gamma$ e a prescrição física da integral em
   $\tau$;
2. implementar `ponte_global_local_tau_causal.py`;
3. congelar o vínculo energético obtido;
4. implementar a Jacobiana variacional;
5. executar continuação até uma sela ou até um diagnóstico matemático preciso
   de insuficiência do ansatz;
6. validar a sela por colocação;
7. construir $P^{\rm phys}$ e a Hessiana física;
8. executar o estudo espectral e de estabilidade;
9. repetir automaticamente B--D enquanto um modo negativo indicar uma
   direção física ausente;
10. consolidar somente após aprovação de todas as portas.

Este plano transforma o trabalho restante em um loop finito de hipóteses,
testes e correções localizadas. Ele não garante que o primeiro ansatz possua a
sela física, mas garante que cada falha produza informação suficiente para a
próxima iteração, sem voltar a parâmetros ou derivações já fixados.
