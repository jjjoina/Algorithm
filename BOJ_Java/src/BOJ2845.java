import java.io.*;
import java.util.*;

public class BOJ2845 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int L = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        int real = L * P;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 5; i++) {
            int n = Integer.parseInt(st.nextToken());
            System.out.print(n - real + " ");
        }
    }
}
