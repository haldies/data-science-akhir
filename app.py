import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# --- LOAD DATA ---
@st.cache_resource
def load_data():
    url = 'https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv'
    df = pd.read_csv(url, sep=';')
    return df

def preprocess(df):
    df['Status_bin'] = df['Status'].apply(lambda x: 1 if x == 'Dropout' else 0)
    df['Gender'] = df['Gender'].apply(lambda x: 1 if x == 'M' else 0)
    return df

def train_model(df):
    features = [
        'Curricular_units_2nd_sem_approved',
        'Curricular_units_2nd_sem_grade',
        'Curricular_units_1st_sem_approved',
        'Curricular_units_1st_sem_grade',
        'Tuition_fees_up_to_date',
        'Scholarship_holder',
        'Age_at_enrollment',
        'Debtor',
        'Gender',
    ]
    X = df[features]
    y = df['Status_bin']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return model, X_test, y_test, y_pred, acc

st.set_page_config(page_title="Deteksi Dropout Mahasiswa", layout="wide")
st.title("🎓 Dashboard Deteksi Dropout Mahasiswa - Jaya Jaya Institut")

# Sidebar navigasi
menu = st.sidebar.radio("Navigasi", ["🤖 Prediksi Dropout","📊 Ringkasan Data" "📈 Evaluasi Model" ])

# Load dan proses data
df = load_data()
df = preprocess(df)
model, X_test, y_test, y_pred, accuracy = train_model(df)

if menu == "📊 Ringkasan Data":
    st.markdown(f"- Jumlah total mahasiswa: **{len(df)}**")
    st.markdown(f"- Jumlah dropout: **{df['Status_bin'].sum()}**")
    st.markdown(f"- Akurasi model saat ini: **{accuracy:.2%}**")

    # Plot visual dropout
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(x='Status', data=df, palette='Set2', ax=ax)
    ax.set_title("Distribusi Status Mahasiswa")
    st.pyplot(fig)

# --- PREDIKSI ---
elif menu == "🤖 Prediksi Dropout":
    st.subheader("🔍 Prediksi Dropout Mahasiswa Baru")

    with st.form("input_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.slider("Usia saat masuk", 17, 60, 22)
            gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
            debtor = st.selectbox("Status Utang", ["Tidak", "Ya"])
            fees_up_to_date = st.selectbox("Pembayaran Tepat Waktu", ["Ya", "Tidak"])

        with col2:
            scholarship = st.selectbox("Penerima Beasiswa", ["Ya", "Tidak"])
            cu_1_approved = st.slider("CU Semester 1 Lulus", 0, 10, 5)
            cu_1_grade = st.slider("Nilai Semester 1", 0.0, 20.0, 10.0)
            cu_2_approved = st.slider("CU Semester 2 Lulus", 0, 10, 5)
            cu_2_grade = st.slider("Nilai Semester 2", 0.0, 20.0, 10.0)

        submitted = st.form_submit_button("Prediksi Dropout")

    if submitted:
        input_df = pd.DataFrame({
            'Curricular_units_2nd_sem_approved': [cu_2_approved],
            'Curricular_units_2nd_sem_grade': [cu_2_grade],
            'Curricular_units_1st_sem_approved': [cu_1_approved],
            'Curricular_units_1st_sem_grade': [cu_1_grade],
            'Tuition_fees_up_to_date': [1 if fees_up_to_date == "Ya" else 0],
            'Scholarship_holder': [1 if scholarship == "Ya" else 0],
            'Age_at_enrollment': [age],
            'Debtor': [1 if debtor == "Ya" else 0],
            'Gender': [1 if gender == "Laki-laki" else 0]
        })

        pred = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][pred]

        if pred == 1:
            st.error(f"⚠️ Mahasiswa ini berpotensi **DROP OUT** dengan probabilitas {prob:.2%}")
        else:
            st.success(f"✅ Mahasiswa ini kemungkinan **TIDAK dropout** dengan probabilitas {prob:.2%}")

# --- EVALUASI MODEL ---
elif menu == "📈 Evaluasi Model":
    st.subheader("📊 Evaluasi Model Random Forest")

    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["Lulus", "Dropout"], yticklabels=["Lulus", "Dropout"])
    ax.set_xlabel("Prediksi")
    ax.set_ylabel("Aktual")
    st.pyplot(fig)

    st.text("Classification Report")
    st.code(classification_report(y_test, y_pred, target_names=["Lulus", "Dropout"]))
