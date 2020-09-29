// A program that uses the Box class...
// Call this file BoxDemo.java

class Box {
    double width;
    double height;
    double depth;

    void setDim(double w, double h, double d) {
        width = w;
        depth = d;
        height = h;
    }

    // display the volume of a box
    double volume() {
        return (width * height * depth);
    }
}

class BoxDemo5 {
    public static void main(String[] args) {
        // this two instance variable are totally separate...
        // change of one variable value not effect others....
        Box box1 = new Box(); 
        Box box2 = new Box();

        box1.setDim(10, 15, 20);
        box2.setDim(30, 50, 100);

        double volume1 = 0.0;
        double volume2 = 0.0;

        // you also do same this call function volume
        volume1 = box1.volume();
        System.out.println(volume1);
    
        volume2 = box2.volume();
        System.out.println(volume2);
    }
}