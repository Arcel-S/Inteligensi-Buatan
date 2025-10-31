from data_module import KnowledgeBase
from forward_chaining_algorithm import ForwardChainingEngine
from backward_chaining_algorithm import BackwardChainingEngine

def run_forward_chaining():
    """Menjalankan simulasi Forward Chaining."""
    print("\n=========================================================")
    print("           SIMULASI FORWARD CHAINING (Data-Driven)")
    print("=========================================================")
    
    # 1. Inisialisasi Basis Data baru
    kb_fc = KnowledgeBase()

    # 2. Inisialisasi dan Jalankan Mesin FC
    fc_engine = ForwardChainingEngine(kb_fc)
    fc_engine.run_inference()

def run_backward_chaining():
    """Menjalankan simulasi Backward Chaining."""
    print("\n=========================================================")
    print("           SIMULASI BACKWARD CHAINING (Goal-Driven)")
    print("=========================================================")
    
    # Tujuan spesifik yang ingin dibuktikan (dari Tugas 3, Bagian 2)
    goal = 'Ganti Aki'
    
    # 1. Inisialisasi Basis Data baru (Fakta awal di-set di __init__ KB)
    kb_bc = KnowledgeBase()

    # 2. Inisialisasi dan jalankan Mesin BC
    bc_engine = BackwardChainingEngine(kb_bc)
    
    # Panggil run_inference(), yang menjalankan prove_goal() dan menampilkan TRACE.
    result = bc_engine.run_inference(target_goal=goal) 
    
    # Cetak hasil akhir setelah trace
    print("\n--- Inferensi Backward Chaining Selesai ---")
    print(f"Final Result: Goal '{goal}' proved: {'Terbukti' if result else 'TIDAK TERBUKTI'}")
    print(f"Known facts after inference: {list(kb_bc.facts)}")


if __name__ == "__main__":
    
    print(" Mode Inferensi Sistem Pakar")
    print("------------------------------------------")
    print("1. Forward Chaining (Mencari semua kesimpulan)")
    print("2. Backward Chaining (Membuktikan target 'Ganti Aki')")
    
    try:
        choice = int(input("Masukkan pilihan (1 atau 2): "))
        
        if choice == 1:
            run_forward_chaining()
        elif choice == 2:
            run_backward_chaining()
        else:
            print("Pilihan tidak valid. Harap masukkan 1 atau 2.")
            
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")