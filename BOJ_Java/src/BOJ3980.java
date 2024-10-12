import java.io.*;
import java.util.*;

public class BOJ3980 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int T;
    static int[][] arr;
    static boolean[] selected;
    static int answer;

    static void init() throws IOException {
        arr = new int[11][11];
        for (int i = 0; i < 11; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 11; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        selected = new boolean[11];
        answer = 0;
    }

    static void backtracking(int i, int sum) {
        if (sum + (11 - i) * 100 <= answer) {
            return;
        }

        if (i == 11) {
            answer = sum;
            return;
        }

        for (int j = 0; j < 11; j++) {
            if (arr[i][j] > 0 && !selected[j]) {
                selected[j] = true;
                backtracking(i + 1, sum + arr[i][j]);
                selected[j] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            init();

            backtracking(0, 0);

            sb.append(answer).append("\n");
        }

        System.out.println(sb);
    }
}
