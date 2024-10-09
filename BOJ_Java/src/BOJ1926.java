import java.io.*;
import java.util.*;

public class BOJ1926 {
    static int n;
    static int m;
    static boolean[][] arr;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = st.nextToken().equals("1");
            }
        }
    }

    static int bfs(int i, int j) {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{i, j});
        arr[i][j] = false;
        int area = 1;

        while (!q.isEmpty()) {
            int[] p = q.poll();

            for (int d = 0; d < 4; d++) {
                int ni = p[0] + di[d];
                int nj = p[1] + dj[d];

                if (ni >= 0 && ni < n && nj >= 0 && nj < m && arr[ni][nj]) {
                    q.offer(new int[]{ni, nj});
                    arr[ni][nj] = false;
                    area++;
                }
            }
        }

        return area;
    }

    public static void main(String[] args) throws IOException {
        input();

        int countPicture = 0;
        int maxArea = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j]) {
                    countPicture++;
                    maxArea = Math.max(maxArea, bfs(i, j));
                }
            }
        }

        System.out.println(countPicture);
        System.out.println(maxArea);
    }
}