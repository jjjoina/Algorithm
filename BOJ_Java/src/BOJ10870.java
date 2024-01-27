import java.io.*;

public class BOJ10870 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] fibo = new int[21];
        fibo[1] = 1;

        for (int i = 2; i < 21; i++) {
            fibo[i] = fibo[i-2] + fibo[i-1];
        }

        int n = Integer.parseInt(br.readLine());
        bw.write(String.valueOf(fibo[n]));

        br.close();
        bw.close();
    }
}
