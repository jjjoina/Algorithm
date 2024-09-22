import java.io.*;

public class BOJ4811_me {
    static int N;
    static long[] answer;

    static long compute(int n) {
        long[][][] dp = new long[2 * n + 1][n + 1][n + 1];

        dp[1][1][n - 1] = 1;

        for (int day = 2; day <= 2 * n; day++) {
            for (int half = 0; half <= n; half++) {
                for (int one = 0; one <= n; one++) {
                    if (half + 1 <= n) {
                        dp[day][half][one] += dp[day - 1][half + 1][one];   // 반 개 먹은 경우
                    }
                    if (half - 1 >= 0 && one + 1 <= n) {
                        dp[day][half][one] += dp[day - 1][half - 1][one + 1];   // 한 개 먹은 경우
                    }
                }
            }
        }

        return dp[2 * n][0][0];
    }

    static void fillAnswer() {
        answer = new long[31];

        for (int i = 1; i <= 30; i++) {
            answer[i] = compute(i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        fillAnswer();

        while (true) {
            N = Integer.parseInt(br.readLine());

            if (N == 0) break;

            sb.append(answer[N]).append('\n');
        }

        System.out.println(sb);
    }
}
