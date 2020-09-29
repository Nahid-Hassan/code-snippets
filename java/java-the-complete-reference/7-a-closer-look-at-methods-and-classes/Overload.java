// Demonstrate method overload ....

class Overload {
    public static void main(String[] args) {
        OverloadDemo ob = new OverloadDemo();

        ob.test();
        ob.test(10);
        ob.test(10, 20);
        double result = ob.test(123.25);
        ob.test(1,2,3); // no method that takes 3 integer value...in that time.
                        // java automatic type casting help...or play role.

        System.out.println(result);
    }
}

class OverloadDemo {
    void test() {
        System.out.println("No parameters.");
    }
    void test(int a) {
        System.out.println("a = " + a);
    }
    void test(int a, int b) {
        System.out.println("a and b: " + a + " " + b);
    }
    double test(double a) {
        System.out.println("double a: " + a);
        return a * a;
    }
    void test(double a, double b, double c) {
        System.out.println("OverloadDemo.test() :" + a + " " + b + " " + c);
    }
}
