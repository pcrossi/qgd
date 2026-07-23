# Fechamento da Questão 43 — Zeeman e \(g-2\)

## 1. Enunciado fechado

A Questão 43 perguntava:

1. se \(g=2\) é derivado ou assumido;
2. se a correção de Schwinger é calculada;
3. qual operador substitui, na GDQ, a linguagem de diagramas para a anomalia;
4. se o resultado depende de escala;
5. como a hierarquia leptônica entra no problema.

## 2. Resultado

A questão fica:

\[
\boxed{
\text{fechada estrutural e operacionalmente, não metrologicamente.}
}
\]

Isso significa:

1. a forma Zeeman foi derivada por Noether, isotropia e fonte externa;
2. o termo mínimo \(g_0=2\) foi derivado como parte protegida da circulação;
3. o fator líder \(\alpha/(2\pi)\) foi obtido pela norma da 1-forma harmônica;
4. a cadeia computável \(H_C,c,m_\perp\to a_\ell\) foi construída;
5. a comparação com experimento foi executada;
6. a parte superior foi isolada como canal transversal da Hessiana, não como
   ajuste fundamental.

## 3. Cadeia dedutiva

O campo magnético externo é dado de aparelho. O funcional vinculado é:

\[
\mathscr I[\Phi,\lambda;B]
=
\mathcal S_{\rm GDQ}[\Phi]
-B\,M[\Phi]
-\lambda\left(\mathcal C[\Phi]-C_\ell\right).
\]

A decomposição magnética é:

\[
m_\ell=\gamma_{0,\ell}c_\ell+m_{\perp,\ell}.
\]

A parte mínima satisfaz:

\[
\gamma_{0,\ell}=\frac{q_\ell}{m_\ell c},
\qquad
g_0=2.
\]

A anomalia é:

\[
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle
}.
\]

## 4. Termo líder

No ciclo de fase:

\[
h=\frac{d\vartheta}{2\pi},
\qquad
\langle h,h\rangle=\frac{1}{2\pi}.
\]

Logo:

\[
a^{(1)}
=
\alpha\langle h,h\rangle
=
\frac{\alpha}{2\pi}.
\]

Com \(\alpha^{-1}=137.035999177\):

\[
a^{(1)}
=
1.161409732097665\times10^{-3},
\]

\[
g^{(1)}
=
2.002322819464196.
\]

## 5. Comparação experimental

### 5.1 Elétron

Valor usado:

\[
g_e^{\rm exp}
=
2.002319304361180.
\]

Diferença líder:

\[
g^{(1)}-g_e^{\rm exp}
=
3.5151030\times10^{-6}.
\]

Em anomalia:

\[
a_e^{\rm exp}-a^{(1)}
=
-1.7575515\times10^{-6}.
\]

### 5.2 Múon

Valor usado:

\[
a_\mu^{\rm exp}
=
1.165920590000000\times10^{-3}.
\]

Logo:

\[
g_\mu^{\rm exp}
=
2.002331841180000.
\]

Em anomalia:

\[
a_\mu^{\rm exp}-a^{(1)}
=
4.5108579\times10^{-6}.
\]

## 6. Modelo reduzido Q39→Q43

A hierarquia intrínseca vigente da Q39 fornece:

| lépton | papel Q39 | \(R_\ell=M_\ell/M_e\) |
|---|---|---:|
| elétron | torção primária | \(1\) |
| múon | torção transversal/biespacial | \(206.7685934706\) |
| tau | saturação tridimensional | \(3477.4464050984\) |

O teste com susceptibilidade escalar simples:

\[
\chi_\ell\propto\frac{1}{R_\ell}
\]

falha para o múon:

\[
\mathcal R_\mu^{(\chi)}
\simeq
-8.50\times10^{-9},
\]

enquanto:

\[
\mathcal R_\mu^{\rm exp}
\simeq
4.51\times10^{-6}.
\]

Portanto:

\[
\boxed{
\text{Q39 fornece o background; não substitui }H_{C,\ell}^{+}m_{\perp,\ell}.
}
\]

## 7. Blocos computacionais construídos

O bloco líder é:

\[
H_{\rm lead}
=
\begin{pmatrix}
1 & -1\\
-1 & 2\pi/\alpha
\end{pmatrix},
\qquad
c=
\begin{pmatrix}
1\\0
\end{pmatrix},
\qquad
m_\perp=
\begin{pmatrix}
0\\1
\end{pmatrix}.
\]

Ele satisfaz:

\[
\frac{\langle c,H_{\rm lead}^{-1}m_\perp\rangle}
{\langle c,H_{\rm lead}^{-1}c\rangle}
=
\frac{\alpha}{2\pi}.
\]

Foram também construídos blocos superiores `required`:

| caso | \(\mu_{2,\ell}^{\rm required}\) | classificação |
|---|---:|---|
| elétron | \(-1.5132915275\times10^{-3}\) | diagnóstico inverso |
| múon | \(8.0307612309\times10^{-1}\) | diagnóstico inverso |

Esses valores não são previsão. Eles medem a resposta transversal superior
que a Hessiana oficial deve produzir.

## 8. Arquivos gerados

1. `questao_43.md`;
2. `associados/expansao_hessiana_g2.md`;
3. `associados/calcular_g2_lider_q43.py`;
4. `associados/calcular_residuos_superiores_q43.py`;
5. `associados/avaliar_hessiana_q43.py`;
6. `associados/modelo_reduzido_q39_q43.py`;
7. `associados/hessiana_operacional_q43.md`;
8. `associados/construir_blocos_hessiana_q43.py`;
9. `associados/saida_blocos_hessiana_q43.md`;
10. `associados/hessiana_lider_q43.npz`;
11. `associados/hessiana_required_e_q43.npz`;
12. `associados/hessiana_required_mu_q43.npz`;
13. saídas independentes do avaliador.

