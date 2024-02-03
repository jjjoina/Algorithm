import java.io.*;
import java.util.*;

public class BOJ13335 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        Queue<Integer> waitingTrucks = new LinkedList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            waitingTrucks.add(Integer.parseInt(st.nextToken()));
        }

        Queue<Integer> bridge = new LinkedList<>();
        for (int i = 0; i < w; i++) {
            bridge.add(0);
        }

        int sumWeight = 0;  // 다리 위의 트럭의 무게 합
        int ans = 0;

        while (true) {
            ans++;

            // 트럭 내리기
            sumWeight -= bridge.poll();

            // 진입 가능하면 진입. 아니면 0(빈칸)이 진입
            if (!waitingTrucks.isEmpty() && sumWeight + waitingTrucks.peek() <= L) {
                int newWeight = waitingTrucks.poll();
                bridge.add(newWeight);
                sumWeight += newWeight;
                if (waitingTrucks.isEmpty()) {
                    ans += w;
                    break;
                }
            } else {
                bridge.add(0);
            }

        }

        bw.write(ans + "\n");

        br.close();
        bw.close();
    }
}
