class fdp {
    public static void main(String[] args) {
        ShapeFactory sf = new ShapeFactory();

        Shape circle = sf.getShape("Circle");
        circle.draw();
    }
}

public interface Shape {
    void draw();
}

public class Circle implements Shape {
    @Override
    public void draw() {
        System.out.println("Circle object is created...");
    }
}

public class ShapeFactory {
    public Shape getShape(String shapeType) {
        if(shapeType.equals(null)) {
            return null;
        } else if (shapeType.equalsIgnoreCase("Circle")) {
            return new Circle();
        }
        return null;
    }
}