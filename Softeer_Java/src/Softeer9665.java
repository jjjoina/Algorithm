import java.io.*;
import java.util.*;

public class Softeer9665 {
    static int n;
    static int m;
    static ArrayList<ArrayList<Integer>> forwardAdjM;
    static ArrayList<ArrayList<Integer>> reverseAdjM;
    static int S;
    static int T;
    static HashSet<Integer> answerSet;
    static HashSet<Integer> tempSet;

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        forwardAdjM = new ArrayList<>();
        reverseAdjM = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            forwardAdjM.add(new ArrayList<>());
            reverseAdjM.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            forwardAdjM.get(x).add(y);
            reverseAdjM.get(y).add(x);
        }

        st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
    }

    static void dfs(int v, int destination, ArrayList<ArrayList<Integer>> adjM) {
        tempSet.add(v);

        if (v == destination) {
            return;
        }

        for (int w : adjM.get(v)) {
            if (!tempSet.contains(w)) {
                dfs(w, destination, adjM);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        input();

        // S에서 도달할 수 있는 정점들 구하기
        tempSet = new HashSet<>();
        dfs(S, T, forwardAdjM);
        answerSet = tempSet;

        // T로 도달할 수 있는 정점들 구하기
        tempSet = new HashSet<>();
        dfs(T, -1, reverseAdjM);
        answerSet.retainAll(tempSet);

        // T에서 도달할 수 있는 정점들 구하기
        tempSet = new HashSet<>();
        dfs(T, S, forwardAdjM);
        answerSet.retainAll(tempSet);

        // S로 도달할 수 있는 정점들 구하기
        tempSet = new HashSet<>();
        dfs(S, -1, reverseAdjM);
        answerSet.retainAll(tempSet);

        System.out.println(answerSet.size() - 2);   // S, T 제외
    }
}
