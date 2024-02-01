import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st

sns.set(style='dark')

PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}

all_df = pd.read_csv("data.csv")

def main():
    st.title("Proyek Analisis Data Menggunakan Python")


    menu = ["Beranda","Pertanyaan 1","Pertanyaan 2","Pertanyaan 3"]
    choice = st.sidebar.selectbox('Menu',menu)
    if choice == 'Beranda':
        st.subheader("Pertanyaan-pertanyaan bisnis: ")
        st.text('1. Bagaimana distribusi penilaian (rating) dari penjualan produk berdasarkan kategori produknya ?')
        st.text('2. Berapa persentase pesanan yang tiba sesuai atau bahkan lebih cepat dari perkiraan waktu pengiriman ?')
        st.text('3. Apa jenis pembayaran yang paling sering digunakan dan yang jarang digunakan dalam transaksi ?')
    elif choice == 'Pertanyaan 1':
        # Sort the data
        st.subheader("1. Bagaimana distribusi penilaian (rating) dari penjualan produk berdasarkan kategori produknya?")

        grouped_data = all_df.groupby(['product_category_name_english', 'review_score']).size().reset_index(name='Jumlah')
        grouped_data = grouped_data.sort_values(by="Jumlah", ascending=False)

        # Select the top and worst 5 categories
        top_5_categories = grouped_data.head(5)
        worst_5_categories = grouped_data.tail(5)

        # Create the plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 6))
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

        # Bar plot for the top categories
        sns.barplot(x="Jumlah", y="product_category_name_english", data=top_5_categories, palette=colors, ax=ax1)
        ax1.set_ylabel(None)
        ax1.set_xlabel(None)
        ax1.set_title("Produk Terbaik", loc="center", fontsize=15)
        ax1.tick_params(axis='y', labelsize=12)

        # Bar plot for the worst categories
        sns.barplot(x="Jumlah", y="product_category_name_english", data=worst_5_categories, palette=colors, ax=ax2)
        ax2.set_ylabel(None)
        ax2.set_xlabel(None)
        ax2.invert_xaxis()
        ax2.yaxis.set_label_position("right")
        ax2.yaxis.tick_right()
        ax2.set_title("Produk Terburuk", loc="center", fontsize=15)
        ax2.tick_params(axis='y', labelsize=12)

        plt.suptitle("Produk Terbaik berdasarkan Jumlah Penjualan (Rating 5 Bintang)", fontsize=20)

        # Display the plot in Streamlit
        st.pyplot(fig)
        st.text('''Kesimpulan : 
            Dari distribusi rating penjualan produk berdasarkan kategori, 
            dapat dilihat bahwa kategori health_beauty dan bed_bath_table 
            mendapatkan rating 5 paling tinggi, dengan lebih dari 600 pesanan.''')

    elif choice == 'Pertanyaan 2':
        st.subheader('2. Berapa persentase pesanan yang tiba sesuai atau bahkan lebih cepat dari perkiraan waktu pengiriman?')
        
        city_customer_counts = all_df['customer_city'].value_counts().reset_index()
        city_customer_counts.columns = ['customer_city', 'customer_count']
        
        sorted_city_customers = city_customer_counts.sort_values(by="customer_count", ascending=False)

        # Ambil 5 lokasi teratas
        top_5_customers_location = sorted_city_customers.head(5)

        # Buat plot
        fig, ax = plt.subplots(figsize=(12, 6))
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
        sns.barplot(x="customer_count", y="customer_city", data=top_5_customers_location, palette=colors, ax=ax)
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.set_title("Kota dengan Distribusi Pelanggan Tertinggi", loc="center", fontsize=15)
        ax.tick_params(axis='y', labelsize=12)

        plt.suptitle("Kota mana dengan distribusi pelanggan tertinggi?", fontsize=20)
        st.pyplot(fig)
        st.text('''Kesimpulan Pertanyaan 2: 
            Kota dengan distribusi pelanggan tertinggi adalah Sao Paulo 
            dengan lebih dari 15.000 pesanan, diikuti oleh Rio de Janeiro 
            dengan sekitar 6.000 pesanan, dan Belo Horizonte dengan lebih dari 2.000 pesanan.''')

        
    elif choice == 'Pertanyaan 3':
        st.subheader('3. Tipe pembayaran apa yang paling banyak dan paling sedikit dipakai')
        payment_counts = all_df['payment_type'].value_counts().reset_index()
        payment_counts.columns = ['payment type', 'Jumlah']

        #membuat subplot
        fig, ax = plt.subplots()
        data_label = payment_counts['payment type']
        votes = payment_counts['Jumlah']
        colors = sns.color_palette("pastel")[0:5]
        explode = (0, 0,0,0)

        # Buat pie chart
        plt.figure(figsize=(8, 8))
        ax.pie(votes, labels=data_label, autopct='%1.1f%%', colors=colors)

        # Tambahkan judul
        plt.title("Persentase Pembayaran Berdasarkan Jenis Pembayaran")

        # Tampilkan pie chart
        st.pyplot(fig)
        
        st.text('''conclution pertanyaan 3: 
          Tipe pembayaran paling banyak dipakai adalah credit_card 
          yaitu sebanyak 73,9% dan setelah itu ada boleto sebanyak 19%, kemudian 5.6% untuk voucher, 
          lalu ada sebanyak 1.5% yang menggunakan kartu debit''')
    

if __name__ == '__main__':
    main()
