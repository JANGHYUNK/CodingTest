import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String na = sc.nextLine();
        String[] parts = new String[na.length()];
        parts = na.split("");
        for (int i = 0; i < na.length(); i++) {
            System.out.println(parts[i]);
        }
    }
}