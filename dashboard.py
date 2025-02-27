# import streamlit as st 
# import datetime
# import pandas as pd  #digunakan untuk data tabel agar data mudah diolah
# import matplotlib.pyplot as plt #digunakan untuk visualisasi data
# import sklearn.cluster as cls #digunakan untuk proses cluster
# from sklearn.preprocessing import MinMaxScaler #digunakan untuk normalisasi atribut
# import numpy as np #digunakan untuk perhitungan outlier 
# import seaborn as sns #digunakan untuk matriks kolerasi

# st.title("Proyek Analisis Data: [Bike Sharing Dataset]")
# st.write(
#     """
#     Nama: Andreas Kevin  
#     Email: Kevinandreas913@gmail.com  
#     ID Dicoding: andreas_kevin_6396  
#     """
# )
# st.write("""
#     Pertanyaan bisnis:  
#     - Bagaimana perkembangan tingkat penyewaan pada 30 hari belakang berdasarkan total semua penyewa (registrasi dan casual)?  
#     - Berdasarkan penyewa casual dan registered, berapa persentase penyewa dari casual dan registered?
# """)

# st.success("Data berhasil dibaca!")
# df_day = pd.read_csv("day.csv", sep=",")
# st.dataframe(df_day)

# df_day['dteday'] = pd.to_datetime(df_day['dteday']) 

# def remove_outliers(df, columns):
#     df_clean = df.copy() 
#     for col in columns:
#         q25, q75 = np.percentile(df_clean[col], 25), np.percentile(df_clean[col], 75)
#         iqr = q75 - q25
#         cut_off = iqr * 1.5
#         minimum, maximum = q25 - cut_off, q75 + cut_off

#         df_clean = df_clean[(df_clean[col] >= minimum) & (df_clean[col] <= maximum)]
    
#     return df_clean

# columns_with_outliers = ["weathersit", "temp", "atemp", "hum", "windspeed", "casual", "registered"]
# df_day_clean = remove_outliers(df_day, columns_with_outliers)

# df_day = df_day_clean 


# min_date = df_day["dteday"].min()
# max_date = df_day["dteday"].max()
 
# with st.sidebar:    
#     start_date, end_date = st.date_input(
#         label='Rentang Waktu',min_value=min_date,
#         max_value=max_date,
#         value=[min_date, max_date]
#     )

# df_filtered = df_day[(df_day["dteday"] >= pd.to_datetime(start_date)) & (df_day["dteday"] <= pd.to_datetime(end_date))]

# st.write(f"### Data Penyewaan dari {start_date} hingga {end_date}")
# if df_filtered.empty:
#     st.warning("Tidak ada data dalam rentang tanggal yang dipilih.")
# else:
#     st.dataframe(df_filtered)

# with st.form(key="form1"):
#     pilihan1 = st.selectbox(
#         "Pilih atribut untuk melihat data mengenai atribut tersebut berdasarkan penyewaan",
#         ["season", "yr", "holiday", "weekday", "workingday"],
#         key="option1"
#     )
#     submit_button_EDA = st.form_submit_button(label="Submit")

# if submit_button_EDA:
#     st.write(f"Anda memilih atribut: **{pilihan1}**")

#     EDA = df_day.groupby(by=pilihan1).agg({
#         "cnt": ["sum", "max", "min", "mean", "std"]
#     })

#     st.write("**Hasil Agregasi**")
#     st.dataframe(EDA)

# with st.form(key="form2"):
#     date = st.date_input("Masukkan tanggal untuk melihat penyewaan yang terjadi di tanggal tersebut!", datetime.date(2011, 1, 1))
#     submit_button_tanggal = st.form_submit_button(label="Submit")

# if submit_button_tanggal:
#     selected_date = date.strftime("%Y-%m-%d")

#     processdate = df_day[df_day["dteday"] == selected_date].groupby("dteday").agg({
#         "casual": ["sum"],
#         "registered": ["sum"],
#         "cnt": ["sum"]
#     })

#     if processdate.empty:
#         st.warning(f"Tidak ada data untuk tanggal {selected_date}.")
#     else:
#         st.write(f"Anda memilih tanggal: **{selected_date}**")
#         st.write("**Hasil Agregasi**")
#         st.dataframe(processdate)


# st.write("**Bagaimana perkembangan tingkat penyewaan pada 30 hari belakang berdasarkan total semua penyewa (registrasi dan casual)?**")
# tanggal = df_day["dteday"][-30:] 
# cnt = df_day["cnt"][-30:] 

