# **Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech**

### **Business Understanding**

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

---

### Permasalahan Bisnis

Permasalahan utama yang dihadapi meliputi:

- Tingginya Angka Dropout Mahasiswa

- Ketiadaan Sistem Deteksi Dini Risiko Dropout

- Minimnya Pemanfaatan Data Historis Mahasiswa untuk Pengambilan Keputusan

- Tidak Adanya Model Prediktif dalam Perencanaan Akademik

### Cakupan Proyek

Fokus proyek ini adalah melakukan analisis serta membangun model prediksi attrition karyawan berdasarkan atribut personal, pekerjaan, dan faktor organisasi. Lingkup pekerjaan meliputi:

* **Pemahaman Data (Data Understanding)**

  * Melakukan import dan eksplorasi awal terhadap dataset karyawan yang bersumber dari data terbuka.
  * Memeriksa struktur, jenis data, dan distribusi nilai setiap variabel.

* **Pembersihan dan Persiapan Data (Data Cleaning & Preparation)**

  * Menangani nilai hilang pada kolom Attrition.
  * Menghapus fitur yang tidak relevan dalam pemodelan.
  * Membersihkan data duplikat dan mengidentifikasi outlier dengan visualisasi boxplot.
  * Menyesuaikan tipe data dan melakukan encoding pada variabel kategori.

* **Eksplorasi Data (Exploratory Data Analysis / EDA)**

  * Memvisualisasikan distribusi variabel target Attrition.
  * Menganalisis hubungan antar fitur numerik menggunakan korelasi Pearson.
  * Membuat scatter plot antara TotalWorkingYears dan MonthlyIncome untuk mengamati pola.

* **Pemodelan Data (Modeling)**

  * Membangun beberapa model klasifikasi seperti K-Nearest Neighbors, Decision Tree, Random Forest, Support Vector Machine, dan Naive Bayes.
  * Melakukan pembagian data menjadi set pelatihan dan pengujian dengan train-test split.

* **Evaluasi Model (Evaluation)**

  * Mengukur kinerja model dengan metrik akurasi, presisi, recall, dan F1-score.
  * Menampilkan confusion matrix untuk mengevaluasi distribusi prediksi.
  * Menentukan model dengan performa terbaik berdasarkan metrik evaluasi.

### Persiapan

Sumber data: [Employee Data Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)


---
#### **1. Setup Lingkungan Kerja (Conda Environment)**

##### 🔹 Buat Environment Baru

```bash
conda create -n student_analysis python=3.11.13 -y
conda activate student_analysis
```

##### 🔹 Instalasi dari `requirements.txt`

Jika environment sudah dibuat:

```bash
pip install -r requirements.txt
```

---

#### **2. Setup Dashboard Metabase (Docker)**

##### 🔹 Jalankan Metabase di Docker

```powershell
docker run -d -p 3000:3000 `
  -v "${PWD}:/metabase-data" `
  -e "MB_DB_FILE=/metabase-data/metabase.db" `
  --name metabase metabase/metabase
