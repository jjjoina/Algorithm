import java.io.*;
import java.util.*;

public class BOJ17144 {
    static int R, C, T, ac, ans = 0, ni, nj, amount;
    static int[][] arr, temp;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        arr = new int[R][C];
        temp = new int[R][C];
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                temp[i][j] = 0;
            }
        }

        // 공기청정기 찾기
        for (int i = 0; i < R; i++) {
            if (arr[i][0] == -1) {
                ac = i;
                break;
            }
        }

        for (int t = 0; t < T; t++) {
            // 확산
            // temp에 저장한뒤에 arr에 더하기
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (arr[i][j] <= 0) continue;
                    amount = arr[i][j] / 5;
                    // 벽이 아니고 공기청청기가 아닌 구역에만 퍼짐
                    for (int d = 0; d < 4; d++) {
                        ni = i + di[d];
                        nj = j + dj[d];
                        if (ni < 0 || ni >= R || nj < 0 || nj >= C) continue;
                        if ((ni == ac || ni == ac + 1) && nj == 0) continue;
                        temp[ni][nj] += amount;
                        temp[i][j] -= amount;
                    }
                }
            }

            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    arr[i][j] += temp[i][j];
                    temp[i][j] = 0;
                }
            }

            // 위쪽 순환
            int i = ac - 1, j = 0, d = 3;
            while (true) {
                ni = i + di[d];
                nj = j + dj[d];
                if (ni < 0 || ni > ac || nj < 0 || nj >= C) {
                    d++;
                    if (d == 4) d = 0;
                    ni = i + di[d];
                    nj = j + dj[d];
                }

                if (ni == ac && nj == 0) {
                    arr[i][j] = 0;
                    break;
                }

                arr[i][j] = arr[ni][nj];
                i = ni;
                j = nj;
            }

            // 아래쪽 순환
            i = ac + 2;
            j = 0;
            d = 1;
            while (true) {
                ni = i + di[d];
                nj = j + dj[d];
                if (ni <= ac || ni >= R || nj < 0 || nj >= C) {
                    d--;
                    if (d == -1) d = 3;
                    ni = i + di[d];
                    nj = j + dj[d];
                }

                if (ni == ac + 1 && nj == 0) {
                    arr[i][j] = 0;
                    break;
                }

                arr[i][j] = arr[ni][nj];
                i = ni;
                j = nj;
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (arr[i][j] > 0) ans += arr[i][j];
            }
        }

        System.out.println(ans);
    }
}
