import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Memasukkan Dataset yang Digunakan
orderpy_df = pd.read_csv("https://raw.githubusercontent.com/sitiaisyahh5/commerce/main/orderpy2_df.csv")
orderpy_df.head()

products_df = pd.read_csv("https://raw.githubusercontent.com/sitiaisyahh5/commerce/main/products2_df.csv")
products_df.head()

sellers_df = pd.read_csv("https://raw.githubusercontent.com/sitiaisyahh5/commerce/main/sellers2_df.csv")
sellers_df.head()


sum_product_df = products_df.groupby("product_category_name")["product_id"].count().reset_index()
sum_product_df = sum_product_df.rename(columns={"product_id": "products"})
sum_product_df = sum_product_df.sort_values(by="products", ascending=False)
sum_product_df = sum_product_df.head(10)

sum_product_df.head()

# Membuat Dashboard 
## Menghapus deskripsi
st.set_option('deprecation.showPyplotGlobalUse', False)

## Mengimport Logo E-Commerce
with st.sidebar:
    st.image("https://github.com/sitiaisyahh5/commerce/raw/c43eac1799bf7bc8bbe7a2d339ba15d40b61069f/images-1-1.jpeg") 
    st.write("Peta Brazil")
    st.image("https://github.com/sitiaisyahh5/commerce/raw/e8b58a031661ad19c45f3b96282115380155c76c/download.jpeg")

## Membuat Bar Plot 
def create_bar_plot(data, x, y, title, x_label, y_label, palette=None):
    plt.figure(figsize=(12, 6))
    sns.barplot(x=x, y=y, data=data, palette=palette)
    plt.title(title, fontsize=20)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(fontsize=12, rotation=30)
    plt.yticks(fontsize=12)
    st.pyplot()

# Menambahkan keterangan
    st.markdown("<p> Berdasarkan grafik hasil visualisasi, terlihat bahwa produk Cama Mesa Banho yang terjual 3029 produk dilanjutkan oleh produk Beleza Saude yang terjual 2867 produk dan lain-lain. Sehingga dapat disimpulkan bahwa produk yang paling banyak terjual adalah Cama Mesa Banho.</p>", 
                unsafe_allow_html=True)

# Membuat Histogram
def create_histogram(data, column, title, x_label, y_label, bins):
    plt.figure(figsize=(10, 6))
    plt.hist(data[column], bins=bins, color='blue', edgecolor='white')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    st.pyplot()
    
# Menambahkan Keterangan 
    st.markdown("<p> Berdasarkan grafik hasil visualisasi, terlihat bahwa range jumlah installment yang paling sering dilakukan oleh pelanggan adalah 1-2 kali berarti pelanggan sering melakukan installment sebanyak 1 kali dengan pembayarannya secara cash sampai 2 kali dengan pembayarannya secara menyicil.</p>", 
                unsafe_allow_html=True)

seller_states = sellers_df['seller_state'].value_counts().sort_values(ascending=False)

top_5_seller_states = seller_states.head(5)

# Membuat Bar Plot 
def create_seller_states_bar_plot(data, title, x_label, y_label, palette):
    plt.figure(figsize=(12, 6))
    sns.barplot(x=data.index, y=data.values, palette=palette)
    plt.title(title, fontsize=20)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(fontsize=12, rotation=30)
    plt.yticks(fontsize=12)
    st.pyplot()

# Menambah Keterangan
    st.markdown("<p> Berdasarkan hasil visualisasi grafik, terlihat bahwa 5 negara yang memiliki jumlah penjual terbanyak yaitu negara bagian SP (Sao Paolo) sebanyak 1849 penjual. Kemudian negara bagian PR (Puerto Riko) sebanyak 349 penjual, disusul oleh negara bagian MG (Minas Gerais) sebanyak 244 penjual. Selanjutnya negara bagian SC (South Carolina) sebanyak 190 penjual, disusul negara bagian RJ (Rio de Janeiro) sebanyak 171 penjual. </p>", 
                unsafe_allow_html=True)

# Membuat Judul
st.title("Analisis Data E-Commerce Dataset Menggunakan Dashboard")
st.write("Siti Aisyah ML-50")

# Membuat Plot dari Pertanyaan Bisnis 1
st.subheader("Top 10 Produk yang Paling Banyak Terjual")
create_bar_plot(sum_product_df, 'product_category_name', 'products',
                "Produk yang Paling Banyak Terjual", "Nama Produk", "Jumlah Produk", ["#ddedea", "#daeaf6"])

# Membuat Plot dari Pertama Bisnis 2
st.subheader("Histogram Jumlah Installment")
create_histogram(orderpy_df, 'payment_installments', 'Range Jumlah Installment', 'Jumlah Installments', 'Jumlah Pelanggan', range(0, 15))

# Membuat Plot dari Pertama Bisnis 3
st.subheader("Top 5 Kota Bagian dengan Penjual Terbanyak")
create_seller_states_bar_plot(top_5_seller_states, "Top 5 Negara Bagian dengan Penjual Terbanyak", "Negara Bagian", "Jumlah Penjual", "Blues")

st.caption('Copyright (c) Dicoding 2024')
st.caption('Linkedln : www.linkedin.com/in/siti-a-isyah-908800255')
st.caption('Instagram : https://www.instagram.com/stsyaah_?igsh=dDlrYzRtNW1zNTVi')
st.caption('Github : https://github.com/sitiaisyahh5')
