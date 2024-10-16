//Create Read Update Delete
//CRUd
//Creat
using System.Text;
using ConsoleApp1;

string pet = "fish";


//COncatenation
pet = "porcupine " + pet;


//Template Literal
// Console.WriteLine($"i am getting a {pet}");


//Read
//Console.Writeline()


//Update
string newPet = pet.Replace("porcupine", "blue dot");
// Console.WriteLine(newPet);


//Delete
//String BUilder // memory economy, doesnt creates a new object but works with the same
StringBuilder newCrustecean = new StringBuilder();
newCrustecean.Append("fiddler crab");
Console.WriteLine(newCrustecean);
newCrustecean.Remove(0, 8); // (start, end)
Console.WriteLine(newCrustecean);

Test myClass = new Test();
myClass.SayHello();
