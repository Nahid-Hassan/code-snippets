// objects may be passed to methods

class Test {
    int a, b;
    double width, height, depth;

    Test(int i, int j) {
        a = i; b = j;
    }

    Test(double width, double height, double depth) {
        this.width = width;
        this.height = height;
        this.depth = depth;
    }

    Test(Test ob) {
        this.width = ob.width;
        this.height = ob.height;
        this.depth = ob.depth;
    }

    double volume() {
        return this.depth * this.height * this.width;
    }

    boolean equalTo(Test o) {
        if(o.a == a && o.b == b) {
            return true;
        } else {
            return false;
        }
    }
}

class PassObject {
    public static void main(String[] args) {
        Test ob1 = new Test(100,22);
        Test ob2 = new Test(100,22);
        Test ob3 = new Test(-1, -1);

        System.out.println("ob1 == ob2: " + ob1.equalTo(ob2));
        System.out.println("ob1 == ob3: " + ob1.equalTo(ob3));
 
        Test box1 = new Test(10, 20, 30);
        Test box2 = new Test(box1);

        double vol = box2.volume();
        System.out.println(vol);
    }
}