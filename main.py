from pyscript import document, display

class Dog:
    def __init__(self, breed, age, name, owner):
        self.breed = document.getElementById("Dbreed").value #Attribute
        self.age = document.getElementById("Dage").value #Attribute
        self.name = document.getElementById("Dname").value #Attribute
        self.owner = document.getElementById("Downer").value #Attribute

def Submit(self):
        breed = document.getElementById("Dbreed").value
        age = document.getElementById("Dage").value
        name = document.getElementById("Dname").value
        owner = document.getElementById("Downer").value
        document.getElementById('output').innerHTML = " "

         # Displaying the attributes of the object
        display(f'{name} is a {age} year old {breed} owned by {owner}', target="output")