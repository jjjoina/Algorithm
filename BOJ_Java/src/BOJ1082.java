import java.io.*;
import java.util.*;

public class BOJ1082 {
    static int N;
    static int[] P;
    static int M;

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        P = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            P[i] = Integer.parseInt(st.nextToken());
        }
        M = Integer.parseInt(br.readLine());
    }

    public static void main(String[] args) throws IOException {
        input();

        if (N == 1) {
            System.out.println("0");
            return;
        }

        int minP = P[1];
        int minI = 1;

        for (int i = 2; i < N; i++) {
            if (minP >= P[i]) {
                minP = P[i];
                minI = i;
            }
        }

        if (M - minP < 0) {     // 0만 살 수 있는 경우
            System.out.println("0");
            return;
        }

        int length;

        if (minP <= P[0]) {
            length = M / minP;
        } else {    // 가장 저렴한 숫자가 0인 경우
            length = 1 + (M - minP) / P[0];
        }

        int[] answer = new int[length];

        if (minP <= P[0]) {
            Arrays.fill(answer, minI);
            M -= minP * length;
        } else {
            answer[0] = minI;
            M -= minP;
            M -= P[0] * (length - 1);
        }

        // 앞 자리에서부터 큰 숫자로 바꾸기
        for (int i = 0; i < length; i++) {
            for (int j = N - 1; j >= 0; j--) {
                if (j == answer[i]) {
                    break;
                }

                int additionalPrice = P[j] - P[answer[i]];

                if (M - additionalPrice >= 0) {
                    M -= additionalPrice;
                    answer[i] = j;
                    break;
                }
            }
        }

        for (int d : answer) {
            System.out.print(d);
        }
    }
}
