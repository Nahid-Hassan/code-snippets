abstract class Figure {
    double dim1;
    double dim2;

    Figure(double a, double b) {
        dim1 = a;
        dim2 = b;
    }

    abstract double area();
}

class Rectangle extends Figure {
    Rectangle(double a, double b) {
        super(a, b);
    }

    double area() {
        System.out.println("Inside the area for Rectangle: ");
        return dim1 * dim2;
    }
}

class Triangle extends Figure {
    Triangle(double a, double b) {
        super(a, b);
    }

    double area() {
        System.out.println("Inside the area for Triangle...");
        return dim1 * dim2 * .5;
    }
}

class AbstractClass {
    public static void main(String[] args) {
        // Figure f = new Figure(10.10, 20.20);  // Error abstract class
        // but
        Figure f; // this is okay....just reference...no object

        Rectangle r = new Rectangle(10, 20);
        double rArea = r.area();
        System.out.println(rArea);

        Triangle t = new Triangle(12, 23);
        double tArea = t.area();
        System.out.println(tArea);
    }
}