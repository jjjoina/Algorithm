import java.io.*;

public class BOJ4811_others {
    static long[][] memo = new long[31][31];

    static long dp(int one, int half) {
        if (memo[one][half] != 0) {
            return memo[one][half];
        }

        if (one == 0) {
            memo[one][half] = 1;    // 반 조각만 있을 때는 경우의 수가 한 가지
        } else {
            memo[one][half] += dp(one - 1, half + 1);   // 한 조각을 꺼내는 경우

            if (half > 0) {
                memo[one][half] += dp(one, half - 1);       // 반 조각을 꺼내는 경우
            }
        }

        return memo[one][half];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            int N = Integer.parseInt(br.readLine());

            if (N == 0) break;

            sb.append(dp(N, 0)).append('\n');
        }

        System.out.println(sb);
    }
}
