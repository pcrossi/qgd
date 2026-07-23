# Metodologia GDQ

Esta pasta reúne o método reutilizável de cálculo da GDQ.

O objetivo é evitar que cada questão reinvente o mesmo processo. A estrutura
geral é:

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
\mathcal O_{\rm obs}.
$$

Onde:

- $\mathcal S_{\rm GDQ}$ é a ação oficial;
- $\Phi_*$ é o background estacionário admissível;
- $P_{\rm phys}$ remove gauge, modos nulos espúrios e vínculos;
- $K_{\rm phys}$ é a Hessiana física;
- $J_{\rm app}$ é fonte, contorno ou vínculo clássico do aparelho;
- $\delta\Phi$ é a resposta linear;
- $\mathsf R_{\rm app}$ é a impedância/DtN/Schur;
- $\mathcal O_{\rm obs}$ é o observável físico.

## Estrutura

- [plano_mestre.md](plano_mestre.md): plano completo de implementação.
- [simbolico/](simbolico/): método formal, variações, Hessiana e projetores.
- [numerico/](numerico/): padrões de scripts, validação e saídas.
- [templates/](templates/): modelos copiáveis para novas questões.
- [aplicacoes/](aplicacoes/): mapa entre questões e blocos metodológicos.
- [checklists/](checklists/): critérios de fechamento e auditoria.

## Regra central

Nenhum resultado deve ser promovido a previsão forte se não passar pela cadeia:

$$
\text{background}
\to
\text{Hessiana física}
\to
\text{fonte/contorno}
\to
\text{resposta}
\to
\text{observável}.
$$

Se algum elo faltar, o resultado deve ser classificado como redução efetiva,
comparação fenomenológica, teste de consistência ou programa futuro.