# fig, axis = plt.subplots(figsize=(10, 5))
# axis.set_title("Grafik Tingkat Penyewaan oleh Registered dan Casual")
# axis.plot(
#     tanggal,
#     cnt,
#     linewidth = 2,
#     color = "black",
#     marker="o"
# )
# for x, y in zip(tanggal, cnt):
#     axis.text(x, y, str(y), fontsize=10, ha="right", va="bottom")
# axis.set_xlabel("Date") 
# axis.set_ylabel("Penyewa") 
# axis.set_xticklabels(tanggal, rotation=45)
# st.pyplot(fig)

# st.write(""" """)
# st.write("**Berdasarkan penyewa casual dan registered, berapa persentase penyewa dari casual dan registered?**")
# keterangan = ["casual", "registered"] 

# def persencasualregistered():
#     casual = df_day["casual"].values
#     sumcasual = sum(casual) 
#     registered = df_day["registered"].values 
#     sumregistered = sum(registered) 
#     totalcasual_registered = sumcasual + sumregistered 
#     persencasual= sumcasual / totalcasual_registered * 100 
#     persenregistered = sumregistered / totalcasual_registered * 100 
#     return persencasual, persenregistered

# persencasual, persenregistered = persencasualregistered()
# nilai = [persencasual, persenregistered] 
# fig2, axis2 =plt.subplots(figsize=(10,5))
# axis2.set_title("Persentase penyewaan berdasarkan casual dan registered")
# axis2.pie(
#     labels=keterangan,
#     x=nilai,
#     autopct='%1.1f%%',
#     colors= ["red", "blue"]
# )
# st.pyplot(fig2)


# st.subheader("Analisis Lanjutan (Clustering)")

# st.write("**Visualisasi heatmap**")
# fig, axheatmap = plt.subplots(figsize=(10, 6))
# sns.heatmap(df_day_clean.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=axheatmap)
# st.pyplot(fig)

# st.write("""
#     Pada contoh kasus ini, clustering dilakukan:  
#     1. Pengambilan pengelompokkan diambil temp, atemp didasarkan pada kolerasi matriks heatmap yang terliht kaitan kuat antara atemp dan temp dengan cnt (total penyewaan).
#     2. Ini berarti bahwa seorang dapat menentukan perkiraan prediksi penyewaan mereka berdasarkan kondisi temp dan atemp setempat.
# """)
# def categorize_temp(temp):
#     q1_temp = df_day["temp"].quantile(0.25)
#     q3_temp = df_day["temp"].quantile(0.75)
#     if temp < q1_temp:
#         return "Cold"
#     elif temp > q3_temp:
#         return "Hot"
#     else:
#         return "Medium"

# def categorize_atemp(atm):
#     q1_atemp = df_day["atemp"].quantile(0.25)
#     q3_atemp = df_day["atemp"].quantile(0.75)
#     if atm < q1_atemp:
#         return "Low"
#     elif atm > q3_atemp:
#         return "Medium"
#     else:
#         return "High"

# def categorize_riders(cnt):
#     if cnt < 900:
#         return "Low Usage"
#     elif 900 <= cnt < 1200:
#         return "Medium Usage"
#     else:
#         return "High Usage"

# df_day["temp_category"] = df_day["temp"].apply(categorize_temp)
# df_day["atemp_category"] = df_day["atemp"].apply(categorize_atemp)
# df_day["usage_category"] = df_day["cnt"].apply(categorize_riders)

# st.dataframe(df_day[["temp_category", "atemp_category", "usage_category"]])

# st.header("Conclusion")
# st.write("""
#     - Pada pertanyaan "Bagaimana perkembangan tingkat penyewaan pada 30 hari belakang berdasarkan total semua penyewa (registrasi dan casual)?" Berdasarkan proses EDA yang dilakukan, penulis berusaha menemukan pergerakkan penyewaan yang dibuktikan dari proses EDA dari atribut "holiday, weekday, workingday, dan mnth" terhadap cnt. Penulis memperoleh pemahaman bahwa berdasarkan atribut cnt tersebut terlihat adanya tingkat penurunan yang terjadi. Penurunan signifikan terlihat pada mnth 12 yang terlihat pada cnt yang semakin menurun. Penulis kemudian melakukan visualisasi untuk membuktikan bahwa pada bulan 12 atau 30 hari belakang menunjukakn penurunan. Berdasarkan visualisasi data yang dimunculkan, terlihat jelas pada bulan 12 terdapat nilai cnt terendah yang hanya mencapai 441.  
#     - Pada pertanyaan "Berdasarkan penyewa casual dan registered, berapa persentase penyewa dari casual dan registered?", penulis menggali informasi dari persentase atas penyewaan casual dan registered. Berdasarkan nilai persentase yang dihasilkan, penyewa registered melakukan penyewaan yang lebih tinggi dibandingkan penyewa casual. Ini memberikan pemahaman bahwa peningkatan promosi untuk registered akan lebih menguntungkan karena berdasarkan persentase yang dihasilkan, penyewa registered memiliki persentasi 83% sedangkan pada penyewa casual hanya di angka 17%.
# """)

