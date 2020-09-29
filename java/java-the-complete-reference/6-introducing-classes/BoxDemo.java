// A program that uses the Box class...
// Call this file BoxDemo.java

class Box {
    double width;
    double height;
    double depth;
}

class BoxDemo {
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

        // compute the volume of the box1
        volume1 = box1.depth * box1.height * box1.width;

        // compute the volume of the box1
        volume2 = box2.depth * box2.height * box2.width;
        
        System.out.println(volume1);
        System.out.println(volume2);
    }
}