import streamlit as st
import streamlit_authenticator as stauth
import yaml


def authentication():
    # config.yaml has 
    #   username: test_user
    #   password: test_user
    with open('data/config.yaml') as file:
        config = yaml.load(file, Loader=stauth.SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        st.title('Some content')
    elif authentication_status == False:
        st.error('Username/password is incorrect')
        st.stop()
    elif authentication_status == None:
        st.warning('Please enter your username and password')    
        st.stop()