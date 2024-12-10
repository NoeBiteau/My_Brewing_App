import streamlit as st

# Main app
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio(
    "Choisissez une section",
    ["Recettes", "Brassins", "Inventaire", "Bibliothèque", "Profil", "Compte"]
)

# Get the current query parameters
query_params = st.get_query_params()

if selected_tab == "Recettes":
    st.title("Recettes")
    st.markdown("---")

    if st.button("Créer une recette"):
        # Set query parameter to open the editor page
        st.set_query_params(page="editor")

    if query_params.get("page") == ["editor"]:
        # Call the recipe editor
        from recipe_editor import show_recipe_editor
        show_recipe_editor()

    else:
        st.markdown("### Liste des recettes")
        # Simulated recipe list
        recipes = [{"name": "IPA Tropicale", "author": "John Doe"}, {"name": "Stout Chocolat", "author": "Jane Smith"}]
        for recipe in recipes:
            st.markdown(f"**{recipe['name']}** par {recipe['author']}")

elif selected_tab in ["Brassins", "Inventaire", "Bibliothèque", "Profil", "Compte"]:
    st.title(selected_tab)
    st.markdown("Page en cours de construction.")
