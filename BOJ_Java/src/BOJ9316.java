import java.io.*;

public class BOJ9316 {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        for (int i = 1; i <= N; i++) {
            bw.write("Hello World, Judge " + i + "!\n");
        }

        bw.close();
    }
}
