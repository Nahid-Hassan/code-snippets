/**
 * final keyword er maddome jodi amra kuno variable declare kori tahole...sei 
 * variable er man amra ekbarei jonnoi change korte parbo....
 * 
 * and 
 * 
 * final keyword use kore kuno method ba class declare korle sei method ba class ke 
 * are override kora jai na....
 */

class FinalDemo {
    public static void main(String[] args) {
        B obj = new B();
        obj.print();
    }
}

class A {
    public void print() {
        System.out.println("Class A...");
    }
}

class B extends A {
    public void print() {
        System.out.println("Class B...");
    }
}

final class D {
    public final void print() {
        System.out.println("Class D...use final keyword");
    }

    public void print1() {
        System.out.println("Class D ... not use final keyword");
    }
}

// cannot extends or inherit class D because final keyword

//class C extends D {
//    // cannot override...because print using final keyword
//    
//    // public void print() {
//    //     System.out.println("Class C...");
//    // }
//
//
//
//    public void print1() {
//        System.out.println("Class C...override Class D print1()...");
//    }
//}

