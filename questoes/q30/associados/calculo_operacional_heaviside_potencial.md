# Q30 — Reconstrução operacional de Heaviside do potencial confinante

## 1. Entrada GDQ

O resultado mecânico-geométrico da Q30 é

$$
\boxed{V_{\rm GDQ}(r)=\sigma_{\rm GDQ}r+V_0,}
$$

onde $\sigma_{\rm GDQ}>0$ é a diferença de ação transversal por unidade de
comprimento do pescoço Ricci--Bohm estabilizado. O objetivo é reconstruir o
operador estático cuja função de Green produz essa resposta.

## 2. Identidade distributiva

Em três dimensões, $\Delta r=2/r$ para $r>0$ e
$\Delta(1/r)=-4\pi\delta^{(3)}(\mathbf r)$. Logo,

$$
\boxed{\Delta^2r=-8\pi\delta^{(3)}(\mathbf r).}
$$

Portanto,

$$
\boxed{
\mathcal L_{\rm conf}
:=-\frac{1}{8\pi\sigma_{\rm GDQ}}\Delta^2
}
$$

satisfaz

$$
\mathcal L_{\rm conf}(\sigma_{\rm GDQ}r)=\delta^{(3)}(\mathbf r).
$$

Na linguagem de Heaviside,

$$
\boxed{V_{\rm GDQ}=\mathcal L_{\rm conf}^{-1}\delta.}
$$

## 3. Símbolo em momento

Com $\widetilde f(\mathbf k)=\int d^3r\,e^{-i\mathbf k\cdot\mathbf r}f(\mathbf r)$
e $\Delta\mapsto-k^2$,

$$
\boxed{
\widetilde V_{\rm GDQ}(\mathbf k)
=-\frac{8\pi\sigma_{\rm GDQ}}{k^4}
}
$$

até termos de contato/constante. Essa é a estrutura operacional associada,
na linguagem externa, a um potencial confinante tipo Yang--Mills.

## 4. Regularização operacional

Para controlar $k=0$ durante a inversão, use

$$
\widetilde V_\mu(k)
=-\frac{8\pi\sigma}{(k^2+\mu^2)^2}.
$$

A transformada tridimensional é

$$
\int\frac{d^3k}{(2\pi)^3}
\frac{e^{i\mathbf k\cdot\mathbf r}}
{(k^2+\mu^2)^2}
=\frac{e^{-\mu r}}{8\pi\mu}.
$$

Subtraindo a constante $V_\mu(0)$,

$$
\boxed{
V_\mu(r)-V_\mu(0)
=\frac{\sigma}{\mu}(1-e^{-\mu r}).
}
$$

Assim,

$$
\boxed{
\lim_{\mu\to0^+}[V_\mu(r)-V_\mu(0)]=\sigma r.
}
$$

$\mu$ é apenas auxiliar distributivo e desaparece após a subtração.

## 5. Resposta de curto e longo alcance

Se a resposta local também contém

$$
\widetilde V_{\rm curto}(k)=-\frac{4\pi\kappa_C}{k^2},
$$

então

$$
\boxed{
V_{\rm eff}(r)
=-\frac{\kappa_C}{r}
+\sigma_{\rm GDQ}r+V_0.
}
$$

Essa forma coincide operacionalmente com um potencial tipo Cornell, mas sua
interpretação é GDQ: o termo linear é o custo do pescoço Ricci--Bohm. O
coeficiente $\kappa_C$ não foi calculado aqui e não deve ser identificado
automaticamente com $4\alpha_s/3$.

## 6. Relação com o gap

O kernel $k^{-4}$ é uma resposta estática entre fontes, não o propagador de um
estado assintótico livre. Portanto, não contradiz

$$
\Delta_{\rm GDQ}=\hbar c/r_\perp>0.
$$

## 7. Alcance

Foi construída exatamente a equivalência

$$
\boxed{
V(r)=\sigma r
\Longleftrightarrow
\widetilde V(k)=-8\pi\sigma/k^4
\Longleftrightarrow
\mathcal L_{\rm conf}=-(8\pi\sigma)^{-1}\Delta^2.
}
$$

Isso reconstrói um potencial efetivo do tipo Yang--Mills a partir do resultado
GDQ. Não demonstra que $\Delta^2$ seja sozinho a Hessiana fundamental: é o
operador de resposta estática após reduzir o tubo.

A tentativa direta foi executada em
`questoes/q30/associados/tentativa_derivacao_direta_k4_hessiana.md`. Ela mostrou que a Hessiana
local não degenerada é de segunda ordem e mantém resposta $k^{-2}$; $k^{-4}$
exige um modo físico crítico ou a redução coletiva não perturbativa do tubo.

## 8. Classificação

- identidade distributiva e inversão: exatas;
- $\mu$: regularização auxiliar removida no limite;
- potencial tipo Yang--Mills: reconstrução efetiva GDQ;
- $\kappa_C$ e valor numérico de $\sigma$: posteriores.
