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
| **URL Akses** | [http://localhost:3000](http://localhost:3000) |
| **Email**     | `root@mail.com`                                |
| **Password**  | `root123`                                      |
| **Port**      | 3000                                           |

### **Business Dashboard**


### Menjalankan Sistem Machine Learning

### **Conclusion**


### **Rekomendasi Action Items (Optional)**

