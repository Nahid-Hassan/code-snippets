// Demonstrate boolean values

class BoolTest {
    public static void main(String[] args) {
        boolean b;
        
        b = false;
        System.out.println("b is " + b);
        b = true;
        System.out.println("b is " + b);
        // a boolean vale can control the if statement
        if(b) {
            System.out.println("This is executed.");
        }
        b = false;
        if(b) {
            System.out.println("This is not executed.");
        }
        // outcome of a relational operator is a boolean value.
        System.out.println("10 > 9 is " + (10 > 9)); 
        // using parenthesis in (10 > 9) because
        // + operator has a higher precedence than the >.
    }
}

/**
 * output:
 * --------- 
 * b is false 
 * b is true 
 * This is executed. 
 * 10 > 9 is true
 */