```

> ⚠️ Untuk pengguna **Linux/Mac**, gunakan tanda `\` untuk line break atau tulis satu baris.

---

##### 🔹 Kredensial Metabase (Default Login)

| Item          | Value                                          |
| ------------- | ---------------------------------------------- |
| **URL Akses** | [http://**localhost**:3000](http://localhost:3000) |
| **Email**     | `root@mail.com`                                |
| **Password**  | `root123`                                      |
| **Port**      | 3000                                           |


## **Business Dashboard**

Untuk mendukung pendeteksian dini risiko dropout dan pengambilan keputusan, dashboard bisnis interaktif sangat esensial. Dengan memanfaatkan Metabase (seperti yang dijelaskan dalam persiapan proyek), sebuah dashboard dapat dibangun untuk memvisualisasikan insight kunci secara real-time.

### **Metrik Utama yang Akan Ditampilkan**

**1. Tren Dropout Berdasarkan Semester**
Visualisasi jumlah atau persentase dropout dari semester 1 ke semester 2.
Contoh insight:

> Mahasiswa Dropout memiliki penurunan tajam dari semester 1 ke semester 2, dengan Grade turun dari 10.311 menjadi 8.383 dan Approved turun dari 3.626 menjadi 2.757.

**2. Proporsi Dropout Berdasarkan Status Pembayaran**
Perbandingan mahasiswa dropout vs. lulus berdasarkan status pembayaran.
Contoh insight:

> Dari 528 mahasiswa yang tidak bayar tepat waktu, \~87% dropout (457 dari 528). Sebaliknya, dari 3.896 mahasiswa yang membayar tepat waktu, hanya \~25% yang dropout.

**3. Proporsi Dropout Berdasarkan Status Beasiswa**
Visualisasi tingkat dropout antara mahasiswa penerima beasiswa dan non-beasiswa.
Contoh insight:

> Mahasiswa tanpa beasiswa lebih banyak mengalami dropout (1.287) dibanding yang lulus (1.374), sementara mahasiswa penerima beasiswa jauh lebih berpeluang lulus (835 lulusan vs 134 dropout).

**4. Rata-rata Usia Masuk Berdasarkan Status Kelulusan**
Membandingkan usia rata-rata mahasiswa dropout (26 tahun) dengan lulus/aktif (\~22 tahun).

**5. Proporsi Dropout Berdasarkan Jenis Kelamin**
Menampilkan tingkat dropout yang lebih tinggi pada laki-laki.
Contoh insight:

> Hampir setengah dari mahasiswa laki-laki (dropout rate \~45.1%) mengalami dropout, dibandingkan dengan perempuan (dropout rate \~25.1%).

**6. Proporsi Dropout Berdasarkan Status Utang (Debtor)**
Contoh insight:

> Dari 503 mahasiswa yang berutang (Debtor=1), 312 (sekitar 62%) adalah dropout.

---

## **Menjalankan Sistem Machine Learning**

**1. Install Dependencies**

```bash
pip install -r requirements.txt
```

**2. Jalankan Aplikasi Streamlit**

```bash
streamlit run app.py
```

---

## **Conclusion**

Proyek ini bertujuan untuk mengatasi masalah tingginya angka dropout di Jaya Jaya Institut dengan memanfaatkan data historis mahasiswa untuk membangun model prediksi. Berikut beberapa temuan utama:

* **Performa Akademik Awal yang Konsisten:**
  Mahasiswa dengan nilai dan jumlah mata kuliah lulus yang baik sejak awal memiliki peluang tinggi untuk lulus.

* **Penurunan Performa di Semester Lanjut:**
  Mahasiswa yang nilai dan kelulusan mata kuliahnya menurun dari semester 1 ke 2 cenderung dropout.

* **Kedisiplinan Pembayaran:**
  Keterlambatan atau ketidakpatuhan dalam membayar uang kuliah berkorelasi tinggi dengan dropout.

* **Dukungan Beasiswa:**
  Penerima beasiswa memiliki tingkat kelulusan lebih tinggi dibandingkan yang tidak menerima beasiswa.

* **Usia Masuk:**
  Mahasiswa dengan usia masuk lebih tua cenderung memiliki risiko dropout yang lebih tinggi.

* **Jenis Kelamin:**
  Mahasiswa laki-laki memiliki dropout rate yang lebih tinggi dibanding perempuan.

* **Status Utang (Debtor):**
  Mahasiswa dengan status utang memiliki kemungkinan dropout yang lebih tinggi.

---

## **Rekomendasi Action Items**

### 1. Program Intervensi Dini Berbasis Akademik

* **Tindakan:** Identifikasi mahasiswa dengan penurunan performa dari semester 1 ke 2.
* **Rekomendasi:** Tawarkan konseling akademik, mentoring, dan pemantauan berkala.

### 2. Sistem Pemantauan dan Dukungan Pembayaran

* **Tindakan:** Deteksi dini keterlambatan pembayaran.
* **Rekomendasi:** Sediakan opsi cicilan, bantuan keuangan, atau informasi beasiswa.

### 3. Perluasan Program Beasiswa dan Bantuan Finansial

* **Tindakan:** Tingkatkan akses dan cakupan beasiswa.
* **Rekomendasi:** Tambahkan sponsor, beasiswa berbasis kebutuhan, dan bantuan pendidikan mikro.

### 4. Program Adaptasi untuk Mahasiswa Usia Lebih Tua

* **Tindakan:** Buat program khusus adaptasi dan pendampingan.
* **Rekomendasi:** Sesi manajemen waktu, dukungan sosial, dan fleksibilitas akademik.

### 5. Inisiatif Dukungan Berbasis Gender

* **Tindakan:** Identifikasi tantangan khusus mahasiswa laki-laki.
* **Rekomendasi:** Program mentoring dan kelompok diskusi yang relevan.

### 6. Pendekatan Proaktif terhadap Mahasiswa dengan Utang

* **Tindakan:** Deteksi dan bantu mahasiswa dengan status Debtor sejak awal.
* **Rekomendasi:** Tawarkan konseling keuangan dan rencana pembayaran bertahap.

