from idna import check_label
import streamlit as st

#
# ページのセッティング
#
st.set_page_config(
    page_title="Streamlit Examples",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

def mainview():
    #
    # st.stop()
    # https://docs.streamlit.io/library/api-reference/control-flow/st.stop
    #
    st.markdown("# control demo")
    st.markdown("## st.stop")
    st.markdown("""
    streamlitでは`st.stop()`以降のステートメントは実行されません．ユーザ入力の状態をもとに
    スクリプトを停止して，所定の入力が得られたら次のステップに進むようなアプリケーションを
    書くことができます．アプリケーション上ではなぜ停止しているのかは分からないので適切な
    メッセージを表示することが望ましいです．
    """)
    with st.echo():
        name = st.text_input("Name")
        if not name:
            st.warning("Please input a name")
            st.stop()
        st.success("Thank you for inputting a name")

    #
    # st.form()
    # https://docs.streamlit.io/library/api-reference/control-flow/st.form
    #
    st.markdown("## st.form")
    st.markdown("""
    `st.form()`を用いることで複数のウィジェットを束ねることができます．
    """)
    with st.echo():
        form = st.form("my_form")
        slider_value = form.slider("inside the form")
        checkbox_val = form.checkbox("inside check box")
        submitted = form.form_submit_button("submit")
        if submitted:
            st.write("slider", slider_value, "checkbox", checkbox_val)

if __name__ == "__main__":
    mainview()