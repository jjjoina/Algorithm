import java.io.*;

public class BOJ13752 {
    static int n, k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            k = Integer.parseInt(br.readLine());
            for (int j = 0; j < k; j++) {
                sb.append("=");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
