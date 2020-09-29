// This program will not compile

/**
 * This 
 * program
 * will not
 * compile
 */

class ScopeError {
    public static void main(String[] args) {
        int bar = 1;

        if (bar == 1) { // create a new scope
            int bar = 2; // compile-time error - bar already defined. 
        }
    }
}