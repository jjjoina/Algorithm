import java.io.*;
import java.util.*;

public class BOJ17069 {
    static int N;
    static int[][] arr;
    static long[][][] dp;
    /*
    dp[i][j][d] : i, j를 기준으로 d 방향으로 놓을 수 있는 경우의 수
    d : 0(가로), 1(대각선), 2(세로)
     */

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        dp = new long[N][N][3];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                for (int d = 0; d < 3; d++) {
                    dp[i][j][d] = 0;
                }
            }
        }
        dp[0][0][0] = 1;

        /*
        (i, j)에 가로로 놓여져 있을 수 있는 경우는
            (i, j-1)에 가로로 놓여져 있었거나
            (i-1, j-1)에 대각선으로 놓여져 있었던 경우

        (i, j)에 대각선으로 놓여져 있을 수 있는 경우는
            (i, j-1)에 가로로 놓여져 있었거나
            (i-1, j-1)에 대각선으로 놓여져 있었거나
            (i-1, j)에 세로로 놓여져 있었던 경우

        (i, j)에 세로로 놓여져 있을 수 있는 경우는
            (i-1, j-1)에 대각선으로 놓여져 있었거나
            (i-1, j)에 세로로 놓여져 있었던 경우
         */

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (j+2 < N && arr[i][j+2] == 0) {
                    dp[i][j+1][0] += dp[i][j][0];
                }
                if (i+1 < N && j+2 < N && arr[i][j+2] == 0 && arr[i+1][j+1] == 0 && arr[i+1][j+2] == 0) {
                    dp[i][j+1][1] += dp[i][j][0];
                }
                if (i+1 < N && j+2 < N && arr[i+1][j+2] == 0) {
                    dp[i+1][j+1][0] += dp[i][j][1];
                }
                if (i+2 < N && j+2 < N && arr[i+1][j+2] == 0 && arr[i+2][j+1] == 0 && arr[i+2][j+2] == 0) {
                    dp[i+1][j+1][1] += dp[i][j][1];
                }
                if (i+2 < N && j+1 < N && arr[i+2][j+1] == 0) {
                    dp[i+1][j+1][2] += dp[i][j][1];
                }
                if (i+2 < N && arr[i+2][j] == 0) {
                    dp[i+1][j][2] += dp[i][j][2];
                }
                if (i+2 < N && j+1 < N && arr[i+1][j+1] == 0 && arr[i+2][j] == 0 && arr[i+2][j+1] == 0) {
                    dp[i+1][j][1] += dp[i][j][2];
                }
            }
        }

        System.out.println(dp[N-2][N-2][1] + dp[N-2][N-1][2] + dp[N-1][N-2][0]);
    }
}
