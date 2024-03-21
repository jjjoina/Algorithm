import java.io.*;

public class BOJ16486 {
	static final double pi = 3.141592;
	static int d1, d2;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		d1 = Integer.parseInt(br.readLine());
		d2 = Integer.parseInt(br.readLine());

		System.out.println(2 * (d1 + pi * d2));
	}
}
