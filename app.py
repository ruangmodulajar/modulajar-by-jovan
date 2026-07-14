import streamlit as st
import google.generativeai as genai
import os

# Konfigurasi Halaman Aplikasi
st.set_page_config(page_title="Generator Modul Ajar Deep Learning", page_icon="📚", layout="wide")

# Mengambil API Key dari sistem Streamlit
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

st.title("📚 Generator Modul Ajar Kurikulum Merdeka created by Jovan Darmawan Togas")
st.markdown("**Pendekatan Deep Learning (Mindful, Meaningful, Joyful)**")

# Input Form
with st.form("modul_form"):
    col1, col2 = st.columns(2)
    with col1:
        mapel = st.text_input("Mata Pelajaran", placeholder="Contoh: Bahasa Indonesia, Informatika")
        fase = st.selectbox("Fase / Kelas", ["Fase A (Kelas 1-2)", "Fase B (Kelas 3-4)", "Fase C (Kelas 5-6)", "Fase D (Kelas 7-9)", "Fase E (Kelas 10)", "Fase F (Kelas 11-12)"])
    with col2:
        materi = st.text_input("Materi Pokok", placeholder="Contoh: Teks Argumentasi, Algoritma Dasar")
        waktu = st.text_input("Alokasi Waktu", placeholder="Contoh: 2 JP (2 x 45 Menit)")
    
    tujuan = st.text_area("Tujuan Pembelajaran Khusus (Opsional)", placeholder="Apa yang ingin dicapai siswa?")
    submit_button = st.form_submit_button("Buat Modul Ajar")

# Logika AI AI
if submit_button:
    if mapel and materi:
        with st.spinner("Meracik modul ajar dengan pendekatan Deep Learning..."):
            prompt = f"""
            Anda adalah pakar kurikulum pendidikan di Indonesia. Buatkan Modul Ajar Kurikulum Merdeka untuk mata pelajaran {mapel} pada {fase}. 
            Materi: {materi}. Waktu: {waktu}. Tujuan khusus: {tujuan}.
            
            Gunakan pendekatan DEEP LEARNING (Mindful, Meaningful, Joyful). 
            
            Struktur Modul Ajar wajib berisi:
            1. Informasi Umum & Identitas
            2. Capaian Pembelajaran & Profil Pelajar Pancasila
            3. Pemahaman Bermakna (Meaningful)
            4. Pertanyaan Pemantik (Mindful)
            5. Langkah-langkah Pembelajaran:
               - Pendahuluan (Joyful & Mindful trigger)
               - Kegiatan Inti (Eksplorasi mendalam, bukan sekadar hafalan. Siswa sebagai subjek aktif).
               - Penutup & Refleksi
            6. Asesmen Formatif (Penilaian pemahaman mendalam, bukan pilihan ganda biasa).
            
            Format ke dalam Markdown agar rapi untuk dibaca. Gunakan bahasa Indonesia yang baku namun mudah dipahami guru.
            """
            
            try:
                response = model.generate_content(prompt)
                st.success("Modul berhasil dibuat!")
                st.markdown("---")
                st.markdown(response.text)
                
                # Tombol Download
                st.download_button(
                    label="Download Modul (Teks)",
                    data=response.text,
                    file_name=f"Modul_Ajar_{mapel.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Mohon isi Mata Pelajaran dan Materi Pokok terlebih dahulu.")
