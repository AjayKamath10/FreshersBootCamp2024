using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        string Name = "";
        int EmployeeId = 0;
        double salary = 0.0;
        
        Console.Write("Enter Name: ");
        Name = Console.ReadLine();
        
        Console.Write("Enter Employee ID: ");
        EmployeeId = Convert.ToInt32(Console.ReadLine());
        
        Console.Write("Enter Salary: ");
        salary = Convert.ToDouble(Console.ReadLine());
		
		string DisplayMessage;
		
        DisplayMessage = "\nName: " + Name;
		DisplayMessage += "\nEmployee Id: " +  EmployeeId;
		DisplayMessage += "\nSalary: " + salary;
		
		Console.WriteLine(DisplayMessage);
    }
}