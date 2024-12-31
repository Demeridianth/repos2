//Create Read Update Delete
//CRUd
//Creat



using System.Text;

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

StringBuilder morePet = new StringBuilder();
morePet.Append("a new pet");
// Console.WriteLine(morePet.ToString());

// REMOVE
morePet.Remove(0, 6);
// Console.WriteLine(morePet);


// class Program
// {
//     static void Main(string[] args)
//     {
//         StringBuilder newPet = new StringBuilder();
//         newPet.Append("This is a test.");
//         Console.WriteLine(newPet.ToString());
//     }
// }



// ARRAY

// Create
string[] favoriteRats = ["fancy rat", "brown rat", "radioactive rat", "wolf rat"];


// Read
// foreach(var rat in favoriteRats)
// {
//     Console.WriteLine(rat);
// }


// Update
// favoriteRats[0] = "Fancy Rat";

// LINQ "Update array linq"
// filter array for everything that starts with a 'B'
var newFavoriteRats = favoriteRats.Where((e) => e.StartsWith("b"));

foreach(var rat in newFavoriteRats)
{
    Console.WriteLine(rat);
}


