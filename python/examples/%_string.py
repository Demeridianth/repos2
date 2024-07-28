

name = ('Bob', 'Richards')

print('Hey, %s-----%s!' % name)
# Hey, Bob-----Richards!

# declaring a string variable
var1 = "Geek!"
var2 = "Geeks for Geeks"

# append multiple strings within a string
print("Hello %s Are you enjoying being at %s for preparations." % (var1, var2))
# Hello Geek! Are you enjoying being at Geeks for Geeks for preparations.





# declaring string variables
str1 = 'Understanding'
str2 = '%s'
str3 = 'at'
str4 = 'GeeksforGeeks'
 
# concatenating strings but %s not equal to string variables
final_str = "%s %s %s %s" % (str1, str2, str3, str4)
 
# printing the final string
print("Concatenating multiple strings using Python '%s' operator:\n")
print(final_str)