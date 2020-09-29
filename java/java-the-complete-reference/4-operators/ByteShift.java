// Left shifting a byte value

class ByteShift {
    public static void main(String[] args) {
        byte a = 64, b;
        int i;

        i = a << 2; // 64 * 2 => 128 * 2 => 256 

        b = (byte) (a << 2);

        System.out.println("i = a << 2 : " + i);
        System.out.println("b = a << 2 : " + b);

        System.out.println("32 << 2 : " + (32 << 2));
        System.out.println("32 >> 2 : " + (32 >> 2));
        System.out.println("32 << 1 : " + (32 << 1));
        System.out.println("32 >> 1 : " + (32 >> 1));
    }
}