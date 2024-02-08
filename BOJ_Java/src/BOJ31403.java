import java.io.*;

public class BOJ31403 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String As = br.readLine();
        String Bs = br.readLine();
        String Cs = br.readLine();

        int Ai = Integer.parseInt(As);
        int Bi = Integer.parseInt(Bs);
        int Ci = Integer.parseInt(Cs);

        System.out.println(Ai + Bi - Ci);
        System.out.println(Integer.parseInt(As + Bs) - Ci);
    }
}
