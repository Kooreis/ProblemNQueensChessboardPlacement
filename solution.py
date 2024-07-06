```python
def solve_n_queens(n):
    ...
    def place_queen(n, ocuppied_positions=[]):
        if n == len(ocuppied_positions):
            return [ocuppied_positions]
        else:
            solutions = []
            for pos in range(n):
                if can_place(pos, ocuppied_positions):
                    solutions += place_queen(n, ocuppied_positions + [pos])
            return solutions
```