import java.io.*;

public class BOJ11729 {
    static int N;
    static StringBuilder sb;

    static void recur(int level, int from, int temp, int to) {
        if (level == 0) return;

        recur(level - 1, from, to, temp);
        sb.append(from).append(" ").append(to).append("\n");
        recur(level - 1, temp, from, to);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        int ans = 1;
        for (int i = 1; i < N; i++) {
            ans = ans + 1 + ans;
        }
        sb.append(ans).append("\n");

        recur(N, 1, 2, 3);

        System.out.println(sb);
    }
}
