
import streamlit as st

def generate_message(text, tone):
    if tone == "Professionnel":
        return f"Bonjour,\n\n{ text.strip().capitalize() }.\n\nCordialement,"
    else:
        return f"Hey !\n\n{ text.strip().capitalize() } 😄"

# Titre de l'application
st.title("Générateur de message")

# Zone de texte
user_input = st.text_area("Écris ton message ici :", height=150)

# Choix du ton
tone = st.radio("Choisis le ton du message :", ("Professionnel", "Casual"))

# Bouton pour générer le message
if st.button("Générer le message"):
    if user_input.strip() == "":
        st.warning("Merci d'écrire un message avant de générer.")
    else:
        result = generate_message(user_input, tone)
        st.subheader("Message généré :")
        st.code(result, language="markdown")
