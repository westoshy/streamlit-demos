_="""

pip install streamlit-authenticator
https://qiita.com/guunonemodemai/items/1b9ffd8702d4e01075dd
"""

import streamlit as st
import streamlit_authenticator as stauth
import yaml

#
# ページのセッティング
#
st.set_page_config(
    page_title="Streamlit Examples",
    page_icon="🧊",
    layout="centered", # or "wide"
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

def sidebar():
    pass

def mainview():
    st.markdown("# authenticator demo")
    st.markdown("""
    [Streamlit-Authenticator](https://github.com/mkhorasani/Streamlit-Authenticator)を用いると簡単な
    ログイン認証付きのWebアプリケーションを作成することができます．Streamlit-Authenticatorを使うには
    次のコマンドでパッケージをインストールする必要があります．
    ```
    pip install streamlit-authenticator
    ```
    このページでは，Streamlit-Authenticatorのドキュメントに記載されている例が動作することを確認します．
    """)
    #
    # 1. hashing passwords
    #
    st.markdown("## パスワードのハッシュ化")
    with st.echo():
        hashed_passwords = stauth.Hasher(['test_user']).generate() 
        st.write(hashed_passwords)

    #
    # 2. creating a login widgets
    #
    st.markdown("## ログイン画面の作成と認証")
    with st.echo():
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

    #
    # 3. Authenticating users
    #
    with st.echo():
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

    # 4. Creating a passowrd reset widget
    with st.echo():
        if authentication_status:
            try:
                if authenticator.reset_password(username, 'Reset password'):
                    st.success('Password modified successfully')
            except Exception as e:
                st.error(e)  

    # 5. Creating a new user registration widget
    with st.echo():
        try:
            if authenticator.register_user('Register user', preauthorization=False):
                st.success('User registered successfully')
        except Exception as e:
            st.error(e)

    # 6. Creating a forgot passowrd widget
    with st.echo():
        try:
            username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
            if username_forgot_pw:
                st.success('New password sent securely')
                # Random password to be transferred to user securely
            elif username_forgot_pw == False:
                st.error('Username not found')
        except Exception as e:
            st.error(e)

    # 7.Creating a forgot username widget
    with st.echo():
        try:
            username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
            if username_forgot_username:
                st.success('Username sent securely')
                # Username to be transferred to user securely
            elif username_forgot_username == False:
                st.error('Email not found')
        except Exception as e:
            st.error(e)   
    
    # 8. Creating an update user details widget
    with st.echo():
        if authentication_status:
            try:
                if authenticator.update_user_details(username, 'Update user details'):
                    st.success('Entries updated successfully')
            except Exception as e:
                st.error(e)    
    
    # 9. Updating the configuration file
    with st.echo():
        with open("data/config.yaml", "w") as file:
            yaml.dump(config, file, default_flow_style=False) 

if __name__ == "__main__":
    sidebar()
    mainview()