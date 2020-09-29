package IntroductionToJava.Overloading;

public class Test {
    public static void main(String[] args) {
        MethodOverlaoding t = new MethodOverlaoding();
        t.print(10);
        t.print(10.10);
    }
}

class MethodOverlaoding {
    void print(int x) {
        System.out.println("int x :" + x);
    }

    void print(double x) {
        System.out.println("double x: " + x);
    }
}