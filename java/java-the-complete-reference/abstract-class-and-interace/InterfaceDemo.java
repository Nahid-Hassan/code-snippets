class InterfaceDemo {
    public static void main(String[] args) {
        B b = new B();
        b.print();
        System.out.println(b.x);
        System.out.println(A.x);

        P p = new P();
        p.fx();
        p.fy();
    }
}

interface A {
    /**
     * by default all the variable you declare in the interface 
     * is already static and final
     * static means you can access it without creating object
     * final means you cannot change the value of this variable
     */
    public final static int x = 10;
    
    /**
     * all the method you declare as prototype in interface...
     * you cannot able to write their definition or implement it
     * by default all the method in interface are abstract 
     * 
     * you cannot create constructor in interface ... because
     * by default all the method in interface are abstract method
     */
    public abstract void print();

    // A() {
        //not possible
    // }
}

/**
 * We can implement multiple class(interface) under one class
 * we can  not extend multiple class under one class
 * 
 * class B extends C implements A, D, E {
 *      // this class is completely okay
 * }
 * 
 * but
 * 
 * class B extends C, M implements A, M {
 *      // wrong cannot extends multiple class........
 * }
 */
class B implements A {
    @Override
    public void print() {
        System.out.println("implemented by class b");
    }
}

interface M {
    int x = 123;
    void print1(); 
}

interface N extends M {
    int x = 230;
    int y = 232;
    void print2();
}

interface O extends N {
    int x = 2323;
    void print3();
}

class P implements O {
    
    /**
     * must use modifier public
     */
    public void print1() {

    }
    public void print2() {

    }
    public void print3() {

    }

    void fx() {
        System.out.println(x);
    }
    void fy() {
        System.out.println(y);
    }
}