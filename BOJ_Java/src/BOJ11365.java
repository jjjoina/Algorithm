import java.io.*;

public class BOJ11365 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            String s = br.readLine();
            if (s.equals("END")) break;

            for (int i = s.length() - 1; i >= 0; i--) {
                bw.write(s.charAt(i));
            }
            bw.newLine();
        }

        br.close();
        bw.close();
    }
}
