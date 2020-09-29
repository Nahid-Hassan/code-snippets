// Demonstrate for-traditional loop

class ForTraditional {
    public static void main(String[] args) {
        int n;

        // declare initialization variable outside the for loop
        for(n = 10; n > 0; n--) {
            System.out.println("tick " + n);
        }
        // declare initialization variable inside the for loop
        // in this you need to remember variable scope....

        System.out.println();
        for(int i = 0; i < 10; i++) {
            System.out.println("tick : " + i);
        }
    }
}