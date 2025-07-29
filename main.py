import streamlit as st
import streamlit_authenticator as stauth
import logging

import yaml
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

logging.basicConfig(level=logging.INFO)

# Lecture des secrets
auth_config = {
    'credentials': {
        'usernames': {
            'xavier': {
                'name': st.secrets["users"]["name"],
                'email': st.secrets["users"]["email"],
                'password': st.secrets["users"]["password"],
            }
        }
    },
    'cookie': {
        'name': st.secrets["auth"]["cookie_name"],
        'key': st.secrets["auth"]["cookie_key"],
        'expiry_days': st.secrets["auth"]["cookie_expiry_days"]
    }
}

# Authentification
authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
st.write(f"name: {name}, auth_status: {auth_status}, username: {username}")

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

if auth_status is True:
    authenticator.logout("Se déconnecter", "sidebar")
    st.sidebar.success(f"Connecté en tant que {name}")

    # Application principale
    def generate_message(text, tone):
        if tone == "Professionnel":
            return f"Bonjour,\n\n{ text.strip().capitalize() }.\n\nCordialement,"
        else:
            return f"Hey !\n\n{ text.strip().capitalize() } 😄"

    st.title("Générateur de message")

    user_input = st.text_area("Écris ton message ici :", height=150)
    tone = st.radio("Choisis le ton du message :", ("Professionnel", "Casual"))

    if st.button("Générer le message"):
        if user_input.strip() == "":
            st.warning("Merci d'écrire un message avant de générer.")
        else:
            result = generate_message(user_input, tone)
            st.subheader("Message généré :")
            st.code(result, language="markdown")
elif auth_status is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect.")
elif auth_status is None:
    st.warning("Veuillez entrer vos identifiants.")
