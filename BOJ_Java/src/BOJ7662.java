import java.io.*;
import java.util.*;

public class BOJ7662 {
    static void insert(int n, PriorityQueue<Integer> minPq, PriorityQueue<Integer> maxPq) {
        minPq.offer(n);
        maxPq.offer(n);
    }

    static void clear(PriorityQueue<Integer> pq, HashMap<Integer, Integer> delCnt) {
        while (!pq.isEmpty() && delCnt.getOrDefault(pq.peek(), 0) > 0) {
            delCnt.put(pq.peek(), delCnt.get(pq.peek()) - 1);
            pq.poll();
        }
    }

    static void delete(PriorityQueue<Integer> pq, HashMap<Integer, Integer> counterDelCnt) {
        if (!pq.isEmpty()) {
            int n = pq.poll();
            counterDelCnt.put(n, counterDelCnt.getOrDefault(n, 0) + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            PriorityQueue<Integer> minPq = new PriorityQueue<>();
            PriorityQueue<Integer> maxPq = new PriorityQueue<>(Collections.reverseOrder());
//            PriorityQueue<Integer> maxPq = new PriorityQueue<>((n1, n2) -> n2 - n1);
            HashMap<Integer, Integer> minPqDelCnt = new HashMap<>();
            HashMap<Integer, Integer> maxPqDelCnt = new HashMap<>();

            int k = Integer.parseInt(br.readLine());
            while (k-- > 0) {
                st = new StringTokenizer(br.readLine());
                String c = st.nextToken();
                int n = Integer.parseInt(st.nextToken());

                if (c.equals("I")) {
                    insert(n, minPq, maxPq);
                } else {
                    if (n == 1) {
                        clear(maxPq, maxPqDelCnt);
                        delete(maxPq, minPqDelCnt);
                    } else {
                        clear(minPq, minPqDelCnt);
                        delete(minPq, maxPqDelCnt);
                    }
                }
            }

            clear(minPq, minPqDelCnt);
            clear(maxPq, maxPqDelCnt);

            if (minPq.isEmpty() && maxPq.isEmpty()) {
                sb.append("EMPTY").append("\n");
            } else {
                sb.append(maxPq.peek()).append(" ").append(minPq.peek()).append("\n");
            }
        }

        System.out.println(sb);
    }
}
