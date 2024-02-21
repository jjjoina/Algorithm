import java.io.*;

public class BOJ1652 {
    static int N, ans1 = 0, ans2 = 0;
    static char[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = new char[N][N];
        for (int i = 0; i < N; i++) {
            arr[i] = br.readLine().toCharArray();
        }

         for (int i = 0; i < N; i++) {
            int cnt = 0;
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == '.') {
                    cnt++;
                    if (cnt == 2) {
                        ans1++;
                    }
                } else {
                    cnt = 0;
                }
            }
        }

        for (int j = 0; j < N; j++) {
            int cnt = 0;
            for (int i = 0; i < N; i++) {
                if (arr[i][j] == '.') {
                    cnt++;
                    if (cnt == 2) {
                        ans2++;
                    }
                } else {
                    cnt = 0;
                }
            }
        }

        System.out.println(ans1 + " " + ans2);
    }
}
