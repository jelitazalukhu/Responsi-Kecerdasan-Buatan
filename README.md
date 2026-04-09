# 🐾 Responsi Kecerdasan Buatan - Animal Classification

Repositori ini disusun untuk memenuhi tugas **Responsi mata kuliah Kecerdasan Buatan**. Fokus utama dari proyek ini adalah menangani masalah **overfitting** pada model klasifikasi citra hewan yang mencakup kategori: 
*🐕 Anjing, 🐈 Kucing, dan 🦁 Hewan Liar.*

---

## 🚀 Link Website
Website dapat diakses secara langsung melalui tautan di berikut ini:
👉 **[Live Demo: Animal Classifier Website](https://responsi-kecerdasan-buatan-jtp8hg2pacvfsxzyns7aua.streamlit.app/)**

---

## 📌 Deskripsi Tugas
Konsep utama dalam tugas ini adalah melakukan optimasi pada model yang sebelumnya mengalami *overfitting* saat proses pelatihan di Google Colab. Melalui penyesuaian arsitektur dan *hyperparameter*, model berhasil diperbaiki hingga mencapai tingkat akurasi yang lebih stabil pada data pengujian.

Untuk memvalidasi hasil optimasi tersebut, model diimplementasikan ke dalam sebuah **website sederhana**. Website ini berfungsi sebagai media interaktif untuk menguji kemampuan model dalam mengenali gambar baru secara langsung melalui browser.

## 📂 Isi Repositori
Berikut adalah komponen utama yang terdapat dalam repositori ini:

| Nama File | Deskripsi |
| :--- | :--- |
| `app.py` | Skrip utama antarmuka website dan logika prediksi model. |
| `animal_classifier.pth` | File bobot model hasil optimasi (otak aplikasi). |
| `animal_classifier_JelitaCrisnaZalukhu.ipynb` | File kode program proses perbaikan model dari overfitting. |
| `Uraian Perbaikan dan Penyelesaian.pdf` | Dokumen penjelasan detail mengenai langkah penyelesaian masalah. |
| `requirements.txt` | Daftar *library* pendukung agar sistem berjalan stabil di cloud. |

---

## 🛠️ Cara Penggunaan
1. Klik link website yang tertera di atas.
2. Unggah foto hewan (Anjing, Kucing, atau Hewan Liar) dalam format JPG/PNG.
3. Website akan memproses gambar dan menampilkan hasil klasifikasi secara otomatis.

---
