

- $(‘tag-name’) selects all elements of a type tag-name in the document
  - $(‘p’) selects all paragraphs in the document.
	
- The html() method gets the html contents (innerHTML) of the first matched element
- We can have only one on-load function but we can have more than one document.ready function. Document.ready function is called DOM when it is loaded. The on-load function is called DOM and images are loaded on the page

- jQuery load method is a powerful AJAX method that is used to load the data from a server and assign the data to the element without loading the page.

- How do you make an ajax call?
  - The load( url, [data], [callback] ) method load HTML from a remote file and inject it into the DOM
	
- jQuery.ajax() is an all-encompassing Ajax request method. It creates customized Ajax requests, with options for response time, handling a failure for blocking (synchronous) or non-blocking (asynchronous) requests, formatting a request for the response, etc.
	jQuery.get() is a shortcut method that uses jQuery.ajax() to create an Ajax request for simple retrieval of information. Other pre-built Ajax requests include jQuery.post(), jQuery.getScript(), and jQuery.getJSON().	

- Can you use your own specific characters in place of $ in jQuery?
	Yes, you can use your own variable in place of $ by using the method called no Conflict () method.
	var sample = $.noConflict()
	
- charAt() method returns the character at the specified index.

- What are the four parameters used for the jQuery Ajax method?
	- URL – Need to specify the URL to send the request
	- Type – Specifies type of request (Get or Post)
	- Data – Specifies data to be sent to the server
	- Cache – Whether the browser should cache the requested page
	
- jQuery.ajax method is used for asynchronous HTTP requests	
 
	
	
