
def move(source, destination):
    print(f"Move disk from {source} to {destination}")


def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 0:
        return

    TowerOfHanoi(n-1, source, auxiliary, destination)
    move(source, destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)


# Driver code
n = 4
TowerOfHanoi(n, 'A', 'B', 'C')
