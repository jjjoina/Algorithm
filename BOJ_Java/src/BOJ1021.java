import java.io.*;
import java.util.*;

public class BOJ1021 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] curIdx = new int[N];
        for (int i = 0; i < N; i++) {
            curIdx[i] = i;
        }

        int l = N;
        int ans = 0;

        int[] lst = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            lst[i] = Integer.parseInt(st.nextToken()) - 1;
        }

        for (int A : lst) {
            if (curIdx[A] < l - curIdx[A]) {
                int round = curIdx[A];
                ans += round;
                for (int i = 0; i < N; i++) {
                    if (curIdx[i] == -1) continue;
                    curIdx[i] -= round;
                    if (curIdx[i] < 0) curIdx[i] += l;
                    curIdx[i]--;
                }
            } else {
                int round = l - curIdx[A];
                ans += round;
                for (int i = 0; i < N; i++) {
                    if (curIdx[i] == -1) continue;
                    curIdx[i] += round;
                    if (curIdx[i] >= l) curIdx[i] -= l;
                    curIdx[i]--;
                }
            }

            l--;
            curIdx[A] = -1;
        }

        System.out.println(ans);
    }
}
