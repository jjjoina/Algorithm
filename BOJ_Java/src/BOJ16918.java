import java.io.*;
import java.util.*;

public class BOJ16918 {
    static int R;
    static int C;
    static int N;
    static int[][] arr;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        arr = new int[R][C];
        for (int i = 0; i < R; i++) {
            String row = br.readLine();
            for (int j = 0; j < C; j++) {
                arr[i][j] = row.charAt(j) == 'O' ? 0 : -1;
            }
        }
    }

    static void plant(int time) {
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (arr[i][j] == -1) {
                    arr[i][j] = time;
                }
            }
        }
    }

    static void explode(int time) {
        int[][] temp = new int[R][C];

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                temp[i][j] = arr[i][j];
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (arr[i][j] == time - 3) {
                    temp[i][j] = -1;
                    for (int d = 0; d < 4; d++) {
                        int ni = i + di[d];
                        int nj = j + dj[d];
                        if (ni >= 0 && ni < R && nj >= 0 && nj < C) {
                            temp[ni][nj] = -1;
                        }
                    }
                }
            }
        }

        arr = temp;
    }

    static void output() {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                sb.append(arr[i][j] != -1 ? 'O' : '.');
            }
            sb.append('\n');
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException {
        input();

        int time = 1;

        while (time < N) {
            time++;

            if (time % 2 == 0) {
                plant(time);
            } else {
                explode(time);
            }
        }

        output();
    }
}
