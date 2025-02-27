import streamlit as st 
import datetime
import pandas as pd  #digunakan untuk data tabel agar data mudah diolah
import matplotlib.pyplot as plt #digunakan untuk visualisasi data
import sklearn.cluster as cls #digunakan untuk proses cluster
from sklearn.preprocessing import MinMaxScaler #digunakan untuk normalisasi atribut

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
st.markdown("Masukkan file csv anda disini!")
st.write("""
    1. file csv harus bernama "day.csv".  
    2. file harus berformat csv.
""")
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
    2. Analisis statistik  
    3. Pembacaan info data
""")
st.write(f"Jumlah duplikasi: {df_day.duplicated().sum()}")

st.write("Pembacaan data statistik")
st.dataframe(df_day.describe())

st.write("Pembacaan info data")
info_df = pd.DataFrame({
    "Column": df_day.columns,
    "Non-Null Count": df_day.notnull().sum(),
    "Data Type": df_day.dtypes.astype(str)
})
st.dataframe(info_df) 



st.subheader("Cleaning Data")
st.write("""
    Cleaning data merupakan proses pembersihan data yang dilakukan untuk mengatasi kesalahan, missing value, outlier, dan lainnya.  
    Pada contoh kasus ini, cleaning data dilakukan dengan:  
    1. Mengubah tipe data "dteday" yang harusnya adalah date
""")
df_day['dteday'] = pd.to_datetime(df_day['dteday']) 
info_df = pd.DataFrame({
    "Column": df_day.columns,
    "Non-Null Count": df_day.notnull().sum(),
    "Data Type": df_day.dtypes.astype(str)
})
st.dataframe(info_df) 



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

st.subheader("Visualization & Explanatory Analysis")
st.write("""
    data visualization merupakan tahapan yang harus kita lakukan sebelum membuat kesimpulan dan mengomunikasikan (draw conclusion & communicate) hasil dari proses analisis yang telah dilakukan.
""")


st.subheader("Analisis Lanjutan (Clustering)")
st.write("""
    clustering merupakan tahap yang digunakan untuk mengkumpulkan data yang berbeda menjadi beberapa kelompok yang menjadi lebih rapi dan jelas.  
    Pada contoh kasus ini, clustering dilakukan:  
    1. Berdasarkan data penyewa casual dan registered menjadi 2 kelompok yaitu penyewaan ramai dan sepi.  
    2. Berdasarkan weathersit, temp, atemp, hum, windspeed, dan cnt dibagi menjadi 2 yaitu penyewaan ramai dan sepi.
""")
def kmeans_clustering(df, n_clusters=2):
    df_cluster = df[['casual', 'registered']].copy() 
    proseskmeans = cls.KMeans(n_clusters=n_clusters)

    proseskmeans.fit(df_cluster)
    df_cluster["labelcluster"] = proseskmeans.labels_

    centroids = proseskmeans.cluster_centers_
    centroid_X = centroids[:, 0]
    centroid_Y = centroids[:, 1]

    figcluster, axiscluster = plt.subplots(figsize=(8, 5))
    axiscluster.scatter(df_cluster["casual"], df_cluster["registered"], c=df_cluster["labelcluster"], cmap="viridis", alpha=0.5)
    axiscluster.scatter(centroid_X, centroid_Y, color="black", marker="X", s=200, label="Centroids")
    axiscluster.set_xlabel("Casual Users")
    axiscluster.set_ylabel("Registered Users")
    axiscluster.set_title("K-Means Clustering of Bike Rentals")
    axiscluster.legend()

    return df_cluster, figcluster

def kmeans_clustering_normalized(df, n_clusters=2):
    scaler = MinMaxScaler()
    df["cnt_minmax"] = scaler.fit_transform(df[["cnt"]]) 

    df_cluster2 = df[["temp", "atemp", "hum", "windspeed", "cnt_minmax"]].copy()

    proseskmeans = cls.KMeans(n_clusters=n_clusters)
    proseskmeans.fit(df_cluster2)

    df_cluster2["labelcluster"] = proseskmeans.labels_
    
    return df_cluster2

df_cluster, figcluster = kmeans_clustering(df_day, n_clusters=2)
st.subheader("Hasil Clustering penyewa casual dan registered menjadi 2 kelompok yaitu penyewaan ramai dan sepi")
st.dataframe(df_cluster) 
st.pyplot(figcluster)

df_cluster2= kmeans_clustering_normalized(df_day, n_clusters=2)
st.subheader("Hasil clustering weathersit, temp, atemp, hum, windspeed, dan cnt dibagi menjadi 2 yaitu penyewaan ramai dan sepi.")
st.dataframe(df_cluster2)

st.header("Conclusion")
st.write("""
    - Pada pertanyaan "Bagaimana perkembangan tingkat penyewaan pada 30 hari belakang berdasarkan total semua penyewa (registrasi dan casual)?" Berdasarkan proses EDA yang dilakukan, penulis berusaha menemukan pergerakkan penyewaan yang dibuktikan dari proses EDA dari atribut "holiday, weekday, workingday, dan mnth" terhadap cnt. Penulis memperoleh pemahaman bahwa berdasarkan atribut cnt tersebut terlihat adanya tingkat penurunan yang terjadi. Penurunan signifikan terlihat pada mnth 12 yang terlihat pada cnt yang semakin menurun. Penulis kemudian melakukan visualisasi untuk membuktikan bahwa pada bulan 12 atau 30 hari belakang menunjukakn penurunan. Berdasarkan visualisasi data yang dimunculkan, terlihat jelas pada bulan 12 terdapat nilai cnt terendah yang hanya mencapai 441.  
    - Pada pertanyaan "Berdasarkan penyewa casual dan registered, berapa persentase penyewa dari casual dan registered?", penulis menggali informasi dari persentase atas penyewaan casual dan registered. Berdasarkan nilai persentase yang dihasilkan, penyewa registered melakukan penyewaan yang lebih tinggi dibandingkan penyewa casual. Ini memberikan pemahaman bahwa peningkatan promosi untuk registered akan lebih menguntungkan karena berdasarkan persentase yang dihasilkan, penyewa registered memiliki persentasi 81,2% sedangkan pada penyewa casual hanya di angka 18,8%. 
""")