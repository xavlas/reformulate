import streamlit as st
import streamlit_authenticator as stauth
import logging

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
authenticator = stauth.Authenticate(
    auth_config['credentials'],
    auth_config['cookie']['name'],
    auth_config['cookie']['key'],
    auth_config['cookie']['expiry_days']
)

# Login et extraction des résultats (version compatible avec v0.1 et v0.2+)
login_result = authenticator.login("main")
st.write("Résultat authenticator.login:", login_result)
if isinstance(login_result, tuple) and len(login_result) == 3:
    name, auth_status, username = login_result
    logging.info("login 3")
elif isinstance(login_result, tuple) and len(login_result) == 2:
    name, auth_status = login_result
    logging.info("login 2")
    username = None
else:
    logging.info("login 0")
    name = auth_status = username = None

st.write(f"name: {name}, auth_status: {auth_status}, username: {username}")

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
