import streamlit as st
import numpy as np

st.write("Aplikasi luas segitiga")

alas = st.number_input("Masukkan Alas", 0)
tinggi = st.number_input("Masukkan Tinggi", 0)

hitung = st.button("Hitung Luas")

if hitung:
      luas = 0.5 * alas * tinggi
      st.success(f"Luas Segitiganya adalah {luas}")
      st.balloons()
