import heapq

def ucs(graph, start, goal):
    """
    Implementasi Uniform Cost Search (UCS).

    Args:
        graph (dict): Representasi adjacency list dari graf.
        start (str): Node awal.
        goal (str): Node tujuan.

    Returns:
        tuple: Path (list) dan cost (int) jika ditemukan, selain itu (None, inf).
    """
    # Priority queue untuk menyimpan (cost, path)
    priority_queue = [(0, [start])]
    visited = set()

    while priority_queue:
        # Ambil path dengan cost terendah
        cost, path = heapq.heappop(priority_queue)
        current_node = path[-1]

        # Jika sudah pernah dikunjungi, lewati
        if current_node in visited:
            continue
        
        visited.add(current_node)

        # Jika tujuan tercapai, kembalikan hasilnya
        if current_node == goal:
            return path, cost

        # Eksplorasi tetangga
        if current_node in graph:
            for neighbor, weight in graph[current_node]:
                if neighbor not in visited:
                    new_cost = cost + weight
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cost, new_path))
    
    # Jika tidak ada path yang ditemukan
    return None, float('inf')
