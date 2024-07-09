import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

# Define the RTC configuration with the STUN server
RTC_CONFIGURATION = RTCConfiguration({
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
})

def main():
    st.title("Webcam Feed using WebRTC STUN")

    webrtc_streamer(
        key="example",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION
    )

if __name__ == "__main__":
    main()
