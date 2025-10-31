# Proyek Sistem Pakar Diagnostik Kerusakan Mobil (Rule-Based System)

Proyek ini mengimplementasikan Sistem Berbasis Aturan (Rule-Based System / RBS) untuk simulasi diagnostik kerusakan mobil, berfokus pada masalah aki/kelistrikan, menggunakan dua mekanisme inferensi inti Kecerdasan Buatan: **Forward Chaining (FC)** dan **Backward Chaining (BC)**.

## Tujuan Proyek

Tugas ini bertujuan untuk memvisualisasikan dan membandingkan dua pendekatan penalaran dalam sistem pakar berdasarkan spesifikasi berikut:

1.  **Forward Chaining (Tugas 1 & 3):** Penalaran *Data-Driven* untuk menarik **semua kemungkinan kesimpulan** dari gejala awal, dengan mendemonstrasikan **Conflict Resolution** (Prioritas > Spesifisitas) di setiap langkah.
2.  **Backward Chaining (Tugas 2):** Penalaran *Goal-Driven* untuk **membuktikan tujuan spesifik** (`Ganti Aki`), dengan menyajikan **Trace Rantai Inferensi** yang detail.

## Fakta Awal (Input Sistem)

Semua simulasi dimulai dengan fakta-fakta berikut dalam Working Memory:
* `Mesin Mati Total`
* `Suara Klik saat Start`
* `Tidak ada Karat pada Terminal`

---

## Struktur Proyek

Proyek ini terbagi menjadi empat modul Python (`.py`):

| File | Peran | Catatan Implementasi Utama |
| :--- | :--- | :--- |
| `data_module.py` | Basis Data | Menyimpan Aturan Produksi (R1-R8) dan Fakta Awal. Menghitung Spesifisitas aturan. |
| `forward_chaining_algorithm.py` | Mesin Inferensi FC | Menerapkan siklus *Recognize-Act* ketat dan `resolve_conflict` (Prioritas > Spesifisitas). Output hasil terprioritas. |
| `backward_chaining_algorithm.py` | Mesin Inferensi BC | Menerapkan logika rekursif `prove_goal` dan mengumpulkan **Trace Inferensi** (langkah *Goal-Driven*). |
| `main.py` | Driver Program | Antarmuka pengguna untuk memilih mode (FC/BC) dan menjalankan simulasi. |

---

## Cara Menjalankan Program

1.  Pastikan Python 3.xx terinstal.
2.  Tempatkan keempat file `.py` di direktori yang sama.
3.  Jalankan file utama melalui Terminal/Command Prompt:

    ```bash
    python main.py
    ```
4.  Pilih opsi **1** atau **2** sesuai mode inferensi yang ingin disimulasikan.

### Output Mode 1: Forward Chaining

Output akan menampilkan proses langkah demi langkah (**Iterasi**) yang berfokus pada:
1.  **Conflict Set** (Aturan yang cocok).
2.  **Aturan yang Dipilih** berdasarkan Prioritas/Spesifisitas.
3.  Hasil akhir dikelompokkan menjadi: **Solusi/Diagnosis Utama** (Prioritas Tinggi) dan **Konsekuensi/Langkah Tambahan** (Prioritas Rendah).

### Output Mode 2: Backward Chaining

Output akan menampilkan **Trace Rantai Inferensi** yang detail, menunjukkan jalur rekursif Mesin BC yang mencari fakta-fakta pendukung dari Tujuan (`Ganti Aki`) hingga mencapai fakta awal.