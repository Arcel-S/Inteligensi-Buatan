import re

class KnowledgeBase:
    def __init__(self):
        # Basis Pengetahuan (Knowledge Base)
        # Tambahkan properti 'specificity' (jumlah premis) untuk CRS
        self.rules = [
            # ID | IF (Premis/LHS) | THEN (Konklusi/RHS) | Prioritas CRS
            {'id': 'R1', 'if': ['Mesin Mati Total'], 'then': 'Cek Kelistrikan', 'priority': 'Rendah'},
            {'id': 'R2', 'if': ['Mesin Berputar Lambat'], 'then': 'Aki Lemah', 'priority': 'Sedang'},
            {'id': 'R3', 'if': ['Lampu Redup'], 'then': 'Aki Lemah', 'priority': 'Sedang'},
            {'id': 'R4', 'if': ['Aki Lemah', 'Tidak ada Karat pada Terminal'], 'then': 'Ganti Aki', 'priority': 'Tinggi'},
            {'id': 'R5', 'if': ['Suara Klik saat Start'], 'then': 'Aki Lemah', 'priority': 'Sedang'},
            {'id': 'R6', 'if': ['Mesin Mati Total', 'Tidak ada Suara'], 'then': 'Fungsi Kelistrikan Terputus', 'priority': 'Tinggi'},
            {'id': 'R7', 'if': ['Aki Lemah'], 'then': 'Mesin Sulit Start', 'priority': 'Rendah'},
            {'id': 'R8', 'if': ['Cek Kelistrikan', 'Terjadi Konsleting'], 'then': 'Isolasi Kelistrikan', 'priority': 'Tertinggi'},
        ]
        
        # Hitung dan tambahkan spesifisitas
        for rule in self.rules:
            rule['specificity'] = len(rule['if'])

        # Basis Fakta Awal (Working Memory)
        # Default facts moved here so callers don't need to set them in main.
        self.facts = set([
            'Mesin Mati Total',
            'Suara Klik saat Start',
            'Tidak ada Karat pada Terminal'
        ])
        
    def set_initial_facts(self, initial_facts: list):
        # Mengatur fakta awal untuk simulasi.
        self.facts = set(initial_facts)

    def add_fact(self, fact):
        # Menambahkan fakta baru ke Working Memory
        if fact not in self.facts:
            self.facts.add(fact)
            return True # Berhasil ditambah
        return False # Sudah ada

    def is_fact_known(self, fact):
        # Mengecek apakah suatu fakta sudah ada di Working Memory.
        return fact in self.facts

    def get_all_rules(self):
        # Mengambil semua aturan
        return self.rules