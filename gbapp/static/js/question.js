const the_question = document.getElementById('form');
the_question.addEventListener('submit', add_question);

// counter to increase the div for map display
var counter = 1

// treatment of the question
function add_question(ev){
    ev.preventDefault();
    fetch('/question', {method: 'POST', body: new FormData(this)})
    .then(function(response) { return response.json()})
    .then(display_ans)
}

// Display of all the information
function display_ans(json){
    // place is where we insert the answers
    const place = document.getElementById('reponses');
    var new_place = document.createElement('div');
    // get the question for display
    var question = json.question;
    var result = json.result;
    // get the link of the wiki
    var link_wiki = json.link_wiki;
    // get the coordinate of the location
    var coord = json.coord;
    var latt = coord['lat'];
    var long = coord['lng'];
    var loca = {lat: latt, lng: long};
    // get the address 
    var addr = json.candidates[0]['formatted_address'];
    // displaying the answers
    var to_show = ` 
            <p> Alors mon petit, ta question est donc: ${question} </p> 
            <p> Voici ma réponse: ${result} et ${addr} </p>
            <div id="map-container-${counter}" class="z-depth-1" style="height: 300px"></div>
            `;
    if (link_wiki != undefined){
        to_show = to_show +
            `
            <p> Mais je fatigue, va lire par toi même: <a href="${link_wiki}">vas-y mon petit</a></p>
            `;
    }
    // converting the answer to htm code
    new_place.innerHTML = to_show
    //new_place.append(question);
    place.append(new_place);
    // Display the map
    var map = new google.maps.Map(document.getElementById('map-container-'+counter), {center: loca, zoom: 15});
    var var_marker = new google.maps.Marker({position: loca, map: map});
    counter = counter + 1
    //new_place = document.createElement('div');
    //new_place.append(result);
    //place.append(new_place);
}
