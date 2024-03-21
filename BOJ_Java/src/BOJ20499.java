import java.io.*;

public class BOJ20499 {
	static int K, D, A;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split("/");
		K = Integer.parseInt(s[0]);
		D = Integer.parseInt(s[1]);
		A = Integer.parseInt(s[2]);

		if (K + A < D || D == 0) {
			System.out.println("hasu");
		} else {
			System.out.println("gosu");
		}
	}
}
