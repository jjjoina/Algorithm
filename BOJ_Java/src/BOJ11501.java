import java.io.*;
import java.util.StringTokenizer;

public class BOJ11501 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            int[] lst = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++)
                lst[i] = Integer.parseInt(st.nextToken());

            long ans = 0;
            int maxP = lst[N-1];
            for (int i = N-2; i >= 0; i--) {
                if (maxP < lst[i])
                    maxP = lst[i];
                else
                    ans += maxP - lst[i];
            }

            bw.write(ans + "\n");
        }

        br.close();
        bw.close();
    }
}