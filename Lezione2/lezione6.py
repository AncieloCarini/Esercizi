# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.



# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type) -> str:
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type




#         def describe_Restaurant():
#             print(f"restaurant Name: {self.restaurant_name}")
#             print(f"cuisine Type: {self.cuisine_type}")



# def open_restaurant():
#     print("The restaurant is open!")
#     restaurant = Restaurant("Burger King", "Fast Food")
#     print(restaurant.restaurant_name)
#     print(restaurant.cuisine_type)



    
# open_restaurant()







# 9-2. Three Restaurants: Start with your class from Exercise 9-1. 
# Create three different instances from the class, and call describe_restaurant() for each instance.



        


# r = Restaurant('Mc_Donald', 'fastfood')
# r2 = Restaurant('burgerKing', 'fastfood')
# r3 = Restaurant('KFC', 'fastfood')



# r.describe_restaurant()
# r2.describe_restaurant()
# r3.describe_restaurant()







# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user. 
# Create several instances representing different users, and call both methods for each user.


# class User:
#     def __init__(self, first_name, last_name, email, age, occupation):

#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.age = age
#         self.occupation = occupation

#     def describe_user(self):
#         print(f"Name: {self.first_name} {self.last_name}")
#         print(f"Email: {self.email}")
#         print(f"Age: {self.age}")
#         print(f"Occupation: {self.occupation}")
        
#     def greet_user(self):
#         print(f"Hello, {self.first_name} {self.last_name}!")
        
# u1 = User('Angelo', 'Locarini', 'angelolocarini@gmail.com', 20, 'Fallito')
# u2 = User('Gabriele', 'De Cupis', 'deCupis@gmail.com', 28, 'Spazzino')
# u3 = User('Giuseppe', 'Guttoriello', 'Guttoriello@gmail.com', 65, 'in pensione')
        
        
# u1.greet_user()
# u1.describe_user()
# u2.greet_user()
# u2.describe_user()
# u3.greet_user()
# u3.describe_user()








# 9-4. Number Served: Start with your program from Exercise 9-1. 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. Print the number of customers the restaurant has served, 
# and then change this value and print it again. Add a method called set_number_served()
# that lets you set the number of customers that have been served. Call this method with a new number and print the value again. 
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business. 






class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served) -> str:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served





        def describe_Restaurant():
            print(f"restaurant Name: {self.restaurant_name}")
            print(f"cuisine Type: {self.cuisine_type}")
            print(f"Number Served: {self.number_served}")
            


        def client_served():
            print(f"Number of clients served: {self.number_served}")




def open_restaurant():
    print("The restaurant is open!")
    restaurant = Restaurant()
    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)
    print(restaurant.number_served)
    restaurant.number_served = 0
    print(restaurant.number_served)
    restaurant.set_number_served(10)
    print(restaurant.number_served)
    restaurant.increment_number_served(5)


            


        



            