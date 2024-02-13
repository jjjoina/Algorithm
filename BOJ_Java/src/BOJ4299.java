import java.io.*;
import java.util.*;

public class BOJ4299 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int sum = Integer.parseInt(st.nextToken());
        int sub = Integer.parseInt(st.nextToken());

        if ((sum + sub) % 2 == 0 && sum >= sub) System.out.printf("%d %d", (sum + sub) / 2, (sum - sub) / 2);
        else System.out.print(-1);
    }
}
