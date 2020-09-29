//char variables behave like integers.

class CharDemo2 {
    public static void main(String[] args) {
        char ch1;

        ch1 = 'X';
        System.out.println("ch1 contains: " + ch1);

        ch1++; // increment ch1, same as statement ch1 = ch1 + 1;
        System.out.println("ch1 is now: " + ch1);
    }
}

/**
 * To compile and run program:
 * 
 * $ javac CharDemo.java 
 * $ java CharDemo 
 * Output: 
 * ch1 contains: X 
 * ch1 is now: Y
 */

 /**
  * Note: IN the formal specification for Java, char is referred to as an integral type, which
  * means that it is in the same as category as int, byte, long, short. However, because its
  * principal use is for representing Unicode characters, char is commonly considered to be in
  * a category of its own.
  */