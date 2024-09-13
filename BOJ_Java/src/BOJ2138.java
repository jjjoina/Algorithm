import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ2138 {
    static int N;
    static int[] current;
    static int[] target;
    static int ans;

    static void backTracking(int i, int cnt) {
        if (ans <= cnt) {
            return;
        }

        if (i == N - 1) {
            if (current[i - 1] == target[i - 1] && current[i] == target[i]) {
                ans = cnt;
            } else if (current[i - 1] != target[i - 1] && current[i] != target[i]) {
                ans = cnt + 1;
            }
            return;
        }

        if (current[i - 1] == target[i - 1]) {
            backTracking(i + 1, cnt);
        } else {
            for (int d = -1; d <= 1; d++) {
                current[i + d] = 1 - current[i + d];
            }

            backTracking(i + 1, cnt + 1);

            for (int d = -1; d <= 1; d++) {
                current[i + d] = 1 - current[i + d];
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        current = new int[N];
        target = new int[N];
        String s = br.readLine();
        for (int i = 0; i < N; i++) {
            current[i] = s.charAt(i) - '0';
        }
        s = br.readLine();
        for (int i = 0; i < N; i++) {
            target[i] = s.charAt(i) - '0';
        }
        ans = N + 1;

        backTracking(1, 0);

        current[0] = 1 - current[0];
        current[1] = 1 - current[1];

        backTracking(1, 1);

        if (ans == N + 1) {
            ans = -1;
        }

        System.out.println(ans);
    }
}
