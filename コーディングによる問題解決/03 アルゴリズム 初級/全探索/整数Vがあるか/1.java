import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int V = sc.nextInt();

        boolean isFound = false;
        for(int n = 0; i < N; i++){
            int A = sc.nextInt();

            if(A == V){
                isFound = true;
            }
        }

        if(isFound){
            System.out.println("Yes");
        }
        else{
        System.out.println("No");
        }
    sc.close();
  }
}