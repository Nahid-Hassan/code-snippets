// Demonstrate char data type

class CharDemo {
    public static void main(String[] args) {
        char ch1, ch2;

        ch1 = 88;
        ch2 = 'Y';

        System.out.println("Ch1 :" + ch1);
        System.out.println("Ch2 :" + ch2);
    }
}
/**
 * To compile and run program:
 * 
 * $ javac CharDemo.java 
 * $ java CharDemo 
 * Output: Ch1 :X 
 * Ch2 :Y
 */

 /**
  * Additional information: 
  * Notice that ch1 is assigned the value 88, which ASCII(and Unicode) value that corresponds to the 
  * letter X. As mentioned, the ASCII character set occupies the first 127 values in the Unicode
  * character set. For this reason, all the "OLD Tricks" that you may have used with characters in
  * others languages will work in Java, too.
  */