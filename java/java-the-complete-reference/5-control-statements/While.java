// Demonstrate the while loop

class While {
    public static void main(String[] args) {
        int n = 10;

        // print 10 to 1;
        while (n > 0) {
            System.out.println("tick " + n);
            n--;
        }

        // while loop with false condition
        int a = 10, b = 20;

        while(a > b) {
            System.out.println("This will not be displayed.");
        }

        // while loop without body...or simply can be empty.
        int i = 100;
        int j = 200;

        while(++i < --j);

        System.out.println("Midpoint is " + i);

        i = 100; j = 200;
        // same example with 
        while (++i < --j);

        System.out.println("Midpoint is " + i);

    }
}