import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(layout="wide")
st.title("Proyek Analisis Data: [Bike Sharing Dataset]")

with st.sidebar:
    st.write("""
             **Nama: Andreas Kevin**  
             **Email: Kevinandreas913@gmail.com**  
             **ID Dicoding: andreas_kevin_6396**  
             """)

df_day = pd.read_csv("day.csv", sep=",")
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

st.success("Data berhasil dibaca!")
st.dataframe(df_day)

def remove_outliers(df, columns):
    df_clean = df.copy()
    for col in columns:
        q25, q75 = np.percentile(df_clean[col], 25), np.percentile(df_clean[col], 75)
        iqr = q75 - q25
        cut_off = iqr * 1.5
        minimum, maximum = q25 - cut_off, q75 + cut_off
        df_clean = df_clean[(df_clean[col] >= minimum) & (df_clean[col] <= maximum)]
    return df_clean

columns_with_outliers = ["weathersit", "temp", "atemp", "hum", "windspeed", "casual", "registered"]
df_day_clean = remove_outliers(df_day, columns_with_outliers)

df_day = df_day_clean

min_date, max_date = df_day["dteday"].min(), df_day["dteday"].max()
with st.sidebar:
    start_date, end_date = st.date_input("Rentang Waktu", min_value=min_date, max_value=max_date, value=[min_date, max_date])
df_filtered = df_day[(df_day["dteday"] >= pd.to_datetime(start_date)) & (df_day["dteday"] <= pd.to_datetime(end_date))]

# Layout
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.write(f"### Data Penyewaan dari {start_date} hingga {end_date}")
    if df_filtered.empty:
        st.warning("Tidak ada data dalam rentang tanggal yang dipilih.")
    else:
        st.dataframe(df_filtered)

with col2:
    with st.expander("Lihat Agregasi Data"):
        pilihan1 = st.selectbox("Pilih atribut untuk melihat data penyewaan", ["season", "yr", "holiday", "weekday", "workingday"], key="option1")
        EDA = df_day.groupby(by=pilihan1).agg({"cnt": ["sum", "max", "min", "mean", "std"]})
        st.dataframe(EDA)
    with st.expander("Lihat Agregasi Penyewaan Berdasarkan Tanggal"):
        date = st.date_input("Masukkan tanggal untuk melihat penyewaan yang terjadi di tanggal tersebut!", datetime.date(2011, 1, 1))
        
        processdate = df_day[df_day["dteday"] == date.strftime("%Y-%m-%d")].groupby("dteday").agg({
            "casual": ["sum"],
            "registered": ["sum"],
            "cnt": ["sum"]
        })

        if processdate.empty:
            st.warning(f"Tidak ada data untuk tanggal {date.strftime('%Y-%m-%d')}.")
        else:
            st.write(f"Anda memilih tanggal: **{date.strftime('%Y-%m-%d')}**")
            st.dataframe(processdate)

with col3:
    st.write("**Bagaimana perkembangan tingkat penyewaan pada 30 hari belakang berdasarkan total semua penyewa (registrasi dan casual)?**")
    tanggal = df_day["dteday"][-30:] 
    cnt = df_day["cnt"][-30:] 

    fig, axis = plt.subplots(figsize=(10, 5))
    axis.set_title("Grafik Tingkat Penyewaan oleh Registered dan Casual")
    axis.plot(
        tanggal,
        cnt,
        linewidth = 2,
        color = "black",
        marker="o"
    )
    for x, y in zip(tanggal, cnt):
        axis.text(x, y, str(y), fontsize=10, ha="right", va="bottom")
    axis.set_xlabel("Date") 
    axis.set_ylabel("Penyewa") 
    axis.set_xticklabels(tanggal, rotation=45)
    st.pyplot(fig)

with col4:
    st.write("**Berdasarkan penyewa casual dan registered, berapa persentase penyewa dari casual dan registered?**")
    keterangan = ["casual", "registered"] 

    def persencasualregistered():
        casual = df_day["casual"].values
        sumcasual = sum(casual) 
        registered = df_day["registered"].values 
        sumregistered = sum(registered) 
        totalcasual_registered = sumcasual + sumregistered 
        persencasual= sumcasual / totalcasual_registered * 100 
        persenregistered = sumregistered / totalcasual_registered * 100 
        return persencasual, persenregistered

    persencasual, persenregistered = persencasualregistered()
    nilai = [persencasual, persenregistered] 
    fig2, axis2 =plt.subplots(figsize=(10,5))
    axis2.set_title("Persentase penyewaan berdasarkan casual dan registered")
    axis2.pie(
        labels=keterangan,
        x=nilai,
        autopct='%1.1f%%',
        colors= ["red", "blue"]
    )
    st.pyplot(fig2)


