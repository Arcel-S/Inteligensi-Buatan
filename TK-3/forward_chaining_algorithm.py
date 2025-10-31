from data_module import KnowledgeBase
import random

class ForwardChainingEngine:
    
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb
        self.fired_rules = set() 
        self.priority_map = {'Tertinggi': 4, 'Tinggi': 3, 'Sedang': 2, 'Rendah': 1}
        # Menambahkan dictionary untuk melacak fakta dan prioritasnya
        self.conclusions_priority = {} 

    def check_match(self, rule):
        """Memeriksa apakah semua premis (LHS) aturan ada di Working Memory."""
        return all(self.kb.is_fact_known(premis) for premis in rule['if'])

    def resolve_conflict(self, conflict_set):
        """Menerapkan Strategi Conflict Resolution (Prioritas > Spesifisitas > Random)."""
        if not conflict_set:
            return None

        # 1. Penyaringan berdasarkan Prioritas (Rendah, Sedang, Tinggi)
        max_priority = -1
        by_priority = []
        for rule in conflict_set:
            p = self.priority_map.get(rule.get('priority', 'Rendah'), 1)
            
            if p > max_priority:
                max_priority = p
                by_priority = [rule]
            elif p == max_priority:
                by_priority.append(rule)

        # 2. Penyaringan berdasarkan SPESIFISITAS
        if len(by_priority) > 1:
            max_specificity = -1
            by_specificity = []
            for rule in by_priority:
                spec = rule['specificity']
                if spec > max_specificity:
                    max_specificity = spec
                    by_specificity = [rule]
                elif spec == max_specificity:
                    by_specificity.append(rule)
            
            # 3. Random sebagai tie-breaker (Rule Order)
            return random.choice(by_specificity)
            
        return by_priority[0] 

    def run_inference(self):
        """Menjalankan Recognize-Act Cycle"""
        self.fired_rules = set()
        self.conclusions_priority = {} # Reset pelacakan
        
        print("--- Memulai Forward Chaining ---")
        print(f"Fakta Awal: {list(self.kb.facts)}")
        
        iteration = 1
        
        while True:
            conflict_set = []

            # 1. Rekognisi
            for rule in self.kb.get_all_rules():
                rule_key = rule['id']
                if rule_key not in self.fired_rules and self.check_match(rule):
                    conflict_set.append(rule)

            if not conflict_set:
                print(f"\nIterasi {iteration}. Tidak ada aturan yang cocok yang tersisa. Proses selesai.")
                break

            print(f"\nIterasi {iteration}. Aturan yang cocok (Conflict Set): {[r['id'] for r in conflict_set]}")
            
            # 2. Aksi Memilih / Seleksi
            rule_to_fire = self.resolve_conflict(conflict_set)
            
            # 3. Aksi Eksekusi
            new_conclusion = rule_to_fire['then']
            rule_priority = rule_to_fire['priority']
            
            self.fired_rules.add(rule_to_fire['id'])
            added = self.kb.add_fact(new_conclusion)

            print(f"Aturan dipilih: {rule_to_fire['id']} (Pri: {rule_priority}, Spec: {rule_to_fire['specificity']})")
            if added:
                print(f"Fakta Baru Ditambahkan: {new_conclusion}")
                self.conclusions_priority[new_conclusion] = rule_priority
            
            print(f"Kondisi Fakta saat ini: {list(self.kb.facts)}")

            iteration += 1

        print("\n--- Inferensi Selesai (Forward Chaining) ---")
        self.display_prioritized_results()


    def display_prioritized_results(self):
        """Mengelompokkan dan menampilkan hasil berdasarkan prioritas aturan."""
        
        # Kelompokkan hasil berdasarkan level prioritas
        grouped_results = {
            'Tertinggi': [], 'Tinggi': [], 'Sedang': [], 'Rendah': []
        }
        
        for fact, priority in self.conclusions_priority.items():
            if priority in grouped_results:
                grouped_results[priority].append(fact)

        print("\n=============================================")
        print(" Hasil Inferensi Terprioritas (FC)")
        print("=============================================")
        
        # Urutan yang disajikan harus dari tertinggi ke terendah
        priority_order = ['Tertinggi', 'Tinggi', 'Sedang', 'Rendah']
        
        for priority in priority_order:
            conclusions = grouped_results[priority]
            
            if conclusions:
                if priority in ['Tertinggi', 'Tinggi']:
                    print(f"Kategori {priority} (Solusi/Diagnosis Utama):")
                else:
                    print(f"Kategori {priority} (Konsekuensi/Langkah Tambahan):")

                for conclusion in conclusions:
                    print(f"  - {conclusion}")