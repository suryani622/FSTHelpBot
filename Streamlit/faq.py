import streamlit as st

def app():

    with open("style.css") as f:
     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True) 

    st.write('''
           # FAQ
          ''')
    
    st.write("")

    paragraph5 = "Selamat datang di halaman FAQ FSTHelpBot. Berikut adalah beberapa pertanyaan yang sering diajukan"

    st.markdown(f'<div style="text-align: justify;">{paragraph5}</div>', unsafe_allow_html=True)

    st.write("")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.write("")

    #Daftar pertanyaan dan Jawaban FAQ
    faqs = [
        {"question": "Apa itu FSTHelpBot?", "answer": "FSTHelpBot adalah chatbot yang melayani informasi administrasi di Fakultas Sains dan Teknologi"},
        {"question": "Apa saja layanan yang disediakan oleh FSTHelpBot?", "answer": "FSTHelpBot menyediakan layanan Administrasi Akademik Mahasiswa yang terdiri atas Surat Aktif Kuliah/Beasiswa, Surat Penunjukkan Pembimbing, Surat Berkelakuan Baik, Surat Keterangan Masih Kuliah, serta informasi terkait seminar proposal dan sidang tugas akhir"},
        {"question": "Apakah FSTHelpBot dapat melakukan tracking surat?", "answer": "Tidak. FSTHelpBot hanya menangani inputan teks, dan memberikan respon teks."},
        {"question": "Apakah FSTHelpBot tersedia 24/7?", "answer": "Ya, FSTHelpBot tersedia 24/7 untuk memberikan informasi yang Anda butuhkan kapan saja"},
        {"question": "Ada kalanya FSTHelpBot memberikan jawaban yang tidak relevan, apa yang terjadi?", "answer": "Jawaban ambigu atau tidak tepat yang diberikan olehFSTHelpBot dapat terjadi akibat model yang belum terlalu cerdas, kurangnya data pelatihan, atau ketidaktepatan inputan yang diberikan oleh user. "},
        {"question": "Siapa yang bisa saya hubungi untuk masalah teknis?", "answer": "Untuk masalah teknis, Anda bisa menghubungi tim pengembang FSTHelpBot di suryaniani0602@gmail.com"}

    ]


    #Tampilkan FAQ
    for faq in faqs:
        with st.expander(faq["question"]):
            st.write(faq["answer"])





