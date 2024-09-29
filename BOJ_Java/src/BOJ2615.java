import java.io.*;
import java.util.*;

public class BOJ2615 {
    static int[][] arr;
    static int[] di = {-1, 0, 1, 1};
    static int[] dj = {1, 1, 1, 0};

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        arr = new int[19][19];
        for (int i = 0; i < 19; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 19; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    public static void main(String[] args) throws IOException {
        input();

        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                if (arr[i][j] == 0) {
                    continue;
                }

                for (int d = 0; d < 4; d++) {
                    int pi = i - di[d];
                    int pj = j - dj[d];

                    if (pi >= 0 && pi < 19 && pj >= 0 && pj < 19 && arr[pi][pj] == arr[i][j]) {
                        continue;
                    }

                    int count = 1;

                    for (int n = 1; n <= 5; n++) {
                        int ni = i + di[d] * n;
                        int nj = j + dj[d] * n;

                        if (ni >= 0 && ni < 19 && nj >= 0 && nj < 19 && arr[ni][nj] == arr[i][j]) {
                            count++;
                        } else {
                            break;
                        }
                    }

                    if (count == 5) {
                        System.out.println(arr[i][j]);
                        System.out.println((i + 1) + " " + (j + 1));
                        return;
                    }
                }
            }
        }

        System.out.println(0);
    }
}
