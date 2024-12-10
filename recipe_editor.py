import streamlit as st

def calculate_recipe(fermentables, hops):
    # Simplified calculations
    total_sugar = sum([f["amount"] * f["yield"] for f in fermentables])  # in points
    abv = total_sugar * 0.131  # Approximation for alcohol by volume
    ibu = sum([h["alpha"] * h["amount"] / (1 + h["time"]) for h in hops])  # Simplistic IBU calc
    return {"abv": abv, "ibu": ibu}

def show_recipe_editor():
    st.title("Éditeur de recette")
    
    # Fermentescibles
    st.subheader("Fermentescibles")
    fermentables = st.data_editor(
        [{"name": "Pale Malt", "amount": 5, "yield": 0.75}, {"name": "Caramel Malt", "amount": 1, "yield": 0.7}],
        key="fermentables",
    )

    # Houblons
    st.subheader("Houblons")
    hops = st.data_editor(
        [{"name": "Cascade", "amount": 10, "alpha": 0.05, "time": 60}, {"name": "Saaz", "amount": 5, "alpha": 0.03, "time": 15}],
        key="hops",
    )

    # Divers
    st.subheader("Divers")
    st.text_area("Ajoutez des détails sur les ingrédients spéciaux", "")

    # Levure
    st.subheader("Levure")
    yeast = st.text_input("Sélectionnez une levure (exemple : US-05)", "US-05")

    # Calcul dynamique
    st.subheader("Résultats")
    recipe_stats = calculate_recipe(fermentables, hops)
    st.write(f"**ABV (Alcool par volume)** : {recipe_stats['abv']:.2f}%")
    st.write(f"**IBU (Amertume)** : {recipe_stats['ibu']:.2f}")

    # Sauvegarde
    if st.button("Enregistrer la recette"):
        st.success("Recette enregistrée avec succès !")
