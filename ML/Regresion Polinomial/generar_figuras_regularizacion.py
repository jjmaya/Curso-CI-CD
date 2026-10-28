"""Genera las figuras y los resultados numéricos citados en
Teoria_RegresionPolinomial.md (sección de regularización).

Uso: python generar_figuras_regularizacion.py
Las imágenes se guardan en la carpeta img/ junto a este archivo.
"""
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import (
    Lasso,
    LassoCV,
    LinearRegression,
    Ridge,
    RidgeCV,
    lasso_path,
)
from sklearn.model_selection import KFold, cross_val_score, validation_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

warnings.filterwarnings("ignore")
IMG = Path(__file__).parent / "img"
IMG.mkdir(exist_ok=True)
plt.rcParams.update({"figure.dpi": 130, "axes.grid": True, "grid.alpha": 0.3})


def guardar(nombre):
    plt.tight_layout()
    plt.savefig(IMG / nombre)
    plt.close()


# ---------------------------------------------------------------------------
# 1. Ejemplo de las notas: 5 puntos y un polinomio de grado 4
# ---------------------------------------------------------------------------
x = np.array([0.5, 1.0, 1.3, 3.5, 4.0]).reshape(-1, 1)
y = np.array([1.0, 2.6, 2.0, 4.4, 5.0])
grilla = np.linspace(0.3, 4.3, 300).reshape(-1, 1)


def modelo_poli(estimador):
    return make_pipeline(
        PolynomialFeatures(4, include_bias=False), StandardScaler(), estimador
    )


fig, ejes = plt.subplots(1, 3, figsize=(12, 3.6), sharey=True)
casos = [
    ("Sin regularización (α = 0)", LinearRegression()),
    ("Ridge (α = 0.01)", Ridge(alpha=0.01)),
    ("Ridge (α = 0.3)", Ridge(alpha=0.3)),
]
for eje, (titulo, est) in zip(ejes, casos):
    m = modelo_poli(est).fit(x, y)
    eje.scatter(x, y, color="darkred", zorder=3)
    eje.plot(grilla, m.predict(grilla), color="steelblue")
    eje.set_title(titulo)
    eje.set_xlabel("x")
ejes[0].set_ylabel("y")
guardar("01_ejemplo_grado4.png")

# ---------------------------------------------------------------------------
# 2. Geometría de L2 y L1
# ---------------------------------------------------------------------------
w1, w2 = np.meshgrid(np.linspace(-1.2, 2.2, 400), np.linspace(-1.2, 2.2, 400))
centro = np.array([1.4, 0.55])
elipse = (
    1.0 * (w1 - centro[0]) ** 2
    + 1.2 * (w1 - centro[0]) * (w2 - centro[1])
    + 2.2 * (w2 - centro[1]) ** 2
)

fig, ejes = plt.subplots(1, 2, figsize=(10, 4.6))
t = np.linspace(0, 2 * np.pi, 400)
for eje, tipo in zip(ejes, ["L2 (Ridge)", "L1 (Lasso)"]):
    eje.contour(w1, w2, elipse, levels=[0.1, 0.35, 0.75, 1.3], colors="steelblue")
    eje.plot(*centro, "k*", markersize=10, label="Solución sin penalizar")
    if tipo.startswith("L2"):
        r = 1.0
        eje.fill(r * np.cos(t), r * np.sin(t), color="orange", alpha=0.35)
        eje.plot(r * np.cos(t), r * np.sin(t), color="darkorange")
        # Punto de tangencia calculado numéricamente sobre el círculo
        c = np.stack([np.cos(t), np.sin(t)])
        q = (
            1.0 * (c[0] - centro[0]) ** 2
            + 1.2 * (c[0] - centro[0]) * (c[1] - centro[1])
            + 2.2 * (c[1] - centro[1]) ** 2
        )
        p = c[:, q.argmin()]
    else:
        rombo = np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 0]])
        eje.fill(rombo[:, 0], rombo[:, 1], color="orange", alpha=0.35)
        eje.plot(rombo[:, 0], rombo[:, 1], color="darkorange")
        p = np.array([1.0, 0.0])
    eje.plot(*p, "ro", label="Solución regularizada")
    eje.axhline(0, color="gray", lw=0.8)
    eje.axvline(0, color="gray", lw=0.8)
    eje.set_title(f"Región permitida {tipo}")
    eje.set_xlabel("$w_1$")
    eje.set_ylabel("$w_2$")
    eje.set_aspect("equal")
    eje.set_xlim(-1.2, 2.2)
    eje.set_ylim(-1.2, 1.6)
ejes[0].legend(loc="upper right", fontsize=8)
guardar("02_geometria_l1_l2.png")

