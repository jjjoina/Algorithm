import java.io.*;
import java.util.*;

public class BOJ9019 {
    static class Node {
        int n;
        String c;

        Node(int n, String c) {
            this.n = n;
            this.c = c;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            ArrayDeque<Node> q = new ArrayDeque<>();
            boolean[] visited = new boolean[10000];
            q.offer(new Node(A, ""));
            visited[A] = true;

            while (!q.isEmpty()) {
                Node v = q.poll();

                if (v.n == B) {
                    sb.append(v.c).append("\n");
                    break;
                }

                int d = v.n * 2 % 10000;
                if (!visited[d]) {
                    q.offer(new Node(d, v.c + "D"));
                    visited[d] = true;
                }

                int s = v.n > 0 ? v.n - 1 : 9999;
                if (!visited[s]) {
                    q.offer(new Node(s, v.c + "S"));
                    visited[s] = true;
                }

                int l = v.n * 10 % 10000 + v.n / 1000;
                if (!visited[l]) {
                    q.offer(new Node(l, v.c + "L"));
                    visited[l] = true;
                }

                int r = v.n % 10 * 1000 + v.n / 10;
                if (!visited[r]) {
                    q.offer(new Node(r, v.c + "R"));
                    visited[r] = true;
                }
            }
        }

        System.out.println(sb);
    }
}
