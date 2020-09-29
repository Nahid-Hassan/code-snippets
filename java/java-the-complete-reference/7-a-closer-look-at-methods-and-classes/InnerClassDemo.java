// this type of coding for event handling........

class Outer {
    int outer_x = 100;

    void test() {
        for(int i = 0; i< 10; i++) {
            class Inner {
                void display() {
                    System.out.println("display: outer_x -> " + outer_x);
                }
            }
            Inner inner = new Inner();
            inner.display();
        }
    }
}

class InnerClassDemo {
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.test();
    
        int num[] = {1,2,3,4,5,6,7,8,9,10};
        System.out.println(num.length);
    }
}