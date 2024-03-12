import java.io.*;

public class BOJ11948 {
    static int score, ans;
    static int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 4; i++) {
            score = Integer.parseInt(br.readLine());
            ans += score;
            if (min1 > score) min1 = score;
        }
        for (int i = 0; i < 2; i++) {
            score = Integer.parseInt(br.readLine());
            ans += score;
            if (min2 > score) min2 = score;
        }

        System.out.println(ans - min1 - min2);
    }
}
