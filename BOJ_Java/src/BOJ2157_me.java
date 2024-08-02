import java.io.*;
import java.util.*;

public class BOJ2157_me {
    static int N, M, K;
    static HashMap<Integer, Integer>[] adjD;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        adjD = new HashMap[N + 1];
        for (int i = 0; i < N + 1; i++) {
            adjD[i] = new HashMap<>();
        }

        for (int k = 0; k < K; k++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a < b && adjD[a].getOrDefault(b, 0) < c) {
                adjD[a].put(b, c);
            }
        }

        dp = new int[N + 1][M];
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }
        dp[1][0] = 0;

        for (int v = 1; v < N; v++) {
            for (int cnt = 0; cnt < M - 1; cnt++) {
                if (dp[v][cnt] < 0) continue;

                for (Map.Entry<Integer, Integer> entry : adjD[v].entrySet()) {
                    int w = entry.getKey();
                    int score = entry.getValue();
                    dp[w][cnt + 1] = Math.max(dp[w][cnt + 1], dp[v][cnt] + score);
                }
            }
        }

        int ans = 0;
        for (int num : dp[N]) {
            ans = Math.max(ans, num);
        }

        System.out.println(ans);
    }
}
