import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import warnings

warnings.filterwarnings('ignore')

# функция для работы с sqlite3 базой retail
connection = sqlite3.connect(r'app/detentions')
def select(sql: str) -> pd.DataFrame:
    return pd.read_sql(sql, connection)


st.set_page_config(page_title='Задержания на публичных акциях', page_icon=':no_pedestrians:', layout='wide')
st.title(':mega: Задержания на публичных акциях, 2012–2024 годы')
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

#col1, col2 = st.columns((2))

st.sidebar.header("Настройте фильтры: ")

# get list of all regions
sql = """
SELECT region, strftime('%Y', date) AS year, subject_type, subject_topic FROM detentions
"""
df = select(sql)


# Create for Region
region = st.sidebar.multiselect("Выбор региона", df['region'].unique(), placeholder="Регионы", default=['Москва', 'Санкт-Петербург'])
if not region:
    df2 = df.copy()
else:
    df2 = df[df["region"].isin(region)]
year = st.sidebar.multiselect("Выбор года", df2['year'].unique(), placeholder="Годы", default=[])
if not year:
    df3 = df2.copy()
else:
    df3 = df2[df2["year"].isin(year)]

subject_type = st.sidebar.multiselect("Тип протеста", df3['subject_type'].unique(), placeholder="Тип", default=[])
if not subject_type:
    df4 = df3.copy()
else:
    df4 = df3[df["subject_type"].isin(subject_type)]

subject_topic = st.sidebar.multiselect("Тематика протеста", df4['subject_topic'].unique(), placeholder="Тематика", default=[])
if not subject_topic:
    df5 = df4.copy()
else:
    df5 = df4[df["subject_topic"].isin(subject_topic)]

st.table(df5)