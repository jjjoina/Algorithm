import java.io.*;

public class BOJ5532 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int L = Integer.parseInt(br.readLine());
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());
        int D = Integer.parseInt(br.readLine());

        int ans = L - (int) Math.max(Math.ceil((double) A / C), Math.ceil((double) B / D));
        System.out.println(ans);
    }
}
