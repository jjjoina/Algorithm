import java.io.*;

public class BOJ2023 {
    static int N;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());

        dfs(2, 1);
        dfs(3, 1);
        dfs(5, 1);
        dfs(7, 1);

        bw.close();
    }

    public static void dfs(int n, int depth) throws IOException {
        if (isPrime(n)) {
            if (depth == N) {
                bw.write(n + "\n");
                return;
            }

            for (int i = 1; i <= 9; i += 2) {
                dfs(n * 10 + i, depth + 1);
            }
        }
    }

    public static boolean isPrime(int n) {
        int sqrt = (int) Math.sqrt(n);
        for (int d = 2; d <= sqrt; d++) {
            if (n % d == 0) return false;
        }
        return true;
    }
}
