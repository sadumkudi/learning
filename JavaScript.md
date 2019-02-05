
# Local storage in JavaScript
localStorage
localStorage.setItem('student', stObjToString);
var stord = localStorage.getItem('student');
	
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
	

