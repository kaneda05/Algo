import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int N = Math.min(A, B);
        int ans = 0;

        for (int i = 1; i <= N; i++){
            if (A % i == 0 && B % i == 0) {
                ans = i;
            }
        }
    
    System.out.println(ans);
    }
}