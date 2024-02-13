import java.io.*;
import java.util.*;

public class BOJ2564 {

    static int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    static int N, M, s, side, dist, si, sj, ni, nj, cnt, ans;
    static int[][] arr;
    static Node v;

    static class Node {
        public int i;
        public int j;

        public Node(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

    public static void bfs() {
        Queue<Node> q = new LinkedList<>();
        int[][] visited = new int[N+1][M+1];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= M; j++) {
                visited[i][j] = -1;
            }
        }
        q.offer(new Node(si, sj));
        visited[si][sj] = 0;

        while (true) {
            v = q.poll();

            if (arr[v.i][v.j] == 1) {
                ans += visited[v.i][v.j];
                cnt++;
                if (cnt == s) break;
            }

            for (int d = 0; d < 4; d++) {
                ni = v.i + dir[d][0];
                nj = v.j + dir[d][1];
                if (0 <= ni && ni <= N && 0 <= nj && nj <= M
                        && (ni == 0 || ni == N || nj == 0 || nj == M)
                        && visited[ni][nj] == -1) {
                    q.offer(new Node(ni, nj));
                    visited[ni][nj] = visited[v.i][v.j] + 1;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        arr = new int[N+1][M+1];

        s = Integer.parseInt(br.readLine());
        for (int i = 0; i < s; i++) {
            st = new StringTokenizer(br.readLine());
            side = Integer.parseInt(st.nextToken());
            dist = Integer.parseInt(st.nextToken());

            if (side == 1)      arr[0][dist] = 1;
            else if (side == 2) arr[N][dist] = 1;
            else if (side == 3) arr[dist][0] = 1;
            else                arr[dist][M] = 1;
        }

        st = new StringTokenizer(br.readLine());
        side = Integer.parseInt(st.nextToken());
        dist = Integer.parseInt(st.nextToken());
        if (side == 1) {
            si = 0;
            sj = dist;
        } else if (side == 2) {
            si = N;
            sj = dist;
        } else if (side == 3) {
            si = dist;
            sj = 0;
        } else {
            si = dist;
            sj = M;
        }

        bfs();

        System.out.println(ans);
    }

}
