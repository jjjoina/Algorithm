import java.io.*;

public class BOJ10987 {
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'a'
                    || s.charAt(i) == 'e'
                    || s.charAt(i) == 'i'
                    || s.charAt(i) == 'o'
                    || s.charAt(i) == 'u'
            ) ans++;
        }

        System.out.println(ans);
    }
}
