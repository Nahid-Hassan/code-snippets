// Demonstrate liftime of a variable

class lifTime {
    public static void main(String[] args) {
        int x;

        for (x  = 0; x < 3; x++) {
            int y = -1; // y is initialized each time block is entered.
            System.out.println("Y is " + y);

            // initialized and value lost every iteration.

            y = 10;
            System.out.println("Y is " + y);
        }
    }
}

/*
 * Output: 
 * Y is -1 
 * Y is 10 
 * Y is -1 
 * Y is 10 
 * Y is -1 
 * Y is 10
 */