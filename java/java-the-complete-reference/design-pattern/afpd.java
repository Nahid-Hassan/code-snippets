class afdp {
    public static void main(String[] args) {
        AbstractFactory af1 = FactoryProducer.getFactory(true);

        Shape shape1 = af1.getShape("circle");
        shape1.draw();

        AbstractFactory af2 = FactoryProducer.getFactory(false);

        Shape shape2 = af2.getShape("circle");
        shape2.draw();
    }
}

// step-1
interface Shape {
    void draw();
}

//step-2
public class RoundedCircle implements Shape {
    public void draw() {
        System.out.println("rounded circle");
    }
}

public class Circle implements Shape {
    public void draw() {
        System.out.println("circle");
    }
}

//step-3
public abstract class AbstractFactory {
    abstract Shape getShape(String shapeType); 
}

//step-4
public class ShapeFactory extends AbstractFactory {
    public Shape getShape(String shapeType) {
        if(shapeType.equalsIgnoreCase("circle")) {
            return new Circle();
        }

        return null;
    }
}

public class RoundedShapeFactory extends AbstractFactory {
    public Shape getShape(String shapeType) {
        if(shapeType.equalsIgnoreCase("circle")) {
            return new RoundedCircle();
        }

        return null;
    }
 }


//step-5
public class FactoryProducer {
    public static AbstractFactory getFactory(boolean rounded) {
        if(rounded) {
            return new RoundedShapeFactory();
        } else {
            return new ShapeFactory();
        }

        // return null; 
    }
}

