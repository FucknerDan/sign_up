import streamlit as st
import pandas as pd
from util import *
import datetime
import numpy as np

side_menu: list = ['Startseite','Erstellen einer Anmeldung', 'Anmelden']

side_option = st.sidebar.radio('Übersicht',side_menu)

if side_option == side_menu[0]:
    st.write('Start')
    vid_file = open("streamlit-app-2020-02-08-15-02-86.webm", "rb")
    vid_bytes = vid_file.read()
    st.video(vid_bytes)
elif side_option == side_menu[1]:
    st.write('Hier können sie eine neue liste erstellen')

    date = st.date_input('Welchen Tag wollen sie machen?')
    time = st.time_input('Welche Uhrzeit')
    slots = st.number_input('Wie viele Slots wollen sie?' , 1)
    size = st.selectbox('Wie groß sollen die slots werden', ['5min','10min','15min' ,'20min' , '30min'])
    datum = datetime.datetime.combine(date,time)

    #st.write(datum)
    name_anf_placeholder = st.empty()
    df = create_table(datum, slots, size)

    st.write(df)
    name_anf = st.text_input('Geben sie ihrer anfragen noch einen namen')
    name_anf_placeholder.text(name_anf)
    check = st.button('Speichern sie ihre anfrage')
    st.write(check)
    if check:
        df.to_csv("tmp_data/" + name_anf + ".csv")
elif side_option == side_menu[2]:
    st.write('Hier können sie sich anmelden')


    data_dict = get_data_from_path("tmp_data/")
    if len(list(data_dict.keys())) > 1:
        anf = st.selectbox('wo wollen sie sich anmelden', list(data_dict.keys()))
    else:
        st.warning("alles ausgebucht")
    dir = "tmp_data/"
    df = pd.read_csv( dir + data_dict[anf], index_col=0)
    df.index.name = " Datum /Uhrzeit"
    df1 = df.replace(np.nan, '', regex=True)

    display_anf = st.empty()
    display_anf.dataframe(df1,height =500)
    time_options = [idx for idx in list(df1.index) if df1['Name'].loc[idx] == ""]
    if len(time_options) > 0:
        options = st.selectbox("möglich time slots verfügbar", time_options)
        input_name = st.text_input("Geben sie bitte ihren namen an")
        input_notiz = st.text_area("Optionale notiz")
        select_slot = st.button("Ihr slot wird reserviert")
        if select_slot and input_name != "":
            df1['Notiz'].loc[options] = input_notiz
            df1['Name'].loc[options] = input_name
            df1.to_csv("tmp_data/" + anf + ".csv")
            display_anf.dataframe(df1, height=500)
    else:
        st.warning("alles ausgebucht")


    #st.write(df1['Name'].loc[options])
