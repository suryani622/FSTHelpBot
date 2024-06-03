import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv

load_dotenv()
import home, about, chatbot, faq

st.set_page_config(
    page_title="FSTHelpBot",
)

st.markdown(
    """
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src=f"https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', os.getenv('analytics_tag'));
    </script>
    """, unsafe_allow_html=True
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='FSTHelpBot', 
                options=['Home','About','Chatbot', 'FAQ'],
                icons=['house-fill','person-circle','chat-fill', 'question-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "3!important","background-color":'#fff'},
                    "icon": {"color": "#f36758", "font-size": "18px"}, 
                    "nav-link": {"color":"black","font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#7eccd9"},
                    "nav-link-selected": {"background-color": "#D3D3D3"},
                }
            )
     
        if app == 'Home':
            home.app()     
        if app=='About':
            about.app()
        if app=='Chatbot':
            chatbot.app()  
        if app=='FAQ':
            faq.app()

    run()
