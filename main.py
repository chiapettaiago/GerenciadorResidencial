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
st.sidebar.selectbox("Cômodo ou setor a ser gerenciado", ["Sala", "Quarto", "Cozinha", "Banheiro", "Escritório"])

dataFaxina = st.date_input("Data da última faxina completa")
hoje = datetime.date.today()
quantidadeDias = abs((hoje - dataFaxina).days)
if (quantidadeDias >= 3):
    st.text("Você já precisa faxinar essa parte.")
else:
    st.text("Pode descansar. A faxina ainda não é necessária.")