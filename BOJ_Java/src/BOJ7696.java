import java.io.*;

public class BOJ7696 {
    public static boolean isNotRepeating(int cnt) {
        int used = 0;   // 비트마스킹
        while (cnt > 0) {
            int d = cnt % 10;
            if ((used & (1<<d)) > 0) return false;
            used |= (1<<d);
            cnt /= 10;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] lst = new int[1000001];
        int cnt = 1;
        int i = 1;

        while (i <= 1000000) {
            if (isNotRepeating(cnt)) {
                lst[i] = cnt;
                i++;
            }
            cnt++;
        }

        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            System.out.println(lst[n]);
        }
    }
}
