import java.io.*;
import java.util.*;

public class BOJ16174_bfs {
    static int N;
    static int[][] arr;
    static int[] di = {0, 1};
    static int[] dj = {1, 0};

    static String bfs() {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][N];
        q.offer(new int[]{0, 0});
        visited[0][0] = true;

        while (!q.isEmpty()) {
            int[] p = q.poll();

            for (int d = 0; d < 2; d++) {
                int ni = p[0] + di[d] * arr[p[0]][p[1]];
                int nj = p[1] + dj[d] * arr[p[0]][p[1]];

                if (0 <= ni && ni < N && 0 <= nj && nj < N && !visited[ni][nj]) {
                    if (arr[ni][nj] == -1) return "HaruHaru";
                    q.offer(new int[]{ni, nj});
                    visited[ni][nj] = true;
                }
            }
        }

        return "Hing";
    }

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

        System.out.println(bfs());
    }
}
