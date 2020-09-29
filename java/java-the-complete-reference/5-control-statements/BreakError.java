/// this program contains an error

/**
 * This program
 * 
 * not run
 * 
 * you get a compile error.
 */

class BreakError {
    public static void main(String[] args) {
        one: for(int i = 0; i < 3; i++) {
            System.out.print("pass " + i + ": ");
        }

        for(int j = 0; j < 100; j++) {
            if(j == 0) {
                break one;
            }
            System.out.print(j + " ");
        }
        System.out.println();
    }
}
/**
 *  BreakError.java:19: error: undefined label: one 
 *               break one;
 *  1 error error:
 *  compilation failed
 */