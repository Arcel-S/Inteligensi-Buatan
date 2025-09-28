import csv  # Mengimpor modul csv untuk membaca file CSV
import sys  # Impor modul sys untuk keluar dari program
from a_star import a_star_search  # Mengimpor fungsi algoritma A* dari file a_star.py

def build_graph(graph_file):  # Mendefinisikan fungsi untuk membangun graf dari file
    graph = {}  # Membuat dictionary kosong untuk menyimpan graf
    with open(graph_file, 'r', encoding='utf-8') as file:  # Membuka file CSV dengan encoding UTF-8
        reader = csv.reader(file)  # Membuat objek pembaca CSV
        next(reader)  # Melewati baris pertama (header) dalam file CSV
        for row in reader:  # Melakukan loop untuk setiap baris dalam file
            source, target, cost = row  # Mengambil nilai sumber, tujuan, dan biaya dari setiap baris
            cost = int(cost)  # Mengubah biaya dari string menjadi integer
            if source not in graph:  # Jika kota sumber belum ada di graf
                graph[source] = []  # Buat list kosong untuk kota sumber
            if target not in graph:  # Jika kota tujuan belum ada di graf
                graph[target] = []  # Buat list kosong untuk kota tujuan
            graph[source].append((target, cost))  # Tambahkan koneksi dari sumber ke tujuan dengan biayanya
            graph[target].append((source, cost))  # Tambahkan koneksi sebaliknya (graf tidak berarah)
    return graph  # Mengembalikan graf yang sudah dibangun

def load_heuristics(heuristic_file):  # Mendefinisikan fungsi untuk memuat nilai heuristik
    heuristics = {}  # Membuat dictionary kosong untuk menyimpan nilai heuristik
    with open(heuristic_file, 'r', encoding='utf-8') as file:  # Membuka file heuristik dengan encoding UTF-8
        reader = csv.reader(file)  # Membuat objek pembaca CSV
        next(reader)  # Melewati baris pertama (header) dalam file CSV
        for row in reader:  # Melakukan loop untuk setiap baris dalam file
            city, value = row  # Mengambil nama kota dan nilai heuristiknya
            heuristics[city] = int(value)  # Menyimpan nilai heuristik sebagai integer
    return heuristics  # Mengembalikan dictionary berisi nilai heuristik

def validate_data(graph, heuristics):  # Mendefinisikan fungsi untuk validasi data
    print("🔍 Memulai validasi data...")  # Menampilkan pesan bahwa validasi dimulai
    all_nodes_valid = True  # Variabel boolean untuk melacak apakah semua node valid
    for node in graph:  # Melakukan loop untuk setiap node di graf
        if node not in heuristics:  # Jika node tidak ditemukan di data heuristik
            print(f"❌ ERROR: Kota '{node}' ditemukan di graph.csv, tapi tidak ada di heuristik.csv.")  # Tampilkan pesan error
            all_nodes_valid = False  # Set flag menjadi False karena ada node yang tidak valid
            
    if not all_nodes_valid:  # Jika ada node yang tidak valid
        print("\n⚠️ Terdapat ketidaksesuaian data. Mohon perbaiki file CSV Anda.")  # Tampilkan pesan peringatan
        sys.exit() # Menghentikan program jika ada error
    else:  # Jika semua node valid
        print("✅ Semua data valid dan konsisten.")  # Tampilkan pesan konfirmasi


if __name__ == "__main__":  # Memastikan kode hanya dijalankan jika file ini dieksekusi langsung
    GRAPH_FILE = 'graph.csv'  # Menetapkan nama file yang berisi data graf
    HEURISTIC_FILE = 'heuristik.csv'  # Menetapkan nama file yang berisi nilai heuristik

    # Membangun graf dan memuat data heuristik
    graph = build_graph(GRAPH_FILE)  # Memanggil fungsi untuk membangun graf dari file CSV
    heuristics = load_heuristics(HEURISTIC_FILE)  # Memanggil fungsi untuk memuat nilai heuristik

    # Lakukan validasi data sebelum menjalankan algoritma
    validate_data(graph, heuristics)  # Memvalidasi apakah data graf dan heuristik konsisten

    START_NODE = "Cilegon"  # Menetapkan kota awal pencarian
    GOAL_NODE = "Banyuwangi"  # Menetapkan kota tujuan pencarian

    print(f"\n🚀 Mencari rute dari {START_NODE} ke {GOAL_NODE}...")  # Menampilkan pesan pencarian rute
    path, cost = a_star_search(graph, START_NODE, GOAL_NODE, heuristics)  # Menjalankan algoritma A* dan menyimpan hasilnya

    if path:  # Jika rute ditemukan (path tidak None atau kosong)
        print(f"🚗 Rute terpendek ditemukan!")  # Tampilkan pesan bahwa rute ditemukan
        print(" -> ".join(path))  # Tampilkan rute dengan panah sebagai pemisah
        print(f"✅ Total biaya perjalanan: {cost}")  # Tampilkan total biaya perjalanan
    else:  # Jika rute tidak ditemukan
        print(f"❌ Tidak ditemukan rute dari {START_NODE} ke {GOAL_NODE}")  # Tampilkan pesan gagal
