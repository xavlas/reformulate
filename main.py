

import streamlit as st
import streamlit_authenticator as stauth

# Lecture des secrets
auth_config = {
    'credentials': {
        'usernames': {
            'xavier': {
                'name': st.secrets.users.name,
                'email': st.secrets.users.email,
                'password': st.secrets.users.password,
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



login_info = authenticator.login("main")
st.write(login_info)

if auth_status:
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
