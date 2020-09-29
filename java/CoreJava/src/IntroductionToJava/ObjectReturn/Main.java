package IntroductionToJava.ObjectReturn;

public class Main {
    public static void main(String[] args) {
        Human human = new Human();
        human.skinTone = "White";
        System.out.println(human.skinTone);

        Human obj1 = human.produce();
//        obj1.skinTone = "Black";
        System.out.println(obj1.skinTone);
    }
}

class Human {
    String skinTone;

    public Human produce() {
        Human human;
        human = new Human();

        human.skinTone = this.skinTone;

        return human;
    }
}