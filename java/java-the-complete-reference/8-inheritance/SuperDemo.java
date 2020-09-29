// demonstrate super()
// for method
// for hidden member


class Box {
    private double width;
    private double height;
    private double depth;

    Box(Box ob) {
        width = ob.width;
        height = ob.height;
        depth = ob.depth;
    }

    Box(double width, double height, double depth) {
        this.width = width;
        this.height = height;
        this.depth = depth;
    }

    Box() {
        width = height = depth = -1;
    } 

    Box(double len) {
        width = height = depth = len;
    }

    double volume() {
        return (width * height * depth);
    }
}

class BoxWeight extends Box {
    double weight;

    BoxWeight(BoxWeight ob) {
        super(ob);
        weight = ob.weight;
    }

    BoxWeight(double width, double height, double depth, double weight) {
        super(width, height, depth);
        this.weight = weight;
    }

    BoxWeight() {
        super();
        weight = -1;
    }

    BoxWeight(double len, double m) {
        super(len);
        this.weight = m;
    }
}


// this two class for another kind use of super
class A {
    int i;
}

class B extends A {
    int i; /// this i hide the i in A

    B(int a, int b) {
        super.i = a; // i in A
        i = b; // i in B
    }

    void show() {
        System.out.println("i in superclass: " + super.i);
        System.out.println("i in subclass:  " + i);
    }
}


class SuperDemo {
    public static void main(String[] args) {
        BoxWeight boxWeight = new BoxWeight(10,20,15,34.6);
        B b = new B(5,10);

        b.show();

        double vol = boxWeight.volume();
        System.out.println(vol);
    }
}


// this class for multi-hierarchy
class Shipment  extends BoxWeight {
    double cost;

    Shipment(Shipment ob) {
        super(ob);

        cost = ob.cost;
    }

    Shipment(double w, double h, double d, double m, double c) {
        super(w, h, d, m);
        cost = c;
    }

    //.............................
    //...................
}