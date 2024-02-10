import java.io.*;

public class BOJ1913 {
    static int[] di = {1, 0, -1, 0};
    static int[] dj = {0, 1, 0, -1};
    static int[][] arr;
    static int N, a, cnt, i, j, d, ai, aj, ni, nj;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        a = Integer.parseInt(br.readLine());

        arr = new int[N][N];
        cnt = N * N;

        while (cnt > 0) {
            arr[i][j] = cnt;
            if (cnt == a) {
                ai = i + 1;
                aj = j + 1;
            }

            ni = i + di[d];
            nj = j + dj[d];
            if (ni < 0 || ni >= N || nj < 0 || nj >= N || arr[ni][nj] != 0) {
                d = (d+1) % 4;
            }
            i += di[d];
            j += dj[d];

            cnt--;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                bw.write(arr[i][j] + " ");
            }
            bw.newLine();
        }
        bw.write(ai + " " + aj);

        bw.close();
    }
}
