import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime
import io
from streamlit_option_menu import option_menu
 
with st.sidebar:
    st.sidebar.title("Bike Sharing Analysis 🚲 \n 👨🏻‍💻 Muhammad Gufril Firdaus")
    selected = option_menu(
	"Main Menu", ["Resume", "Data Wrangling", "Exploratory Data Analysis (EDA)", "Data Visualization & Explanatory Analysis"], 
         menu_icon="cast", 
	 default_index=0)

day_df = pd.read_csv("https://github.com/Gufril-dev/Analisis_Data/blame/main/day.csv")
hour_df = pd.read_csv("https://github.com/Gufril-dev/Analisis_Data/blame/main/hour.csv")

if selected == "Resume":
    st.title(f"📑 Resume Bike Sharing 🚲")
    st.markdown(
    """
   <b>Hadi Fanaee-T</b><br>
    <br>
    Laboratory of Artificial Intelligence and Decision Support<br>
    (LIAAD), University of Porto<br>
    INESC Porto, Campus da FEUP<br>
    Rua Dr. Roberto Frias, 378<br>
    4200 - 465 Porto, Portugal<br>
    <br>
    <br>
    <b>Background</b><br>
    Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return 
    back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return 
    back at another position. Currently, there are about over 500 bike-sharing programs around the world which is composed of 
    over 500 thousands bicycles. Today, there exists great interest in these systems due to their important role in traffic, 
    environmental and health issues.
    <br>
    Apart from interesting real world applications of bike sharing systems, the characteristics of data being generated by
    these systems make them attractive for the research. Opposed to other transport services such as bus or subway, the duration
    of travel, departure and arrival position is explicitly recorded in these systems. This feature turns bike sharing system into
    a virtual sensor network that can be used for sensing mobility in the city. Hence, it is expected that most of important
    events in the city could be detected via monitoring these data.
    <br>
    <br>
    <b>Data Set</b><br>
    Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions,
    precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to  
    the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
    publicly available in http://capitalbikeshare.com/system-data. We aggregated the data on two hourly and daily basis and then 
    extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com.
    <br>
    <br>
    <b>Associated tasks</b><br>
    - Regression: <br>
		Predication of bike rental count hourly or daily based on the environmental and seasonal settings.
	<br>
	- Event and Anomaly Detection:  <br>
		Count of rented bikes are also correlated to some events in the town which easily are traceable via search engines.
		For instance, query like "2012-10-30 washington d.c." in Google returns related results to Hurricane Sandy. Some of the important events are 
		identified in [1]. Therefore the data can be used for validation of anomaly or event detection algorithms as well.
    <br>
    <br>
    <b>Files</b><br>
    - Readme.txt<br>
	- hour.csv : bike sharing counts aggregated on hourly basis. Records: 17379 hours<br>
	- day.csv - bike sharing counts aggregated on daily basis. Records: 731 days
    <br>
    <br>
    <b>Dataset characteristics</b><br>
    Both hour.csv and day.csv have the following fields, except hr which is not available in day.csv
	- instant: record index<br>
	- dteday : date<br>
	- season : season (1:springer, 2:summer, 3:fall, 4:winter)<br>
	- yr : year (0: 2011, 1:2012)<br>
	- mnth : month ( 1 to 12)<br>
	- hr : hour (0 to 23)<br>
	- holiday : weather day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)<br>
	- weekday : day of the week<br>
	- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.<br>
	+ weathersit : <br>
		- 1: Clear, Few clouds, Partly cloudy, Partly cloudy<br>
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist<br>
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds<br>
		- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog<br>
	- temp : Normalized temperature in Celsius. The values are divided to 41 (max)<br>
	- atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)<br>
	- hum: Normalized humidity. The values are divided to 100 (max)<br>
	- windspeed: Normalized wind speed. The values are divided to 67 (max)<br>
	- casual: count of casual users<br>
	- registered: count of registered users<br>
	- cnt: count of total rental bikes including both casual and registered
    <br>
    <br>
    <b>License</b><br>
    Use of this dataset in publications must be cited to the following publication:<br>
<br>
[1] Fanaee-T, Hadi, and Gama, Joao, "Event labeling combining ensemble detectors and background knowledge", Progress in Artificial Intelligence (2013): pp. 1-15, Springer Berlin Heidelberg, doi:10.1007/s13748-013-0040-3.
<br>
@article{  <br>
	year={2013},<br>
	issn={2192-6352},<br>
	journal={Progress in Artificial Intelligence},<br>
	doi={10.1007/s13748-013-0040-3},<br>
	title={Event labeling combining ensemble detectors and background knowledge},<br>
	url={http://dx.doi.org/10.1007/s13748-013-0040-3},<br>
	publisher={Springer Berlin Heidelberg},<br>
	keywords={Event labeling; Event detection; Ensemble learning; Background knowledge},<br>
	author={Fanaee-T, Hadi and Gama, Joao},<br>
	pages={1-15}<br>
}<br>
<br>
<br>
    """,
     unsafe_allow_html=True
    )
    st.title("Data Analysis Project: BIKE SHARING DATASET")
    st.markdown(
    """
    Name : Muhammad Gufril Firdaus<br>
    Email : Gufril57@gmail.com<br>
    <br>
    <b>Pertanyaan Bisnis</b>
    1. Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?(Apakah ada perbedaan signifikan dalam jumlah penyewaan sepeda antara musim panas, musim gugur, musim dingin, dan musim semi?) <br>
    2. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?(Apakah ada pola tertentu dalam jumlah penyewaan sepeda berdasarkan curah hujan, suhu dan kelembapan?)<br>
    3. Bagaimana korelasi antara temperature dengan jumlah penyewaan sepeda?(apakah memiliki korelasi positif atau negatif?)<br>
    4. Bagaimana pengaruh variabel lain seperti kecepatan angin dan visibilitas terhadap jumlah penyewaan sepeda? (Apakah variabel-variabel ini memiliki korelasi yang signifikan dengan jumlah penyewaan sepeda?)<br>
    <br>
    <br>
    <b>Detail : </b><br>
    - Analisis Data dengan Menggunakan Python<br>
    - Data Science Libraries (Numpy, Pandas, Matplotlib, Seaborn, Streamlit)<br>
    - Dasar Descriptive Statistics & Demografi Data<br>
    - Data Wrangling (Gathering Data, Assessing Data, Cleaning Data)<br>
    - Exploratory Data Analysis (EDA)<br>
    - Data Visualization & Explanatory Analysis<br>
    """,
     unsafe_allow_html=True
    )
    
