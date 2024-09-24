# Island Perimeter

This project calculates the perimeter of an island represented in a 2D grid.

## Function

### `island_perimeter(grid)`

- **Input**: A grid of 0s and 1s where 1 represents land and 0 represents water.
- **Output**: The perimeter of the island in the grid.

### Example

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12
