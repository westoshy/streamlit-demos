import streamlit as st
from PIL import Image

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

    st.markdown("# media demo")

    #
    # st.audio
    # https://docs.streamlit.io/library/api-reference/media/st.audio
    #
    st.markdown("## audio")
    st.markdown("""
    `st.audio()`でオーディオファイルを読み込み，プレイヤーを表示することができます．
    """)
    with st.echo():
        audio_file = open('data/myaudio.oga', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/oga')

    #
    # st.image
    # https://docs.streamlit.io/library/api-reference/media/st.image
    #
    st.markdown("## image")
    st.markdown("""
    `st.image()`を用いてPIL imageを表示することができます．OpenCVなど別のライブラリで処理した
    結果を表示する場合にはPIL形式に変換する必要があります．
    """)
    with st.echo():
        image = Image.open('data/sunrise.png')
        st.image(image, caption='Sunrise by the mountains')

    #
    # st.video
    # https://docs.streamlit.io/library/api-reference/media/st.image
    #
    st.markdown("## video")
    st.markdown("""
    `st.video()`を用いて動画ファイルを読み込み，プレイヤーを表示することができます．
    """)
    with st.echo():
        video_file = open('data/star.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    #
    # st.camera_input
    # https://docs.streamlit.io/library/api-reference/widgets/st.camera_input
    #
    st.markdown("## camera input")
    st.markdown("""
    `st.camera_input()`でカメラを起動して画像をキャプチャすることができます．
    """)
    with st.echo():
        img_file_buffer = st.camera_input("Take a picture")
        if img_file_buffer is not None:
            # To read image file buffer as bytes:
            bytes_data = img_file_buffer.getvalue()
            # Check the type of bytes_data:
            # Should output: <class 'bytes'>
            st.write(type(bytes_data))

    #
    # st.file_uploader
    # https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
    #
    st.markdown("## st.file_uploader")
    st.markdown("""
    st.file_uploader()を用いてファイルの読み込みを実装することができます．デフォルトの設定では
    ファイル容量の上限は200MBとなっていますが`server.maxUploadSize`で変更することも可能です．
    """)
    with st.echo():
        uploaded_file = st.file_uploader("Choose a csv file")
        if uploaded_file is None:
            st.stop()
        st.write(uploaded_file.name)

    #
    # st.download_button
    # https://docs.streamlit.io/library/api-reference/widgets/st.download_button
    #
    st.markdown("## st.download_button")
    st.markdown("""
    st.download_button()を用いてファイルのダウンロードを実行できます．
    """)
    st.markdown("### テキストファイルの出力")
    with st.echo():
        text_contents = '''This is some text'''
        st.download_button('Download some text', text_contents)

if __name__ == "__main__":
    mainview()