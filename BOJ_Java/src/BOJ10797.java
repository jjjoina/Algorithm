import java.io.*;
import java.util.*;

public class BOJ10797 {
    static int day, car, ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        day = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 5; i++) {
            car = Integer.parseInt(st.nextToken());
            if (car % 10 == day) {
                ans++;
            }
        }

        System.out.println(ans);
    }
}
