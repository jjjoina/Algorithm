import java.io.*;

public class BOJ1550 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 풀이 2. Integer.parseInt(s, radix)
        bw.write(String.valueOf(Integer.parseInt(br.readLine(), 16)));



        // 풀이 1.
//        String s = br.readLine();
//
//        int ans = 0;
//        int mul = 1;
//
//        for (int i = s.length()-1; i >= 0; i--) {
//            char c = s.charAt(i);
//            if (Character.isDigit(c)) {
//                ans += (int) ((c - '0') * mul);
//            } else {
//                ans += (int) ((c - 'A' + 10) * mul);
//            }
//            mul *= 16;
//        }
//
//        bw.write(String.valueOf(ans));

        br.close();
        bw.close();
    }
}
