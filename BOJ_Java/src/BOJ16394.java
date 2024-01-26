import java.io.*;

public class BOJ16394 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int ans = N - 1946;

        bw.write(String.valueOf(ans));
        bw.flush();
    }
}