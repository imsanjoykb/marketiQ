import streamlit as st
import webbrowser

def redirect_to_google():
    webbrowser.open_new_tab("D:/Intelytics/IntelyticsPro/src/pages/demo1.html")

def footer():
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""###### MARKETLYTICS""")
        st.markdown("""<a href="https://drive.google.com/uc?id=1sVYKG7c3IxEPoFm7CDZYtYD-mSWR5dMx" style="text-decoration: none; color: red;"><b>About</b></a>""" , unsafe_allow_html=True)
        st.markdown("""<a href="https:/example.com" style="text-decoration: none; color: red;"><b>Products</b></a>""" , unsafe_allow_html=True)
        st.markdown("""<a href="https:/example.com" style="text-decoration: none; color: red;"><b>Guideline</b></a>""" , unsafe_allow_html=True)

    with col2:
        st.markdown("###### Legal")
        st.markdown("""<a href="https:/example.com" style="text-decoration: none; color: red;"><b>Privacy & Policy</b></a>""" , unsafe_allow_html=True)
        st.markdown("""<a href="https:/example.com" style="text-decoration: none; color: red;"><b>Terms & Condition</b></a>""" , unsafe_allow_html=True)
        st.markdown("""<a href="https:/example.com" style="text-decoration: none; color: red;"><b>Data Privacy</b></a>""" , unsafe_allow_html=True)

    with col3:
        st.markdown("###### Contact")
        st.markdown("""<a href="contact@marketlytics.pro" style="text-decoration: none; color: red;"><b>contact@marketlytics.pro</b></a>""" , unsafe_allow_html=True)
        st.markdown("""<a href="https://intelyticsai.beehiiv.com/subscribe" style="text-decoration: none; color: red;"><b>Subscribe to Newsletter</b></a>""" , unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)

    st.markdown("---")
    st.markdown("###### For Supporting")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<a href="https://www.buymeacoffee.com/imsanjoykb"><img height=35 style="border:0px;height:46px;" src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" border="0" alt="Buy Me a Coffee" />', unsafe_allow_html=True)
    with col2:
        st.markdown('<a href="https://www.patreon.com/imsanjoykb"><img height=35 style="border:0px;height:46px;" src="https://c5.patreon.com/external/logo/become_a_patron_button.png" border="0" alt="Donate" />', unsafe_allow_html=True)
    st.markdown("Copyright © 2023 MarketiQ. All Rights Reserved")

#Button Design 
m = st.markdown("""
<style> 
div.stButton > button:first-child {
    background-color: #8F6301;
    color:#FFCFB3;
    justify-content: center;
    align-items: center;
    text-align: center;
    border-radius:6px;
}
</style>""", unsafe_allow_html=True)

## Remove "Made with streamlit"
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    footer()
