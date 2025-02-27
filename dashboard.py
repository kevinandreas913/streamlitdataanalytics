import streamlit as st 
import datetime
import pandas as pd  #digunakan untuk data tabel agar data mudah diolah
import matplotlib.pyplot as plt #digunakan untuk visualisasi data
import sklearn.cluster as cls #digunakan untuk proses cluster
from sklearn.preprocessing import MinMaxScaler #digunakan untuk normalisasi atribut
import numpy as np #digunakan untuk perhitungan outlier 
import seaborn as sns #digunakan untuk matriks kolerasi

st.title("Proyek Analisis Data: [Bike Sharing Dataset]")
st.write(
    """
    Nama: Andreas Kevin  
    Email: Kevinandreas913@gmail.com  
    ID Dicoding: andreas_kevin_6396  
    """
)
st.write("""
    Pertanyaan bisnis:  
    - Bagaimana perkembangan tingkat penyewaan pada 30 hari belakang berdasarkan total semua penyewa (registrasi dan casual)?  
    - Berdasarkan penyewa casual dan registered, berapa persentase penyewa dari casual dan registered?
""")

st.header("Data Wrangling")
st.write("Data wrangling merupakan sebuah proses atau kumpulan kegiatan yang meliputi pengumpulan data (Gathering data), penilaian data (Assessing data), serta pembersihan data (Cleaning data)")



st.subheader("Gathering data")
st.write("""
    Gathering data merupakan proses pengumpulan data!  
    Pada contoh kasus ini, pegumpulan data dilakukan dengan data "Bike Sharing Dataset"
""")
# st.markdown("Masukkan file csv anda disini!")
# st.write("""
#     1. file csv harus bernama "day.csv".  
#     2. file harus berformat csv.
# """)
# uploaded_file = st.file_uploader("upload file anda!", type="csv")

# if uploaded_file is None:
#     st.stop()

# if uploaded_file.name != "day.csv" or not uploaded_file.name.endswith(".csv"):
#     st.write("Masukkan ulang data, data tidak sesuai. Pastikan untuk saat ini anda menggunakan data day.csv")
#     st.stop()

st.success("Data berhasil dibaca!")
df_day = pd.read_csv("day.csv", sep=",")
st.dataframe(df_day)



st.subheader("Assesing Data")
st.write("""
    Assesing data merupakan proses penilaian data!  
    Pada contoh kasus ini, penilaian data akan berdasarkan:  
    1. Jumlah duplikasi pada data  
    2. Jumlah data kosong  
    3. Analisis statistik  
    4. Pembacaan info data  
    5. Perkiraan outlier berdasarkan Q1 dan Q2  
    6. Box plot untuk visualisasi point 5  
""")
st.write(f"**1. Jumlah duplikasi: {df_day.duplicated().sum()}**")
st.write("**2. jumlah data kosong:**")
st.write(df_day.isnull().sum())
st.write("**3. Pembacaan data statistik**")
st.dataframe(df_day.describe())

st.write("**4. Pembacaan info data**")
info_df = pd.DataFrame({
    "Column": df_day.columns,
    "Non-Null Count": df_day.notnull().sum(),
    "Data Type": df_day.dtypes.astype(str)
})
st.dataframe(info_df) 

def outlier(nama):
    q25, q75 = np.percentile(df_day[nama], 25), np.percentile(df_day[nama], 75)
    iqr = q75 - q25
    cut_off = iqr * 1.5
    minimum, maximum = q25 - cut_off, q75 + cut_off
     
    outlier = [x for x in df_day[nama] if x < minimum or x > maximum]
    return outlier

st.write("**5. Perkiraan outlier berdasarkan Q1 dan Q3**")
st.write(f"Adapun outlier pada atribut weathersit : {outlier("weathersit")}")
st.write(f"Adapun outlier pada atribut temp : {outlier("temp")}")
st.write(f"Adapun outlier pada atribut atemp : {outlier("atemp")}")
st.write(f"Adapun outlier pada atribut hum : {outlier("hum")}")
st.write(f"Adapun outlier pada atribut windspeed : {outlier("windspeed")}")
st.write(f"Adapun outlier pada atribut casual : {outlier("casual")}")
st.write(f"Adapun outlier pada atribut registered : {outlier("registered")}")

st.write("**6. Box plot untuk visualisasi point 5**")
def boxplot(name):
    fig, axisboxplot = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_day[[name]], ax=axisboxplot)
    st.pyplot(fig) 

boxplot_columns = ["weathersit", "temp", "atemp", "hum", "windspeed", "casual", "registered"]

for col in boxplot_columns:
    st.write(f"**Boxplot untuk {col}:**")
    boxplot(col)



st.subheader("Cleaning Data")
st.write("""
    Cleaning data merupakan proses pembersihan data yang dilakukan untuk mengatasi kesalahan, missing value, outlier, dan lainnya.  
    Pada contoh kasus ini, cleaning data dilakukan dengan:  
    1. Mengubah tipe data "dteday" yang harusnya adalah date
    2. Menghapus outlier
    3. Kolerasi heatmap
""")

