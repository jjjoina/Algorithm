import java.io.*;
import java.util.*;

public class BOJ2110 {
    static int N, C;
    static int[] lst;

    static boolean isPossible(int n) {
        int cnt = 1;
        int prev = 0;

        for (int i = 1; i < N; i++) {
            if (lst[i] - lst[prev] < n) continue;

            prev = i;
            cnt++;

            if (cnt == C) return true;
        }

        return false;
    }

    static int binarySearch() {
        int l = 0;
        int r = lst[N - 1] - lst[0];

        while (l <= r) {
            int m = (l + r) / 2;

            if (isPossible(m)) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return r;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        lst = new int[N];
        for (int i = 0; i < N; i++) {
            lst[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(lst);

        System.out.println(binarySearch());
    }
}