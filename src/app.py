import streamlit as st
import pandas as pd
import json
import google.generativeai as genai

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(page_title="ALVO - Mentor Financeiro", page_icon="🎯", layout="centered")
st.title("🎯 ALVO: Seu Mentor Financeiro")
st.write("Acelere suas metas com inteligência e matemática.")

# ==========================================
# 2. CARREGAMENTO DOS DADOS (PANDAS & JSON)
# ==========================================
@st.cache_data
def carregar_dados():
    try:
        # Lendo os CSVs
        df_transacoes = pd.read_csv("data/transacoes.csv")
        df_atendimento = pd.read_csv("data/historico_atendimento.csv")
        
        # Lendo os JSONs
        with open("data/perfil_investidor.json", "r", encoding="utf-8") as f:
            perfil = json.load(f)
        with open("data/produtos_financeiros.json", "r", encoding="utf-8") as f:
            produtos = json.load(f)
            
        # O "Pulo do Gato" Matemático: Calculando o saldo líquido real
        entradas = df_transacoes[df_transacoes['tipo'] == 'entrada']['valor'].sum()
        saidas = df_transacoes[df_transacoes['tipo'] == 'saida']['valor'].sum()
        saldo_livre = entradas - saidas
        
        return perfil, produtos, saldo_livre, df_atendimento
    except Exception as e:
        st.error(f"⚠️ Erro ao carregar os dados. Verifique se os arquivos estão na pasta 'data/'. Detalhe: {e}")
        return None, None, None, None

perfil, produtos, saldo_livre, df_atendimento = carregar_dados()

# ==========================================
# 3. PREPARAÇÃO DO SYSTEM PROMPT
# ==========================================
def montar_system_prompt():
    if not perfil:
        return "Erro ao carregar dados."
    
    aceita_risco = "SIM" if perfil.get("aceita_risco") else "NÃO"
    
    prompt = f"""
    Você é o ALVO (Assistente Lógico para Valorizar Objetivos), um mentor financeiro virtual.
    Seu objetivo principal é analisar a realidade matemática do cliente e incentivar a conclusão da Reserva de Emergência.

    REGRAS DE COMPORTAMENTO:
    1. Baseie suas contas EXATAMENTE no bloco de contexto abaixo.
    2. Seja direto, prático e motivador. Fale em "prazos", "meses" e "dinheiro na conta".
    3. Nunca invente taxas ou produtos. Se não estiver no catálogo, diga que não tem.
    4. SEGURANÇA DE PERFIL (MUITO IMPORTANTE): Verifique a regra "Aceita Risco". Se for NÃO, você está ESTRITAMENTE PROIBIDO de indicar Renda Variável ou Ações.

    === DADOS DO CLIENTE ===
    - Nome: {perfil.get('nome')}
    - Renda Mensal: R$ {perfil.get('renda_mensal')} 
    - Reserva Atual: R$ {perfil.get('reserva_emergencia_atual')} | Meta da Reserva: R$ 15000.00
    - Perfil: {perfil.get('perfil_investidor')} | Aceita Risco: {aceita_risco}
    
    === FLUXO DE CAIXA CALCULADO ===
    - Saldo Livre no Mês: R$ {saldo_livre:.2f}

    === CATÁLOGO OFICIAL ===
    {json.dumps(produtos, indent=2, ensure_ascii=False)}
    """
    return prompt

# ==========================================
# 4. CONFIGURAÇÃO DA API DO GEMINI
# ==========================================
# Para testar localmente, você pode colocar sua chave da API do Google Gemini aqui na barra lateral
api_key = st.sidebar.text_input("Insira sua API Key do Google Gemini:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # Inicializando o modelo
    modelo = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=montar_system_prompt()
    )

    # ==========================================
# 5. LÓGICA DO CHAT DA INTERFACE
# ==========================================
    # Criando o histórico de mensagens na sessão do Streamlit
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = modelo.start_chat(history=[])

    # Exibir as mensagens anteriores na tela
    for mensagem in st.session_state.chat_session.history:
        papel = "user" if mensagem.role == "user" else "assistant"
        with st.chat_message(papel):
            st.markdown(mensagem.parts[0].text)

    # Receber a nova mensagem do usuário
    entrada_usuario = st.chat_input("Digite sua dúvida financeira aqui...")

    if entrada_usuario:
        # Exibir a mensagem do usuário na tela
        with st.chat_message("user"):
            st.markdown(entrada_usuario)
        
        # Obter resposta da IA e exibir
        with st.chat_message("assistant"):
            resposta_placeholder = st.empty()
            with st.spinner("O ALVO está calculando..."):
                resposta = st.session_state.chat_session.send_message(entrada_usuario)
                resposta_placeholder.markdown(resposta.text)

else:
    st.warning("👈 Por favor, insira sua API Key do Gemini na barra lateral para iniciar o assistente.")
    st.info("Dica: Você pode gerar uma chave gratuita no site do Google AI Studio.")