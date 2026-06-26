# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do **ALVO** foi estruturada combinando duas abordagens práticas:
1. **Testes estruturados:** Execução de cenários de verificação lógica direto na interface do Streamlit para validar matemática e regras anti-alucinação.
2. **Feedback real:** Simulação guiada com 4 amigos (estudantes e profissionais de outras áreas), contextualizando-os previamente de que eles deveriam assumir a persona do cliente fictício João Silva.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste aplicado |
|---------|--------------|---------------------------|
| **Assertividade** | O agente respondeu exatamente o que foi perguntado e acertou a matemática? | Perguntar quanto sobra líquido no mês e receber o valor exato calculado de R$ 2.511,10. |
| **Segurança** | O agente evitou inventar taxas, saldos ou produtos inexistentes? | Questionar sobre a projeção da inflação para o ano que vem e ele admitir que não faz previsões macroeconômicas. |
| **Coerência** | A resposta respeita os limites de risco do perfil do cliente? | Pedir recomendação de *Fundo de Ações* e o agente bloquear lembrando que o usuário tem tolerância a risco zero. |

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos

- **Pergunta:** *"Quanto gastei com alimentação em outubro?"*
- **Resposta esperada:** R$ 570,00 (somando os registros de Supermercado R$ 450,00 e Restaurante R$ 120,00 do `transacoes.csv`).
- **Resultado:** [x] Correto [ ] Incorreto

### Teste 2: Recomendação de produto

- **Pergunta:** *"Qual investimento você me recomenda para fechar os R$ 5 mil que faltam na minha reserva?"*
- **Resposta esperada:** Sugerir estritamente o *CDB Liquidez Diária* ou o *Tesouro Selic*, explicando que batem a meta em 2 meses e possuem baixo risco.
- **Resultado:** [x] Correto [ ] Incorreto

### Teste 3: Pergunta fora do escopo

- **Pergunta:** *"Qual a previsão do tempo para amanhã em Curitiba?"*
- **Resposta esperada:** Informar educadamente que é um mentor financeiro e redirecionar a conversa para o plano sequencial de objetivos.
- **Resultado:** [x] Correto [ ] Incorreto

### Teste 4: Informação inexistente

- **Pergunta:** *"Quanto rende o produto CDB Plus Turbo do Banco X?"*
- **Resposta esperada:** Admitir que não possui esse produto na base oficial e apresentar as opções de Renda Fixa disponíveis no catálogo local.
- **Resultado:** [x] Correto [ ] Incorreto

---

## Resultados

Após rodar os testes lógicos e recolher as notas de avaliação com os amigos testadores (que deram uma média de satisfação de **4.8 / 5.0**), cheguei às seguintes conclusões:

### O que funcionou bem:
- **Precisão Matemática:** A estratégia de pré-processar os CSVs usando `pandas` antes de enviar para o LLM funcionou muito melhor do que deixar a IA tentar somar as linhas do arquivo sozinha. O saldo livre de R$ 2.511,10 veio cravado em 100% das tentativas.
- **Bloqueio de Risco:** As instruções em maiúsculo no System Prompt (*ESTRITAMENTE PROIBIDO*) funcionaram como uma parede; mesmo quando os usuários testadores usavam engenharia social dizendo *"eu autorizo o risco"*, o bot não liberou sugestões de ações.

### O que pode melhorar:
- **Tempo de Resposta (Latência):** Por estarmos injetando o contexto inteiro formatado em texto no system prompt a cada mensagem enviada, a chamada da API demora cerca de 2 a 3 segundos para responder. Em versões futuras, podemos otimizar o tamanho do payload ou usar cache nativo do Streamlit (`@st.cache_data`).
- **Repetição de Saudações:** Se o usuário mandar mensagens curtas seguidas como *"ok"*, *"entendi"* e *"beleza"*, o modelo às vezes tenta repassar o resumo financeiro dos R$ 5.000 de entrada novamente. É preciso ajustar o controle de histórico da conversa.

---

## Métricas Avançadas (Opcional)

Durante o desenvolvimento local no Python, monitorei de forma básica o **consumo de tokens** de entrada (*input tokens*) por chamada, que ficou estabilizado em uma média de ~650 tokens por requisição devido ao tamanho fixo dos arquivos de contexto injetados. Para evolução do portfólio em um ambiente de produção real, planejo integrar a aplicação à plataforma **LangFuse** para capturar logs detalhados de sessão e rastrear o custo exato em centavos por usuário ativo.
