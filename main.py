import streamlit as st
import pandas as pd
import re

def clean_addresses(dataframe, column_name):
    # Rimuove le righe dove la colonna specificata non contiene numeri
    return dataframe[dataframe[column_name].str.contains(r'\d', na=False)]

def main():
    st.title('Pulizia degli Indirizzi')
    st.write("Carica un file CSV e verranno rimossi gli indirizzi senza numeri.")

    uploaded_file = st.file_uploader("Scegli un file CSV", type='csv')
    if uploaded_file is not None:
        # Leggere il file CSV
        df = pd.read_csv(uploaded_file)

        # Controllare se la colonna 'Indirizzo' esiste
        if 'Indirizzo' in df.columns:
            # Pulizia degli indirizzi
            clean_df = clean_addresses(df, 'Indirizzo')
            
            # Mostrare il dataframe pulito
            st.write("Anteprima dei dati puliti:")
            st.dataframe(clean_df)
            
            # Permettere all'utente di scaricare il dataframe pulito
            csv = clean_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Scarica i dati puliti come CSV",
                data=csv,
                file_name='indirizzi_puliti.csv',
                mime='text/csv',
            )
        else:
            st.error("Il file CSV deve contenere una colonna 'Indirizzo'.")

if __name__ == '__main__':
    main()
