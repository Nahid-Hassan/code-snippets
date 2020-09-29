class AbstractDemo {
    public static void main(String[] args) {
        B b = new B();
        b.print();
    }
}

class B extends A {
    @Override
    public void print() {
        System.out.println("Defined under class B.");
    }
}

abstract class A {
    public abstract void print();
}