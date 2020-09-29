class OuterClass {
    int x = 14;
    int y = 15;
    // static int c = x * y; //Error.. x and y is not static
    static int c = 232;

    class InnerClass {
        //code
        int x; // this x is different from outer class x;
        
        // we cannot access inner class member from outer class
        // but we can access outer class member from inner class

        void show() {
            System.out.println("i am in inner class....");
            System.out.println(x);
        }

        void callOuterClassMethod() {
            show1();
        }

        void print() {
            System.out.println(y);
        }
    }

    static class StaticInnerClass{
        void printNonStatic() {
            // System.out.println(x); // compile error...we cannot access non_static_variable/member
            // System.out.println(y); // compile error...we cannot access non_static_variable/member
        }
        void printStatic() {
            System.out.println("i am in static inner class...print static method");
            System.out.println(c);
        }
    }

    void show() {
        System.out.println("i am in outer class....");
        System.out.println(x);
    }

    void show1() {
        System.out.println("i am in outer class....");
        System.out.println(x);
    }
}

class NonStaticInner {
    public static void main(String[] args) {
        // we can not create object below like this
        // InnerClass obj = new InnerClass() 

        // To create InnerClass object...first we create OuterClass object
        OuterClass oc = new OuterClass();

        //then using OuterClass object we create InnerClass object...
        //because InnerClass is member Class for OuterClass

        OuterClass.InnerClass ic = oc.new InnerClass();

        // create static inner class object
        OuterClass.StaticInnerClass sic = new OuterClass.StaticInnerClass();

        // we cannot create StaticInnerClass object like non-static inner class...

        ic.x = 10;
        ic.show();
        ic.callOuterClassMethod();
        ic.print();

        oc.show();

        sic.printStatic();
    }
}