/*
Finding HTML elements

document.getElementById(id)
document.getElementsByTagName(name)
document.getElementsByClassName(name)
*/
/*
Changing HTML Elements

element.innerHTML =  new html content	--> Change the inner HTML of an element
element.attribute = new value	--> Change the attribute value of an HTML element
element.style.property = new style -->Change the style of an HTML element
element.setAttribute(attribute, value) --> Change the attribute value of an HTML element
*/

/*
Adding and Deleting Elements

document.createElement(element)	Create an HTML element
document.removeChild(element)	Remove an HTML element
document.appendChild(element)	Add an HTML element
document.replaceChild(new, old)	Replace an HTML element
document.write(text)	Write into the HTML output stream
*/

/*
Adding Events Handlers

document.getElementById(id).onclick = function(){code}	Adding event handler code to an onclick event

*/

const myElement = document.getElementById("title");

document.getElementById("description").innerHTML=myElement.innerHTML;

