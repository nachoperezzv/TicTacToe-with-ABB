let inputTxt = document.querySelector('.clearfix');
const recognition = new WebkitSprecasdasd
recognition.lang = 'en-US';
recognition.continues = true
recognition.onresult = function(event) {
    var color = event.results[0][0].transcript;
    console.log('Confidence: ' + event.results[0][0].confidence);
    inputTxt.innerHTML(JSONSTRINGY(color))
}


function comienzo (){
    recognition.start();
}
function fin (){
    recognition.stop();
}