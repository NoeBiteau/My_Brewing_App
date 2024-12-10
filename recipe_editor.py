import streamlit as st
from ingredient_manager import get_fermentables, get_hops

def calculate_recipe(fermentables, hops):
    # Calcul simplifié pour ABV et IBU
    total_sugar = sum([f["amount"] * f["yield"] for f in fermentables])  # en points
    abv = total_sugar * 0.131  # Approximation pour l'alcool
    ibu = sum([h["alpha"] * h["amount"] / (1 + h["time"]) for h in hops])  # Calcul simplifié pour IBU
    return {"abv": abv, "ibu": ibu}

def show_recipe_editor():
    st.title("Éditeur de recette")
    
    # Récupérer les fermentescibles depuis la base de données
    fermentables_data = get_fermentables()
    fermentables = st.data_editor(
        [{"name": f[1], "amount": 5, "yield": f[2]} for f in fermentables_data],
        key="fermentables",
    )

    # Récupérer les houblons depuis la base de données
    hops_data = get_hops()
    hops = st.data_editor(
        [{"name": h[1], "amount": 10, "alpha": h[2], "time": 60} for h in hops_data],
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
        # Enregistrer la recette dans la base de données (par exemple)
        st.success("Recette enregistrée avec succès !")
