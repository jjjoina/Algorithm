import java.io.*;
import java.util.*;

public class BOJ1922 {
    static class Edge implements Comparable<Edge> {
        int a;
        int b;
        int c;

        Edge(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        @Override
        public int compareTo(Edge edge) {
            return this.c - edge.c;
        }
    }

    static int N;
    static int M;
    static Edge[] edges;
    static int[] parent;

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        edges = new Edge[M];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            edges[i] = new Edge(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );
        }
    }

    static int find(int v) {
        if (parent[v] != v) {
            parent[v] = find(parent[v]);
        }
        return parent[v];
    }

    static void union(int u, int v) {
        parent[find(v)] = find(u);
    }

    static int kruskal() {
        parent = new int[N + 1];

        for (int i = 0; i <= N; i++) {
            parent[i] = i;
        }

        int cost = 0;
        int count = 0;

        for (Edge edge : edges) {
            if (find(edge.a) != find(edge.b)) {
                union(edge.a, edge.b);
                cost += edge.c;
                count++;

                if (count == N - 1) {
                    break;
                }
            }
        }

        return cost;
    }

    public static void main(String[] args) throws IOException {
        input();

        Arrays.sort(edges);

        System.out.println(kruskal());
    }
}
