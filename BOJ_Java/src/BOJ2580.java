import java.io.*;
import java.util.*;

public class BOJ2580 {
    static int[][] arr = new int[9][9];
    static boolean flag = false;

    static void print() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append(arr[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    static boolean isPossible(int i, int j, int n) {
        for (int c = 0; c < 9; c++) {
            if (arr[i][c] == n)
                return false;
        }

        for (int r = 0; r < 9; r++) {
            if (arr[r][j] == n)
                return false;
        }

        int sr = i / 3 * 3;
        int sc = j / 3 * 3;
        for (int r = sr; r < sr + 3; r++) {
            for (int c = sc; c < sc + 3; c++) {
                if (arr[r][c] == n)
                    return false;
            }
        }

        return true;
    }

    static void backTracking(int idx) {
        if (flag) return;

        if (idx == 81) {
            print();
            flag = true;
            return;
        }

        int i = idx / 9;
        int j = idx % 9;

        if (arr[i][j] == 0) {
            for (int n = 1; n <= 9; n++) {
                if (isPossible(i, j, n)) {
                    arr[i][j] = n;
                    backTracking(idx + 1);
                    arr[i][j] = 0;
                }
            }
        } else {
            backTracking(idx + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int i = 0; i < 9; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        backTracking(0);
    }
}
