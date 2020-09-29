// Demonstrate casts.

class Conversion {
    public static void main(String[] args) {
        byte b;
        int i = 257;
        double d = 323.121;

        System.out.println("\nConversion of int ot byte: ");
        b = (byte) i;

        System.out.println("i and b " + i + " " + b);
    
        System.out.println("\nConversion of double to int: "); 
        i = (int) d;

        System.out.println("d and i " + d + " " + i);

        System.out.println("\nConversion of double to byte: ");
        b = (byte) d;

        System.out.println("d and b " + d + " " + b);
    }
}

/*
 * Output: Conversion of int ot byte: 
 * i and b 257 1
 * 
 * Conversion of double to int: 
 * d and i 323.121 323
 * 
 * Conversion of double to byte: 
 * d and b 323.121 67
 * 
 */

 /** 
    Why output: 1 and 67.

    for type casting integer to byte. then the integer value modulo by (% 256);
    so, 257 % 256 = 1;

    byte <-- double.
    first fraction part is remove. then modulo by 256
    that's why output is 256
    
    But why modulo by 256!!!!!!!
    modulo by range of type. here is byte.
  */