import java.io.*;

public class BOJ5524 {
	static int N;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		N = Integer.parseInt(br.readLine());

		for (int i = 0; i < N; i++) {
			sb.append(br.readLine().toLowerCase() + "\n");
		}

		System.out.println(sb);
	}
}
