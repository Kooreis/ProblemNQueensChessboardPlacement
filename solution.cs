Here is a simple console application in C# that solves the N-Queens problem:

```csharp
using System;

class Program
{
    static int N = 8;
    static int[] position = new int[N];

    static void Main(string[] args)
    {
        Solve();
    }

    static void Solve()
    {
        PutQueen(position, 0);
    }

    static void PutQueen(int[] position, int targetRow)
    {
        if (targetRow == N)
        {
            PrintQueens(position);
            return;
        }
        for (int column = 0; column < N; column++)
        {
            if (Check(position, targetRow, column))
            {
                position[targetRow] = column;
                PutQueen(position, targetRow + 1);
            }
        }
    }

    static bool Check(int[] position, int occupiedRows, int column)
    {
        for (int i = 0; i < occupiedRows; i++)
        {
            if (position[i] == column || (i - occupiedRows) == (position[i] - column) || (i - occupiedRows) == (column - position[i]))
            {
                return false;
            }
        }
        return true;
    }

    static void PrintQueens(int[] position)
    {
        for (int row = 0; row < N; row++)
        {
            for (int column = 0; column < N; column++)
            {
                if (position[row] == column)
                {
                    Console.Write(" Q ");
                }
                else
                {
                    Console.Write(" * ");
                }
            }
            Console.WriteLine();
        }
        Console.WriteLine();
    }
}
```

This program uses a backtracking algorithm to solve the N-Queens problem. It starts by placing a queen in the first column of the first row, then moves to the next row. If it finds a conflict, it moves the queen to the next column. If it can't find a place to put the queen in the current row, it backtracks and moves the queen in the previous row to the next column. This process continues until it has placed all N queens on the board.