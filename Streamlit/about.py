import streamlit as st


def app():
    # Menggunakan indentasi 4 spasi di bawah ini
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    st.markdown('''
        ### **About**
        ##### 
        ''')

    paragraph1 ='Fakultas Sains dan Teknologi didirikan pada akhir tahun 2001 sebagai persiapan perubahan status dari Institut Agama Islam Negeri Sultan Syarif Qasim (IAIN SUSQA) Pekanbaru menjadi Universitas Islam Negeri Sultan Syarif Kasim Riau (UIN Suska) Riau. Cikal bakal berdirinya Fakultas Sains dan Teknologi bermula dibukanya Jurusan Teknik Informatika pada tahun 1999 dan jurusan Teknik Industri pada tahun 2001. Kedua jurusan tersebut berada di bawah naungan Fakultas Dakwah. Dengan adanya kedua jurusan tersebut , maka dibentuklah Fakultas Sains dan Teknologi. Saat ini, Fakultas Sains dan Teknologi memiliki 5 program studi. Yaitu Teknik Informatika, Teknik Industri, Sistem Informasi, Matematika, dan Teknik Elektro.'

    for paragraph in [paragraph1]:
        st.markdown(f'<div style="text-align: justify;">{paragraph}</div>', unsafe_allow_html=True)
        st.write("")

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown('''
        ### **Visi & Misi**
        ##### 
        ''')
    

    st.write("")
    # Bagi Halaman About Menjadi dua Kolom

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Visi Fakultas Sains dan Teknologi**")
        st.markdown('''
        
                    Menjadi fakultas yang unggul di Asia Tenggara dalam pendidikan dan riset sains dan teknologi yang terintegrasi dengan Islam dan berdampak pada masyarakat pada tahun 2025
        ''')

    with col2:
        st.write("**Misi Fakultas Sains dan Teknologi**")

        items = [
            "Menyelenggarakan pendidikan untuk menghasilkan lulusan yang kompeten dalam bidang sains dan teknologi, berintegritas Islami, dan memiliki kemampuan kepemimpinan.", 
            "Memperkuat riset sains dan teknologi yang bermanfaat bagi kesejahteraan masyarakat.", "Mengembangkan jejaring kerjasama multidisiplin dengan berbagai mitra nasional dan internasional dalam rangka pengembangan tridarma perguruan tinggi.", 
            "Meningkatkan tata kelola organisasi secara berkelanjutan dengan prinsip-prinsip akuntabel, transparan, serta adaptif melalui penggunaan teknologi"]
        
        # Gunakan tag HTML <ol> untuk membuat ordered list
        st.markdown("<ol>", unsafe_allow_html=True)

        # Tampilkan setiap item dalam ordered list
        for item in items:
            st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)

    # Akhiri ordered list
    st.markdown("</ol>", unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


    st.markdown('''
        ### **Layanan Mahasiswa**
        ##### 
        ''')

    paragraph3 = 'Layanan Mahasiswa Fakultas Sains dan Teknologi terdiri atas layanan administrasi umum dan layanan administrasi akademik. Layanan administrasi akademik meliputi:'

    st.markdown(f'<div style="text-align: justify;">{paragraph3}</div>', unsafe_allow_html=True)

    items2 = ["Pendaftaran Seminar/Sidang TA/KP/Proyek Mini", 
            "Surat Penunjukkan Pembimbing/Penguji TA/KP/Proyek Mini", 
            "Surat Keterangan Aktif Kuliah dan Keterangan Beasiswa", 
            "Surat Keterangan Masih Kuliah", 
            "Surat Keterangan Berkelakuan Baik"]

    # Gunakan tag HTML <ol> untuk membuat ordered list
    st.markdown("<ol>", unsafe_allow_html=True)

    # Tampilkan setiap item dalam ordered list
    for item in items2:
        st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)

    # Akhiri ordered list
    st.markdown("</ol>", unsafe_allow_html=True)

    #Button ke Seminar FST
    url = "https://seminar-fst.uin-suska.ac.id/"

    # Tombol dengan gaya tautan
    st.markdown(f'<a href="{url}" target="_blank" class="btn btn-outline-primary" style="color: #000;">Kunjungi Halaman Seminar FST</a>', unsafe_allow_html=True)


    st.write("")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    #####################

