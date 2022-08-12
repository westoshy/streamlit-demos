import streamlit as st
import pandas as pd

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


def sidebar():
    pass

def mainview():
    st.markdown("# data display")

    #
    # json
    # https://docs.streamlit.io/library/api-reference/data/st.json
    #
    st.json({
        'foo': 'bar',
        'baz': 'boz',
        'stuff': [
            'stuff 1',
            'stuff 2',
            'stuff 3',
            'stuff 5',
        ],
    })

    #
    # dataframe
    # https://docs.streamlit.io/library/api-reference/data/st.dataframe
    #
    dataframe = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
    })
    st.experimental_show(dataframe)

    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

if __name__ == "__main__":
    mainview()