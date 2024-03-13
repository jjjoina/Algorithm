import java.io.*;

public class BOJ31612 {
    static int N, ans;
    static String S;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        S = br.readLine();

        for (int i = 0; i < N; i++) {
            if (S.charAt(i) == 'o') ans += 1;
            else ans += 2;
        }

        System.out.println(ans);
    }
}
