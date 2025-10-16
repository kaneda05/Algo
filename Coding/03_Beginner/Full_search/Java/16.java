import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int K = sc.nextInt();
        int[] A = new int[N];
        int[] B = new int[M];

        for (int i = 0; i < N; i++) A[i] = sc.nextInt();
        for (int j = 0; j < M; j++) B[j] = sc.nextInt();
        
        int cnt = 0;
        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++){
                if (A[i] + B[j] == K) cnt++;
            }
        }

        System.out.println(cnt);
    }
}