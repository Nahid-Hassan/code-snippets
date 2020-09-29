// A program that uses the Box class...
// Call this file BoxDemo.java

class Box {
    double width;
    double height;
    double depth;

    // constructor with parameter.
    Box(double w, double h, double d) {
        System.out.println("Constructor creating........");
        width = w;
        depth = d;
        height = h;
    }

    // display the volume of a box
    double volume() {
        return (width * height * depth);
    }
}

class BoxDemo7 {
    public static void main(String[] args) {
        // this two instance variable are totally separate...
        // change of one variable value not effect others....
        Box box1 = new Box(10, 20, 30); 
        Box box2 = new Box(14, 17, 19);

        double volume1 = 0.0;
        double volume2 = 0.0;

        // you also do same this call function volume
        volume1 = box1.volume();
        System.out.println(volume1);
    
        volume2 = box2.volume();
        System.out.println(volume2);
    }
}