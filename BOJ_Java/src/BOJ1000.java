import java.io.*;
import java.util.StringTokenizer;

public class BOJ1000 {
    public static void main(String[] args) throws IOException {
        // 풀이 2. StringTokenizer
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        bw.write(String.valueOf(a + b));

        br.close();
        bw.close();

        // 풀이 1.
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//
//        String[] AB = br.readLine().split(" ");
//        int A = Integer.parseInt(AB[0]);
//        int B = Integer.parseInt(AB[1]);
//        int ans = A + B;
//
//        bw.write(String.valueOf(ans));
//        bw.flush();
    }
}