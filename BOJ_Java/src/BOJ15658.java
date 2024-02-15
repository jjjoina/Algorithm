import java.io.*;
import java.util.*;

public class BOJ15658 {
    static int max_ans = Integer.MIN_VALUE;
    static int min_ans = Integer.MAX_VALUE;

    static int plus, minus, mul, div, N;
    static int[] A;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        plus = Integer.parseInt(st.nextToken());
        minus = Integer.parseInt(st.nextToken());
        mul = Integer.parseInt(st.nextToken());
        div = Integer.parseInt(st.nextToken());

        // 깊이 1부터 시작
        dfs(A[0], 1, 0, 0, 0, 0);

        System.out.println(max_ans);
        System.out.println(min_ans);
    }

    // 아직 연산자만큼 사용하지 않았으면 사용 가능
    public static void dfs(int cur, int depth, int usedPlus, int usedMinus, int usedMul, int usedDiv) {
        if (usedPlus > plus || usedMinus > minus || usedMul > mul || usedDiv > div) return;

        if (depth == N) {
            if (max_ans < cur) max_ans = cur;
            if (min_ans > cur) min_ans = cur;
            return;
        }

        dfs(cur + A[depth], depth + 1, usedPlus + 1, usedMinus, usedMul, usedDiv);
        dfs(cur - A[depth], depth + 1, usedPlus, usedMinus + 1, usedMul, usedDiv);
        dfs(cur * A[depth], depth + 1, usedPlus, usedMinus, usedMul + 1, usedDiv);
        dfs(cur / A[depth], depth + 1, usedPlus, usedMinus, usedMul, usedDiv + 1);
    }
}
