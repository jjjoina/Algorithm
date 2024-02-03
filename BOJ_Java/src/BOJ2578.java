import java.io.*;
import java.util.*;

public class BOJ2578 {
    static int[][] arr = new int[5][5];
    static int[] call = new int[25];

    public static void mark(int num) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (arr[i][j] == num) {
                    arr[i][j] = -1;
                    return;
                }
            }
        }
    }

    public static boolean isBingo() {
        boolean flag;
        int cnt = 0;

        // 가로줄 검사
        for (int i = 0; i < 5; i++) {
            flag = true;
            for (int j = 0; j < 5; j++) {
                if (arr[i][j] != -1) {
                    flag = false;
                    break;
                }
            }
            if (flag) cnt++;
        }

        // 세로줄 검사
        for (int j = 0; j < 5; j++) {
            flag = true;
            for (int i = 0; i < 5; i++) {
                if (arr[i][j] != -1) {
                    flag = false;
                    break;
                }
            }
            if (flag) cnt++;
        }

        // 대각선 검사
        flag = true;
        for (int i = 0; i < 5; i++) {
            if (arr[i][i] != -1) {
                flag = false;
                break;
            }
        }
        if (flag) cnt++;

        flag = true;
        for (int i = 0; i < 5; i++) {
            if (arr[i][4 - i] != -1) {
                flag = false;
                break;
            }
        }
        if (flag) cnt++;

        return cnt >= 3;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                call[i * 5 + j] = Integer.parseInt(st.nextToken());
            }
        }

        int ans = 0;
        while (true) {
            mark(call[ans]);
            if (isBingo()) {
                System.out.println(ans+1);
                break;
            }
            ans++;
        }
    }
}