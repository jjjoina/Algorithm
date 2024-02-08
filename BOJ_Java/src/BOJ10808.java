import java.io.*;

public class BOJ10808 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String S = br.readLine();
        int[] cnt = new int[26];

        for (int i = 0; i < S.length(); i++) {
            int idx = S.charAt(i) - 'a';
            cnt[idx] += 1;
        }

        for (int i = 0; i < 26; i++) {
            System.out.printf("%d ", cnt[i]);
        }
    }
}
