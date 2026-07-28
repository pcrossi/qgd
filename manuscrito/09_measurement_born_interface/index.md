---
title: "09. Regra de Born, medida e interface clássico--quântica"
---

# 09. Regra de Born, medida e interface clássico--quântica

A GDQ não toma a regra de Born como axioma primário. A teoria começa com
densidade geométrica, fase, medida ponderada, ação oficial, contornos e
Hessiana física. A regra de probabilidade aparece quando essa estrutura é
observada por um aparelho macroscópico e projetada no espaço de Hilbert físico
reconstruído no Capítulo 8.

O objetivo deste capítulo é separar cuidadosamente três afirmações que muitas
vezes são confundidas:

1. a GDQ possui uma densidade positiva conservada;
2. no setor regular, essa densidade pode ser escrita como $|\Psi|^2$;
3. uma medição real exige aparelho, contorno, registro e regra operacional
   para alternativas exclusivas.

A primeira afirmação é geométrica. A segunda é uma representação local. A
terceira é a teoria de medida.

## Roteiro

- [[09.1 - Por que Born não é apenas rho igual a R ao quadrado]]
- [[09.2 - Densidade positiva conservada da GDQ]]
- [[09.3 - Probabilidades operacionais no Hilbert reconstruído]]
- [[09.4 - Sistema, aparelho, ambiente e registros]]
- [[09.5 - O aparelho como fonte e contorno]]
- [[09.5A - Calibração multiparamétrica e imersão invariante]]
- [[09.6 - Decoerência, bacias dinâmicas e resultado único]]
- [[09.7 - Stern-Gerlach como medida de eixo]]
- [[09.8 - Escolha retardada como mudança de contorno]]
- [[09.9 - Emaranhamento como não fatoração geométrica]]
- [[09.10 - Limites e programa metrológico]]

## Resultado central

A cadeia de medida usada neste capítulo é:

$$
J_{\rm app}^{\rm classico}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm app}
\to
\text{resposta espectral}
\to
\text{registro}.
$$

O aparelho não altera a ação oficial. Ele fornece dados externos clássicos:
fonte, vínculo, impedância ou contorno. Esses dados selecionam o domínio
efetivo do problema e, portanto, a base de ponteiro observada.

No espaço de Hilbert físico reconstruído,

$$
\mathcal H_{\rm phys}
=
\overline{\mathcal D_+/(\mathcal N+\mathcal G)},
$$

a regra operacional admissível para alternativas projetivas é:

$$
\mu(P)=\operatorname{Tr}(\varrho P).
$$

Para estado puro e projetor $P_i=|i\rangle\langle i|$, ela se reduz a:

$$
P(i|\psi)=|\langle i|\psi\rangle|^2.
$$

Assim, Born não é introduzida como remendo. Ela é a regra operacional no setor
reconstruído, enquanto a GDQ fornece a densidade, a fase, o contorno e a
dinâmica de interface que tornam uma medição física.

Com isso, a mecânica quântica de projetores é recuperada como caso particular
de medição: quando o aparelho reduz a interface a alternativas ortogonais em
$\mathcal H_{\rm phys}$, o registro obedece à regra de Born. Mas a GDQ não se
reduz a esse caso. A ação ainda descreve a fonte clássica, o contorno, a
impedância, a Hessiana física e o processo pelo qual o domínio projetivo é
selecionado.

Em forma condensada:

$$
\boxed{
\text{Born/projetores}
=
\text{leitura operacional de um setor da GDQ, não axioma primário da GDQ.}
}
$$

## Estatuto do resultado

| Bloco | Status | Observação |
|---|---|---|
| Densidade positiva $\rho$ | Derivada/constitutiva | Vem de $f$ e da medida GDQ. |
| $\rho=|\Psi|^2$ local | Demonstrado no setor regular | Não basta para Born completa. |
| Born operacional | Fechada estruturalmente | Depende do Hilbert físico reconstruído. |
| Aparelho como contorno/fonte | Estrutural | Não muda a ação oficial. |
| Calibração por imersão invariante | Fechada estruturalmente; validação inicial | Benchmark de césio generaliza fora do ajuste; canal magnético ainda é entrada operacional. |
| Decoerência e registros | Redução efetiva | Explica mistura diagonal e repetibilidade. |
| Resultado individual único | Fechado condicionalmente no setor QND gaussiano | Fora desse setor, depende de bacias reais e dinâmica específica. |
| Stern--Gerlach | Protótipo estrutural | Spin/orientação existem; aparelho seleciona eixo. |
| Escolha retardada | Fechada estruturalmente | Mudança de contorno, não retrocausalidade. |
| Emaranhamento | Estrutural/condicional | Não fatoração em espaço de configuração; Bell/no-signalling metrológico fica futuro. |

## Controle editorial

- [[checklist_operacional|Checklist operacional do capítulo]]
- [[notes/provas_lemas_definicoes|Provas, lemas e definições associados]]
- [[notes/construcao_gdq_medida|Construção GDQ da medida]]
- [[notes/born_operacional_gleason_traco|Born operacional por medida em projetores]]
- [[notes/aparelho_como_contorno_hessiana_schur|Aparelho como contorno e complemento de Schur]]
- [[notes/calibracao_multiparametrica_imersao_invariante|Calibração multiparamétrica por imersão invariante]]
- [[notes/detector_ohmico_captura_born|Detector ôhmico, filtragem causal e captura Born]]
- [[notes/bacias_dinamicas_resultado_unico|Bacias dinâmicas e resultado único]]
- [[notes/teorema_born_bacias_qnd_gaussiano|Teorema Born–bacias para aparelhos QND gaussianos]]
- [[notes/emaranhamento_nao_fatoracao_no_signalling|Emaranhamento, não fatoração e no-signalling]]

[[../index|← Home]] | [[09.1 - Por que Born não é apenas rho igual a R ao quadrado|Next →]]
