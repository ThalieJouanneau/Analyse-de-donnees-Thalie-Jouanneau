#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats
import matplotlib.pyplot as plt
import os

#https://docs.scipy.org/doc/scipy/reference/stats.html

dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']

print(dist_names)

# Question 1
print("Question 1")

# Distributions statistiques de variables discrètes
# Loi de Dirac

x = np.arange(0, 7)
y = np.zeros(len(x))
y[3] = 1

plt.figure()
plt.bar(x, y)
plt.title("Loi de Dirac")
plt.xlabel("Valeurs possibles")
plt.ylabel("Probabilite")
plt.xticks(x)
plt.savefig("./img/loi_dirac.png")
plt.close()


# Loi uniforme discrète

x = np.arange(1, 7)
y = scipy.stats.randint.pmf(x, 1, 7)

plt.figure()
plt.bar(x, y)
plt.title("Loi uniforme discrete")
plt.xlabel("Valeurs possibles")
plt.ylabel("Probabilite")
plt.xticks(x)
plt.savefig("./img/loi_uniforme_discrete.png")
plt.close()

# Loi binomiale

n = 10
p = 0.5
x = np.arange(0, n + 1)
y = scipy.stats.binom.pmf(x, n, p)

plt.figure()
plt.bar(x, y)
plt.title("Loi binomiale (n=10, p=0.5)")
plt.xlabel("Nombre de succes")
plt.ylabel("Probabilite")
plt.xticks(x)
plt.savefig("./img/loi_binomiale.png")
plt.close()

# Loi de Poisson

lambda_poisson = 4
x = np.arange(0, 16)
y = scipy.stats.poisson.pmf(x, lambda_poisson)

plt.figure()
plt.bar(x, y)
plt.title("Loi de Poisson (lambda=4)")
plt.xlabel("Nombre d'evenements")
plt.ylabel("Probabilite")
plt.xticks(x)
plt.savefig("./img/loi_poisson.png")
plt.close()

# Loi de Zipf-Mandelbrot

k = np.arange(1, 21)
q = 1
s = 1.2

poids = 1 / ((k + q) ** s)
y = poids / np.sum(poids)

plt.figure()
plt.bar(k, y)
plt.title("Loi de Zipf-Mandelbrot")
plt.xlabel("Rang")
plt.ylabel("Probabilite")
plt.savefig("./img/loi_zipf_mandelbrot.png")
plt.close()

# Distributions statistiques de variables continues
# Loi normale

x = np.linspace(-4, 4, 300)
y = scipy.stats.norm.pdf(x, loc=0, scale=1)

plt.figure()
plt.plot(x, y)
plt.title("Loi normale (moyenne=0, ecart-type=1)")
plt.xlabel("Valeurs")
plt.ylabel("Densite de probabilite")
plt.savefig("./img/loi_normale.png")
plt.close()

# Loi log-normale

x = np.linspace(0.01, 5, 300)
y = scipy.stats.lognorm.pdf(x, s=0.5, loc=0, scale=1)

plt.figure()
plt.plot(x, y)
plt.title("Loi log-normale")
plt.xlabel("Valeurs")
plt.ylabel("Densite de probabilite")
plt.savefig("./img/loi_lognormale.png")
plt.close()


# Loi uniforme continue

x = np.linspace(-1, 11, 300)
y = scipy.stats.uniform.pdf(x, loc=0, scale=10)

plt.figure()
plt.plot(x, y)
plt.title("Loi uniforme continue")
plt.xlabel("Valeurs")
plt.ylabel("Densite de probabilite")
plt.savefig("./img/loi_uniforme_continue.png")
plt.close()

# Loi du khi-deux

x = np.linspace(0, 15, 300)
y = scipy.stats.chi2.pdf(x, df=4)

plt.figure()
plt.plot(x, y)
plt.title("Loi du khi-deux (4 degres de liberte)")
plt.xlabel("Valeurs")
plt.ylabel("Densite de probabilite")
plt.savefig("./img/loi_chi2.png")
plt.close()

# Loi de Pareto

x = np.linspace(1, 10, 300)
y = scipy.stats.pareto.pdf(x, b=3, loc=0, scale=1)

plt.figure()
plt.plot(x, y)
plt.title("Loi de Pareto")
plt.xlabel("Valeurs")
plt.ylabel("Densite de probabilite")
plt.savefig("./img/loi_pareto.png")
plt.close()

# Question 2
print("Question 2")

def moyenne_ecart_type(loi):
    moyenne = loi.mean()
    ecart_type = loi.std()
    return moyenne, ecart_type

# Loi de Dirac : la valeur 3 a une probabilite de 1
loi_dirac = scipy.stats.rv_discrete(
    values=([3], [1])
)

print("Dirac :", moyenne_ecart_type(loi_dirac))



# Loi uniforme discrete : valeurs de 1 a 6
loi_uniforme_discrete = scipy.stats.randint(1, 7)
print("Uniforme discrete :", moyenne_ecart_type(loi_uniforme_discrete))

# Loi binomiale : 10 essais, probabilite de succes de 0.5
loi_binomiale = scipy.stats.binom(n=10, p=0.5)
print("Binomiale :", moyenne_ecart_type(loi_binomiale))

# Loi de Poisson : moyenne theorique de 4 evenements
loi_poisson = scipy.stats.poisson(mu=4)
print("Poisson :", moyenne_ecart_type(loi_poisson))

# Loi de Zipf simple
loi_zipf = scipy.stats.zipf(a=2)
print("Zipf :", moyenne_ecart_type(loi_zipf))

# Loi de Zipf-Mandelbrot
moyenne_zipf_mandelbrot = np.sum(k * probabilites)

variance_zipf_mandelbrot = np.sum(
    ((k - moyenne_zipf_mandelbrot) ** 2) * probabilites
)

ecart_type_zipf_mandelbrot = np.sqrt(variance_zipf_mandelbrot)

print("Zipf-Mandelbrot :")
print("Moyenne :", moyenne_zipf_mandelbrot)
print("Ecart type :", ecart_type_zipf_mandelbrot)

# Loi normale : moyenne 0, ecart type 1
loi_normale = scipy.stats.norm(loc=0, scale=1)
print("Normale :", moyenne_ecart_type(loi_normale))

# Loi log-normale : memes parametres que pour le graphique
loi_lognormale = scipy.stats.lognorm(s=0.5, loc=0, scale=1)
print("Log-normale :", moyenne_ecart_type(loi_lognormale))

# Loi uniforme continue entre 0 et 10
loi_uniforme_continue = scipy.stats.uniform(loc=0, scale=10)
print("Uniforme continue :", moyenne_ecart_type(loi_uniforme_continue))

# Loi du khi-deux : 4 degres de liberte
loi_chi2 = scipy.stats.chi2(df=4)
print("Khi-deux :", moyenne_ecart_type(loi_chi2))

# Loi de Pareto
loi_pareto = scipy.stats.pareto(b=3, loc=0, scale=1)
print("Pareto :", moyenne_ecart_type(loi_pareto))
