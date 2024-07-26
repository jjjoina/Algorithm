import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] lst = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            lst[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(lst);

        int l = 0;
        int r = N - 1;
        long ansSum = Math.abs(lst[l] + lst[r]);
        int ansMin = lst[l];
        int ansMax = lst[r];

        while (l < r) {
            long sum = (long) lst[l] + lst[r];

            if (ansSum > Math.abs(sum)) {
                ansSum = Math.abs(sum);
                ansMin = lst[l];
                ansMax = lst[r];
            }

            if (sum < 0) {
                l++;
            } else if (sum > 0) {
                r--;
            } else {
                ansMin = lst[l];
                ansMax = lst[r];
                break;
            }
        }

        System.out.println(ansMin + " " + ansMax);
    }
}