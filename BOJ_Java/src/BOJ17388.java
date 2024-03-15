import java.io.*;
import java.util.*;

public class BOJ17388 {
	static List<Univ> univList = new ArrayList<>();
	static String ans;

	static class Univ {
		String name;
		int score;

		Univ(String name, int score) {
			this.name = name;
			this.score = score;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		univList.add(new Univ("Soongsil", Integer.parseInt(st.nextToken())));
		univList.add(new Univ("Korea", Integer.parseInt(st.nextToken())));
		univList.add(new Univ("Hanyang", Integer.parseInt(st.nextToken())));

		int sumScore = 0;
		for (int i = 0; i < 3; i++) {
			sumScore += univList.get(i).score;
		}

		if (sumScore >= 100) ans = "OK";
		else {
			univList.sort((o1, o2) -> o1.score - o2.score);
			ans = univList.get(0).name;
		}

		System.out.println(ans);
	}
}
