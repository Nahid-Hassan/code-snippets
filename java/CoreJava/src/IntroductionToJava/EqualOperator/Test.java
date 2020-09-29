package IntroductionToJava.EqualOperator;

public class Test {
    public static void main(String[] args) {
        A obj1 = new A();
        obj1.x = 10;

        A obj2 = new A();
        obj2.x = 10;

        System.out.println(obj1 == obj2); // false, because addr(obj1) != addr(obj2)
        System.out.println(obj1.x == obj2.x); // true 10 == 10

        A obj3 = obj1;
        System.out.println(obj3 == obj1); // true
    }
}

class A {
    public int x;
}