class StaticClass {
    static int a = 40;
    static int b;
    int c;

    static {
        System.out.println("Static block initialize...");
        b = a * 4;
        // c = 10; // Error!! cannot access without static variable in static block
    }

    static void meth(int x) {
        System.out.println(a);
        System.out.println(b);
        System.out.println(x);
        // System.out.println(c); // Error!! c is not static variable
    }
}

class StaticDemo {
    public static void main(String[] args) {
        StaticClass.meth(10);
    }
}