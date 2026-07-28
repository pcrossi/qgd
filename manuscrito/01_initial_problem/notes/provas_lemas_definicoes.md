---
title: "Provas, lemas e definições — Capítulo 1"
---

# Provas, lemas e definições — Capítulo 1

Esta nota registra o que deve ficar associado ao Capítulo 1 sem transformar a
introdução em capítulo técnico.

| Item | Forma de inserção | Status |
|---|---|---|
| Diferença entre integral oscilatória de Feynman e integral positiva de Wiener | Explicação didática com equações mínimas | Conceitual/demonstrativo |
| Rotação de Wick como continuação condicional | Enunciado com ressalva de domínio e contorno | Condicional |
| Transformação de Madelung | Definição operacional inicial | Preparatória |
| Equação de continuidade de Madelung | Demonstração curta ou referência ao Cap. 5 | Demonstrada depois |
| Termo de Bohm como derivada de amplitude | Fórmula e interpretação segura | Demonstrado no setor regular |
| Difusão de Nelson/Wiener | Ponte condicional, não axioma definitivo | Condicional |
| Identidade osmótica de Bohm | Nota e script autocontido | Verificação simbólico-numérica |
| Contraste Wiener/Feynman | Corpo do texto e script autocontido | Teste pedagógico de consistência |

A identidade diferencial local de Bohm também possui certificação complementar
em [BohmIdentity.lean](../../../formal/GDQ/BohmIdentity.lean). O módulo prova,
para uma log-densidade regular unidimensional $q$ e
$R=\exp(q/2)$,

$$
\frac{R''}{R}
=
\frac{q''}{2}
+
\frac{(q')^2}{4}.
$$

Ele também certifica a forma algébrica da identidade de Fisher--Bohm. A
extensão com $\nabla$ e $\Delta_g$ em variedade riemanniana continua sendo a
mesma prova humana do Capítulo 5; ainda não foi internalizada no Lean.

## Não antecipar aqui

- prova completa da ação oficial;
- prova da polarização $\Pi_{S_R}=\rho$;
- regra de Born;
- Wallstrom;
- spin;
- espectros ou massas.

O Capítulo 1 deve formular o problema. As provas técnicas entram nos capítulos
onde seus domínios e hipóteses já foram definidos.

## Estado após revisão didática

O capítulo já contém as transições mínimas entre:

1. integral positiva e integral oscilatória;
2. rotação de Wick e dados de contorno;
3. calibre/bordo e decomposição de Madelung;
4. Nelson/difusão e necessidade de geometria;
5. fluxo geométrico e introdução do domínio da GDQ no Capítulo 2.

As demonstrações extensas permanecem em notas chamadas. Os scripts do capítulo
servem apenas como verificação pedagógica, não como evidência física
independente.
