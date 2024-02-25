import java.io.*;
import java.util.*;

public class BOJ16946 {
    static class Point {
        int i, j;

        public Point(int i, int j) {
            this.i = i;
            this.j = j;
        }

        @Override
        public int hashCode() {
            return Objects.hash(i, j);
        }

        @Override
        public boolean equals(Object obj) {
            Point p = (Point) obj;
            return p.i == this.i && p.j == this.j;
        }
    }

    static int N, M;
    static int[][] arr;
    static boolean[][] visited;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    public static void bfs(int si, int sj) {
        Queue<Point> q = new ArrayDeque<>();
        Set<Point> walls = new HashSet<>();
        int cnt = 1;

        q.offer(new Point(si, sj));
        visited[si][sj] = true;

        while (!q.isEmpty()) {
            Point p = q.poll();
            for (int d = 0; d < 4; d++) {
                int ni = p.i + di[d];
                int nj = p.j + dj[d];
                if (0 <= ni && ni < N && 0 <= nj && nj < M) {
                    if (arr[ni][nj] > 0) {
                        walls.add(new Point(ni, nj));
                    }
                    else if (!visited[ni][nj]) {
                        q.offer(new Point(ni, nj));
                        visited[ni][nj] = true;
                        cnt++;
                    }
                }
            }
        }

        for (Point w : walls) {
            arr[w.i][w.j] += cnt;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        visited = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = s.charAt(j) - '0';
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 0 && !visited[i][j]) bfs(i, j);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(arr[i][j] % 10);
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
