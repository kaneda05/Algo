import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        boolean flag = true;

        if (N >= 2) {
            for (int i = 2; i < N; i++) {
                if (N % i == 0) {
                    flag = false;
                    break;
                }
            }
        } else {
            flag = false;
        }

        if (flag) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
