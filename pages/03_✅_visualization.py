import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
import graphviz as graphviz

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
    st.markdown("# visualization demo")

    #
    # st.chart
    #
    st.markdown("## st.chart")

    with st.echo():
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])
        st.line_chart(chart_data)

    #
    # st.area_chart
    #
    st.markdown("## st.area_chart")
    with st.echo():
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])
        st.area_chart(chart_data)       

    #
    # st.bar_chart
    #
    st.markdown("## st.bar_chart")
    with st.echo():
        chart_data = pd.DataFrame(
            np.random.randn(50, 3),
            columns=["a", "b", "c"])
        st.bar_chart(chart_data)

    #
    # st.pyplot
    #
    st.markdown("## st.pyplot")
    with st.echo():
        arr = np.random.normal(1, 1, size=100)
        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)

        st.pyplot(fig)

    #
    # st.altair_chart
    #
    st.markdown("## st.altair_chart")
    with st.echo():
        df = pd.DataFrame(
            np.random.randn(200, 3),
            columns=['a', 'b', 'c'])

        c = alt.Chart(df).mark_circle().encode(
            x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

        st.altair_chart(c, use_container_width=True)    
    
    #
    # st.plotly
    #
    st.markdown("## st.plotly")
    with st.echo():
        # Add histogram data
        x1 = np.random.randn(200) - 2
        x2 = np.random.randn(200)
        x3 = np.random.randn(200) + 2

        # Group data together
        hist_data = [x1, x2, x3]

        group_labels = ['Group 1', 'Group 2', 'Group 3']

        # Create distplot with custom bin_size
        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])

        # Plot!
        st.plotly_chart(fig, use_container_width=True)

    #
    #
    #
    st.markdown("## st.map")
    with st.echo():
        df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

        st.map(df)

    #
    # st.graphviz_chart
    #
    st.markdown("## st.graphviz_chart")
    st.markdown("""
    ```
    pip install graphviz
    ```
    graphvizは表示されない場合はレジストリを変更する必要があるかも（未解決）
    """)
    st.image("data/graphviz_registory.png")
    with st.echo():
        # Create a graphlib graph object
        graph = graphviz.Digraph()
        graph.edge('run', 'intr')
        graph.edge('intr', 'runbl')
        graph.edge('runbl', 'run')
        graph.edge('run', 'kernel')
        graph.edge('kernel', 'zombie')
        graph.edge('kernel', 'sleep')
        graph.edge('kernel', 'runmem')
        graph.edge('sleep', 'swap')
        graph.edge('swap', 'runswap')
        graph.edge('runswap', 'new')
        graph.edge('runswap', 'runmem')
        graph.edge('new', 'runmem')
        graph.edge('sleep', 'runmem')

        st.graphviz_chart(graph)

    st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
    ''')    

if __name__ == "__main__":
    sidebar()
    mainview()