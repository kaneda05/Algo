import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) A[i] = sc.nextInt();

        int cnt = 0;
        for (int i = 0; i < N; i++){
            if (A[i] >= 2){
                boolean flag = true;
                for (int j = 2; j < A[i]-1; j++){
                    if (A[i] % j == 0){
                        flag = false;
                        break;
                    }
                }
                if (flag) cnt++;
            }
        }

        System.out.println(cnt);
    }
}