import java.io.*;
import java.util.*;

public class BOJ1074 {
    static int N, r, c, ans;

    static void recur(int si, int sj, int n) {
        if (n == 0) return;

        if (r < si + Math.pow(2, n - 1)) {
            if (c < sj + Math.pow(2, n - 1)) {
                recur(si, sj, n - 1);
            } else {
                ans += (int) Math.pow(4, n - 1);
                recur(si, sj + (int) Math.pow(2, n - 1), n - 1);
            }
        } else {
            if (c < sj + Math.pow(2, n - 1)) {
                ans += 2 * (int) Math.pow(4, n - 1);
                recur(si + (int) Math.pow(2, n - 1), sj, n - 1);
            } else {
                ans += 3 * (int) Math.pow(4, n - 1);
                recur(si + (int) Math.pow(2, n - 1), sj + (int) Math.pow(2, n - 1), n - 1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        recur(0, 0, N);

        System.out.println(ans);
    }
}
