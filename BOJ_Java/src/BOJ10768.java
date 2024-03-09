import java.io.*;

public class BOJ10768 {
    static int month, day;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        month = Integer.parseInt(br.readLine());
        day = Integer.parseInt(br.readLine());
        String ans;

        if (month > 2) ans = "After";
        else if (month < 2) ans = "Before";
        else {
            if (day > 18) ans = "After";
            else if (day < 18) ans = "Before";
            else ans = "Special";
        }

        System.out.println(ans);
    }
}