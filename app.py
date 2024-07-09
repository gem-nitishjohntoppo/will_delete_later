import streamlit as st
from streamlit_webrtc import webrtc_streamer


def main():
    st.title("Webcam Feed using WebRTC")

    webrtc_streamer(key="example")


if __name__ == "__main__":
    main()
