
# Local storage in JavaScript
localStorage
```
localStorage.setItem('student', stObjToString);
var stord = localStorage.getItem('student');
```
	
# Parsing JSON and STRINGIFY
Convert an object into a string to be stored in local storage
	
	```
	const student = {
		name: 'john',
		age: 23,
		isActive: true,
	}
	const stObjToString = JSON.stringify(student);
	const stJSON = JSON.parse(stObjToString) // to convert the string back to JSON 
	```
	
# Classes and Objects
class User{
    constructor(firstname, lastname, credit){
        this.firstname = firstname;
        this.lastname  = lastname;
        this.credit   = credit;
    }
    getFullName(){
        return `${this.firstname} ${this.lastname} is my fullname`;
    }
    editName(newname){
        const myname = newname.split(' ');
        this.firstname = myname[0];
        this.lastname = myname[1];
    }
}    

const john = new User('John', 'Anderson', 34);
//console.log(john);
console.log(john.getFullName());
john.editName('Alex Sam');
console.log(john.getFullName());

# Inheritance and method overriding
class Teacher extends User{
    constructor (firstname, lastname, credit, subject){
        super(firstname, lastname, credit);
        this.subject = subject;
    }
}
	

