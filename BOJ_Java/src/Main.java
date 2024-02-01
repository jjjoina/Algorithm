import java.io.*;
import java.util.*;

public class Main {



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 0) {
                    bfs(arr, i, j);
                    ans++;
                }
            }
        }

        bw.write(ans + "\n");

        br.close();
        bw.close();
    }

    static void bfs(int[][] arr, int i, int j) {
        Queue q = new LinkedList();
        int[] v = {i, j};
        q.add(v);
        arr[i][j] = 1;
        while (!q.isEmpty()) {
            v = (int[]) q.poll();
            i = v[0];
            j = v[1];
            for (int d = 0; d < 4; d++) {

            }
        }
    }
}