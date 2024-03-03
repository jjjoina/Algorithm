import java.io.*;
import java.util.*;

public class BOJ13460 {
    static int N, M;
    static char[][] arr;
    static int ri, rj, bi, bj;
    static boolean rIn, bIn;
    static int ans = -1;

    static class Case {
        int ri, rj, bi, bj;
        int depth;

        public Case(int ri, int rj, int bi, int bj, int depth) {
            this.ri = ri;
            this.rj = rj;
            this.bi = bi;
            this.bj = bj;
            this.depth = depth;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new char[N][M];
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = s.charAt(j);
                if (arr[i][j] == 'R') {
                    ri = i; rj = j;
                }
                if (arr[i][j] == 'B') {
                    bi = i; bj = j;
                }
            }
        }

        ArrayDeque<Case> q = new ArrayDeque<>();
        q.offer(new Case(ri, rj, bi, bj, 1));
        while (!q.isEmpty()) {
            Case c = q.poll();
            if (c.depth > 10) break;

            // 왼쪽으로 기울이기
            ri = c.ri; rj = c.rj;
            bi = c.bi; bj = c.bj;
            rIn = false; bIn = false;
            if (ri == bi) {     // 같은 행에 있는 경우
                if (rj < bj) {  // 빨파 순으로 있는 경우
                    while (true) {  // 빨강 이동
                        if (arr[ri][rj] == 'O') {
                            rIn = true;
                            break;
                        }
                        if (arr[ri][rj] == '#') {
                            rj++;
                            break;
                        }
                        rj--;
                    }
                    while (true) {  // 파랑 이동
                        if (arr[bi][bj] == 'O') {
                            bIn = true;
                            break;
                        }
                        if (arr[bi][bj] == '#' || bj == rj) {
                            bj++;
                            break;
                        }
                        bj--;
                    }
                }
                else {          // 파빨 순으로 있는 경우
                    while (true) {  // 파랑 이동
                        if (arr[bi][bj] == 'O') {
                            bIn = true;
                            break;
                        }
                        if (arr[bi][bj] == '#') {
                            bj++;
                            break;
                        }
                        bj--;
                    }
                    while (true) {  // 빨강 이동
                        if (arr[ri][rj] == 'O') {
                            rIn = true;
                            break;
                        }
                        if (arr[ri][rj] == '#' || rj == bj) {
                            rj++;
                            break;
                        }
                        rj--;
                    }
                }
            }
            else {              // 다른 행에 있는 경우
                while (true) {  // 빨강 이동
                    if (arr[ri][rj] == 'O') {
                        rIn = true;
                        break;
                    }
                    if (arr[ri][rj] == '#') {
                        rj++;
                        break;
                    }
                    rj--;
                }
                while (true) {  // 파랑 이동
                    if (arr[bi][bj] == 'O') {
                        bIn = true;
                        break;
                    }
                    if (arr[bi][bj] == '#') {
                        bj++;
                        break;
                    }
                    bj--;
                }
            }
            if (!bIn) {
                if (rIn) {
                    ans = c.depth;
                    break;
                } else {
                    q.offer(new Case(ri, rj, bi, bj, c.depth + 1));
                }
            }

            // 오른쪽으로 기울이기
            ri = c.ri; rj = c.rj;
            bi = c.bi; bj = c.bj;
            rIn = false; bIn = false;
            if (ri == bi) {     // 같은 행에 있는 경우
                if (rj < bj) {  // 빨파 순으로 있는 경우
                    while (true) {  // 파랑 이동
                        if (arr[bi][bj] == 'O') {
                            bIn = true;
                            break;
                        }
                        if (arr[bi][bj] == '#') {
                            bj--;
                            break;
                        }
                        bj++;
                    }
                    while (true) {  // 빨강 이동
                        if (arr[ri][rj] == 'O') {
                            rIn = true;
                            break;
                        }
                        if (arr[ri][rj] == '#' || rj == bj) {
                            rj--;
                            break;
                        }
                        rj++;
                    }
                }
                else {          // 파빨 순으로 있는 경우
                    while (true) {  // 빨강 이동
                        if (arr[ri][rj] == 'O') {
                            rIn = true;
                            break;
                        }
                        if (arr[ri][rj] == '#') {
                            rj--;
                            break;
                        }
                        rj++;
                    }
                    while (true) {  // 파랑 이동
                        if (arr[bi][bj] == 'O') {
                            bIn = true;
                            break;
                        }
                        if (arr[bi][bj] == '#' || bj == rj) {
                            bj--;
                            break;
                        }
                        bj++;
                    }
                }
            }
            else {              // 다른 행에 있는 경우
                while (true) {  // 빨강 이동
                    if (arr[ri][rj] == 'O') {
                        rIn = true;
                        break;
                    }
                    if (arr[ri][rj] == '#') {
                        rj--;
                        break;
                    }
                    rj++;
                }
                while (true) {  // 파랑 이동
                    if (arr[bi][bj] == 'O') {
                        bIn = true;
                        break;
                    }
                    if (arr[bi][bj] == '#') {
                        bj--;
                        break;
                    }
                    bj++;
                }
            }
            if (!bIn) {
                if (rIn) {
                    ans = c.depth;
                    break;
                } else {
                    q.offer(new Case(ri, rj, bi, bj, c.depth + 1));
                }
            }

            // 위쪽으로 기울이기
            ri = c.ri; rj = c.rj;
            bi = c.bi; bj = c.bj;
            rIn = false; bIn = false;
            if (rj == bj) {     // 같은 열에 있는 경우
                if (ri < bi) {  // 빨파 순으로 있는 경우
                    while (true) {  // 빨강 이동
                        if (arr[ri][rj] == 'O') {
                            rIn = true;
                            break;
                        }
                        if (arr[ri][rj] == '#') {
                            ri++;
                            break;
                        }
                        ri--;
                    }
                    while (true) {  // 파랑 이동
                        if (arr[bi][bj] == 'O') {
                            bIn = true;
                            break;
                        }
                        if (arr[bi][bj] == '#' || bi == ri) {
                            bi++;
                            break;
                        }
                        bi--;
                    }
                }
                else {          // 파빨 순으로 있는 경우
                    while (true) {  // 파랑 이동
                        if (arr[bi][bj] == 'O') {
                            bIn = true;
                            break;
                        }
                        if (arr[bi][bj] == '#') {
                            bi++;
                            break;
                        }
                        bi--;
                    }
                    while (true) {  // 빨강 이동
                        if (arr[ri][rj] == 'O') {
                            rIn = true;
                            break;
                        }
                        if (arr[ri][rj] == '#' || ri == bi) {
                            ri++;
                            break;
                        }
                        ri--;
                    }
                }
            }
            else {              // 다른 열에 있는 경우
                while (true) {  // 빨강 이동
                    if (arr[ri][rj] == 'O') {
                        rIn = true;
                        break;
                    }
                    if (arr[ri][rj] == '#') {
                        ri++;
                        break;
                    }
                    ri--;
                }
                while (true) {  // 파랑 이동
                    if (arr[bi][bj] == 'O') {
                        bIn = true;
                        break;
                    }
                    if (arr[bi][bj] == '#') {
                        bi++;
                        break;
                    }
                    bi--;
                }
            }
            if (!bIn) {
                if (rIn) {
                    ans = c.depth;
                    break;
                } else {
                    q.offer(new Case(ri, rj, bi, bj, c.depth + 1));
                }
            }

            // 아래쪽으로 기울이기
            ri = c.ri; rj = c.rj;
            bi = c.bi; bj = c.bj;
            rIn = false; bIn = false;
            if (rj == bj) {     // 같은 열에 있는 경우
                if (ri < bi) {  // 빨파 순으로 있는 경우
                    while (true) {  // 파랑 이동
                        if (arr[bi][bj] == 'O') {
                            bIn = true;
                            break;
                        }
                        if (arr[bi][bj] == '#') {
                            bi--;
                            break;
                        }
                        bi++;
                    }
                    while (true) {  // 빨강 이동
                        if (arr[ri][rj] == 'O') {
                            rIn = true;
                            break;
                        }
                        if (arr[ri][rj] == '#' || ri == bi) {
                            ri--;
                            break;
                        }
                        ri++;
                    }
                }
                else {          // 파빨 순으로 있는 경우
                    while (true) {  // 빨강 이동
                        if (arr[ri][rj] == 'O') {
                            rIn = true;
                            break;
                        }
                        if (arr[ri][rj] == '#') {
                            ri--;
                            break;
                        }
                        ri++;
                    }
                    while (true) {  // 파랑 이동
                        if (arr[bi][bj] == 'O') {
                            bIn = true;
                            break;
                        }
                        if (arr[bi][bj] == '#' || bi == ri) {
                            bi--;
                            break;
                        }
                        bi++;
                    }
                }
            }
            else {              // 다른 열에 있는 경우
                while (true) {  // 빨강 이동
                    if (arr[ri][rj] == 'O') {
                        rIn = true;
                        break;
                    }
                    if (arr[ri][rj] == '#') {
                        ri--;
                        break;
                    }
                    ri++;
                }
                while (true) {  // 파랑 이동
                    if (arr[bi][bj] == 'O') {
                        bIn = true;
                        break;
                    }
                    if (arr[bi][bj] == '#') {
                        bi--;
                        break;
                    }
                    bi++;
                }
            }
            if (!bIn) {
                if (rIn) {
                    ans = c.depth;
                    break;
                } else {
                    q.offer(new Case(ri, rj, bi, bj, c.depth + 1));
                }
            }
        }

        System.out.println(ans);
    }
}
