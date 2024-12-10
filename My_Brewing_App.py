import streamlit as st

# Main app
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio(
    "Choisissez une section",
    ["Recettes", "Brassins", "Inventaire", "Bibliothèque", "Profil", "Compte"]
)

# Access the current query parameters
st.query_params.page = ""
query_params = st.query_params

# Check if 'page' query parameter is set to "editor"
if selected_tab == "Recettes":
    st.title("Recettes")
    st.markdown("---")
    st.query_params.page = ""

    if st.button("Créer une recette"):
        # Set the query parameter 'page' to 'editor'
        st.query_params.page = "editor"  # This updates the URL to reflect the editor page

    # If the 'page' parameter is 'editor', show the recipe editor
    if query_params.get("page") == "editor":
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