# ---------------------------------------------------------------------------
# 3. Contracción: Ridge vs umbral suave de Lasso
# ---------------------------------------------------------------------------
z = np.linspace(-3, 3, 400)
lam = 1.0
plt.figure(figsize=(5.5, 4.2))
plt.plot(z, z, "k--", label="Sin regularización")
plt.plot(z, z / (1 + lam), color="darkorange", label="Ridge: $z/(1+\\lambda)$")
plt.plot(
    z,
    np.sign(z) * np.maximum(np.abs(z) - lam / 2, 0),
    color="steelblue",
    label="Lasso: umbral suave",
)
plt.xlabel("Coeficiente sin penalizar")
plt.ylabel("Coeficiente estimado")
plt.title("Ridge encoge; Lasso encoge y anula")
plt.legend()
guardar("03_contraccion_ridge_lasso.png")

# ---------------------------------------------------------------------------
# 4. Caminos de coeficientes con el conjunto 'diabetes' (scikit-learn)
# ---------------------------------------------------------------------------
datos = load_diabetes()
Xd = StandardScaler().fit_transform(datos.data)
yd = datos.target - datos.target.mean()
nombres = datos.feature_names

alphas = np.logspace(-3, 4, 80)
coef_ridge = np.array([Ridge(alpha=a).fit(Xd, yd).coef_ for a in alphas])
alphas_l, coef_lasso, _ = lasso_path(Xd, yd, alphas=np.logspace(-3, 1.5, 80))

fig, ejes = plt.subplots(1, 2, figsize=(11, 4.2))
ejes[0].plot(alphas, coef_ridge)
ejes[0].set_xscale("log")
ejes[0].set_title("Ridge: los coeficientes se encogen, pero no llegan a 0")
ejes[1].plot(alphas_l, coef_lasso.T)
ejes[1].set_xscale("log")
ejes[1].set_title("Lasso: los coeficientes se van anulando uno a uno")
for eje in ejes:
    eje.set_xlabel("α (escala logarítmica)")
    eje.set_ylabel("Coeficiente")
ejes[1].legend(nombres, ncol=2, fontsize=7, loc="upper right")
guardar("04_caminos_coeficientes.png")

# ---------------------------------------------------------------------------
# 5. Efecto de α: ajuste y curva de validación (seno con ruido, grado 12)
# ---------------------------------------------------------------------------
rng = np.random.default_rng(0)
xs = np.sort(rng.uniform(0, 1, 40)).reshape(-1, 1)
ys = np.sin(2 * np.pi * xs[:, 0]) + rng.normal(0, 0.3, 40)
xg = np.linspace(0, 1, 300).reshape(-1, 1)


def poli_ridge(alpha, grado=12):
    return make_pipeline(
        PolynomialFeatures(grado, include_bias=False), StandardScaler(), Ridge(alpha)
    )


fig, ejes = plt.subplots(1, 4, figsize=(15, 3.4), sharey=True)
for eje, a in zip(ejes, [1e-8, 1e-3, 1e-1, 100]):
    m = poli_ridge(a).fit(xs, ys)
    eje.scatter(xs, ys, s=14, color="gray")
    eje.plot(xg, np.sin(2 * np.pi * xg), "g--", lw=1, label="Función real")
    eje.plot(xg, m.predict(xg), color="crimson", label="Modelo")
    eje.set_title(f"α = {a:g}")
    eje.set_ylim(-2, 2)
ejes[0].legend(fontsize=7)
guardar("05_efecto_alpha_ajuste.png")

alphas_v = np.logspace(-8, 3, 30)
cv = KFold(5, shuffle=True, random_state=0)
tr, va = validation_curve(
    poli_ridge(1.0),
    xs,
    ys,
    param_name="ridge__alpha",
    param_range=alphas_v,
    cv=cv,
    scoring="neg_root_mean_squared_error",
)
mejor = alphas_v[(-va.mean(axis=1)).argmin()]
plt.figure(figsize=(6, 4))
plt.semilogx(alphas_v, -tr.mean(axis=1), label="Entrenamiento")
plt.semilogx(alphas_v, -va.mean(axis=1), label="Validación cruzada")
plt.axvline(mejor, color="k", ls=":", label=f"Mejor α ≈ {mejor:.1e}")
plt.xlabel("α")
plt.ylabel("RMSE")
plt.title("Curva de validación: bajo ajuste ← → sobreajuste")
plt.legend()
guardar("06_curva_validacion_alpha.png")
print(f"[seno grado 12] mejor alpha CV = {mejor:.2e}")

# ---------------------------------------------------------------------------
# 6. Multicolinealidad: estabilidad de coeficientes (bootstrap)
# ---------------------------------------------------------------------------
rng = np.random.default_rng(1)
n = 60
a = rng.normal(size=n)
Xc = np.column_stack([a, a + rng.normal(0, 0.05, n), rng.normal(size=n)])
yc = 3 * Xc[:, 0] + 3 * Xc[:, 1] + 1 * Xc[:, 2] + rng.normal(0, 1, n)

corr = np.corrcoef(Xc[:, 0], Xc[:, 1])[0, 1]
vif = []
for j in range(3):
    otros = np.delete(Xc, j, axis=1)
    r2 = LinearRegression().fit(otros, Xc[:, j]).score(otros, Xc[:, j])
    vif.append(1 / (1 - r2))
