import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_webrtc import webrtc_streamer


# Page Configuration
st.set_page_config(page_title="Swapnil Nanda", page_icon=":alien:", layout="wide")

# Navigation Bar
selected = option_menu(
    menu_title=None,
    options = ["Home","Image","Video"],
    icons = ["house-fill","image-fill","camera-video-fill"],
    orientation="horizontal",
)
# When different options are selected in NavBar
# When Home is selected
if selected == "Home":
    st.title("Hi, I am Swapnil Nanda from the department of Computer Science and Engineering.")
    st.write("This is my first webapp using streamlit. Initial testing of camera access...")
# When Image is selected
if selected == "Image":
    # Option menu after selecting Image
    selectedimg = option_menu(
    menu_title=None,
    options = ["Select a Local Image","Use Camera"],
    icons = ["file-image-fill","camera-fill"],
    orientation="vertical",
    )
    str = st.text_input("Enter caption")
    # When "Select a local image" is selected
    if selectedimg == "Select a Local Image":
        # Uploading image
        image = st.file_uploader("Please upload an image", type = ["png","jpg","jpeg","bmp","gif"])
        if image is not None:
            st.image(image)
            st.caption(str)
    # When "Use Camera" is selected
    if selectedimg == "Use Camera":
        # Taking image input from camera
        image = st.camera_input("Please upload an image", key = None)
        if image is not None:
            st.image(image)
            st.caption(str)

# When "Video" is selected
if selected == "Video":
    # Option menu after selecting Video
    selectedvid = option_menu(
    menu_title=None,
    options = ["Select a Local Video","Use Camera"],
    icons = ["file-play-fill","camera-reels-fill"],
    orientation="vertical",
    )
    str = st.text_input("Enter caption")
    # When "Select a local video" is selected
    if selectedvid == "Select a Local Video":
        # Uploading a video
        video = st.file_uploader("Please upload an video", type = ["mp4","mov","wmv","flv","avi","mpg"])
        if video is not None:
            st.video(video)
            st.caption(str)
    
    if selectedvid == "Use Camera":
        # Capturing video from camera
        
        webrtc_streamer(key="key")
        st.caption(str)
        
        
