### Etapa 1
#### 1.1 Tema e Horizonte de tempo
Tema: Análise de contenção e sobrecarga no uso de servidores de GPU de um laboratório de pesquisa da UFMG, focado na análise em períodos próximos a deadlines de submissão de artigos científicos.

Horizonte de tempo: Maio de 2025 a Dezembro de 2026 (20 meses), cobrindo o histórico registrado na planilha de reservas e o cronograma de alocações futuras já agendadas para o fechamento de 2026.

#### 1.2 Evidências Empíricas e Comportamento ao Longo do Tempo

A planilha de dados do laboratório possui 46 registros e dois servidores (denominados Netuno e Mars), além de contar também com data de início e término de uso do servidor, e quem está usando.
A partir disso, foram definidas 4 conferências científicas e seus respectivos prazos de deadline de submissão de artigos, a fim de analisar como se da o uso dos servidores no período em que ocorre essas conferências:
- WebMedia 2025 (11/08/25):
- WebScience 2026 (17/12/25):
- WebMedia 2026 (21/08/26):
- WebScience 2027 (15/12/26):

Indicador Extraído da Planilha	Valor Observado
Total de reservas registradas	46 (37 no Netuno, 9 no Mars)
Pesquisadores ativos	15 usuários
Duração das reservas
Média: 4,8 dias | Mediana: 3,00 dias | Máx.: 31,00 dias

#### 1.3 Pergunta norteadora
Como a proximidade de deadlines de projetos afetam o tempo de espera, acesso e a ociosidade/sobrecarga dos servidores e o risco de atraso nos experimentos do laboratório?

#### 1.4 Fronteiras do sistema
Endógeno (dentro do sistema): Taxa de submissão de experimentos pelos pesquisadores, fila de espera por GPU, duração das reservas solicitadas, tempo efetivo de execução, disponibilidade de GPUs livres (Netuno e Mars), falhas técnicas/cancelamentos, comunicação no canal (WhatsApp) e pressão percebida pela proximidade do prazo.

Exógeno (entradas externas): Calendário fixo das deadlines das conferências (WebMedia e WebScience) e capacidade física instalada de hardware (número total de GPUs do laboratório).

Excluído: possíveis alterações dos prazos das conferências (os prazos citados aqui são hard-deadlines das conferências) e processos de revisão/aceites dos artigos após a submissão.

#### 1.5 Complexidade e emergência
Quando a ocupação dos servidores está em uma taxa muito alta, um pequeno atraso de um usuário pode se propagar em cascata para os próximos usuários que estão em uma fila de espera, gerando problemas de entrega.

Comportamento emergente: Ao perceberem uma possível lotação dos servidores perto de um deadline, pode acontecer de pesquisadores reservarem janelas de tempo cada vez maiores por precaução ou iniciar execuções no servidor sem aviso prévio, gerando atrasos artificiais e problemas técnicos.

### 2 Diagramas de Loop Causal

Ver 'diagrama_loop_causal' em imagens.
Foi identificado 4 ciclos de reforços em vermelho e 2 ciclos de equilíbrio em azuis.