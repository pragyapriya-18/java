public class BoxingAndUnboxing {
    public static void main(String[] args) {
        int a = 10;  // Boxing: converting int to Integer
        Integer boxedA = a; // Auto-boxing
        System.out.println("Boxed value: " + boxedA);

        Integer b = 20;  // Unboxing: converting Integer to int
        int unboxedB = b; // Auto-unboxing
        System.out.println("Unboxed value: " + unboxedB);

    }
}
