import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int V = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        boolean flag = false;
        int ans = -1;

        for (int i = 0; i < N; i++){
            if (A[i] == V){
                ans = i;
                flag = true;
            }
        }

        if (flag){
            System.out.println(ans);
        }else{
            System.out.println(-1);
        }
    }
}