import java.io.*;
import java.util.*;

public class BOJ3079 {
    static BufferedReader br;
    static StringTokenizer st;

    static int N;
    static int M;
    static ArrayList<Long> times;

    static void input() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        times = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            times.add(Long.parseLong(br.readLine()));
        }
    }

    static boolean isPossible(long totalTime) {
        long count = 0;

        for (long time : times) {
            count += totalTime / time;

            if (count >= M) {
                return true;
            }
        }

        return false;
    }

    static long parametricSearch() {
        long left = Collections.min(times);
        long right = Collections.max(times) * M;

        while (left <= right) {
            long mid = (left + right) / 2;

            if (isPossible(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    public static void main(String[] args) throws IOException {
        input();

        System.out.println(parametricSearch());
    }
}
