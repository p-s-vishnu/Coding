public class Person {
    private int age;

	public Person(int initialAge) {
  		    age = initialAge;
    }

	public void amIOld() {
  		String s = " ";
        if(age<0){
            System.out.println("Age is not valid, setting age to 0.");
            age=0;
        }
        if(age<13 ){
            s="You are young.";
        }else if (age >= 13 && age <18){
            s="You are a teenager.";
        }else{
            s="You are old.";
        }
        System.out.println(s);
	}

	public void yearPasses() {
  		age++;
	}
