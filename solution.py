Sure, here is a Python solution for the N-Queens problem:

```python
def solve_n_queens(n):
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queen(n, ocuppied_positions=[]):
        if n == len(ocuppied_positions):
            return [ocuppied_positions]
        else:
            solutions = []
            for pos in range(n):
                if can_place(pos, ocuppied_positions):
                    solutions += place_queen(n, ocuppied_positions + [pos])
            return solutions

    solutions = place_queen(n)
    return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in solutions]


def main():
    n = int(input("Enter the number of queens: "))
    solutions = solve_n_queens(n)
    for i in range(len(solutions)):
        print("Solution " + str(i + 1) + ":")
        for row in solutions[i]:
            print(row)
        print("\n")


if __name__ == "__main__":
    main()
```

This console application will ask for the number of queens and then print all the possible solutions for the N-Queens problem. Each solution is represented as a list of strings, where each string represents a row on the chessboard. A "Q" represents a queen and a "." represents an empty space.