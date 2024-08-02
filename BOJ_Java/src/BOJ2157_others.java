import java.io.*;
import java.util.*;

public class BOJ2157_others {
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

        dp = new int[N + 1][M + 1];
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{1, 1});   // {도시 번호, 경유한 도시 수}

        while (!q.isEmpty()) {
            int[] node = q.poll();
            int v = node[0];
            int cnt = node[1];

            if (cnt == M) continue;

            for (Map.Entry<Integer, Integer> entry : adjD[v].entrySet()) {
                int w = entry.getKey();
                int score = entry.getValue();

                if (dp[w][cnt + 1] == 0) {  // {w, cnt} 쌍을 큐에 한번만 넣기 위함
                    q.offer(new int[]{w, cnt + 1});
                }

                dp[w][cnt + 1] = Math.max(dp[w][cnt + 1], dp[v][cnt] + score);
            }
        }

        int ans = 0;
        for (int num : dp[N]) {
            ans = Math.max(ans, num);
        }

        System.out.println(ans);
    }
}
