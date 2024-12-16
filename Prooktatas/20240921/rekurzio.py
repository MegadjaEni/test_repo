from numpy.version import git_revision


def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)


n = 5
print(f'A számok összege 1-től {n}-ig: {sum_recursive(5)}')


# fib(0) => 0
# fib(1) => 1
#fib(n) => fib(n - 1) + fib(n - 2) (n > 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 6
print(f'Az {n}-dik fibonacci szám: {fibonacci(n)}')


def flood_fill(grid, row, col, new_value):
    # Határkezelés
    if not (0 <= row < len(grid) and 0 <= col < len(grid)):
        return
    if grid[row][col] == new_value:
        return
    grid[row][col] = new_value
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        flood_fill(grid, row + dr, col + dc, new_value)

grid = [
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.']
]

# (2, 2)
"""
. . . .
. x x .
. x x .
. . . .
"""
flood_fill(grid, 2, 2, 'x')

for row in grid:
    print(' '.join(row))