import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = 9;
        int[] arr = new int[N];
        for(int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }

        int value = arr[0];

        for(int i = 1; i < N; i++) {
            if(value < arr[i] ) {
                value = arr[i];
            }
        }

        int count = 0;
        for(int i = 0; i < N; i++) {
            if(value == arr[i]) {
                count = i + 1;
            }
        }

        System.out.println(value);
        System.out.println(count); // 인덱스 번호 찾는방법
    }
}
