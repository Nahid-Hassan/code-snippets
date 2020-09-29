// A program that uses the Box class...
// Call this file BoxDemo.java

class Box {
    double width;
    double height;
    double depth;

    // display the volume of a box
    double volume() {
        return (width * height * depth);
    }
}

class BoxDemo4 {
    public static void main(String[] args) {
        // this two instance variable are totally separate...
        // change of one variable value not effect others....
        Box box1 = new Box(); 
        Box box2 = new Box();

        double volume1 = 0.0;
        double volume2 = 0.0;

        // assign values to box1 instance variable
        box1.width = 10;
        box1.height = 20;
        box1.depth = 14;

        // assign values to box2 instance variable
        box2.width = 10;        
        box2.height = 10;
        box2.depth = 10;        

        // you also do same this call function volume
        volume1 = box1.volume();
        System.out.println(volume1);
    
        volume2 = box2.volume();
        System.out.println(volume2);
    }
}