// A program that uses the Box class...
// Call this file BoxDemo.java

class Box {
    double width;
    double height;
    double depth;

    // display the volume of a box
    void volume() {
        System.out.print("Volume is: ");
        System.out.println(width * height * depth);
    }
}

class BoxDemo4 {
    public static void main(String[] args) {
        // this two instance variable are totally separate...
        // change of one variable value not effect others....
        Box box1 = new Box(); 
        Box box2 = new Box();

        // assign values to box1 instance variable
        box1.width = 10;
        box1.height = 20;
        box1.depth = 14;

        // assign values to box2 instance variable
        box2.width = 10;        
        box2.height = 10;
        box2.depth = 10;        

        // you also do same this call function volume
        box1.volume();
        box2.volume();
    }
}