import streamlit as st
import os

base_url = os.environ.get('BASE_URL')
google_drive = os.environ.get('GOOGLE_DRIVE')

def products_list():
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>Products</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'''<a href="{base_url}/AI_Write" target="_self"><img height=46 style="border:0px;height:95px;" src="{google_drive}1S-YsX8FrgGdZRrpBNFEm0LMWah33YURK" border="0" alt="AI Write" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Invoice_Generator" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1kgAo8sgh16jy_y4r9JuKsbKMfSLj6628" border="0" alt="Invoice Generator" /></a>''', unsafe_allow_html=True)
    with col2:
        st.markdown(f'''<a href="{base_url}/Email_Generator" target="_self"><img height=46 style="border:0px;height:95px;" src="{google_drive}1WFrPJ4i0nn8juN6kjszG8OEgM18KYkdM" border="0" alt="Email Generator" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Product_Description_Generator" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1V4UhYcM3nmHHyg8h7hek-s9zF4Y699SL" border="0" alt="Product Description Generator" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Social_Media_Caption_Generator" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1YLWBqL427Ei3WO5ItXGVy5kileno1IcD" border="0" alt="Social_Media_Caption_Generator" /></a>''', unsafe_allow_html=True)
    with col3:
        st.markdown(f'''<a href="{base_url}/Article_Generator" target="_self"><img height=46 style="border:0px;height:95px;" src="{google_drive}1PLpSIoVZaVFJjdeyoLpXHnxpCynyFVpG" border="0" alt="Article Generator" /></a>''', unsafe_allow_html=True)        
        st.markdown(f'''<a href="{base_url}/Product_Listing_Generator" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1n0PFIJkSJwCDQEcBL0BLMVoeIeTVrzPA" border="0" alt="Product Listing Generator" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Chat_with_Document" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1fOi7Y6Z4825k_z8rnvrFef2BRcpHpZPC" border="0" alt="Chat_with_Document" /></a>''', unsafe_allow_html=True)
    with col4:
        st.markdown(f'''<a href="{base_url}/Ad_Generator" target="_self"><img height=46 style="border:0px;height:95px;" src="{google_drive}1NZFbyyFmuW8ibaUFmM8Umx5SWGfEiEU_" border="0" alt="Ad Generator" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Product_Comparison" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1bW3Q6lLsmGFYaQtBrSHHK3wOoAfEkTxT" border="0" alt="Product Comparison" /></a>''', unsafe_allow_html=True)

    st.markdown("---")

## Remove "Made with streamlit"
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    products_list()
