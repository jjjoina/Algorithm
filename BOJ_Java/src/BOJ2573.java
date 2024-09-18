import java.io.*;
import java.util.*;

public class BOJ2573 {
    static int N;
    static int M;
    static int[][] arr;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    static int[] findStartPoint() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] > 0) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{-1, -1};
    }

    static void melt() {
        int[] startPoint = findStartPoint();
        ArrayDeque<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][M];
        q.offer(startPoint);
        visited[startPoint[0]][startPoint[1]] = true;

        while (!q.isEmpty()) {
            int[] point = q.poll();

            for (int d = 0; d < 4; d++) {
                int ni = point[0] + di[d];
                int nj = point[1] + dj[d];

                if (ni >= 0 && ni < N && nj >= 0 && nj < M && !visited[ni][nj]) {
                    if (arr[ni][nj] > 0) {
                        q.offer(new int[]{ni, nj});
                        visited[ni][nj] = true;
                    } else {
                        arr[point[0]][point[1]]--;
                        if (arr[point[0]][point[1]] < 0) {
                            arr[point[0]][point[1]] = 0;
                        }
                    }
                }
            }
        }
    }

    static void bfs(int[] startPoint, boolean[][] visited) {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(startPoint);
        visited[startPoint[0]][startPoint[1]] = true;

        while (!q.isEmpty()) {
            int[] point = q.poll();

            for (int d = 0; d < 4; d++) {
                int ni = point[0] + di[d];
                int nj = point[1] + dj[d];

                if (ni >= 0 && ni < N && nj >= 0 && nj < M && !visited[ni][nj] && arr[ni][nj] > 0) {
                    q.offer(new int[]{ni, nj});
                    visited[ni][nj] = true;
                }
            }
        }
    }

    static int getResult() {
        int result = 0;
        boolean[][] visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 0) {
                    continue;
                }

                if (result == 0) {
                    bfs(new int[]{i, j}, visited);
                    result = 1;
                } else if (!visited[i][j]) {
                    return 2;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = 1;

        while (true) {
            melt();

            int result = getResult();

            if (result == 0) {
                answer = 0;
                break;
            } else if (result == 2) {
                break;
            }

            answer++;
        }

        System.out.println(answer);
    }
}