print(f"[colinealidad] corr(x1,x2)={corr:.3f}  VIF={np.round(vif, 1)}")

coefs = {"OLS": [], "Ridge": []}
for _ in range(300):
    idx = rng.integers(0, n, n)
    coefs["OLS"].append(LinearRegression().fit(Xc[idx], yc[idx]).coef_)
    coefs["Ridge"].append(Ridge(alpha=5.0).fit(Xc[idx], yc[idx]).coef_)
fig, ejes = plt.subplots(1, 2, figsize=(9, 3.8), sharey=True)
for eje, (nombre, c) in zip(ejes, coefs.items()):
    c = np.array(c)
    eje.boxplot(c, tick_labels=["$w_1$", "$w_2$", "$w_3$"])
    eje.axhline(3, color="g", ls=":", lw=1)
    eje.set_title(f"{nombre}: coeficientes en 300 remuestreos")
guardar("07_multicolinealidad.png")
for nombre, c in coefs.items():
    c = np.array(c)
    print(f"[colinealidad] {nombre}: media={c.mean(0).round(2)} desv={c.std(0).round(2)}")

# ---------------------------------------------------------------------------
# 7. Solución matemática programada desde cero
# ---------------------------------------------------------------------------
def ridge_cerrado(X, y, alpha):
    """min ||y - b - Xw||² + α||w||²  →  w = (XᵀX + αI)⁻¹ Xᵀy (datos centrados)."""
    mx, my = X.mean(0), y.mean()
    Xc_, yc_ = X - mx, y - my
    w = np.linalg.solve(Xc_.T @ Xc_ + alpha * np.eye(X.shape[1]), Xc_.T @ yc_)
    return my - mx @ w, w


def umbral_suave(rho, lam):
    return np.sign(rho) * np.maximum(np.abs(rho) - lam, 0.0)


def lasso_cd(X, y, alpha, iteraciones=2000, tol=1e-10):
    """min 1/(2n)||y - b - Xw||² + α||w||₁ por descenso de coordenadas."""
    n_, d = X.shape
    mx, my = X.mean(0), y.mean()
    Xc_, yc_ = X - mx, y - my
    w = np.zeros(d)
    z = (Xc_**2).sum(0)
    for _ in range(iteraciones):
        w_ant = w.copy()
        for j in range(d):
            r_j = yc_ - Xc_ @ w + Xc_[:, j] * w[j]
            w[j] = umbral_suave(Xc_[:, j] @ r_j, n_ * alpha) / z[j]
        if np.max(np.abs(w - w_ant)) < tol:
            break
    return my - mx @ w, w


b1, w1_ = ridge_cerrado(Xd, yd, 10.0)
m = Ridge(alpha=10.0).fit(Xd, yd)
print("[ridge] max|w_propio - w_sklearn| =", np.abs(w1_ - m.coef_).max())

b2, w2_ = lasso_cd(Xd, yd, 1.0)
m = Lasso(alpha=1.0, tol=1e-12, max_iter=100000).fit(Xd, yd)
print("[lasso] max|w_propio - w_sklearn| =", np.abs(w2_ - m.coef_).max())
print("[lasso] coeficientes propios:", dict(zip(nombres, w2_.round(2))))

# ---------------------------------------------------------------------------
# 8. Polinomial + regularización (diabetes, grado 2 → 65 variables)
# ---------------------------------------------------------------------------
Xr, yr = datos.data, datos.target
cv_ext = KFold(5, shuffle=True, random_state=42)
al = np.logspace(-3, 3, 60)
al_lasso = np.logspace(-1, 1.7, 40)


def pipe(est, grado):
    return make_pipeline(
        PolynomialFeatures(grado, include_bias=False), StandardScaler(), est
    )


modelos = {
    "Lineal (grado 1)": pipe(LinearRegression(), 1),
    "Polinomial g=2, sin regularizar": pipe(LinearRegression(), 2),
    "Polinomial g=2 + Ridge": pipe(RidgeCV(alphas=al), 2),
    "Polinomial g=2 + Lasso": pipe(LassoCV(alphas=al_lasso, cv=5, max_iter=20000), 2),
}
print("[diabetes] RMSE medio (CV externa 5-fold):")
for nombre, mod in modelos.items():
    s = -cross_val_score(
        mod, Xr, yr, cv=cv_ext, scoring="neg_root_mean_squared_error"
    )
    print(f"  {nombre}: {s.mean():.2f} ± {s.std():.2f}")

lasso_poli = pipe(LassoCV(alphas=al_lasso, cv=5, max_iter=20000), 2).fit(Xr, yr)
coef = lasso_poli[-1].coef_
print(f"[diabetes] Lasso g=2: {np.sum(coef != 0)} coeficientes no nulos de {coef.size}")
ridge_poli = pipe(RidgeCV(alphas=al), 2).fit(Xr, yr)
print(f"[diabetes] alpha Ridge={ridge_poli[-1].alpha_:.3g}  alpha Lasso={lasso_poli[-1].alpha_:.3g}")
