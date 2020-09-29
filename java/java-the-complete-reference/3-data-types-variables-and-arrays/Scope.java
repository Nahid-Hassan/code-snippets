// Demonstrate block scope

class Scope {
    public static void main(String[] args) {
        int x; // know to all code within main

        x = 10;

        if(x == 10) { // start a new scope
            int y = 10; // know only to this block

            // x and y both know here.
            
            x = y * 2;
        }
        // y = 100; // Error! y not known here

        // x is steal know here
        System.out.println("x is " + x);
    }
}

//output:
//x is 20