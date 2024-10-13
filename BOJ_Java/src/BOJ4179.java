import java.io.*;
import java.util.*;

public class BOJ4179 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int R;
    static int C;
    static int[][] arr;
    static ArrayDeque<int[]> jihunQ = new ArrayDeque<>();
    static ArrayDeque<int[]> fireQ = new ArrayDeque<>();
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        arr = new int[R][C];
        /*
        0 : 빈칸
        1 이상 : 거리 (지나온 곳)
        -1 : 벽
        -2 : 불
         */
        for (int i = 0; i < R; i++) {
            String str = br.readLine();
            for (int j = 0; j < C; j++) {
                if (str.charAt(j) == '#') {
                    arr[i][j] = -1;
                } else if (str.charAt(j) == 'J') {
                    arr[i][j] = 1;
                    jihunQ.offer(new int[]{i, j});
                } else if (str.charAt(j) == 'F') {
                    arr[i][j] = -2;
                    fireQ.offer(new int[]{i, j});
                }
            }
        }
    }

    static boolean spreadJihun() {
        ArrayDeque<int[]> nextJihunQ = new ArrayDeque<>();

        while (!jihunQ.isEmpty()) {
            int[] jihun = jihunQ.poll();

            if (arr[jihun[0]][jihun[1]] == -2) {    // 지훈이가 있던 자리에 불이 침범한 경우
                continue;
            }

            for (int d = 0; d < 4; d++) {
                int ni = jihun[0] + di[d];
                int nj = jihun[1] + dj[d];

                if (ni < 0 || ni >= R || nj < 0 || nj >= C) {   // 탈출 성공한 경우
                    System.out.println(arr[jihun[0]][jihun[1]]);
                    return true;
                }

                if (arr[ni][nj] == 0) {     // 지훈이는 빈칸으로만 이동 가능
                    nextJihunQ.offer(new int[]{ni, nj});
                    arr[ni][nj] = arr[jihun[0]][jihun[1]] + 1;
                }
            }
        }

        jihunQ = nextJihunQ;

        return false;
    }

    static void spreadFire() {
        ArrayDeque<int[]> nextFireQ = new ArrayDeque<>();

        while (!fireQ.isEmpty()) {
            int[] fire = fireQ.poll();

            for (int d = 0; d < 4; d++) {
                int ni = fire[0] + di[d];
                int nj = fire[1] + dj[d];

                if (ni < 0 || ni >= R || nj < 0 || nj >= C) {
                    continue;
                }

                if (arr[ni][nj] >= 0) {     // 불은 빈칸이거나 지훈이가 있는 곳에 번짐
                    nextFireQ.offer(new int[]{ni, nj});
                    arr[ni][nj] = -2;
                }
            }
        }

        fireQ = nextFireQ;
    }

    public static void main(String[] args) throws IOException {
        input();

        while (!jihunQ.isEmpty()) {
            if (spreadJihun()) {
                return;
            }

            spreadFire();
        }

        System.out.println("IMPOSSIBLE");
    }
}
