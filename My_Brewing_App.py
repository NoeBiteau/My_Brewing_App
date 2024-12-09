import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio(
    "Choisissez une section",
    ["Recettes", "Brassins", "Inventaire", "Bibliothèque", "Profil", "Compte"]
)

# Add a logo at the top of the sidebar
st.sidebar.image("Logo_KORAI.png", use_column_width=True, caption="KORAI Brewing")

# Page Content
if selected_tab == "Recettes":
    st.title("Recettes")
    st.markdown("---")
    st.markdown("### Barre de recherche")
    search_term = st.text_input("Recherchez une recette :", placeholder="Tapez ici...")
    st.markdown("---")
    st.markdown("### Liste des recettes disponibles")
    
    # Example of recipes display
    recipes = [
        {
            "name": "IPA Tropicale",
            "author": "John Doe",
            "style": "IPA",
            "method": "All-Grain",
            "abv": "6.5%",
            "di": "1.060",
            "df": "1.010",
            "ibu": 55,
        },
        {
            "name": "Stout Chocolat",
            "author": "Jane Smith",
            "style": "Stout",
            "method": "Extract",
            "abv": "5.2%",
            "di": "1.055",
            "df": "1.012",
            "ibu": 40,
        },
    ]
    
    for recipe in recipes:
        st.markdown(f"**{recipe['name']}** — Auteur : {recipe['author']}")
        st.markdown(f"Style : {recipe['style']} | Méthode : {recipe['method']}")
        st.markdown(f"ABV : {recipe['abv']} | DI : {recipe['di']} | DF : {recipe['df']} | IBU : {recipe['ibu']}")
        st.markdown("---")

elif selected_tab == "Brassins":
    st.title("Brassins")
    st.markdown("Suivi des brassins lancés")

elif selected_tab == "Inventaire":
    st.title("Inventaire")
    st.markdown("Suivi de l'inventaire des brassages")

elif selected_tab == "Bibliothèque":
    st.title("Bibliothèque")
    st.markdown("Consultation de nombreuses recettes disponibles en ligne")

elif selected_tab == "Profil":
    st.title("Profil")
    st.markdown("Configuration de votre équipement, empâtage, fermentation, eau, et styles personnalisés.")

elif selected_tab == "Compte":
    st.title("Compte")
    st.markdown("Gestion du compte utilisateur")
