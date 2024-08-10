import java.io.*;
import java.util.*;

public class BOJ10942 {
    static int N, M;
    static int[] lst;
    static int[][] ansM;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        lst = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            lst[i] = Integer.parseInt(st.nextToken());
        }
        ansM = new int[N][N];

        for (int i = 0; i < N; i++) {
            int l = i;
            int r = i;

            while (l >= 0 && r < N && lst[l] == lst[r]) {
                ansM[l--][r++] = 1;
            }

            l = i;
            r = i + 1;

            while (l >= 0 && r < N && lst[l] == lst[r]) {
                ansM[l--][r++] = 1;
            }
        }

        M = Integer.parseInt(br.readLine());
        for (int m = 0; m < M; m++) {
            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            sb.append(ansM[S - 1][E - 1]).append("\n");
        }

        System.out.println(sb);
    }
}
