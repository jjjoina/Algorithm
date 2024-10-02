import java.io.*;
import java.util.*;

public class BOJ1946 {
    static class Rank {
        int rank1;
        int rank2;

        Rank(int rank1, int rank2) {
            this.rank1 = rank1;
            this.rank2 = rank2;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());

            Rank[] ranks = new Rank[N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                ranks[i] = new Rank(
                        Integer.parseInt(st.nextToken()),
                        Integer.parseInt(st.nextToken())
                );
            }

            Arrays.sort(ranks, (r1, r2) -> r1.rank1 - r2.rank1);

            int answer = 1;
            int minRank2 = ranks[0].rank2;

            for (int i = 1; i < N; i++) {
                if (ranks[i].rank2 < minRank2) {
                    minRank2 = ranks[i].rank2;
                    answer++;
                }
            }

            sb.append(answer).append("\n");
        }

        System.out.println(sb);
    }
}
