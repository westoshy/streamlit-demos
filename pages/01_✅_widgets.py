import streamlit as st
import time
import datetime

def mainview():
    st.markdown("# widgets demo")


    # -------------------------------------------------------
    # buttonの表示
    # -------------------------------------------------------
    st.markdown("## push buttonの表示")
    st.markdown("""
    `st.button()`でプッシュボタンを設置してボタンを押下したかどうかで条件分岐することができます．
    ボタンを押下した後に別のUI部品を操作するとボタンの状態はFalseに戻ります．
    """)

    with st.echo():
        answer = st.button("Press Button")
        if answer is True:
            st.markdown("Button is Pressed.")
        else:
            st.markdown("Button is not Pressed.")

    # -------------------------------------------------------
    # check buttonの表示
    # -------------------------------------------------------
    st.markdown("## check buttonの表示")
    st.markdown("""
    `st.checkbox()`でチェックボタンを設置することができます．チェック状態に応じて条件分岐を作る
    ことができます．

    """)

    with st.echo():
        checked = st.checkbox("checked")
        if checked is True:
            st.markdown("checked.")
        else:
            st.markdown("not checked.")

    # -------------------------------------------------------
    # radio buttonの表示
    # -------------------------------------------------------
    st.markdown("## radio buttonの表示")
    st.markdown("""
    `st.radio()`でラジオボタンを設置することができます．ラジオボタンの返却値は設定した項目の文字列
    になっています．
    """)

    with st.echo():
        answer = st.radio(
            "choose radio button", ("first", "second", "third")
        )
        if answer == "first":
            st.write("first is selected")
        else:
            st.write("you didn't select first")

    # -------------------------------------------------------
    # dropdown listの表示(selectbox/multiselect)
    # -------------------------------------------------------
    st.markdown("## dropdown listの表示")
    st.markdown("### selectbox")
    st.markdown("""
    `st.selectbox()`を用いると1つだけ選択可能なドロップダウンリストを表示することができます．
    dropdown listで選択した項目の文字列が返却されます．
    ```python
    option = st.selectbox(
        "select answer", ("first", "second", "third")
    )
    st.markdown("your selection: " + option)
    ```
    """)
    option = st.selectbox(
        "select answer", ("first", "second", "third")
    )
    st.markdown("your selection: " + option)

    st.markdown("### multiselect")
    st.markdown("""
    `st.multiselect()`を用いると複数選択可能なドロップダウンリストを表示することができます．
    選択された項目の文字列をもつリストが返却されます．またデフォルトの項目も設定することができます．
    ```python
    options = st.multiselect(
        "select multipule answers", ["first", "second", "third"], ["second"]
    )
    st.table(options)
    ```
    """)
    options = st.multiselect(
        "select multipule answers", ["first", "second", "third"], ["second"]
    )
    st.table(options)

    # -------------------------------------------------------
    # slider
    # -------------------------------------------------------
    st.markdown("## Sliderの表示")
    st.markdown("### 1つの値の設定")
    st.markdown("""
    `st.slider()`を用いてスライダーを設置することができます．最小値と最大値，間隔，初期値を
    設定することが可能です．
    ```python
    value =st.slider("adjust value", min_value=0, max_value=100, step=10, value=50)
    st.markdown("value: " + str(value))
    ```
    """)

    value =st.slider("adjust value", min_value=0, max_value=100, step=10, value=50)
    st.write(value)

    st.markdown("### 2つの値の設定")
    st.markdown("""
    2つの値を選んで範囲を設定することもできます．
    ```python
    ```
    """)

    values = st.slider("select range", 0.0, 100.0, (25.0, 75.0))
    st.write(values)

    st.markdown("## select slider")
    st.markdown("""
    `st.select_slider()`を用いてカテゴリ値をスライダーにセットすることができます．
    ```python
    color = st.select_slider(
        'Select a color of the rainbow',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    st.write('My favorite color is', color)
    start_color, end_color = st.select_slider(
        'Select a range of color wavelength',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
        value=('red', 'blue'))
    st.write('You selected wavelengths between', start_color, 'and', end_color)
    ```
    """)
    color = st.select_slider(
        'Select a color of the rainbow',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    st.write('My favorite color is', color)
    start_color, end_color = st.select_slider(
        'Select a range of color wavelength',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
        value=('red', 'blue'))
    st.write('You selected wavelengths between', start_color, 'and', end_color)

    # -------------------------------------------------------
    # Progress bar
    # ------------------------------------------------------- 
    st.markdown("## Progress Barの表示")
    st.markdown("""
    `st.progress()`でプログレスバーを表示することができます．時間を要する処理において実行中である
    ことが分かるようにリアルタイムにステータスを確認することができます．
    ```python
    latest_iteration = st.empty()
    answer = st.button("iteration start")
    bar = st.progress(0)
    if answer is True:
        for i in range(10):
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i*10)
            time.sleep(0.1)    
    ```
    """)
    latest_iteration = st.empty()

    answer = st.button("iteration start")
    bar = st.progress(0)
    if answer is True:
        for i in range(10):
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i*10)
            time.sleep(0.1)  

    # -------------------------------------------------------
    # Spinner
    # -------------------------------------------------------
    st.markdown("## Spinnerの表示") 
    st.markdown("""
    `st.spinner()`で実行中であることを表すspinnerを表示することができます．
    """)
    answer = st.button("iteration start1")
    if answer is True:
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success('Done!')

    # -------------------------------------------------------
    # Text box
    # -------------------------------------------------------
    st.markdown("## テキスト入力")
    st.markdown("""
    `st.text_input()`でテキストボックスを表示できます．
    """)
    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)

    #
    # Date input
    #
    st.markdown("## 日付入力")
    d = st.date_input(
        "When's your birthday",
        datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)

    # -------------------------------------------------------
    # color picker
    # https://docs.streamlit.io/library/api-reference/widgets/st.color_picker
    # -------------------------------------------------------
    st.markdown("## color pickerの設置")
    st.markdown("""
    `st.color_picker()`でカラーピッカーを設置できます．
    """)
    with st.echo():
        color = st.color_picker('Pick A Color', '#00f900')
        st.write('The current color is', color)

if __name__ == "__main__":
    mainview()