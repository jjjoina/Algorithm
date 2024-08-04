import java.io.*;
import java.util.*;

public class BOJ16174_dp {
    static int N;
    static int[][] arr;
    static boolean[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp = new boolean[N][N];
        dp[0][0] = true;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!dp[i][j]) continue;
                if (i + arr[i][j] < N) dp[i + arr[i][j]][j] = true;
                if (j + arr[i][j] < N) dp[i][j + arr[i][j]] = true;
            }
        }

        System.out.println(dp[N - 1][N - 1] ? "HaruHaru" : "Hing");
    }
}