elif selected == "Data Wrangling":
    st.title(f"{selected} 📁 ")
    st.markdown(
        "<h1 style='font-size:25px;'>Gathering Data 💾 </h1>",
        unsafe_allow_html=True
    )
    st.write("Mendapatkan data penyewaan sepeda perhari")
    st.write(day_df.head())
    st.write("Mendapatkan data penyewaan sepeda per jam")
    st.write(hour_df.head())
    st.markdown(
        "<h2 style='font-size:20px;'>Insight 💡 </h1>",
        unsafe_allow_html=True
    )
    st.markdown(
    """
    - Terdapat 16 kolom pada data penyewaan sepeda berdasarkan hari.
    - Terdapat 17 kolom pada data penyewaan sepeda berdasarkan jam. <br>
    - <b>Informasi Kolom :</b>
   
        - instant: indeks catatan
        - dteday : tanggal
        - season : musim (1: musim semi, 2: musim panas, 3: musim gugur, 4: musim dingin)
        - yr : tahun (0: 2011, 1: 2012)
        - bulan : bulan (1 sampai 12)
        - hr : jam (0 hingga 23)
        - holiday : hari cuaca hari libur atau tidak (diambil dari http://dchr.dc.gov/page/holiday-schedule)
        - hari kerja : hari dalam seminggu
        - hari kerja : jika hari tersebut bukan akhir pekan atau hari libur maka nilainya 1, jika tidak maka nilainya 0.
        + cuaca : 
            - 1: Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian
            - 2: Kabut + Berawan, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut
            - 3: Salju Ringan, Hujan Ringan + Badai Petir + Awan berserakan, Hujan Ringan + Awan berserakan
            - 4: Hujan Lebat + Butiran Es + Badai Petir + Kabut, Salju + Kabut
        - temp: Suhu yang dinormalisasi dalam Celcius. Nilai dibagi menjadi 41 (maks)
        - atemp: Suhu perasaan yang dinormalisasi dalam Celcius. Nilai dibagi menjadi 50 (maks)
        - hum: Kelembapan yang dinormalisasi. Nilai dibagi menjadi 100 (maks)
        - windspeed: Kecepatan angin yang dinormalisasi. Nilai dibagi menjadi 67 (maks)
        - casual: jumlah pengguna biasa
        - terdaftar: jumlah pengguna terdaftar
        - cnt: jumlah total sepeda sewaan termasuk pengguna kasual dan terdaftar
    """,
      unsafe_allow_html=True
    )
    
    st.markdown(
        "<h1 style='font-size:25px;'>Assessing Data 🔍 </h1>",
        unsafe_allow_html=True
    )
    st.markdown(
    """
    <h2 style='font-size:20px;'>1. Melakukan Penilaian Kualitas Data Penyewaan Sepeda Berdasarkan Hari</h1>
        <b>- Melakukan Pemerikasaan Tipe Data, Missing Value dan Null Data</b>
    """,
        unsafe_allow_html=True
    )
    
    st.write("Jumlah Data Duplikat pada data day_df: ", (day_df.duplicated().sum()))
    st.write("Dataset Informasi:")
    buffer = io.StringIO()
    day_df.info(buf=buffer)
    info_output = buffer.getvalue()
    st.text(info_output)
    
    st.markdown(
    """
        <b>- Melakukan Pemerikasaan Parameter Statistik Data day_df</b>
    """,
        unsafe_allow_html=True
    )
    st.write(day_df.describe())
    
    st.markdown(
        "<h2 style='font-size:20px;'>Insight 💡</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
    """ 
    - Terdapat Tipe Data pada kolom <mark>dteday_df</mark> yaitu <mark>object</mark> yang seharusnya bertipe data <mark>datetime</mark> karena merupakan data yang berisi tanggal<br>
    - Tidak terdapat <mark>Missing Value</mark> atau Nilai yang hilang pada setiap kolom, indikasi penghitung <mark>non-null</mark> disetiap kolom<br>
    - Tidak terdapat <mark> Data Duplikat </mark> , indikasi hasil operasi fungsi pengecekan data <mark> .duplicated().sum() </mark><br>
    - Tidak Terdapat Kejanggalan input pada setiap kolom dengan <mark>parameter statistik</mark>, indikasi sesuai aturan bisnis <bar>
    """,unsafe_allow_html=True 
    )
    
    st.markdown(
        "<h1 style='font-size:25px;'>Cleaning Data 🧼 </h1>",
        unsafe_allow_html=True
    )
    st.write("Pada proses sebelumnya struktur dan nilai data hanya terdapat sedikit kasus yang perlu dilakukan perbaikan yaitu berupa perubahan tipe data object menjadi datetime")
    
    st.markdown(
    """
    <h2 style='font-size:18px;'>1. Melakukan Perubahan tipe data dteday dari type data object menjadi datetime pada data penyewaan berdasarkan hari</h1>
    """,
        unsafe_allow_html=True
    )
    datetime_columns = ["dteday"]
    for column in datetime_columns:
        day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    st.write(day_df.info())
    day_df.info()
    st.write(day_df.dtypes)
    
    st.markdown(
    """
    <h2 style='font-size:18px;'>2. Melakukan Perubahan tipe data dteday dari type data object menjadi datetime pada data penyewaan berdasarkan jam </h1>
    """,       
    unsafe_allow_html=True
    )
    datetime_columns = ["dteday"]
    for column in datetime_columns:
            hour_df['dteday'] = pd.to_datetime(day_df['dteday'])
    st.write(hour_df.info())
    hour_df.info()
    st.write(hour_df.dtypes)
    
    st.markdown(
        "<h2 style='font-size:20px;'>Insight 💡</h1>",
        unsafe_allow_html=True
    )    
    st.markdown(
    """
    - Berhasil melakukan perubahan tipe data pada kolom day_df dan hour_df<br>
    - Cleaning Data sudah selesai dilakukan dan data tersebut ready untuk dilakukan proses Exploratory Data Analysis (EDA)<br>
    """,
    unsafe_allow_html=True
    )
    
