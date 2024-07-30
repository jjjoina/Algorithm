import java.io.*;
import java.util.*;

public class BOJ20058 {
    static int N, Q;
    static int size;
    static int[][] A;
    static int[] L;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    static void rotate(int si, int sj, int s) {
        ArrayDeque<Integer> q = new ArrayDeque<>();

        for (int i = si; i < si + s; i++) {
            for (int j = sj; j < sj + s; j++) {
                q.offer(A[i][j]);
            }
        }

        for (int j = sj + s - 1; j >= sj; j--) {
            for (int i = si; i < si + s; i++) {
                A[i][j] = q.poll();
            }
        }
    }

    static void melt() {
        ArrayDeque<int[]> tmp = new ArrayDeque<>();

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (A[i][j] == 0) continue;

                int cnt = 0;

                for (int d = 0; d < 4; d++) {
                    int ni = i + di[d];
                    int nj = j + dj[d];
                    if (0 <= ni && ni < size && 0 <= nj && nj < size && A[ni][nj] > 0) {
                        cnt += 1;
                    }
                }

                if (cnt < 3) {
                    tmp.offer(new int[]{i, j});
                }
            }
        }

        while (!tmp.isEmpty()) {
            int[] v = tmp.poll();
            A[v[0]][v[1]]--;
        }
    }

    static int bfs(int si, int sj, boolean[][] visited) {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{si, sj});
        visited[si][sj] = true;
        int cnt = 0;

        while (!q.isEmpty()) {
            int[] v = q.poll();

            cnt++;

            for (int d = 0; d < 4; d++) {
                int ni = v[0] + di[d];
                int nj = v[1] + dj[d];
                if (0 <= ni && ni < size && 0 <= nj && nj < size && !visited[ni][nj] && A[ni][nj] > 0) {
                    q.offer(new int[]{ni, nj});
                    visited[ni][nj] = true;
                }
            }
        }

        return cnt;
    }

    static void printAnswer() {
        int ansSum = 0;
        int ansMax = 0;
        boolean[][] visited = new boolean[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (A[i][j] == 0) continue;

                ansSum += A[i][j];

                if (!visited[i][j]) {
                    int cnt = bfs(i, j, visited);
                    if (ansMax < cnt) ansMax = cnt;
                }
            }
        }

        System.out.println(ansSum);
        System.out.println(ansMax);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        size = (int) Math.pow(2, N);
        A = new int[size][size];
        L = new int[Q];

        for (int i = 0; i < size; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < size; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < Q; i++) {
            L[i] = Integer.parseInt(st.nextToken());
        }

        for (int l : L) {
            int s = (int) Math.pow(2, l);

            for (int i = 0; i < size; i += s) {
                for (int j = 0; j < size; j += s) {
                    rotate(i, j, s);
                }
            }

            melt();
        }

        printAnswer();
    }
}
