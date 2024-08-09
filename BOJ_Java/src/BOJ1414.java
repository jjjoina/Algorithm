import java.io.*;
import java.util.*;

public class BOJ1414 {
    static class Edge implements Comparable<Edge> {
        int u;
        int v;
        int length;

        Edge(int u, int v, int length) {
            this.u = u;
            this.v = v;
            this.length = length;
        }

        @Override
        public int compareTo(Edge e) {
            return this.length - e.length;
        }
    }

    static int N;
    static ArrayList<Edge> edges = new ArrayList<>();
    static int sum = 0;
    static int[] parent;

    static int convert(char c) {
        if (c == '0')
            return 0;
        else if ('a' <= c && c <= 'z')
            return c - 'a' + 1;
        else
            return c - 'A' + 27;
    }

    static int find(int v) {
        if (parent[v] != v)
            parent[v] = find(parent[v]);

        return parent[v];
    }

    static void union(int u, int v) {
        int pu = find(u);
        int pv = find(v);

        if (pu < pv)
            parent[pu] = pv;
        else
            parent[pv] = pu;
    }

    static int kruskal() {
        int cnt = 0;

        for (Edge edge : edges) {
            if (find(edge.u) != find(edge.v)) {
                union(edge.u, edge.v);
                sum -= edge.length;
                if (++cnt == N - 1) break;
            }
        }

        if (cnt == N - 1)
            return sum;
        else
            return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < N; j++) {
                int length = convert(s.charAt(j));
                sum += length;
                if (i != j && length > 0)
                    edges.add(new Edge(i, j, length));
            }
        }

        Collections.sort(edges);
        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }

        System.out.println(kruskal());
    }
}