elif selected == "Exploratory Data Analysis (EDA)":
    st.title(f"{selected} 🔍 ")
    st.markdown(
        "<h1 style='font-size:20px;'>Statistik Deskriptif | Memahami Distribusi Data</h1>",
        unsafe_allow_html=True
    )    
    st.write("- Statistik deskriptif berdasarkan hari")
    st.write(day_df.describe(include="all"))
    st.write("- Statistik deskriptif berdasarkan jam")
    st.write(hour_df.describe(include="all"))
    
    st.markdown(
        "<h1 style='font-size:20px;'>Demografi Data | Memahami Pola Data</h1>",
        unsafe_allow_html=True
    )  
    
    weather_labels = {1: 'Clear', 2: 'Mist', 3: 'Light Snow', 4: 'Heavy Rain'}
    day_df['weathersit'] = day_df['weathersit'].map(weather_labels)
    rentals_by_weather = day_df.groupby('weathersit')['cnt']
    stats = pd.DataFrame({
        'Mean': rentals_by_weather.mean(),
        'Median' : rentals_by_weather.median(),
        'Mode' : rentals_by_weather.apply(lambda x: x.mode().iloc[0]),
        'Max' : rentals_by_weather.max(),
        'Min' : rentals_by_weather.min(),
        'Total' : rentals_by_weather.sum()    
    }).reset_index()
    st.write("- Jumlah Penyewaan sepeda berdasarkan cuaca dari data day_df: ")
    st.table(stats)
    
    season_labels = {1: 'springer', 2: 'summer', 3: 'fall', 4: 'winter'}
    day_df['season'] = day_df['season'].map(season_labels)
    rentals_by_season = day_df.groupby('season')['cnt']
    stats = pd.DataFrame({
        'Mean': rentals_by_season.mean(),
        'Median' : rentals_by_season.median(),
        'Mode' : rentals_by_season.apply(lambda x: x.mode().iloc[0]),
        'Max' : rentals_by_season.max(),
        'Min' : rentals_by_season.min(),
        'Total' : rentals_by_season.sum()    
    }).reset_index()
    st.write("- Jumlah Penyewaan sepeda berdasarkan musim dari data day_df: ")
    st.table(stats)
    
    st.write("- Pengaruh variabel lain (temp, hum, winspeed) dan visbilitas terhadap jumlah penyewaan sepeda ")
    fig, ax = plt.subplots()
    select_columns =['temp', 'hum', 'windspeed', 'cnt']
    subset_data = day_df[select_columns]
    numerical_data = day_df.select_dtypes(include=['float64', 'int64'])
    correlaction_matrix = subset_data.corr()
    st.write("Matriks Korelasi : ")
    st.write(subset_data.corr())
     
    comparison = day_df.groupby('yr')['cnt'].agg(['mean', 'sum', 'median', 'count']).reset_index()
    comparison['yr'] = comparison['yr'].replace({0:"2011", 1:"2012"})
    st.write("- Perbandingan Penyewaan Sepeda berdasarkan Tahun :")
    st.dataframe(comparison)
    
    st.markdown(
        "<h2 style='font-size:20px;'>Insight 💡</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
    """ 
    - Dari data demografi tersebut kami dapatkan bahwa cuaca cerah menghasilkan total penyewaan terbanyak diikuti cuaca berkabut kemudian yang selanjutnya cuaca bersalju. <br>
    - Dari data demografi tersebut kami dapatkan bahwa dari ke 4 musim yang menyumbang total penyewaan terbanyak yakni di musim gugur diikuti musim panas, musim dingin dan musim semi. <br>
    - Dari Matriks Korelasi didapatkan bahwa temperatur menunjukan hubungan positif yang sedang. <br>
    - Dari Tabel Perbandingan penyewaan sepeda, didapatkan bahwa dari aspek rata-rata maupun total penyewaan tertinggi pada tahun 2012. <br>
    """,unsafe_allow_html=True 
    )
    
