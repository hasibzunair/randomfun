
class Person:
	# class attribute
	def __init__(self, first_name):
		self.first_name = first_name

class Person_1:
	# public variable
	first_name = "Hasib"


#tk = Person("Hasib")
#print(tk.first_name)

#tk = Person_1()
#print(tk.first_name)

# since its a public variable, we can easily change it
#tk.first_name = "Not Hasib"
#print(tk.first_name)

class Person_3:
	def __init__(self, first_name, email, age):
		self.first_name = first_name
		self.email = email
		self.age = age

	def update_email(self, new_email):
		self.email = new_email	

	def show_age(self):
		return self.age

tk = Person_3("Hasib", "hz@gmail.com", 24)
tk.update_email("zz@gmail.com")

print(tk.email)
age = tk.show_age()
print(age)










