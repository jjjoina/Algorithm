import java.io.*;
import java.util.*;

public class BOJ16932 {
    static int N, M;
    static int[][] arr;
    static int[][] numbering;
    static int shapeNumber = 0;
    static ArrayList<Integer> shapeSize = new ArrayList<>();
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    static void bfs(int i, int j) {
        shapeSize.add(1);
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{i, j});
        numbering[i][j] = ++shapeNumber;

        while (!q.isEmpty()) {
            int[] p = q.poll();

            for (int d = 0; d < 4; d++) {
                int ni = p[0] + di[d];
                int nj = p[1] + dj[d];

                if (ni >= 0 && ni < N && nj >= 0 && nj < M && arr[ni][nj] == 1 && numbering[ni][nj] == 0) {
                    q.offer(new int[]{ni, nj});
                    numbering[ni][nj] = shapeNumber;
                    shapeSize.set(shapeNumber, shapeSize.get(shapeNumber) + 1);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        numbering = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        shapeSize.add(0);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 1 && numbering[i][j] == 0) {
                    bfs(i, j);
                }
            }
        }

//        for (int[] row : numbering) {
//            System.out.println(Arrays.toString(row));
//        }

        int answer = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (numbering[i][j] == 0) {
                    HashSet<Integer> around = new HashSet<>();

                    for (int d = 0; d < 4; d++) {
                        int ni = i + di[d];
                        int nj = j + dj[d];

                        if (ni >= 0 && ni < N && nj >= 0 && nj < M && numbering[ni][nj] > 0) {
                            around.add(numbering[ni][nj]);
                        }
                    }

                    int result = 1;

                    for (int shape : around) {
                        result += shapeSize.get(shape);
                    }

                    if (answer < result) {
                        answer = result;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
