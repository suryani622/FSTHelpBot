import streamlit as st
from PIL import Image


def app():
    # Menggunakan indentasi 4 spasi di bawah ini
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    
    
    st.write('''
           # Selamat Datang
          ''')
    
    st.write("##### Layanan Chatbot Administrasi Akademik Fakultas Sains dan Teknologi")

    image = Image.open('main page.jpg') #di bagian sini, bisa tambahkan foto/ilustrasi chatbot
    st.image(image, use_column_width=True)
