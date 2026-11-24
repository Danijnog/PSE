# Espera média por Little (W = fila média no tempo / λ) por cenário. Rodar na pasta do repositório: python3 espera_little.py
import json, numpy as np, pandas as pd, datetime, re
nb = json.load(open('main.ipynb'))
src3 = ''.join(nb['cells'][3]['source']).split("print(df[['Nome")[0]
src7 = ''.join(nb['cells'][7]['source'])
src7 = src7.split("print(f\"Chegadas")[0] + "\n" + src7.split("print(f\"Carga")[1].split("\n",1)[1] if False else src7
df = pd.read_excel('data/servidores_gpu.xlsx')
df = df[df["Data e Hora de Início"].notna() & df["Data e Hora de Término"].notna()]
g = {'pd': pd, 'np': np, 'datetime': datetime, 're': re, 'df': df}
exec(src3, g)
df = g['df']
df_clean = df.copy()
valid = df_clean.dropna(subset=['inicio']).copy()
date_range = pd.date_range(start='2025-05-01', end='2026-12-20', freq='D')
ts = pd.DataFrame(index=date_range); ts['reservas_ativas'] = 0.0
g.update({'valid': valid, 'ts': ts})
exec(src7.replace("print(", "(lambda *a, **k: None)("), g)
simular_def, monte_carlo, DIAS, LAMBDA = g['simular_def'], g['monte_carlo'], g['DIAS'], g['LAMBDA']
print('LAMBDA', round(LAMBDA, 4), 'DBAR', round(g['DBAR'], 3))
rng_res = {}
for nome, K, alpha, lam in [('Base',2,0.5,LAMBDA),('Sem precaucao',2,0.0,LAMBDA),('K=1',1,0.5,LAMBDA),('Carga x3',2,0.5,3*LAMBDA)]:
    rng = np.random.default_rng(42)
    medQ, medW, maxQ = [], [], []
    for _ in range(200):
        sim = simular_def(DIAS, rng.poisson(lam, size=len(DIAS)), K=K, alpha=alpha)
        medQ.append(sim['Q'].mean()); maxQ.append(sim['Q'].max())
    medQ = np.array(medQ)
    print(f"{nome}: fila media (tempo) = {medQ.mean():.3f} reservas; espera media por Little = {medQ.mean()/lam:.2f} dias (lam={lam:.3f}); p95 da fila media = {np.percentile(medQ,95):.3f}")
