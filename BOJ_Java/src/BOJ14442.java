import java.io.*;
import java.util.*;

public class BOJ14442 {
    static class Node {
        int i;
        int j;
        int k;

        Node(int i, int j, int k) {
            this.i = i;
            this.j = j;
            this.k = k;
        }
    }

    static int N;
    static int M;
    static int K;
    static int[][] arr;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = s.charAt(j) - '0';
            }
        }
    }

    static int bfs() {
        ArrayDeque<Node> q = new ArrayDeque<>();
        int[][][] visited = new int[N][M][K + 1];
        q.offer(new Node(0, 0, 0));
        visited[0][0][0] = 1;

        while (!q.isEmpty()) {
            Node node = q.poll();

            if (node.i == N - 1 && node.j == M - 1) {
                return visited[node.i][node.j][node.k];
            }

            for (int d = 0; d < 4; d++) {
                int ni = node.i + di[d];
                int nj = node.j + dj[d];

                if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
                    if (arr[ni][nj] == 0 && visited[ni][nj][node.k] == 0) {
                        q.offer(new Node(ni, nj, node.k));
                        visited[ni][nj][node.k] = visited[node.i][node.j][node.k] + 1;
                    } else {
                        if (node.k < K && visited[ni][nj][node.k + 1] == 0) {
                            q.offer(new Node(ni, nj, node.k + 1));
                            visited[ni][nj][node.k + 1] = visited[node.i][node.j][node.k] + 1;
                        }
                    }
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {
        input();

        System.out.println(bfs());
    }
}
