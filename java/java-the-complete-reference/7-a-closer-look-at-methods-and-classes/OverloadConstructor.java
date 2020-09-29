// demonstrate overload-constructor

class Box {
    double width;
    double height;
    double depth;

    Box(double w, double h, double d) {
        width = w;
        height = h;
        depth = d;
    }

    Box() {
        width = -1;
        height = -1;
        depth = -1;
    }

    Box(double len) {
        width = depth = height = len;
    }

    double volume() {
        return width * depth * height;
    }
}

class OverloadConstructor {
    public static void main(String[] args) {
        Box box1 = new Box(10,20,25);
        Box box2 = new Box();
        Box box3 = new Box(7);

        double vol;

        vol = box1.volume();
        System.out.println("Volume of box1 is " + vol);

        vol = box2.volume();
        System.out.println("Volume of box2 is " + vol);

        vol = box3.volume();
        System.out.println("Volume of box3 is " + vol);
    }
}