import java.io.*;
import java.util.*;

public class BOJ1987 {
	static int R, C, ans = 1, maxAns;
	static int[][] arr;
	static boolean[] used = new boolean[26];
	static int[] di = {0, 1, 0, -1};
	static int[] dj = {1, 0, -1, 0};

	public static void dfs(int i, int j, int depth) {
		if (ans < depth) ans = depth;

		if (ans == maxAns) return;

		for (int d = 0; d < 4; d++) {
			int ni = i + di[d];
			int nj = j + dj[d];
			if (0 <= ni && ni < R && 0 <= nj && nj < C && !used[arr[ni][nj]]) {
				used[arr[ni][nj]] = true;

				dfs(ni, nj, depth + 1);
				if (ans == maxAns) return;

				used[arr[ni][nj]] = false;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		arr = new int[R][C];
		for (int i = 0; i < R; i++) {
			String s = br.readLine();
			for (int j = 0; j < C; j++) {
				arr[i][j] = s.charAt(j) - 'A';
			}
		}
		used[arr[0][0]] = true;

		Set<Integer> allAlphas = new HashSet<>();
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				allAlphas.add(arr[r][c]);
			}
		}
		maxAns = allAlphas.size();

		dfs(0, 0, 1);

		System.out.println(ans);
	}
}
