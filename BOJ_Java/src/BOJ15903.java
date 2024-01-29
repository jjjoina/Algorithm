import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ15903 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        PriorityQueue<Long> pq = new PriorityQueue<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            pq.add(Long.parseLong(st.nextToken()));
        }

        for (int i = 0; i < m; i++) {
            long sumV = pq.poll() + pq.poll();
            pq.add(sumV);
            pq.add(sumV);
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += pq.poll();
        }

        bw.write(ans + "\n");

        br.close();
        bw.close();
    }
}
