import streamlit as st
from model import model_predictions
import numpy as np

# Cabeçalho principal
st.title("🔋 Previsão do Consumo de Energia")
st.markdown(
    """
    Este projeto visa desenvolver um sistema de **previsão do consumo de energia** 
    com base em variáveis como modelo preditivo, horário, temperatura, e outros fatores.
    """
)

# Barra lateral
st.sidebar.title("⚙️ Configurações")
st.sidebar.info("Personalize os parâmetros para obter as previsões.")

# Seção do modelo
st.sidebar.subheader("Modelo de Previsão")
type_model = ["LinearRegression", "RandomForestRegressor"]
selected_model = st.sidebar.radio("Escolha o modelo:", type_model)

# Seção principal
st.markdown("---")  # Linha horizontal
st.header("📋 Insira os dados abaixo")

# Inputs organizados lado a lado
col1, col2 = st.columns(2)
with col1:
    month = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    selected_month = st.selectbox("🗓️ Selecione o mês:", month)

    hour = [f"{h:02d}:00" for h in range(24)]
    selected_hour = st.selectbox("⏰ Selecione a hora:", hour)

with col2:
    DayOfWeek = [
        "Domingo", "Segunda-feira", "Terça-feira",
        "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"
    ]
    selected_DayOfWeek = st.selectbox("📅 Dia da semana:", DayOfWeek)

    Holiday = ["Não", "Sim"]
    selected_Holiday = st.selectbox("🎉 É feriado?", Holiday)

# Inputs adicionais com placeholders
st.markdown("---")
st.subheader("🔢 Dados adicionais")
col3, col4 = st.columns(2)

with col3:
    temperature = st.text_input(
        '🌡️ Digite a temperatura em °C:',
        placeholder="Exemplo: 25.5"
    )

    Occupancy = st.text_input(
        '👥 Total de ocupantes no local:',
        placeholder="Exemplo: 10"
    )

with col4:
    LightingUsage = ["Não", "Sim"]
    selected_LightingUsage = st.selectbox("💡 Uso da iluminação:", LightingUsage)

# Botão de envio
st.markdown("---")
if st.button('📊 Enviar'):
    st.text('⚙️ Processando os dados...')
    
    # Converte as strings de input para valores numéricos
    month_num = month.index(selected_month) + 1
    hour_num = int(selected_hour[:2])
    dayOfWeek_num = DayOfWeek.index(selected_DayOfWeek) + 1
    holiday_num = 1 if selected_Holiday == "Sim" else 0
    temperature_num = float(temperature)
    occupancy_num = int(Occupancy)
    lightingUsage_num = 1 if selected_LightingUsage == "Sim" else 0
    
    # Cria um array com os dados de entrada
    inputs = np.array([month_num, hour_num, dayOfWeek_num, holiday_num, temperature_num, occupancy_num, lightingUsage_num]).reshape(1, -1)
    
    # Resultados
    results = model_predictions(type_model=selected_model, predictions=inputs)
    
    st.success("✅ Processamento concluído!")
    # Ajuste no tratamento do resultado para evitar erros de formatação
    st.subheader("📈 Resultado da previsão:")

    # Extrai o valor do array e formata como float
    predicted_value = float(results[0])  # Extrai o primeiro valor do array

    # Layout para mostrar os resultados
    st.markdown("#### 🔍 Detalhes da Previsão")
    st.write(f"**Modelo Selecionado:** {selected_model}")
    st.write(f"**Consumo Previsto:** {predicted_value:.2f} kWh")