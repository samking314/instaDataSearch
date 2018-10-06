//right click on the hashtag page on IG and click on 'Inspect'
//then run the following code from the console

var pictureCount = 40
var links = []

var intervalID = window.setInterval(function() 
{
    if(document.getElementsByClassName("v1Nh3 kIKUG  _bz0w").length < pictureCount) {
        console.log("scrolled bottom")
        window.scrollTo(0,document.body.scrollHeight);

        setTimeout(function() {
                        console.log("scrolled top");
                        window.scrollTo(0,0);
                    },250);
    } 
    else {
        clearInterval(intervalID);
        alert("Finished!")
        docData = document.querySelectorAll("a[href^='/p/']")
         for (var data in docData) {
  	       links.push(docData[data].href);
         }
		console.log(links)
    }

}, 500);

//OR run this command if the above doesn't work

docData = document.querySelectorAll("a[href^='/p/']")
for (var data in docData) {
    links.push(docData[data].href);
}
console.log(links)