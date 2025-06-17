import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

url = 'https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv'

@st.cache_resource
def load_data():
    df = pd.read_csv(url, sep=';')
    return df

df = load_data()

st.title("Dashboard Deteksi Dropout Jaya Jaya Institut")

# Prediksi Dropout sederhana
st.header("Model Prediksi Dropout")

# Ubah label Status ke numerik
df['Status_bin'] = df['Status'].apply(lambda x: 1 if x == 'Dropout' else 0)

# Fitur dan target
features = ['Admission_grade', 'Age_at_enrollment', 'Curricular_units_1st_sem_approved', 'Curricular_units_2nd_sem_approved']
X = df[features]
y = df['Status_bin']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediksi dan akurasi
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Akurasi model Random Forest: {accuracy:.2f}")

# Prediksi untuk input user
st.subheader("Coba Prediksi Dropout Siswa Baru")
admission_grade = st.slider("Admission Grade", float(df['Admission_grade'].min()), float(df['Admission_grade'].max()), float(df['Admission_grade'].mean()))


age = st.slider("Age at Enrollment", int(df['Age_at_enrollment'].min()), int(df['Age_at_enrollment'].max()), int(df['Age_at_enrollment'].mean()))
cu_1st_approved = st.slider("Curricular Units 1st Sem Approved", int(df['Curricular_units_1st_sem_approved'].min()), int(df['Curricular_units_1st_sem_approved'].max()), int(df['Curricular_units_1st_sem_approved'].mean()))
cu_2nd_approved = st.slider("Curricular Units 2nd Sem Approved", int(df['Curricular_units_2nd_sem_approved'].min()), int(df['Curricular_units_2nd_sem_approved'].max()), int(df['Curricular_units_2nd_sem_approved'].mean()))

input_data = pd.DataFrame({
    'Admission_grade': [admission_grade],
    'Age_at_enrollment': [age],
    'Curricular_units_1st_sem_approved': [cu_1st_approved],
    'Curricular_units_2nd_sem_approved': [cu_2nd_approved]
})

pred = model.predict(input_data)[0]
prob = model.predict_proba(input_data)[0][pred]

if st.button("Prediksi Dropout"):
    if pred == 1:
        st.warning(f"Siswa ini berpotensi DROP OUT dengan probabilitas {prob:.2f}")
    else:
        st.success(f"Siswa ini kemungkinan TIDAK dropout dengan probabilitas {prob:.2f}")
