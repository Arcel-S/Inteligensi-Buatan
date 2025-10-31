from data_module import KnowledgeBase

class BackwardChainingEngine:
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb
        self.proved_goals = set() 
        self.history = set() 
        self.path = [] 

    def prove_goal(self, goal):
        """Fungsi rekursif untuk membuktikan suatu goal."""
        
        # 1. Cek: Apakah goal sudah terbukti di WM?
        if self.kb.is_fact_known(goal):
            self.path.append(f"-> Goal '{goal}' ditemukan di Fakta Awal.")
            return True
        
        # Mencegah loop rekursif tak terbatas
        if goal in self.history:
            return False 
        
        self.history.add(goal)
        self.path.append(f"\n--- [Proving: {goal}] ---")

        # 2. Cari Aturan: Aturan mana yang menghasilkan goal ini (RHS = goal)?
        candidate_rules = [rule for rule in self.kb.get_all_rules() if rule['then'] == goal]
        
        if not candidate_rules:
            self.path.append(f"Goal '{goal}' gagal. Tidak ada aturan yang dapat menyimpulkannya.")
            self.history.remove(goal)
            return False 
        
        # 3. Iterasi Aturan Kandidat
        for rule in candidate_rules:
            self.path.append(f"-> Mencoba Aturan {rule['id']} untuk Goal: {goal}")
            all_sub_goals_proved = True
            
            # Sub-Goal: Premis (LHS) dari aturan ini
            for sub_goal in rule['if']:
                
                # Panggil rekursif untuk membuktikan setiap sub-goal
                if not self.prove_goal(sub_goal):
                    all_sub_goals_proved = False
                    break
            
            # 4. Jika semua sub-goal terbukti, goal utama terbukti!
            if all_sub_goals_proved:
                self.kb.add_fact(goal)
                self.proved_goals.add(goal)
                self.path.append(f"GOAL BERHASIL: '{goal}' terbukti melalui Aturan {rule['id']}")
                self.history.remove(goal)
                return True
            else:
                self.path.append(f"Aturan {rule['id']} Gagal membuktikan '{goal}' (Sub-goal tidak terpenuhi).")
                
        self.history.remove(goal)
        return False

    def run_inference(self, target_goal: str):
        """Menjalankan proses Backward Chaining dan menampilkan trace."""
        
        # Reset data untuk run baru (fakta sudah di-set di main.py)
        self.path = []
        self.history = set()
        self.proved_goals = set()
        
        print(f"--- Memulai Backward Chaining (Goal-Driven) ---")
        print(f"Fakta Awal: {list(self.kb.facts)}")
        print(f"Tujuan yang Ingin Dibuktikan: {target_goal}")
        
        result = self.prove_goal(target_goal)
        
        # Tampilkan Trace di akhir
        print("\n=============================================")
        print(" Trace Rantai Inferensi (Backward Chaining)")
        print("=============================================")
        for step in self.path:
            print(step)
            
        return result