st.write("**1. Mengubah tipe data dteday yang harusnya adalah date**")
df_day['dteday'] = pd.to_datetime(df_day['dteday']) 
info_df = pd.DataFrame({
    "Column": df_day.columns,
    "Non-Null Count": df_day.notnull().sum(),
    "Data Type": df_day.dtypes.astype(str)
})
st.dataframe(info_df) 


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

st.write("**2. Menghapus outlier**")
st.write(f"Jumlah data sebelum menghapus outlier: {len(df_day)}")
st.write(f"Jumlah data setelah menghapus outlier: {len(df_day_clean)}")
df_day = df_day_clean 

st.write("**3. Visualisasi heatmap**")
fig, axheatmap = plt.subplots(figsize=(10, 6))
sns.heatmap(df_day.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=axheatmap)
st.pyplot(fig)


st.subheader("EDA (Exploratory Data Analysis)")
st.write("""
    Exploratory Data Analysis (EDA) merupakan tahap eksplorasi data yang telah dibersihkan guna memperoleh insight dan menjawab pertanyaan analisis.  
    Pada contoh kasus ini, Pengguna dapat memilih proses eda yang akan dimunculkan:
""")

with st.form(key="form1"):
    pilihan1 = st.selectbox(
        "Pilih atribut",
        ["season", "yr", "holiday", "weekday", "workingday"],
        key="option1"
    )
    submit_button_EDA = st.form_submit_button(label="Submit")

if submit_button_EDA:
    st.write(f"Anda memilih atribut: **{pilihan1}**")

    EDA = df_day.groupby(by=pilihan1).agg({
        "cnt": ["sum", "max", "min", "mean", "std"]
    })

    st.write("**Hasil Agregasi**")
    st.dataframe(EDA)

with st.form(key="form2"):
    date = st.date_input("Masukkan tanggal!", datetime.date(2011, 1, 1))
    submit_button_tanggal = st.form_submit_button(label="Submit")

if submit_button_tanggal:
    selected_date = date.strftime("%Y-%m-%d")

    processdate = df_day[df_day["dteday"] == selected_date].groupby("dteday").agg({
        "casual": ["sum"],
        "registered": ["sum"],
        "cnt": ["sum"]
    })

    if processdate.empty:
        st.warning(f"Tidak ada data untuk tanggal {selected_date}.")
    else:
        st.write(f"Anda memilih tanggal: **{selected_date}**")
        st.write("**Hasil Agregasi**")
        st.dataframe(processdate)



st.subheader("Visualization & Explanatory Analysis")
st.write("""
    data visualization merupakan tahapan yang harus kita lakukan sebelum membuat kesimpulan dan mengomunikasikan (draw conclusion & communicate) hasil dari proses analisis yang telah dilakukan.
""")
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

st.write(""" """)
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


st.subheader("Analisis Lanjutan (Clustering)")
st.write("""
    clustering merupakan tahap yang digunakan untuk mengkumpulkan data yang berbeda menjadi beberapa kelompok yang menjadi lebih rapi dan jelas.  
    Pada contoh kasus ini, clustering dilakukan:  
    1. Pengambilan pengelompokkan diambil temp, atemp didasarkan pada kolerasi matrik yang terliht kaitan kuat antara atemp dan temp dengan cnt (total penyewaan).
    2. Ini berarti bahwa seorang dapat menentukan total penyewaan mereka berdasarkan kondisi temp dan atemp setempat.
""")
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

st.dataframe(df_day[["temp_category", "atemp_category", "usage_category"]])

st.header("Conclusion")
st.write("""
    - Pada pertanyaan "Bagaimana perkembangan tingkat penyewaan pada 30 hari belakang berdasarkan total semua penyewa (registrasi dan casual)?" Berdasarkan proses EDA yang dilakukan, penulis berusaha menemukan pergerakkan penyewaan yang dibuktikan dari proses EDA dari atribut "holiday, weekday, workingday, dan mnth" terhadap cnt. Penulis memperoleh pemahaman bahwa berdasarkan atribut cnt tersebut terlihat adanya tingkat penurunan yang terjadi. Penurunan signifikan terlihat pada mnth 12 yang terlihat pada cnt yang semakin menurun. Penulis kemudian melakukan visualisasi untuk membuktikan bahwa pada bulan 12 atau 30 hari belakang menunjukakn penurunan. Berdasarkan visualisasi data yang dimunculkan, terlihat jelas pada bulan 12 terdapat nilai cnt terendah yang hanya mencapai 441.  
    - Pada pertanyaan "Berdasarkan penyewa casual dan registered, berapa persentase penyewa dari casual dan registered?", penulis menggali informasi dari persentase atas penyewaan casual dan registered. Berdasarkan nilai persentase yang dihasilkan, penyewa registered melakukan penyewaan yang lebih tinggi dibandingkan penyewa casual. Ini memberikan pemahaman bahwa peningkatan promosi untuk registered akan lebih menguntungkan karena berdasarkan persentase yang dihasilkan, penyewa registered memiliki persentasi 83% sedangkan pada penyewa casual hanya di angka 17%.
""")