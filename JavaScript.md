
# Local storage in JavaScript
- localStorage
	 - localStorage.setItem('student', stObjToString);
	 - var stord = localStorage.getItem('student');
	
# Parsing JSON and STRINGIFY
- convert an object into a string to be stored in local storage

	const student = {
		name: 'john',
		age: 23,
		isActive: true,
	}
	const stObjToString = JSON.stringify(student);
	const stJSON = JSON.parse(stObjToString) // to convert the string back to JSON
	
# Classes and Objects:
class User{
    constructor(firstname, lastname, credit){
        this.firstname = firstname;
        this.lastname  = lastname;
        this.credit   = credit;
    }
    getFullName(){
        return `${this.firstname} ${this.lastname} is my fullname`;
    }
}

const john = new User('John', 'Anderson', 34);
console.log(john.getFullName());
	

