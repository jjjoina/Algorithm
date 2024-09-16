import java.io.*;
import java.util.*;

public class BOJ1647_array {
    static int N, M;
    static int[][] edges;
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

        for (int[] edge : edges) {
            if (count == N - 2) {
                break;
            }

            if (find(edge[0]) == find(edge[1])) {
                continue;
            }

            union(edge[0], edge[1]);
            answer += edge[2];
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
        edges = new int[M][3];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                edges[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Arrays.sort(edges, (e1, e2) -> e1[2] - e2[2]);

        parent = new int[N + 1];
        for (int i = 0; i <= N; i++) {
            parent[i] = i;
        }

        System.out.println(kruskal());
    }
}
