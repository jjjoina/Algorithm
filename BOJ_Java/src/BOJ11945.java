import java.io.*;
import java.util.*;

public class BOJ11945 {
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = M-1; j >= 0; j--) {
                sb.append(s.charAt(j));
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
