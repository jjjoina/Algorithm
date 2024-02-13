import java.io.*;
import java.util.*;

public class BOJ17087_2 {
    static int gcd(int a, int b) {
        int temp;
        while (b > 0) {
            temp = a;
            a = b;
            b = temp % b;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        int[] dist = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            dist[i] = Math.abs(Integer.parseInt(st.nextToken()) - S);
        }

        int ans = dist[0];
        for (int i = 1; i < N; i++) {
            ans = gcd(Math.max(ans, dist[i]), Math.min(ans, dist[i]));
        }

        System.out.println(ans);
    }
}
