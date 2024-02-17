import java.io.*;
import java.util.*;

public class BOJ17070 {
    static int N, ans = 0;
    static int[][] arr;

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

        dfs(0, 0, 0);

        System.out.println(ans);
    }

    public static void dfs(int i, int j, int dir) {
        // dir : 0(가로), 1(대각선), 2(세로)

        if ((dir == 0 && i == N-1 && j == N-2)
                || (dir == 1 && i == N-2 && j == N-2)
                || (dir == 2 && i == N-2 && j == N-1)) {
            ans++;
            return;
        }

        if (dir == 0) {
            if (j+2 < N && arr[i][j+2] == 0) {
                dfs(i, j+1, 0);
            }
            if (i+1 < N && j+2 < N && arr[i][j+2] == 0 && arr[i+1][j+1] == 0 && arr[i+1][j+2] == 0) {
                dfs(i, j+1, 1);
            }
        } else if (dir == 1) {
            if (i+1 < N && j+2 < N && arr[i+1][j+2] == 0) {
                dfs(i+1, j+1, 0);
            }
            if (i+2 < N && arr[i+2][j+1] == 0) {
                dfs(i+1, j+1, 2);
            }
            if (i+2 < N && j+2 < N && arr[i+1][j+2] == 0 && arr[i+2][j+1] == 0 && arr[i+2][j+2] == 0) {
                dfs(i+1, j+1, 1);
            }
        } else {
            if (i+2 < N && arr[i+2][j] == 0) {
                dfs(i+1, j, 2);
            }
            if (i+2 < N && j+1 < N && arr[i+1][j+1] == 0 && arr[i+2][j] == 0 && arr[i+2][j+1] == 0) {
                dfs(i+1, j, 1);
            }
        }
    }
}
