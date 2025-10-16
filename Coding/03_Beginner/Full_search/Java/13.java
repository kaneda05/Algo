import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        String c = sc.next();
        boolean found = false;

        for (int i = 0; i < S.length(); i++){
            if (S.charAt(i) == c.charAt(0)){
                found = true;
                break;
            }
        }

        if (found){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}