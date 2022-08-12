#
# このファイルはページ追加のテンプレートです．
# 新しいページを追加したい場合はpagesディレクトリに追加してください．
#

import streamlit as st
from authentication import authentication

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
    pass

if __name__ == "__main__":
    #authentication()
    sidebar()
    mainview()