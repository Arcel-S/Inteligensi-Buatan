import csv
from collections import defaultdict
from ucs import ucs # Hanya mengimpor algoritma

def read_graph_from_csv(file_path):
    graph = defaultdict(list)
    try:
        with open('graph.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Normalisasi nama kolom
            reader.fieldnames = [h.strip().lower() for h in reader.fieldnames]
            print("Header CSV:", reader.fieldnames)  # Tambahkan baris ini untuk debug
            for row in reader:
                # Normalisasi key row
                row = {k.strip().lower(): v for k, v in row.items()}
                source = row['source']
                target = row['target']
                try:
                    cost = int(row['cost'])
                    # Menambahkan edge untuk kedua arah
                    graph[source].append((target, cost))
                    graph[target].append((source, cost))
                except (ValueError, KeyError) as e:
                    print(f"Melewatkan baris karena error data: {row} -> {e}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' tidak ditemukan.")
        return None
    return graph

def main():
    file_path = 'data/graph.csv'
    graph = read_graph_from_csv(file_path)

    if graph is None:
        return

    start_node = 'Cilegon'
    goal_node = 'Banyuwangi'
    
    print("=============================================")
    print(f"Mencari rute dari {start_node} ke {goal_node}")
    print("Menggunakan algoritma Uniform Cost Search (UCS)")
    print("=============================================")
    
    path, cost = ucs(graph, start_node, goal_node)

    print("---------------------------------------------")
    if path:
        print("Pencarian berhasil! ✅")
        print(f"Total Biaya (Jarak): {cost} km")
        print("Rute yang ditemukan:")
        print(" -> ".join(path))
    else:
        print("Pencarian gagal. Tidak ada rute yang ditemukan. ❌")
    print("---------------------------------------------")


if __name__ == "__main__":
    main();
