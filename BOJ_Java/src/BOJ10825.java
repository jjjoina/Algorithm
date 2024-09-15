import java.io.*;
import java.util.*;

public class BOJ10825 {
    static class Score {
        String name;
        int korean;
        int english;
        int math;

        Score(String name, int korean, int english, int math) {
            this.name = name;
            this.korean = korean;
            this.english = english;
            this.math = math;
        }
    }

    static int N;
    static Score[] scores;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        scores = new Score[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int korean = Integer.parseInt(st.nextToken());
            int english = Integer.parseInt(st.nextToken());
            int math = Integer.parseInt(st.nextToken());

            scores[i] = new Score(name, korean, english, math);
        }

        Arrays.sort(scores, (s1, s2) -> {
            if (s1.korean != s2.korean)         return s2.korean - s1.korean;
            else if (s1.english != s2.english)  return s1.english - s2.english;
            else if (s1.math != s2.math)        return s2.math - s1.math;
            else                                return s1.name.compareTo(s2.name);
        });

        for (Score score : scores) {
            sb.append(score.name).append('\n');
        }

        System.out.println(sb);
    }
}