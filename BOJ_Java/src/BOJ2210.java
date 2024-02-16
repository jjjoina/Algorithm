import java.io.*;
import java.util.*;

public class BOJ2210 {
    static String[][] arr;
    static int ni, nj;
    static Set<String> set = new HashSet<>();
    static final int[] di = {0, 1, 0, -1};
    static final int[] dj = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        arr = new String[5][5];
        for (int i = 0; i < 5; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < 5; j++) {
                arr[i][j] = s[j];
            }
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                dfs(arr[i][j], 1, i, j);
            }
        }

        System.out.println(set.size());
    }

    public static void dfs(String cur, int depth, int i, int j) {
        if (depth == 6) {
            set.add(cur);
            return;
        }

        for (int d = 0; d < 4; d++) {
            ni = i + di[d];
            nj = j + dj[d];
            if (ni < 0 || ni >= 5 || nj < 0 || nj >= 5) continue;
            dfs(cur + arr[ni][nj], depth + 1, ni, nj);
        }
    }
}
