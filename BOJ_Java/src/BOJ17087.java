import java.io.*;
import java.util.*;

public class BOJ17087 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        int[] A = new int[N];
        int minDist = Integer.MAX_VALUE;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
            int dist = Math.abs(S - A[i]);
            if (minDist > dist) minDist = dist;
        }

        for (int d = minDist; d > 0; d--) {
            boolean flag = true;
            for (int i = 0; i < N; i++) {
                if ((S - A[i]) % d != 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                System.out.println(d);
                break;
            }
        }
    }
}
