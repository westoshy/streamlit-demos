import streamlit as st
import numpy as np
import time

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


def mainview():
    st.markdown("# layouts and containers demo")
    #
    # sidebar
    #
    st.markdown("## st.sidebar")
    st.markdown("""
    `st.sidebar.<widget name>`あるいは`with st.sidebar`を用いてサイドバーを設置することができます．
    `with`を使う場合には次のように記述します．`<widget name>`にはbuttonやcheckboxなどが入ります．
    ```python
    with st.sidebar:
        st.<widget name>
    ```
    ```python
    st.sidebar.<widget name>
    ```
    例えば，サイドバーにチェックボタンを設置する場合は次のように記述します．
    """)

    with st.echo():
        answer = st.sidebar.checkbox("checkbox in sidebar")
        if answer is True:
            st.write("checked", answer)
        else:
            st.write("not checked", answer)

    #
    # st.column
    #
    st.markdown("## st.column")
    st.markdown("""
    `st.column`を用いて複数列に分割したコンテナを設置ことが可能です．分割したコンテナ内は
    `with`を使って記述します．
    """)

    with st.echo():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.markdown("### A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.markdown("### An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg")   

    #
    # st.tab
    #  
    st.markdown("## st.tab")
    st.markdown("""
    `st.tab`を用いてタブを設定することができます．
    """)

    with st.echo():
        tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
        with tab1:
            st.markdown("### A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

        with tab2:
            st.markdown("### A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

        with tab3:
            st.markdown("### An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    #
    # st.expandar
    #
    st.markdown("## st.expander")

    with st.echo():
        with st.expander("See explanation"):
            st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
            st.image("https://static.streamlit.io/examples/dice.jpg")

    #
    # st.container
    #
    st.markdown("## st.container")
    with st.echo():
        with st.container():
            st.write("This is inside the container")

            # You can call any Streamlit command, including custom components:
            st.bar_chart(np.random.randn(50, 3))

    #
    # st.empty
    #
    st.markdown("## st.empty")
    with st.echo():
        with st.empty():
            for seconds in range(5):
                st.write(f"⏳ {seconds} seconds have passed")
                time.sleep(1)
            st.write("✔️5 sec over!")

if __name__ == "__main__":
    mainview()