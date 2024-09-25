import java.io.*;
import java.util.*;

public class BOJ2583 {
    static int M;
    static int N;
    static int K;
    static boolean[][] arr;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new boolean[N][M];

        for (int k = 0; k < K; k++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            for (int x = x1; x < x2; x++) {
                for (int y = y1; y < y2; y++) {
                    arr[x][y] = true;
                }
            }
        }
    }

    static int bfs(int i, int j) {
        int area = 0;
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{i, j});
        arr[i][j] = true;

        while (!q.isEmpty()) {
            int[] p = q.poll();

            area++;

            for (int d = 0; d < 4; d++) {
                int ni = p[0] + di[d];
                int nj = p[1] + dj[d];

                if (ni >= 0 && ni < N && nj >= 0 && nj < M && !arr[ni][nj]) {
                    q.offer(new int[]{ni, nj});
                    arr[ni][nj] = true;
                }
            }
        }

        return area;
    }

    static void output(int answerCount, ArrayList<Integer> areas) {
        StringBuilder sb = new StringBuilder();

        sb.append(answerCount).append("\n");

        for (int area : areas) {
            sb.append(area).append(" ");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException {
        input();

        int answerCount = 0;
        ArrayList<Integer> areas = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!arr[i][j]) {
                    areas.add(bfs(i, j));
                    answerCount++;
                }
            }
        }

        Collections.sort(areas);

        output(answerCount, areas);
    }
}
