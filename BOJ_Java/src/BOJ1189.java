import java.io.*;
import java.util.*;

public class BOJ1189 {
    static int R;
    static int C;
    static int K;
    static char[][] arr;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};
    static int ans = 0;

    static void dfs(int i, int j, int depth) {
        if (depth == K && i == 0 && j == C - 1) {
            ans++;
        }

        if (depth >= K) {
            return;
        }

        for (int d = 0; d < 4; d++) {
            int ni = i + di[d];
            int nj = j + dj[d];

            if (ni >= 0 && ni < R && nj >= 0 && nj < C && arr[ni][nj] != 'T') {
                arr[ni][nj] = 'T';
                dfs(ni, nj, depth + 1);
                arr[ni][nj] = '.';
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new char[R][C];
        for (int i = 0; i < R; i++) {
            arr[i] = br.readLine().toCharArray();
        }

        arr[R - 1][0] = 'T';
        dfs(R - 1, 0, 1);

        System.out.println(ans);
    }
}
