import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    
    verificacao = ['instrutor', 'aprovado', 'nm_formacao', 'nm_unidade']
    
    if all(col in df.columns for col in verificacao):
        width, height = 700, 400

        aprovados_instrutor = df[df['aprovado'] == True].groupby('instrutor').size().reset_index(name='Quantidade')
        fig1 = px.bar(aprovados_instrutor, x='instrutor', y='Quantidade', title='', 
                      color='instrutor', width=width, height=height, color_discrete_sequence=px.colors.qualitative.Set2)

        reprovados_instrutor = df[df['aprovado'] == False].groupby('instrutor').size().reset_index(name='Quantidade')
        fig2 = px.bar(reprovados_instrutor, x='instrutor', y='Quantidade', title='', 
                      color='instrutor', width=width, height=height, color_discrete_sequence=px.colors.qualitative.Set2)

        aprovados_formacao = df[df['aprovado'] == True].groupby('nm_formacao').size().reset_index(name='Quantidade')
        fig3 = px.bar(aprovados_formacao, x='nm_formacao', y='Quantidade', title='', 
                      color='nm_formacao', width=width, height=height, color_discrete_sequence=px.colors.qualitative.Set2)

        aprovados_unidade = df[df['aprovado'] == True].groupby('nm_unidade').size().reset_index(name='Quantidade')
        fig4 = px.bar(aprovados_unidade, x='nm_unidade', y='Quantidade', title='', 
                      color='nm_unidade', width=width, height=height, color_discrete_sequence=px.colors.qualitative.Set2)

        aprovados_top10_unidade = aprovados_unidade.sort_values(by='Quantidade', ascending=False).head(10)
        fig5 = px.bar(aprovados_top10_unidade, x='nm_unidade', y='Quantidade', title='', 
                      color='nm_unidade', width=width, height=height, color_discrete_sequence=px.colors.qualitative.Set2)

        aprovados_bottom10_unidade = aprovados_unidade.sort_values(by='Quantidade', ascending=False).tail(10)
        fig6 = px.bar(aprovados_bottom10_unidade, x='nm_unidade', y='Quantidade', title='', 
                      color='nm_unidade', width=width, height=height, color_discrete_sequence=px.colors.qualitative.Set2)

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        col5, col6 = st.columns(2)

        with col1:
            st.header('Aprovados por Instrutor')
            st.plotly_chart(fig1)

        with col2:
            st.header('Reprovados por Instrutor')
            st.plotly_chart(fig2)

        with col3:
            st.header('Aprovados por Formação')
            st.plotly_chart(fig3)

        with col4:
            st.header('Aprovados por Unidade (Todos)')
            st.plotly_chart(fig4)

        with col5:
            st.header('10 Unidades com mais Aprovados')
            st.plotly_chart(fig5)

        with col6:
            st.header('10 Unidades com menos Aprovados')
            st.plotly_chart(fig6)
            
    else:
        st.error(f"Colunas faltando. O arquivo deve conter as colunas: {verificacao}")
else:
    st.info("Carregue um arquivo Excel.")