import streamlit as st

if "login" not in st.session_state:
    st.session_state.login = False

st.title("Chat Assistant LogIn")

if st.session_state["login"]:
    st.success("LogIn Successfull")
    st.switch_page("chatbot.py")  # <-- Redirection ici (à ajuster selon le chemin de ta page)
else:
    password = st.text_input("Please enter the password", disabled=st.session_state.login, type="password")
    if st.button("LogIn"):
        if not password:
            st.error("Please Type the Password", icon = "🚨")
        else:
            if password == st.secrets["PASSWORD"]:
                st.session_state.login = True
                st.toast("Login Successful 🤩")
                st.success("LogIn Successfull")
                st.switch_page("chatbot.py")  # <-- Redirection ici aussi après login
            else:
                st.toast("Incorrect Password 😶")
                st.error('Incorrect Password', icon = "🚨")
