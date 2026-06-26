# 🎯 ALVO: Agente Financeiro Inteligente com IA Generativa

## Contexto do Projeto

Este repositório contém a solução final desenvolvida para o Lab **"Construa seu Assistente Virtual com Inteligência Artificial"** da DIO. 

O projeto apresenta o **ALVO** (*Assistente Lógico para Valorizar Objetivos*), um agente financeiro proativo construído com Python. Ao invés de atuar como um simples chatbot de perguntas e respostas, o ALVO cruza dados de fluxo de caixa, calcula a capacidade real de aporte do usuário e sugere um plano de ação matemático e sequencial (focado inicialmente na conclusão da Reserva de Emergência).

O grande diferencial tecnológico da aplicação é o uso de travas de segurança rigorosas (via System Prompt e pré-processamento de dados) para impedir a Inteligência Artificial de alucinar informações ou sugerir investimentos que violem a tolerância a risco do cliente.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

| Componente | Tecnologia |
|------------|-----------|
| **Linguagem Base** | Python 3 |
| **Interface Visual** | Streamlit |
| **Manipulação de Dados** | Pandas |
| **Modelo de IA (LLM)** | Google Gemini (via `google-generativeai`) |
| **Base de Conhecimento** | Arquivos locais estruturados em `.csv` e `.json` |

---

## 🚀 Como Executar o Projeto Localmente

Para rodar a interface do ALVO na sua máquina, siga os passos abaixo:

### 1. Clone o repositório
Abra o seu terminal e digite:
```bash
git clone [https://github.com/SEU_USUARIO/nome-do-repositorio.git](https://github.com/SEU_USUARIO/nome-do-repositorio.git)
cd nome-do-repositorio
```

### 2. Instale as dependências
Certifique-se de ter o Python instalado. Rode o comando para instalar as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 3. Inicie a aplicação
Execute o Streamlit com o comando:
```bash
streamlit run src/app.py
```
O seu navegador abrirá automaticamente no endereço `http://localhost:8501`. Insira sua chave de API gratuita do **Google AI Studio** na barra lateral para iniciar o assistente.

---

## 📚 Documentação do Agente (Entregáveis do Lab)

Todo o processo de ideação, arquitetura, testes lógicos e mitigação de alucinações da IA foi documentado passo a passo. Você pode conferir os detalhes nos links abaixo:

- 📄 [01. Documentação e Arquitetura do Agente](./docs/01-documentacao-agente.md)
- 📄 [02. Estratégia da Base de Conhecimento](./docs/02-base-conhecimento.md)
- 📄 [03. Engenharia de Prompts e Edge Cases](./docs/03-prompts.md)
- 📄 [04. Avaliação e Métricas de Qualidade](./docs/04-metricas.md)
- 📄 [05. Roteiro do Pitch de Apresentação](./docs/05-pitch.md)

---

## 📂 Estrutura do Repositório

```text
📁 lab-agente-financeiro/
│
├── 📄 README.md                      # Apresentação do projeto (Você está aqui)
├── 📄 requirements.txt               # Lista de dependências do Python
│
├── 📁 data/                          # Base de Conhecimento Local
│   ├── historico_atendimento.csv     # Histórico de chamados do cliente
│   ├── perfil_investidor.json        # Restrições e tolerância a risco
│   ├── produtos_financeiros.json     # Catálogo oficial de Renda Fixa/Variável
│   └── transacoes.csv                # Extrato de fluxo de caixa mensal
│
├── 📁 docs/                          # Documentação detalhada
│   ├── 01-documentacao-agente.md     
│   ├── 02-base-conhecimento.md       
│   ├── 03-prompts.md                 
│   ├── 04-metricas.md                
│   └── 05-pitch.md                   
│
└── 📁 src/                           # Código-fonte da aplicação
    └── app.py                        # Script principal rodando Streamlit + Gemini API
```

---
*Projeto desenvolvido para fins educacionais de composição de portfólio de tecnologia.*
