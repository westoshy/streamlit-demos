import streamlit as st
from authentication import authentication
from streamlit_cropper import st_cropper
from PIL import Image

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


    st.markdown("# image cropper demo")
    st.markdown("""
    [streamlit-cropper](https://github.com/turner-anderson/streamlit-cropper)を用いることで
    インタラクティブに画像の必要な領域の切り出しを行うことができます．`st_cropper()`は選択
    した領域をPIL画像として返却しますが`retury_type`を`box`と指定することで座標値を取得する
    こともできます．このページでは座標値を取得するサンプルの動作を確認します．
    """)

    with st.echo():

        # 設定メニューをサイドバーに表示する
        with st.sidebar:
            realtime_update = st.checkbox(label="Update in Real Time", value=True)
            box_color = st.color_picker(label="Box Color", value='#0000FF')
            aspect_choice = st.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])

        image = Image.open('data/sunrise.png')
        aspect_dict = {
            "1:1": (1, 1),
            "16:9": (16, 9),
            "4:3": (4, 3),
            "2:3": (2, 3),
            "Free": None
        }
        aspect_ratio = aspect_dict[aspect_choice]

        st.write("画像から切り出す領域を選択してください．")
        rect = st_cropper(img=image, 
                          realtime_update=realtime_update, 
                          box_color=box_color, 
                          aspect_ratio=aspect_ratio,
                          return_type="box")
        cropped_img = image.crop((rect['left'], 
                                  rect['top'], 
                                  rect['width'] + rect['left'], 
                                  rect['height'] + rect['top']))
            
        st.write("切り出した領域を表示します．")
        st.image(cropped_img)

    st.markdown("""
    `st_cropper`が画像の切り出しを行うメソッドです．引数として与えたPIL形式の画像から
    選択した範囲の画像を切り出して返却します．返却値を座標にしたい場合には`retury_type`を
    `box`とします．そのほかにも下記のようなパラメータを設定することができます．

    | parameters | description |
    |--|--|
    | img           | The image to be cropped.                                  |
    | box_color     | The color of the cropper's bounding box. Defaults to blue,\
                      can accept other string colors recognized by fabric.js or \
                      hex colors in a format like '#ff003c'                     |
    | aspect_ratio  | Tuple representing the ideal aspect ratio: e.g. 1:1 aspect\
                      is (1,1) and 4:3 is (4,3)                                 |
    | box_algorithm | A function that can return a bounding box, the function \
                      should accept a PIL image and return a dictionary with keys:\
                      'left', 'top', 'width', 'height'. Note that if you use a \
                      box_algorithm with an aspect_ratio, you will need to decide how to\
                      handle the aspect_ratio yourself                          |
    | return_type |   The return type that you would like. The default, 'image',\
                      returns the cropped image, while 'box' returns a dictionary\
                      identifying the box by its left and top coordinates as well \
                      as its width and height. |
    | key          | An optional key that uniquely identifies this component. If this is\
        None, and the component's arguments are changed, the component will\
        be re-mounted in the Streamlit frontend and lose its current state. |
    """)

if __name__ == "__main__":
    #authentication()
    sidebar()
    mainview()