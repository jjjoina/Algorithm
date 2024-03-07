import java.io.*;
import java.util.*;

public class BOJ17143 {
    static int R, C;
    static int M;       // 상어의 수
    static int[][] arr;     // 빈 칸 또는 상어의 번호
    static Shark[] sharks;
    static int[][] temp;
    static int r, c, s, d, z;
    static int ans;

    static class Shark {
        int r, c, s, d, z;

        Shark(int r, int c, int s, int d, int z) {
            this.r = r;
            this.c = c;
            this.s = s;
            this.d = d;
            this.z = z;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[R][C];
        temp = new int[R][C];
        sharks = new Shark[M + 1];
        for (int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine());
            r = Integer.parseInt(st.nextToken()); r--;
            c = Integer.parseInt(st.nextToken()); c--;
            s = Integer.parseInt(st.nextToken());   // 속력
            d = Integer.parseInt(st.nextToken());   // 이동 방향 - 1:위, 2:아래, 3:오른쪽, 4:왼쪽
            z = Integer.parseInt(st.nextToken());   // 크기

            if (d <= 2) s %= 2 * R - 2;
            else        s %= 2 * C - 2;

            sharks[i] = new Shark(r, c, s, d, z);    // 상어
            arr[r][c] = i;
        }

        for (int fishingKing = 0; fishingKing < C; fishingKing++) {
//            System.out.println();
//            System.out.println(fishingKing + 1 + "초");
//            for (int[] row : arr) System.out.println(Arrays.toString(row));

            // 상어 잡기
            for (int i = 0; i < R; i++) {
                if (arr[i][fishingKing] > 0) {
                    // 행열로 찾음
//                    System.out.println(arr[i][fishingKing] + "번 상어 먹힘");
                    ans += sharks[arr[i][fishingKing]].z;
//                    System.out.println("ans = " + ans);
                    sharks[arr[i][fishingKing]] = null;
                    arr[i][fishingKing] = 0;
                    break;
                }
            }

            // 상어 이동
            for (int i = 1; i <= M; i++) {
                if (sharks[i] == null) continue;
                arr[sharks[i].r][sharks[i].c] = 0;

                // 이동
                if (sharks[i].d == 1) {         // 위
                    sharks[i].r -= sharks[i].s;
                    if (sharks[i].r < 0) {
                        sharks[i].r *= -1;
                        sharks[i].d = 2;    // 방향 전환
                    }
                    if (sharks[i].r >= R) {
                        sharks[i].r = (R - 1) - (sharks[i].r - (R - 1));
                        sharks[i].d = 1;    // 방향 전환
                    }
                }
                else if (sharks[i].d == 2) {  // 아래
                    sharks[i].r += sharks[i].s;
                    if (sharks[i].r >= R) {
                        sharks[i].r = (R - 1) - (sharks[i].r - (R - 1));
                        sharks[i].d = 1;    // 방향 전환
                    }
                    if (sharks[i].r < 0) {
                        sharks[i].r *= -1;
                        sharks[i].d = 2;    // 방향 전환
                    }
                }
                else if (sharks[i].d == 3) {  // 오른쪽
                    sharks[i].c += sharks[i].s;
                    if (sharks[i].c >= C) {
                        sharks[i].c = (C - 1) - (sharks[i].c - (C - 1));
                        sharks[i].d = 4;    // 방향 전환
                    }
                    if (sharks[i].c < 0) {
                        sharks[i].c *= -1;
                        sharks[i].d = 3;    // 방향 전환
                    }
                }
                else {                        // 왼쪽
                    sharks[i].c -= sharks[i].s;
                    if (sharks[i].c < 0) {
                        sharks[i].c *= -1;
                        sharks[i].d = 3;    // 방향 전환
                    }
                    if (sharks[i].c >= C) {
                        sharks[i].c = (C - 1) - (sharks[i].c - (C - 1));
                        sharks[i].d = 4;    // 방향 전환
                    }
                }

                // temp에 기록
                if (temp[sharks[i].r][sharks[i].c] > 0) {   // 해당 자리에 상어가 이미 있는 경우
                    // 새로온 상어가 이기는 경우
                    if (sharks[i].z > sharks[temp[sharks[i].r][sharks[i].c]].z) {
                        sharks[temp[sharks[i].r][sharks[i].c]] = null;  // 기존에 있던 상어 사라짐
                        temp[sharks[i].r][sharks[i].c] = i;     // 새로온 상어가 자리 차지
                    }
                    // 새로온 상어가 지는 경우
                    else {
                        sharks[i] = null;
                    }
                } else {    // 빈 자리인 경우
                    temp[sharks[i].r][sharks[i].c] = i;
                }
            }

            // arr에 반영하며 temp 원복
            for (int i = 1; i <= M; i++) {
                if (sharks[i] == null) continue;
                arr[sharks[i].r][sharks[i].c] = i;
                temp[sharks[i].r][sharks[i].c] = 0;
            }
        }

        System.out.println(ans);
    }
}
