import java.io.*;
import java.util.*;

public class BOJ1647_priority_queue_with_inner_class {
    static class Edge implements Comparable<Edge> {
        int a;
        int b;
        int cost;

        Edge(int a, int b, int cost) {
            this.a = a;
            this.b = b;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge e) {
            return this.cost - e.cost;
        }
    }

    static int N, M;
    static PriorityQueue<Edge> edges;
    static int[] parent;

    static int find(int v) {
        if (parent[v] != v) {
            parent[v] = find(parent[v]);
        }
        return parent[v];
    }

    static void union(int u, int v) {
        int pu = find(u);
        int pv = find(v);

        if (pu < pv) {
            parent[pv] = pu;
        } else if (pu > pv) {
            parent[pu] = pv;
        }
    }

    static int kruskal() {
        int answer = 0;
        int count = 0;

        while (count < N - 2) {
            Edge edge = edges.poll();

            if (find(edge.a) == find(edge.b)) {
                continue;
            }

            union(edge.a, edge.b);
            answer += edge.cost;
            count++;
        }

        return answer;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        edges = new PriorityQueue<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            edges.offer(new Edge(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            ));
        }

        parent = new int[N + 1];
        for (int i = 0; i <= N; i++) {
            parent[i] = i;
        }

        System.out.println(kruskal());
    }
}
