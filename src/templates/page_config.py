import streamlit as st

def pagset_page_confige_config():

    #Button Design 
    m = st.markdown("""
    <style> 
    div.stButton > button:first-child {
        background-color: #E07A5F;
        color:#FFF7D4;
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
    pagset_page_confige_config()