st.header("Conclusion")
st.write("""
    - Pada pertanyaan "Bagaimana perkembangan tingkat penyewaan pada 30 hari belakang berdasarkan total semua penyewa (registrasi dan casual)?" Berdasarkan proses EDA yang dilakukan, penulis berusaha menemukan pergerakkan penyewaan yang dibuktikan dari proses EDA dari atribut "holiday, weekday, workingday, dan mnth" terhadap cnt. Penulis memperoleh pemahaman bahwa berdasarkan atribut cnt tersebut terlihat adanya tingkat penurunan yang terjadi. Penurunan signifikan terlihat pada mnth 12 yang terlihat pada cnt yang semakin menurun. Penulis kemudian melakukan visualisasi untuk membuktikan bahwa pada bulan 12 atau 30 hari belakang menunjukakn penurunan. Berdasarkan visualisasi data yang dimunculkan, terlihat jelas pada bulan 12 terdapat nilai cnt terendah yang hanya mencapai 441.  
    - Pada pertanyaan "Berdasarkan penyewa casual dan registered, berapa persentase penyewa dari casual dan registered?", penulis menggali informasi dari persentase atas penyewaan casual dan registered. Berdasarkan nilai persentase yang dihasilkan, penyewa registered melakukan penyewaan yang lebih tinggi dibandingkan penyewa casual. Ini memberikan pemahaman bahwa peningkatan promosi untuk registered akan lebih menguntungkan karena berdasarkan persentase yang dihasilkan, penyewa registered memiliki persentasi 83% sedangkan pada penyewa casual hanya di angka 17%.
""")



st.subheader("Analisis Lanjutan (Clustering)")

with st.expander("Lihat Heatmap Korelasi"):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_title("Heatmap Korelasi", fontsize=14, fontweight="bold")
    sns.heatmap(df_day_clean.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

st.markdown(
    """
    **Clustering dilakukan berdasarkan:**  
    **Temp & Atemp**: Berdasarkan matriks korelasi, terdapat hubungan kuat antara temperatur dan jumlah penyewaan.  
    **Prediksi Penyewaan**: Dengan mengetahui temperatur setempat, dapat dilakukan estimasi terhadap jumlah penyewaan.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**Kategori Temperatur**")
    st.write("- **Cold**: Temp < Q1")
    st.write("- **Medium**: Q1 ≤ Temp ≤ Q3")
    st.write("- **Hot**: Temp > Q3")

with col2:
    st.info("**Kategori Atemp**")
    st.write("- **Low**: Atemp < Q1")
    st.write("- **Medium**: Atemp > Q3")
    st.write("- **High**: Q1 ≤ Atemp ≤ Q3")

with col3:
    st.info("**Kategori Penyewaan**")
    st.write("- **Low Usage**: cnt < 900")
    st.write("- **Medium Usage**: 900 ≤ cnt < 1200")
    st.write("- **High Usage**: cnt ≥ 1200")

# Tampilkan DataFrame hasil kategori
with st.expander("📋 Lihat Data Kategori Clustering"):
    def categorize_temp(temp):
        q1_temp = df_day["temp"].quantile(0.25)
        q3_temp = df_day["temp"].quantile(0.75)
        if temp < q1_temp:
            return "Cold"
        elif temp > q3_temp:
            return "Hot"
        else:
            return "Medium"

    def categorize_atemp(atm):
        q1_atemp = df_day["atemp"].quantile(0.25)
        q3_atemp = df_day["atemp"].quantile(0.75)
        if atm < q1_atemp:
            return "Low"
        elif atm > q3_atemp:
            return "Medium"
        else:
            return "High"

    def categorize_riders(cnt):
        if cnt < 900:
            return "Low Usage"
        elif 900 <= cnt < 1200:
            return "Medium Usage"
        else:
            return "High Usage"

    df_day["temp_category"] = df_day["temp"].apply(categorize_temp)
    df_day["atemp_category"] = df_day["atemp"].apply(categorize_atemp)
    df_day["usage_category"] = df_day["cnt"].apply(categorize_riders)

    st.dataframe(df_day[["dteday", "temp_category", "atemp_category", "usage_category"]])
