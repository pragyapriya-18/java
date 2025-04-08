import java.util.Scanner;

class WhileLoopReverse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        int rev = 0;

        // Using while loop to reverse the number
        while (num != 0) {
            int digit = num % 10;
            rev = rev * 10 + digit;
            num /= 10;
        }

        System.out.println("Reversed number: " + rev);
        sc.close();
    }
}