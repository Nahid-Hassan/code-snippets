// Demonstrate java ternary operator

class Ternary {
    public static void main(String[] args) {
        int i = 10;
        int k = i < 0 ? -i : i; // get absolute value of i
        System.out.println("i " + i + " is k " + k);

        i = -10;
        k = i < 0 ? -i : i; // get absolute value of i
        System.out.println("i " + i + " is k " + k);
    }
}