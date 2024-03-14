import java.io.*;
import java.util.*;

public class BOJ5575 {
    static int sh, sm, ss;
    static int eh, em, es;
    static int ah, am, as;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            sh = Integer.parseInt(st.nextToken());
            sm = Integer.parseInt(st.nextToken());
            ss = Integer.parseInt(st.nextToken());
            eh = Integer.parseInt(st.nextToken());
            em = Integer.parseInt(st.nextToken());
            es = Integer.parseInt(st.nextToken());

            ah = eh - sh;
            am = em - sm;
            as = es - ss;

            if (as < 0) {
                am--;
                as += 60;
            }
            if (am < 0) {
                ah--;
                am += 60;
            }

            System.out.println(ah + " " + am + " " + as);
        }
    }
}
