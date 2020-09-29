// Demonstrate literal in java

/**
 * Literal : Any constant value which can be assigned to the variable is called
 * as literal/constant.
 */

class LiteralInteger {
    public static void main(String[] args) {
        // Integer literal
        // ----------------------------------------------------------------        
        // int base 10 or decimal
        int num_base_10 = 10; // here 10 is integer literal which is not changed.
        System.out.println(num_base_10);

        num_base_10 = 24;      // Here value of num is change to 24, before it 10.
                     // Here num value is change but 24 is literal which constant all time.  
        System.out.println(num_base_10);

        // int base 8 or octal
        int num_base_8 = 01232;
        System.out.println(num_base_8);

        // int base 16 or hexa-decimal
        int num_base_16 = 0x32983729;
        System.out.println(num_base_16);

        // int base 2 or binary
        int num_base_2 = 0b1010101010;
        System.out.println(num_base_2);

        // in JDK 7 underscore(_, __) is an integer literal
        int num_with_underscore_literal = 123_456_678;
        System.out.println(num_with_underscore_literal);

        // you also can use __ (double underscore) but it cannot come at the beginning or end of a literal
        num_with_underscore_literal = 123__456__789;             
        System.out.println(num_with_underscore_literal);
    
        // The use of underscore in an integer literal is especially useful when encoding such things
        // as telephone numbers, customer ID numbers, part of numbers and so on.
        // They are also useful for providing visual groups when specifying binary literals.

        int binary_value = 0b0001_0010_0011;
        System.out.println(binary_value);
    }
}

/**
 * output: 
 * 10 
 * 24 
 * 666 
 * 848836393 
 * 682 
 * 123456678 
 * 123456789 
 * 291
 */

 // Additional information: http://java.boot.by/ocpjp7-upgrade/ch01s02.html
