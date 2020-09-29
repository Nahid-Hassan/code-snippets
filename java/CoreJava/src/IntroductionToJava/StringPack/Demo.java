package IntroductionToJava.StringPack;

public class Demo {
    public static void main(String[] args) {
        String name = "Nahid";
        name.concat(" Hassan");
        System.out.println(name);

        name = name.concat(" Hassan");
        System.out.println(name);
    }
}
// String immutable
// String pool concept......
// String concat()