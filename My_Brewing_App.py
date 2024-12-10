import streamlit as st

# Main app
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio(
    "Choisissez une section",
    ["Recettes", "Brassins", "Inventaire", "Bibliothèque", "Profil", "Compte"]
)

if selected_tab == "Recettes":
    st.title("Recettes")
    st.markdown("---")

    if st.button("Créer une recette"):
        st.session_state.show_recipe_editor = True

    if st.session_state.get("show_recipe_editor", False):
        st.experimental_set_query_params(page="editor")  # Open editor page

    st.markdown("### Liste des recettes")
    # Simulated recipe list
    recipes = [{"name": "IPA Tropicale", "author": "John Doe"}, {"name": "Stout Chocolat", "author": "Jane Smith"}]
    for recipe in recipes:
        st.markdown(f"**{recipe['name']}** par {recipe['author']}")

elif st.query_params().get("page") == ["editor"]:
    # Call the recipe editor
    from recipe_editor import show_recipe_editor
    show_recipe_editor()

else:
    st.title(selected_tab)
    st.markdown("Page en cours de construction.")
