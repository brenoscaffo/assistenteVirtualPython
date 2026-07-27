# Criando um assitente de IA
# Importaçao das bibliotecas necessárias

# biblioteca para acessar variáveis de ambiente do sistema operacional
import os
# biblioteca para criar a interface do usuário
import streamlit as st
# biblioteca para interagir com a API da Groq
from groq import Groq

# Configurações da página do Streamlit
st.set_page_config(
    page_title="AI Coder Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Customização do prompt do sistema para o assistente de IA
CUSTOM_PROMPT = """
Você é o "DSA Coder", um assistente de IA especialista em programação, com foco principal em Python. Sua missão é ajudar desenvolvedores iniciantes com dúvidas de programação de forma clara, precisa e útil.

REGRAS DE OPERAÇÃO:
1.  **Foco em Programação**: Responda apenas a perguntas relacionadas a programação, algoritmos, estruturas de dados, bibliotecas e frameworks. Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é exclusivamente em auxiliar com código.
2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
    * **Exemplo de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta. O código deve ser bem comentado para explicar as partes importantes.
    * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
    * **Documentação de Referência**: Ao final, inclua uma seção chamada "📚 Documentação de Referência" com um link direto e relevante para a documentação oficial da Linguagem Python (docs.python.org) ou da biblioteca em questão.
3.  **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
4.  **Exemplos Práticos**: Sempre que possível, forneça exemplos práticos de como aplicar o conceito ou função discutida, incluindo casos de uso comuns e melhores práticas.
"""

# Criação da barra lateral no Streamlit
with st.sidebar:
    # Título da barra lateral
    st.title("AI Coder Assistant")

    # Texto explicativo sobre o assistente
    st.markdown("Um assistente de IA focado em Python para apoiar devs iniciantes na linguagem.")

    # Campo para inserir a chave de API da Groq
    groq_api_key = st.text_input(
        "Insira sua API Key Groq", 
        type="password",
        help="Sua chave de API Groq"
    )

    # Adiciona linhas divisórias e explicações extras na barra lateral
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com Linguagem Python. IA pode cometer erros. Sempre verifique as respostas.")

    st.markdown("---")
    st.markdown("Projeto de introdução a LLMs e IA Generativa, desenvolvido para fins educacionais e de estudo de caso.")

    # link do diretorio github pessoal
    st.markdown("🔗 [GitHub](https://github.com/brenoscaffo)") 

    # link do linkedin pessoal
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/brenoscaffo/)")

# Mensagem de boas-vindas na interface principal do Streamlit
st.title("Assistente de Programação Python")

# Subtítulo adicional
st.title("Projeto de cunho educacional, desenvolvido para fins de aprendizado.")

#Textio auxiliar abaixo do título
st.caption("Tire suas dúvidas com o assistente de IA, focado em programação Python. Obtenha a solução de código, explicação e referência com facilidade.")

# Inicializa histórico de mensagens na sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico de mensagens na interface principal do Streamlit
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Inicializa a variável do cliente Groq como None
client = None

if groq_api_key:

    try: 
        # Cria uma instância do cliente Groq com a chave de API fornecida
        client = Groq(api_key=groq_api_key)

    except Exception as e:
        # Exibe uma mensagem de erro caso a criação do cliente falhe
        st.error(f"Erro ao criar o cliente Groq: {e}")

elif st.session_state.messages:
    
    # Se não houver chave de API fornecida, exibe uma mensagem de aviso
    st.warning("Por favor, insira sua chave de API Groq na barra lateral para continuar.")

if prompt := st.chat_input("Digite sua pergunta sobre programação Python aqui..."):

    if not client:
        # Se o cliente Groq não estiver inicializado, exibe uma mensagem de aviso
        st.warning("Por favor, insira sua chave de API Groq na barra lateral para continuar.")
        st.stop()

    # Adiciona a pergunta do usuário ao histórico de mensagens
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibe a pergunta do usuário na interface
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara as mensagens para enviar à API, incluindo o prompt do sistema
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        messages_for_api.append(msg)

    with st.chat_message("assistant"):

        with st.spinner("Aguarde enquanto o assistente processa sua pergunta..."):

            try:

                # Chama a API da Groq para obter a resposta do modelo
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model = "openai/gpt-oss-120b",
                    temperature=0.7,
                    max_tokens=2408
                )

                # Obtém a resposta do modelo
                resposta_ai = chat_completion.choices[0].message.content

                # Exibir a resposta do assistente na interface
                st.markdown(resposta_ai)

                # Adiciona a resposta do assistente ao histórico de mensagens
                st.session_state.messages.append({"role": "assistant", "content": resposta_ai})

            except Exception as e:
                # Exibe uma mensagem de erro caso a chamada à API falhe
                st.error(f"Ocorreu um erro durante a comunicação com a API da Groq: {e}")

st.markdown(
     """
        <div style="text-align: center; color: gray;">
            <hr>
            <p>Plataforma de Assistente de Programação Python - Desenvolvida para fins educacionais</p>
        </div>
        """,
        unsafe_allow_html=True
)
            
