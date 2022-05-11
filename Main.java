public class Main {

    static class House {

        private String name = null;
    
        House(String name){
            this.name = name;
        }
    
        public String getName() {
            return this.name;
        }
    
        public void setName(String name) {
            this.name = name;
        }
    }

    static class Human {
        
        private String name_human = null;
        private House house_human;

        Human(String name, House house){
            this.name_human = name;
            this.house_human = house;
        }

        public String getNameHumanAndHouse() {
            return this.name_human + " И у него есть дом с именем \"" + this.house_human.getName() + "\"";
        }

        public void setNameHouse(String name_house){
            this.house_human.setName(name_house);
        }
    }

    public static void main(String[] args) {
        System.out.println("\n");
        House home = new House("Я дом и я приватный");
        System.out.println("Объект home = " + home.getName());

        System.out.println();

        Human max = new Human("Максим", home);
        System.out.println("Объект max = " + max.getNameHumanAndHouse());
        
        System.out.println();

        max.setNameHouse("Дом Максима");
        System.out.println("Объект home = " + home.getName());
        System.out.println("Объект max = " + max.getNameHumanAndHouse());

        System.out.println("\n");
    }
}

