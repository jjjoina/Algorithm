import java.io.*;
import java.util.*;

public class BOJ1600 {
    static int K, W, H;
    static int[][] arr;
    static int[][][] visited;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};
    static int[] hi = {1, 2, 2, 1, -1, -2, -2, -1};
    static int[] hj = {2, 1, -1, -2, -2, -1, 1, 2};
    static int ans = -1;

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

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        K = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        arr = new int[H][W];
        visited = new int[H][W][K+1];
        for (int i = 0; i < H; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < W; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Queue<Node> q = new ArrayDeque<>();
        q.offer(new Node(0, 0, 0));
        visited[0][0][0] = 1;
        while (!q.isEmpty()) {
            Node v = q.poll();
            if (v.i == H - 1 && v.j == W - 1) {
                ans = visited[v.i][v.j][v.k] - 1;
                break;
            }
            for (int d = 0; d < 4; d++) {   // 4방향으로 움직임
                int ni = v.i + di[d];
                int nj = v.j + dj[d];
                if (ni >= 0 && ni < H && nj >= 0 && nj < W && visited[ni][nj][v.k] == 0 && arr[ni][nj] == 0) {
                    q.offer(new Node(ni, nj, v.k));
                    visited[ni][nj][v.k] = visited[v.i][v.j][v.k] + 1;
                }
            }
            if (v.k < K) {  // 말처럼 움직임 가능
                for (int d = 0; d < 8; d++) {
                    int ni = v.i + hi[d];
                    int nj = v.j + hj[d];
                    if (ni >= 0 && ni < H && nj >= 0 && nj < W && visited[ni][nj][v.k+1] == 0 && arr[ni][nj] == 0) {
                        q.offer(new Node(ni, nj, v.k + 1));
                        visited[ni][nj][v.k+1] = visited[v.i][v.j][v.k] + 1;
                    }
                }
            }
        }

        System.out.println(ans);
    }
}
