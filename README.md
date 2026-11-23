# Análise de Contenção e Sobrecarga em Servidores de GPU (UFMG)

Modelagem de Dinâmica de Sistemas aplicada ao gerenciamento de infraestrutura computacional compartilhada em um laboratório de pesquisa da UFMG, com foco no impacto de prazos de submissão científica (*deadlines*) sobre filas de espera, ociosidade e sobrecarga de GPUs.

---

## Sumário

- [Etapa 1 — Contextualização e Definição do Problema](#etapa-1--contextualização-e-definição-do-problema)
  - [1.1 Tema e Horizonte de Tempo](#11-tema-e-horizonte-de-tempo)
  - [1.2 Evidências Empíricas e Comportamento ao Longo do Tempo](#12-evidências-empíricas-e-comportamento-ao-longo-do-tempo)
  - [1.3 Pergunta Norteadora](#13-pergunta-norteadora)
  - [1.4 Fronteiras do Sistema](#14-fronteiras-do-sistema)
  - [1.5 Complexidade e Emergência](#15-complexidade-e-emergência)
- [Etapa 2 — Diagramas de Loop Causal](#etapa-2--diagramas-de-loop-causal)

---

## Etapa 1 — Contextualização e Definição do Problema

### 1.1 Tema e Horizonte de Tempo

* **Tema:** Análise de contenção e sobrecarga no uso de servidores de GPU de um laboratório de pesquisa da UFMG, focada em períodos próximos a *deadlines* de submissão de artigos científicos.
* **Horizonte de tempo:** **Maio de 2025 a Dezembro de 2026 (20 meses)**, cobrindo o histórico registrado na planilha de reservas e o cronograma de alocações futuras já agendadas para o fechamento de 2026.

---

### 1.2 Evidências Empíricas e Comportamento ao Longo do Tempo

A base de dados do laboratório contém **46 registros válidos** distribuídos entre dois servidores (**Netuno** e **Mars**), contemplando data/hora de início, data/hora de término e o pesquisador responsável pela alocação.

Para avaliar o comportamento da demanda sob pressão temporal, foram mapeadas **4 conferências científicas** e suas respectivas datas limite de submissão:

* **WebMedia 2025:** `11/08/2025`
* **WebScience 2026:** `17/12/2025`
* **WebMedia 2026:** `21/08/2026`
* **WebScience 2027:** `15/12/2026`

#### Resumo dos Indicadores Extraídos

| Indicador Extraído da Planilha | Valor Observado |
| :--- | :--- |
| **Total de reservas registradas** | 46 (37 no **Netuno**, 9 no **Mars**) |
| **Pesquisadores ativos** | 15 usuários |
| **Duração das reservas** | **Média:** 4,8 dias \| **Mediana:** 3,00 dias \| **Máx.:** 31,00 dias |

---

### 1.3 Pergunta Norteadora

> *Como a proximidade de deadlines de projetos afeta o tempo de espera, o acesso, a ociosidade/sobrecarga dos servidores e o risco de atraso nos experimentos do laboratório?*

---

### 1.4 Fronteiras do Sistema

| Classificação | Elementos Considerados |
| :--- | :--- |
| **Endógeno** *(dentro do sistema)* | Taxa de submissão de experimentos pelos pesquisadores, fila de espera por GPU, duração das reservas solicitadas, tempo efetivo de execução, disponibilidade de GPUs livres (Netuno e Mars), falhas técnicas/cancelamentos, comunicação no canal (WhatsApp) e pressão percebida pela proximidade do prazo. |
| **Exógeno** *(entradas externas)* | Calendário fixo das *deadlines* das conferências (WebMedia e WebScience) e capacidade física instalada de hardware (número total de GPUs do laboratório). |
| **Excluído** *(fora de escopo)* | Possíveis alterações ou prorrogações dos prazos das conferências (considerados *hard-deadlines*) e processos de revisão/aceite dos artigos após a submissão. |

---

### 1.5 Complexidade e Emergência

* **Efeito Cascata:** Quando a taxa de ocupação dos servidores atinge níveis críticos, um pequeno atraso na execução de um usuário propaga-se em cascata para os demais pesquisadores na fila de espera, comprometendo o cronograma de entregas.
* **Comportamento Emergente:** Ao perceberem a iminência de lotação dos servidores próximo a um *deadline*, os pesquisadores tendem a reservar janelas de tempo cada vez maiores por precaução (*hoarding* de recursos) ou iniciar execuções sem aviso prévio no canal oficial, gerando ociosidade artificial, conflitos de acesso e problemas técnicos.

---

## Etapa 2 — Diagramas de Loop Causal

O modelo qualitativo do sistema identifica **4 ciclos de reforço** (destacados em **vermelho**) e **2 ciclos de equilíbrio** (destacados em **azul**).

![Diagrama de Loop Causal](imagens/diagrama_loop_causal.pdf)
