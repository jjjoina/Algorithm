import java.io.*;
import java.util.HashSet;
import java.util.Set;

public class BOJ2295 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] lst = new int[N];
        for (int i = 0; i < N; i++) {
            lst[i] = Integer.parseInt(br.readLine());
        }

        Set<Integer> xy = new HashSet<>();
        for (int x = 0; x < N; x++) {
            for (int y = x; y < N; y++) {
                xy.add(lst[x] + lst[y]);
            }
        }

        int ans = 0;
        for (int k = 0; k < N; k++) {
            for (int z = 0; z < N; z++) {
                if (xy.contains(lst[k] - lst[z]) && ans < lst[k]) {
                    ans = lst[k];
                }
            }
        }

        bw.write(ans + "\n");

        br.close();
        bw.close();
    }
}
