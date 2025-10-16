import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        int maxA = A[0];
        for (int i = 0; i < N; i++){
            if (A[i] > maxA){
                maxA = A[i];
            }
        }

        int cnt = 0;
        for (int i = 0; i < N; i++){
            if (A[i] == maxA){
                cnt++;
            }
        }
        
        System.out.println(cnt);    
    }
}