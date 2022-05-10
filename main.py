import datetime
import streamlit as st

st.set_page_config(
   page_title="Gerenciador Residencial e empresarial",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("Gerenciador residencial e empresarial")

st.sidebar.title("Opções")
comodo = st.sidebar.selectbox("Cômodo ou setor a ser gerenciado", ["Sala", "Quarto", "Cozinha", "Banheiro", "Escritório"])

if (comodo == "Sala"):
    dataFaxina = st.date_input("Data da última faxina completa da Sala")
    hoje = datetime.date.today()
    quantidadeDias = abs((hoje - dataFaxina).days)
    if (quantidadeDias >= 7):
        st.text("Você já precisa faxinar essa parte.")
    else:
        st.text("Pode descansar. A faxina ainda não é necessária.")
elif (comodo == "Quarto"):
    dataFaxina = st.date_input("Data da última faxina completa do Quarto")
    hoje = datetime.date.today()
    quantidadeDias = abs((hoje - dataFaxina).days)
    if (quantidadeDias >= 3):
        st.text("Você já precisa faxinar essa parte.")
    else:
        st.text("Pode descansar. A faxina ainda não é necessária.")
elif (comodo == "Cozinha"):
    dataFaxina = st.date_input("Data da última faxina completa na Cozinha")
    hoje = datetime.date.today()
    quantidadeDias = abs((hoje - dataFaxina).days)
    if (quantidadeDias >= 5):
        st.text("Você já precisa faxinar essa parte.")
    else:
        st.text("Pode descansar. A faxina ainda não é necessária.")
elif (comodo == "Banheiro"):
    dataFaxina = st.date_input("Data da última faxina completa do Banheiro")
    hoje = datetime.date.today()
    quantidadeDias = abs((hoje - dataFaxina).days)
    if (quantidadeDias >= 3):
        st.text("Você já precisa faxinar essa parte.")
    else:
        st.text("Pode descansar. A faxina ainda não é necessária.")
elif (comodo == "Escritório"):
    dataFaxina = st.date_input("Data da última faxina completa do Escritório")
    hoje = datetime.date.today()
    quantidadeDias = abs((hoje - dataFaxina).days)
    if (quantidadeDias >= 7):
        st.text("Você já precisa faxinar essa parte.")
    else:
        st.text("Pode descansar. A faxina ainda não é necessária.")