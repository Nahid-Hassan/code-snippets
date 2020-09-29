class AbstractDemo {
    public static void main(String[] args) {
        B b = new B();
        
        // A a = b; //okay
        // or
        //superClass obj = new subClass();
        A a =  new B();
        a.print();
        
        // a.print1(); // error compile time
        b.print1();
    }   
}

class B extends A {
    B() {
        super(10);
        System.out.println("Constructor for class B");
    }

    @Override
    public void print() {
        System.out.println("Defined under class B.");
    }

    public void print1() {
        System.out.println("print--1");
    }
}

abstract class A {
    A() {
        System.out.println("constructor without parameter....");
    }
    
    A(int x) {
        System.out.println("Constructor with parameter...");
    }

    public abstract void print();
}