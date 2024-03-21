import java.io.*;

public class BOJ1110 {
	static int N, newNum, ans;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		newNum = N;
		while (true) {
			ans++;

			newNum = newNum % 10 * 10 + (newNum / 10 + newNum % 10) % 10;

			if (newNum == N) break;
		}

		System.out.println(ans);
	}
}
