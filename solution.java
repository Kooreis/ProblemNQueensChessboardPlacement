```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int n = 4;
        solveNQueens(n).forEach(System.out::println);
    }

    public static List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        int[] queens = new int[n];
        placeQueen(queens, 0, n, result);
        return result;
    }

    private static void placeQueen(int[] queens, int row, int n, List<List<String>> result) {
        if (row == n) {
            addResult(queens, result);
            return;
        }

        for (int i = 0; i < n; i++) {
            queens[row] = i;
            if (isValid(queens, row)) {
                placeQueen(queens, row + 1, n, result);
            }
        }
    }

    private static boolean isValid(int[] queens, int row) {
        for (int i = 0; i < row; i++) {
            if (queens[i] == queens[row] || Math.abs(queens[i] - queens[row]) == (row - i)) {
                return false;
            }
        }
        return true;
    }

    private static void addResult(int[] queens, List<List<String>> result) {
        List<String> list = new ArrayList<>();
        for (int i = 0; i < queens.length; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < queens.length; j++) {
                if (queens[i] == j) {
                    sb.append("Q");
                } else {
                    sb.append(".");
                }
            }
            list.add(sb.toString());
        }
        result.add(list);
    }
}
```