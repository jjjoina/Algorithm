import java.io.*;
import java.util.*;

public class BOJ17281 {
    static int N, ans, hitterIdx, res, out, score;
    static int[][] scores;
    static ArrayList<Integer> p = new ArrayList<>();
    static boolean[] used = new boolean[9];
    static int[] ground = new int[3];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        scores = new int[N][9];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                scores[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        perm(0);

        System.out.println(ans);
    }

    public static void perm(int len) {
        if (len == 9) {
            game();
            return;
        }

        // 1번 선수를 4번 타자로 추가
        if (len == 3) {
            p.add(0);
            perm(len + 1);
            p.remove(len);
            return;
        }

        for (int i = 1; i < 9; i++) {
            if (!used[i]) {
                p.add(i);
                used[i] = true;
                perm(len + 1);
                p.remove(len);
                used[i] = false;
            }
        }
    }

    public static void game() {
        hitterIdx = 0;
        score = 0;
        for (int i = 0; i < N; i++) {   // 각 이닝
            out = 0;
            for (int j = 0; j < 3; j++) ground[j] = 0;

            while (out < 3) {
                res = scores[i][p.get(hitterIdx)];
                if (res == 0) out++;
                else {
                    // res는 1,2,3,4 중 하나
                    for (int r = 0; r < res; r++) {
                        score += ground[2];
                        ground[2] = ground[1];
                        ground[1] = ground[0];
                        ground[0] = r == 0 ? 1 : 0;
                    }
                }

                hitterIdx++;
                if (hitterIdx == 9) hitterIdx = 0;
            }
        }

        if (ans < score) ans = score;
    }
}