## 9. Pendência que não reabre a questão

A pendência restante é:

\[
\boxed{
\text{derivar, da ação oficial, os canais superiores que substituem }
\mu_{2,\ell}^{\rm required}.
}
\]

Isso é necessário para uma previsão metrológica completa de \(g_e\),
\(g_\mu\) e \(g_\tau\), mas não reabre o fechamento estrutural da Q43.

## 10. Veredito final

\[
\boxed{
\text{Q43 fechada estrutural e operacionalmente.}
}
\]

\[
\boxed{
\text{Q43 não fechada como previsão metrológica completa de }g-2.
}
\]

O ponto exato que separa as duas afirmações está identificado:

\[
H_{C,\ell}^{+}m_{\perp,\ell}
\quad
\text{nos canais superiores da Hessiana oficial.}
\]

Refinamento posterior: a expansão cúbica/quártica da truncagem Galerkin
reduzida da ação oficial foi calculada em
`associados/calcular_variacoes_superiores_gdq_q43.py`. O acoplamento direto
líder² → superior saiu compatível com zero,
`T112 ≃ -2.66e-6`, enquanto o canal robusto foi
`T123 ≃ -6.2831748693 ≃ -2π`. Portanto, no modelo reduzido, o canal superior
aparece mediado pela densidade `Re(f)`, não como fonte linear direta universal.

Isso não fecha a metrologia, mas remove uma ambiguidade: a etapa restante é
avaliar as variações superiores na sela leptônica 8D estável e contrair esses
tensores com o mapa magnético de contorno `M[Phi;B]`.

O operador condicional dessa contração foi implementado em
`associados/contrair_canal_densidade_q43.py`. Ele aplica
`Delta H12 = eta_l T123`. Nos backgrounds efetivos mínimos atuais,
`eta_l=0`, portanto `a_eff=a0=alpha/(2*pi)` para elétron, múon e tau. A
metrologia superior exige o perfil estacionário de densidade `Re(f)` da sela
leptônica 8D; esse é agora o dado físico ausente.

O valor de `eta_l` foi depois calculado pela sela angular reduzida normalizada
em `associados/calcular_eta_pela_sela_q43.py`. A fase multivalorada foi
diferenciada pela conexão regular

\[
P'=\frac{1}{2\pi}+a_1\cos\theta+2a_2\cos2\theta,
\]

e o modo constante de `Re(f)` foi eliminado pelo vínculo

\[
\frac1{2\pi}\int_0^{2\pi}\rho\sqrt g\,d\theta=1.
\]

Em quatro malhas, a única raiz encontrada foi

\[
a_1=a_2=\eta_\ell=\sigma=0.
\]

Assim, a sela angular normalizada demonstra
`Delta H12 = eta_l T123 = 0`. A raiz possui um autovalor negativo reduzido,
aproximadamente `-6.247e-2`; por isso o cálculo não substitui a sela física 8D.
A solução não normalizada `|eta| ≃ 1.064` foi descartada por sair do domínio
normalizado. O resultado é negativo, mas fecha a tentativa de obter a
metrologia superior apenas pela sela angular homogênea.

## 11. Hipóteses conservadoras de melhoria

O fechamento acima deve ser lido de forma conservadora. A Q43 não precisa
promover resíduos metrológicos a novos termos fundamentais da ação. O que
existe hoje é:

\[
\text{ação oficial}
\to
\text{fonte/contorno magnético}
\to
\text{Hessiana física}
\to
\text{resposta Zeeman/anomalia}.
\]

Dentro dessa cadeia, as melhorias admissíveis são:

1. **correção térmica de fundo**: temperatura do espaço cosmológico de
   Einstein, quando usada como dado global de contorno, pode modificar a sela
   física por

\[
\delta_T\Phi_\ell
=
-H_{\ell,\rm phys}^{+}J_\ell^{(\beta)};
\]

2. **correção térmica de aparelho**: temperatura efetiva do detector ou da
   armadilha pode alterar o mapa de fonte \(M[\Phi;B]\), mas isso é dado
   experimental do aparato, não constante universal da GDQ;

3. **background 8D não homogêneo, warped ou misto**: pode produzir
   \(\eta_\ell\neq0\) ou fatores tensoriais superiores que a sela angular
   homogênea eliminou;

4. **variações superiores da Hessiana oficial**: os tensores cúbicos e
   quárticos devem ser avaliados no background físico, não escolhidos para
   reproduzir \(g-2\).

Essas hipóteses melhoram a metrologia possível, mas não reabrem o problema de
princípio. Elas pertencem ao programa de previsão fina:

\[
H_{\ell,\rm phys}^{+}m_{\perp,\ell}
\quad
\text{com}
\quad
\Phi_\ell(T,B,\text{contorno})
\]

e não à definição da ação oficial.

## 12. Fechamento conservador

A Questão 43 fica encerrada como problema estrutural:

\[
\boxed{
\text{Zeeman e o termo líder de }g-2\text{ foram derivados no formalismo GDQ.}
}
\]

A previsão metrológica completa permanece uma extensão controlada:

\[
\boxed{
\text{calcular a resposta térmica/8D da Hessiana física, sem pós-ajuste.}
}
\]

Portanto, a temperatura é importante para corrigir valores finos, mas entra
como condição global ou de aparelho que deforma a sela, não como alteração da
ação fundamental.
