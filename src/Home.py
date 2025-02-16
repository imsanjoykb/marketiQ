import streamlit as st
import templates.pricing
import templates.footer
import templates.teams
import templates.products_list
import templates.page_config

def home():

    # Create the Markdown content with aligned image
    markdown_content = f"""
    <div style="display: flex; align-items: center;">
        <h3>MarketiQ | Amplify Marketing Brainpower</h3>
    </div>

    """

    # Render the Markdown content in Streamlit
    st.markdown(markdown_content, unsafe_allow_html=True)

    st.markdown("---")
    #Description
    st.markdown(
        """ 
        <h5 style='text-align:center;'>MarketiQ is an advanced application that leverages cutting-edge technologies to provide intelligent and faster marketing solutions.</h5>
        """,
        unsafe_allow_html=True)

    #templates.products_list.products_list()
    templates.pricing.pricing_page()
    templates.teams.teams_member()
    templates.footer.footer()
    templates.page_config.pagset_page_confige_config()

if __name__ == "__main__":
    home()





