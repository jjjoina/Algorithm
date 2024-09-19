import java.io.*;
import java.util.*;

public class BOJ21610 {
    static int N;
    static int M;
    static int[][] arr;
    static boolean[][] clouds;
    static boolean[][] cloudsAfterMove;
    static int[] di = {0, -1, -1, -1, 0, 1, 1, 1};
    static int[] dj = {-1, -1, 0, 1, 1, 1, 0, -1};

    static void initCloud() {
        clouds = new boolean[N][N];
        clouds[N - 2][0] = true;
        clouds[N - 2][1] = true;
        clouds[N - 1][0] = true;
        clouds[N - 1][1] = true;
    }

    static void moveCloudAndRain(int d, int s) {
        cloudsAfterMove = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (clouds[i][j]) {
                    int ni = (i + di[d] * s) % N;
                    int nj = (j + dj[d] * s) % N;
                    if (ni < 0) ni += N;
                    if (nj < 0) nj += N;

                    cloudsAfterMove[ni][nj] = true;
                    arr[ni][nj]++;
                }
            }
        }
    }

    static void waterCopyBug() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (cloudsAfterMove[i][j]) {
                    for (int d = 1; d < 8; d += 2) {
                        int ni = i + di[d];
                        int nj = j + dj[d];

                        if (ni >= 0 && ni < N && nj >= 0 && nj < N && arr[ni][nj] > 0) {
                            arr[i][j]++;
                        }
                    }
                }
            }
        }
    }

    static void makeCloud() {
        clouds = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] >= 2 && !cloudsAfterMove[i][j]) {
                    clouds[i][j] = true;
                    arr[i][j] -= 2;
                }
            }
        }
    }

    static int getAnswer() {
        int answer = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                answer += arr[i][j];
            }
        }

        return answer;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        initCloud();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());

            moveCloudAndRain(d - 1, s);
            waterCopyBug();
            makeCloud();
        }

        System.out.println(getAnswer());
    }
}
