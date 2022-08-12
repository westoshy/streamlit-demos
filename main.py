import streamlit as st
import pandas as pd
import time
import plotly.graph_objs as go

#
# ページのセッティング
#
st.set_page_config(
    page_title="Streamlit Examples",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


def mainview():
    st.markdown("# Streamlit Examples Demo")

    # -------------------------------------------------------
    # タイトルとテキストの表示
    # -------------------------------------------------------
    st.markdown("## 文字表示")
    st.markdown("""
    markdownでテキストやヘッダを記述することができます．markdown以外にもタイトルの表示には
    `st.title()`，テキストの表示には`st.write()`を使うことができます．
    `st.write()`はテキスト以外にもデータフレームや数値など様々な形式を汎用的に扱えます．

    markdownでのコードブロックの表示や数式の表示にも対応しています．
    ```python
    print("Hello World")
    ```
    $$
    e^{i \pi} + 1 = 0
    $$
    
    コードは`st.code()`，数式は`st.latex()`でも表示可能です．また，`st.echo()`を用いると
    コードを実行しつつ表示することが可能です．
    """)
    
    st.markdown("## メッセージの装飾")
    st.info('This is a purely informational message')
    st.warning('This is a warning')
    st.error('This is an error')
    st.success('This is a success message!')
    e = RuntimeError('This is an exception of type RuntimeError')
    st.exception(e)   

    #
    # multipage
    #
    st.markdown("## multipage")

if __name__ == "__main__":
    mainview()