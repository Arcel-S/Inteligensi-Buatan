import heapq

def a_star_search(graph, start, goal, heuristics):
    """
    Implementasi algoritma pencarian A*.

    Args:
        graph (dict): Representasi graf dalam bentuk adjacency list.
        start (str): Node awal.
        goal (str): Node tujuan.
        heuristics (dict): Nilai heuristik dari setiap node ke tujuan.

    Returns:
        tuple: Mengembalikan path dari start ke goal dan total biayanya.
               Jika tidak ada path, kembalikan (None, None).
    """
    # Priority queue untuk menyimpan node yang akan dieksplorasi.
    # Disimpan dalam format (f_score, g_score, path)
    # f_score = g_score (biaya riil) + heuristic (estimasi biaya)
    open_list = [(heuristics[start], 0, [start])]
    heapq.heapify(open_list)

    # Dictionary untuk menyimpan g_score (biaya terendah dari start ke suatu node)
    g_scores = {node: float('inf') for node in heuristics}
    g_scores[start] = 0

    while open_list:
        # Ambil node dengan f_score terendah dari priority queue
        _, current_g, current_path = heapq.heappop(open_list)
        current_node = current_path[-1]

        # Jika sudah sampai di tujuan, kembalikan hasilnya
        if current_node == goal:
            return current_path, current_g

        # Jika tidak, eksplorasi semua tetangga dari node saat ini
        for neighbor, cost in graph.get(current_node, []):
            # Hitung g_score baru jika melalui node saat ini
            g_score = current_g + cost

            # Jika path baru ini lebih baik dari yang sudah ada, perbarui
            if g_score < g_scores[neighbor]:
                g_scores[neighbor] = g_score
                f_score = g_score + heuristics[neighbor]
                new_path = current_path + [neighbor]
                heapq.heappush(open_list, (f_score, g_score, new_path))

    # Jika open_list habis tapi tujuan tidak tercapai, berarti tidak ada path
    return None, None
