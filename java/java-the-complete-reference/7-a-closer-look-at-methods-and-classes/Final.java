class Final {
    public static void main(String[] args) {
        Test t = new Test(10);
        // Test.b = 10;  // Error cannot assign final variable

        t.printNonStatic();
        Test.printStatic();
    }
}

class Test {
    final int a; // non-static final
    final static int b; // static final 

    Test(int y) {
        a = y;
    }

    static {
        b  =  12;
    }

    static void printStatic() {
        System.out.println(b);
    }

    void printNonStatic() {
        System.out.println(a);
    }
}