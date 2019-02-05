1. Syntax Parser
2. Lexical Environment
3. Execution Context
	- Global
	- Execution context is created in two phases
		1. Creation phases
		2. Code execution

### Name/value pairs and Objects
	Object - Collection of name value pairs
	
* Outer environemnt
* Hoisting - Set up memory space for variables and functions
* JS is single threaded, synchronous execution

### Function invocation and the execution stack
	- Execution contect is created in the stack starting with a 'Global Execution Context'
	
### Functions, context and variable environments
### The scope chain
### Scope, ES6 And Let
### Asynchronous callbacks
	* Event queue
### Types and JavaScript	
	- Dynamic typing
### Datatypes
- primitive
		- undefined
		- null
		- boolean
		- number
		- string
		- symbol
		
### coersion
### Comparison operators
### Default values
- window.var1 = window.var1 || "abc"

### Objects and functions	
- object can contain
		- primitive property
		- object property
		- function/method
### Object and literals
### Faking Namespaces
### JSON and Object literals
	- JSON.stringify()
	- JSON.parse()
### functions are objects
	first class functions
	function statements and function expressions	
### fuctional programming
### pass by value vs reference
### Objects, functions and this

### Arrays in JS
### Arguments and Spreads
### Function overloading		
### Syntax Parsers
### Automatic semicolon insertion
### Immediately invoked function expressions(IIFE)
```
eg: 
var greeting = function(name) {
		console.log('Hello ' + name);
	}('John');
eg:	
(function(name) {
	console.log('Hello ' + name);
})('John');
```
### IIFEs and Safe Code
- pass global object to IIFE
	
### Closures	
### Function factories
```
eg:
function makeGreeting(language) {
 
    return function(firstname, lastname) {
     
        if (language === 'en') {
            console.log('Hello ' + firstname + ' ' + lastname);   
        }

        if (language === 'es') {
            console.log('Hola ' + firstname + ' ' + lastname);   
        }
        
    }
    
}

var greetEnglish = makeGreeting('en');
var greetSpanish = makeGreeting('es');

greetEnglish('John', 'Doe');
greetSpanish('John', 'Doe');
```
### Closures and Callbacks

### Call, Apply and Bind 
### Bind
```
eg:	var person = {
		firstname: 'John',
		lastname: 'Doe',
		getFullName: function() {
			var fullname = this.firstname + ' ' + this.lastname;
			return fullname;
		}    
	}

	var logName = function(lang1, lang2){
		console.log('Logged:' + this.getFullName());
	}.bind(person); 
	logName();
```	

### Call
```
logName.call(person, 'en'); # to bind object while invoking a function and execute the function
```

### apply 
```
logName.call(person, ['en', 'es']);
```

### Function borrowing
```
person.getFullName.apply(person2); # borrow person's function to person2
```

### Function currying - Create a a copy of a function but with some preset parameters
```
eg:
function multiply(a, b) {
	return a*b;
}
var multipleByTwo = multiply.bind(this, 2);
```

## Functional Programming 

### Underscore.js
### loadash.com

## OO JS and Prototypal inheritance

### Classical vs Prototypal Inheritance
	- all objects in js have a 'proto{}' property
	- prototype chain
### Everything in JavaScript is an object (or a primitive)
	- base object - Object{}
	- function empty() {} - prototype of all function objects
	- array's proto - [] 
	
### Reflection and Extend	
- Reflection - An object can look at itself, listing and changing its properties and methods
- Extend - 
- Extends 
	
### building objects	
```	
  new 
	* function constructor - a function that's used specifically to construct an object.
		The 'this' variable points a new empty object, and that object is returned from the function automatically.
# function constructors and prototypes 
	Person.prototype.getFullName = function() {
		return this.firstname + ' ' + this.lastname;
	}	
```  
		
### Moment.js - momentjs.com		

### Arrays are objects in javascript
### Arrays and for .. in : why using for ..in on array for looping is dangerous:
	- it can iterate through the prototypes as well
	- so, it is safe to use normal for loop
	
	
### Object.create and Pure Prototypal Inheritance
```
eg:
	var person = {
		firstname: 'Default',
		lastname: 'Default',
		greet: function(){
			return 'Hi ' + this.firstname;
		}	
	}	
	var john = Object.create(person);
	john.firstname = 'John';
	john.lastname = 'Doe';
```
### Polyfill:
	Code that adds a feature which the engine may lack

### ES6 and Classes
	
### typeof, insstanceof
### Strict Mode

### Method chaining
```
	obj1.method1().method2() - Where both methods end up with a 'this' variable pointing to obj1
```  


## Build a library 	
	- Reusable library/framework
	- Easy to type structure like 'G$()'
	- Support jQuery
```	
=> structuring safe code
	// wrap up the code in an immediately invoked function
	
		(function(global, $) {
			
			var Greetr = function(firstName, lastName, language) {
				return new Greetr.init(firstName, lastName, language);
			}
			
			Greetr.prototype = {};
			
			Greetr.init = function(firstName, lastName, language) {
				var self = this;
				self.firstName = firstName || '';
				self.lastName = lastName || '';
				self.language = language || 'en';
			}
			
			Greetr.init.prototype = Greetr.prototype;
			global.Greetr = global.G$ = Greetr
			
		}(window, jQuery));
		
// Adding jQuery support
```
	

## Questions
1. What would the below code print?
```
b();
console.log(a);
var a = 'Hello World!';
function b() {
    var c = "test";
    console.log('Called b! ' + c);
}
```
	
