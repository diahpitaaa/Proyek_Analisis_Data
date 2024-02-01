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


	menu = ["Home","Pertanyaan 1","Pertanyaan 2","Pertanyaan 3"]
	choice = st.sidebar.selectbox('Menu',menu)
	if choice == 'Home':
		st.subheader("Pertanyaan-pertanyaan bisnis: ")
		st.text('1. Bagaimana persebaran rating dari penjualan produk berdasarkan kategorinya ?')
		st.text('2. Berapa persen pesanan yang datang sesuai atau bahkan lebih cepat dari estimasi?')
		st.text('3. Tipe pembayaran apa yang paling banyak dan paling sedikit dipakai?')
	elif choice == 'Pertanyaan 1':
		# Sort the data first
		st.subheader("1. Bagaimana persebaran rating dari penjualan produk berdasarkan kategorinya ?")

		grouped_data = all_df.groupby(['product_category_name_english', 'review_score']).size().reset_index(name='Jumlah')
		grouped_data = grouped_data.sort_values(by="Jumlah", ascending=False)

		# Take the top and worst 5 categories
		top_5_categories = grouped_data.head(5)
		worst_5_categories = grouped_data.tail(5)

		# Create the plot
		fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 6))
		colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

		# Bar plot for the top categories
		sns.barplot(x="Jumlah", y="product_category_name_english", data=top_5_categories, palette=colors, ax=ax1)
		ax1.set_ylabel(None)
		ax1.set_xlabel(None)
		ax1.set_title("Best Performing Product", loc="center", fontsize=15)
		ax1.tick_params(axis='y', labelsize=12)

		# Bar plot for the worst categories
		sns.barplot(x="Jumlah", y="product_category_name_english", data=worst_5_categories, palette=colors, ax=ax2)
		ax2.set_ylabel(None)
		ax2.set_xlabel(None)
		ax2.invert_xaxis()
		ax2.yaxis.set_label_position("right")
		ax2.yaxis.tick_right()
		ax2.set_title("Worst Performing Product", loc="center", fontsize=15)
		ax2.tick_params(axis='y', labelsize=12)

		plt.suptitle("Best Performing Product by Number of Sales (5 Star Rating)", fontsize=20)

		# Display the plot in Streamlit
		st.pyplot(fig)
		st.text('''Conclution Pertanyaan 1: 
		  Dari persebaran rating dari penjualan produk berdasarkan kategorinya, 
		  maka bisa kita lihat bahwa health_beauty dan bed_bath_table merupakan 
		  yang paling banyak mendapat rating 5 paling banyak, 
		  yaitu sekitar lebih dari 600 orderan.''')

	elif choice == 'Pertanyaan 2':
		st.subheader('2. Kota apa dengan sebaran pelanggan terbanyak?')
		city_customer_counts = all_df['customer_city'].value_counts().reset_index()
		city_customer_counts.columns = ['customer_city', 'customer_count']

		sorted_city_customers = city_customer_counts.sort_values(by="customer_count", ascending=False)

		# Ambil 5 kategori teratas
		top_5_customers_location = sorted_city_customers.head(5)

		# Buat plot
		fig, ax = plt.subplots(figsize=(24, 6))
		colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
		sns.barplot(x="customer_city", y="customer_count", data=top_5_customers_location, palette=colors, ax=ax)
		ax.set_ylabel(None)
		ax.set_xlabel(None)
		ax.set_title("Best Performing Product", loc="center", fontsize=15)
		ax.tick_params(axis='y', labelsize=12)

		plt.suptitle("Which city has the highest customer distribution?", fontsize=20)
		st.pyplot(fig)
		st.text('''conclution pertanyaan 4: 
		  Kota yang paling banyak memiliki persebaran data adalah 
		  saopaolo dengan sebanyak lebih dari 15000 orderan yang berada di saopolo, 
		  diikuti dengan rio de jeinaro sebanyak 6000 orderan, belo horizonte 
		  sekitaran lebih dari 2000 oderan.''')
        
	elif choice == 'Pertanyaan 3':
		st.subheader('3. Tipe pembayaran apa yang paling banyak dan paling sedikit dipakai')
		payment_counts = all_df['payment_type'].value_counts().reset_index()
		payment_counts.columns = ['payment type', 'Jumlah']

		#membuat subplot
		fig, ax = plt.subplots()
		data_label = payment_counts['payment type']
		votes = payment_counts['Jumlah']
		colors = ('#8B4513','#E67F0D', '#93C572', '#FFF8DC')
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