elif selected == "Data Visualization & Explanatory Analysis":
    st.title("📊 Visualization & Explanatory Analysis Bike Sharing 🚲")
    col1, col2 = st.columns(2)
    
    with col1:
        fig, ax = plt.subplots()
        bins = [0.5, 1.5, 2.5, 3.5, 4.5]
        bar_width = 0.8
        plt.hist(day_df['season'], width=bar_width, bins=bins, color='skyblue', alpha=0.7)
        plt.title('Histogram of Season')
        plt.xlabel('Season')
        plt.ylabel('Frequency')
        plt.xticks([1, 2, 3, 4], ['Springer', 'Summer', 'Fall', 'Winter'])
        plt.show()
        st.pyplot(fig)
        
        fig, ax = plt.subplots()
        bins = [0.5, 1.5, 2.5, 3.5]
        bar_width = 0.8
        plt.hist(day_df['weathersit'], width=bar_width, bins=bins, color='grey', edgecolor='white', alpha=0.7)
        plt.title('Histogram of Weathersit')
        plt.xlabel('Weathersit')
        plt.ylabel('Frequency')
        plt.xticks([1, 2, 3], ['Clear', 'Mist', 'Light Snow'])
        _ = plt.legend(loc='upper right')
        plt.gca().set_facecolor('lavender')
        plt.gcf().set_facecolor('white')
        plt.show()
        st.pyplot(fig)
        
        comparison = day_df.groupby('yr')['cnt'].agg(['mean', 'sum', 'count']).reset_index()
        comparison['yr'] = comparison['yr'].replace({0:"2011", 1:"2012"})
        fig, ax = plt.subplots()
        ax.bar(comparison['yr'], comparison['sum'], color=['blue', 'orange'], label='Total Penyewaan')
        ax.set_title("Total Bike Rentals : 2011 vs 2012", fontsize=14)
        ax.set_xlabel("Year", fontsize=12)
        ax.set_ylabel("Total Bike Rental", fontsize=12)
        ax.legend()
        st.pyplot(fig)
        
        day_df['dteday'] = pd.to_datetime(day_df['dteday'])
        day_df = day_df.sort_values(by='dteday')
        day_df['rolling_mean'] = day_df['cnt'].rolling(window=7).mean()
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(day_df['dteday'], day_df['cnt'], color='grey', alpha=0.5, label='Daily Count')
        ax.plot(day_df['dteday'], day_df['rolling_mean'], color='blue', linewidth=2, label='7-Day Rolling Mean')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Bike Rental Count', fontsize=12)
        ax.set_title('Trend of Bike Rentals Over Time', fontsize=14)
        ax.legend()
        ax.grid(True)

        # Rotasi label tanggal agar terlihat jelas
        plt.xticks(rotation=45)

        # Tampilkan grafik
        plt.show()
        st.pyplot(fig)
        
    with col2: 
        fig, ax = plt.subplots()
        sns.boxplot(x='season', y='cnt', data=day_df, palette="coolwarm")
        plt.xlabel('Season')
        plt.ylabel('Bike Rentals Count', size=15)
        ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter']) 
        _ = plt.title('Bike Rentals by Season')
        st.pyplot(fig)

        fig, ax = plt.subplots()
        sns.scatterplot(x="temp", y="cnt", data=day_df)
        plt.title("Bike Rentals vs Temperature")
        plt.xlabel("Temperature(°C)")
        plt.ylabel("Bike Rental Count")
        plt.show()
        st.pyplot(fig)
        
       
        comparison = day_df.groupby('yr')['cnt'].agg(['mean', 'sum', 'count']).reset_index()
        comparison['yr'] = comparison['yr'].replace({0:"2011", 1:"2012"})
        fig, ax = plt.subplots()
        ax.bar(comparison['yr'], comparison['mean'], color=['green', 'red'], label='Average')
        ax.set_title("Average Bike Bentals : 2011 vs 2012", fontsize=14)
        ax.set_xlabel("Year", fontsize=12)
        ax.set_ylabel("Average", fontsize=12)
        ax.legend()
        st.pyplot(fig)
        
        fig, ax = plt.subplots()
        select_columns =['temp', 'hum', 'windspeed', 'cnt']
        subset_data = day_df[select_columns]
        numerical_data = day_df.select_dtypes(include=['float64', 'int64'])
        correlaction_matrix = subset_data.corr()
        sns.heatmap(correlaction_matrix, annot=True, cmap="coolwarm", fmt='.2f', linewidths=0.5)
        plt.title('Correlation Matrix')
        plt.show()
        st.pyplot(fig)
        
    st.markdown(
    "<h2 style='font-size:20px;'>Insight 💡</h1>",
    unsafe_allow_html=True
    )
    st.markdown(
    """ 
    - Pada hasil analisis data, grafik boxplot menunjukan bahwa performa tertinggi pada musim gugur (Fall) hal ini dapat dilihat dari jumlah unit sebanyak 5.353 unit, juga median yang lebih tinggi dari musim lainnya.
      Pada Musim Summer dan Fall memiliki penyebaran data yang lebih lebar, menunjukkan variabilitas yang lebih tinggi dalam jumlah penyewaan sepeda sedangkan 
      pada Musim Spring dan Winter memiliki penyebaran data yang lebih sempit, menunjukkan bahwa jumlah penyewaan lebih konsisten.
      sehingga dapat disimpulkan jika musim mempengaruhi jumlah penyewaan sepeda. <br>

    - Pada hasil analisis dan grafik diatas, menunjukan bahwa cuaca cerah (Clear) merupakan faktor tertinggi pada jumlah 
      penyewaan sepeda mencapai angka 4.876 unit, kemudian diikuti cuaca berkabut (Mist) dengan 4.035 unit dan bersalju (Light Rain) 1.803 unit. 
      Selain itu juga perbedaan pada jumlah penyewaan sepeda tidak terlalu signifikan untuk cuaca cerah dan berkabut, berbeda hal nya dengan cuaca bersalju 
      yang mengalami perbedaan cukup signifikan yang bisa disebabkan suhu udara dan kelembapan yang tinggi. 
      bisa kita cermati bahwa cuaca cerah (Clear) merupakan waktu yang lebih banyak disukai oleh orang-orang untuk menggunakan sepeda dalam beraktivitas.
      Hal ini dapat disimpulkan bahwa kondisi cuaca sangat berpengaruh terhadap jumlah penyewaan sepeda. <br>
      
    - Berdasarkan metriks korelasi menunjukan bahwa hubungan antara temperatur dan jumlah penyewaan sepeda berada di angka 0.63 yang artinya memiliki hubungan positif.
      Hal ini juga didukung dengan scatter diagram atau diagram tebar membentuk pola yang cenderung naik kekanan dan sebaran yang merapat sehingga dapat disimpulkan bahwa 
      temperatur memiliki hubungan positif dengan jumlah penyewaan sepeda. <br>  
    
    - Pada Grafik Bar perbandingan antara periode 2011 dan 2012 berdasarkan dua parameter yaitu total dan average menunjukan bahwa tahun 2012 merupakan yang tertinggi dalam penyewaan sepeda.
    
    - Pada Periode 2011 hingga 2012 grafik tren penyewaan sepeda mengalami peningkatan yang konsisten terutama dilihat dari akumulasi nya.
      Namun terlihat adanya penurunan signifikan pada bulan oktober di kedua tahun tersebut dan bisa saja terjadi karena cuaca atau kegiatan-kegiatan akhir tahun.
      
    """,
    unsafe_allow_html=True 
        )
        

        
