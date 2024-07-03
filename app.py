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

# st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

# with st.expander("See explanation"):
#     st.write('''
#         The chart above shows some numbers I picked for you.
#         I rolled actual dice for these, so they're *guaranteed* to
#         be random.
#     ''')
#     st.image("https://static.streamlit.io/examples/dice.jpg")
    
    
# Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

# col1, col2 = st.columns([3, 1])
# data = np.random.randn(10, 1)

# col1.subheader("A wide column with a chart")
# col1.line_chart(data)

# col2.subheader("A narrow column with the data")
# col2.write(data)


