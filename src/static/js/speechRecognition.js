// import {language} from "./language"
// import {dialect} from "./language"

const coordinates = [ 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'];

if ("webkitSpeechRecognition" in window) {
  let speechRecognition = new webkitSpeechRecognition();
  let final_transcript = "";
  let lastCoordinate = "";    // Ultima coordenada encontrada en final_transcript

  speechRecognition.continuous = true;
  speechRecognition.interimResults = true;
  speechRecognition.lang = 'es-ES'

  // speechRecognition.lang = document.querySelector("#select_dialect").value;

  speechRecognition.onstart = () => {
    //document.querySelector("#status").style.display = 'block';
  };
  speechRecognition.onerror = () => {
    //document.querySelector("#status").style.display = 'none';
    console.log("Speech Recognition Error");
  };
  speechRecognition.onend = () => {
    //document.querySelector("#status").style.display = 'none';
    console.log("Speech Recognition Ended");    

  }

  speechRecognition.onresult = (event) => {
    let interim_transcript = "";

    for (let i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        final_transcript += event.results[i][0].transcript;
      } else {
        interim_transcript += event.results[i][0].transcript;
      }
    }
    document.querySelector("#final").innerHTML = final_transcript;
    document.querySelector("#interim").innerHTML = interim_transcript;
  };

  document.querySelector("#btn__mic__start").onclick = () => {
    document.querySelector("#btn__mic__start").style.display = 'none'
    document.querySelector("#btn__mic__stop").style.display = 'block'

    document.querySelector("#final").innerHTML = "";
    final_transcript = "";
    lastCoordinate = "";

    document.querySelector("#interim").innerHTML = "";
    interim_transcript = "";

    speechRecognition.start();
  };

  document.querySelector("#btn__mic__stop").onclick = () => {
    document.querySelector("#btn__mic__start").style.display = 'block'
    document.querySelector("#btn__mic__stop").style.display = 'none'

    speechRecognition.stop();

    let data = {"text": final_transcript};

    fetch('http://localhost:5000/play/getIntention', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(result => {
      getSpeechMove(result.intention)
      console.log(result)
    })
    .catch(error => {
      console.error(error);
    });

    getSpeechMove(result);
  };
} else {
  console.log("Speech Recognition Not Available");
}
