import java.io.*;

public class BOJ6749 {
    static int Y, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Y = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        System.out.println(M + M - Y);
    }
}
