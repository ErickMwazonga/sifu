def get_min_time(total_servers: int, servers: list[int]) -> int:
    total_diffs = total_differences(total_servers, servers)
    return sum(total_diffs) - max(total_diffs)

def total_differences(total_servers: int, servers: list[int]) -> list[int]:
    if len(servers) <= 1:
        return []
    
    total_diffs = []
    round_servers = servers + [servers[0]]
    for i, server in enumerate(round_servers):
        if i == 0:
            continue

        if server >= servers[i - 1]:
            diff = server - servers[i - 1]
        else:
            diff = (total_servers - servers[i - 1]) + server
        total_diffs.append(diff)

    return total_diffs

total_servers, servers = 8, [2, 6, 8]
assert get_min_time(total_servers, servers) == 4


def max_rook_sum(matrix: list[list[int]]) -> int:
    n, m = len(matrix), len(matrix[0])

    max_in_row = [float('-inf')] * n
    max_in_col = [float('-inf')] * m

    max_sum = 0
    for i in range(n):
        for j in range(m):
            max_in_row[i] = max(max_in_row[i], matrix[i][j])
            max_in_col[j] = max(max_in_col[j], matrix[i][j])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != max_in_row[i] and matrix[i][j] != max_in_col[j]:
                max_sum = max(max_sum, max_in_row[i] + max_in_col[j])

    return max_sum

matrix = [
    [1, 4],
    [2, 3]
]
assert max_rook_sum(matrix) == 6

