import streamlit as st
from api import fetch_data

def main():
    st.title("Pokemon Information Viewer")
    
    # Sidebar für zusätzliche Optionen
    st.sidebar.title("Optionen")
    display_image = st.sidebar.checkbox("Bild anzeigen", value=True)
    
    # Input des Users
    name = st.text_input("Name des Pokemons von Interesse?")
    
    if name:
        # Daten von der API abfragen
        data = fetch_data(name)
        if data:
            # Daten visualisieren
            st.header("Informationen")
            st.subheader("Name")
            st.write(data['name'])
            st.subheader("Gewicht")
            st.write(data['weight'])
            st.subheader("Größe")
            st.write(data['height'])
            st.subheader("Fähigkeiten")
            for ability in data['abilities']:
                st.write(ability['ability']['name'])
            
            # Optionales Anzeigen des Pokemon-Bildes
            if display_image:
                if 'sprites' in data:
                    sprite_url = data['sprites']['front_default']
                    st.image(sprite_url, caption="Bild des Pokemons", use_column_width=True)
                else:
                    st.warning("Bild nicht verfügbar")
        else:
            st.error("Pokemon nicht gefunden. Bitte überprüfen Sie den Namen.")

if __name__ == "__main__":
    main()
