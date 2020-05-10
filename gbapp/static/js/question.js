const the_question = document.getElementById('form');
the_question.addEventListener('submit', add_question);

// counter to increase the div for map display
var counter = 1


function scrollDown(){
    var objDiv = document.getElementById("reponses");
    objDiv.scrollTop = objDiv.scrollHeight;
}

/*
 * Function to display question and the waiting sing
 */
function print_question(question){
    var parent_place = document.getElementById('reponses');
    var question_place = document.createElement('div');
    question_place.setAttribute('id', 'qplace');
    var to_show = ` 
            <p> Alors mon petit, ta question est donc: ${question} </p> 
            <p> Je dois réfléchir </p>
            <p>
                <img src="https://i.gifer.com/ZKZx.gif" alt="" />
            </p>
            `;
    question_place.innerHTML = to_show
    parent_place.append(question_place);
    scrollDown();
}

/*
 * Function to do the treatment of the question
 */ 
function add_question(ev){
    ev.preventDefault();
    var def_quest = document.getElementById('input').value;
    print_question(def_quest);
    fetch('/question', {method: 'POST', body: new FormData(this)})
    .then(function(response) { return response.json()})
    .then(display_ans)
}

/*
 * Function to do the display of all the information
 */ 
function display_ans(json){
    // Remove the waiting
    var elem_to_remove = document.getElementById('qplace');
    elem_to_remove.parentNode.removeChild(elem_to_remove);
    // place is where we insert the answers
    const place = document.getElementById('reponses');
    var new_place = document.createElement('div');
    // get the question for display
    var question = json.question;
    var err_parse = json.err_parse;
    var err_map = json.err_map;
    var err_wiki = json.err_wiki;
    // get the link of the wiki
    var link_wiki = json.link_wiki;
    var blabla_google = json.blabla_google;
    var blabla_wiki  = json.blabla_wiki;
    var blabla_error = json.error_bla;
    // displaying the answers
    var to_show = ` 
            <p> Alors mon petit, ta question est donc: ${question} </p> 
            `;

    if (err_parse != ''){
        to_show = to_show +
            `
            <p> ${blabla_error} ${err_parse} </p>
            `;
    } 
    else if (err_map != '' || err_wiki != '') {
        to_show = to_show +
            `
            <p> ${blabla_error} ${err_map} -- ${err_wiki} </p>
            `;
    } 
    else {
        // get the address 
        var addr = json.addr;
        to_show = to_show +
            `
            <p> ${blabla_google} - ${addr} </p>
            <div id="map-container-${counter}" class="z-depth-1" style="height: 300px"></div>
            `;
    }

    if (link_wiki != undefined){
        var wiki_ans = json.wiki_ans
        to_show = to_show +
            `
            <p> ${blabla_wiki} ${wiki_ans}</p>
            <p> Mais je fatigue, va lire par toi même: <a href="${link_wiki}" target="_blank">vas-y mon petit</a></p>
            `;
    }

    to_show = to_show +
        `
        <p> ------------------------------------------------------------------------------------------------------- </p>
        `
    // converting the answer to htm code
    new_place.innerHTML = to_show
    //new_place.append(question);
    place.append(new_place);
    // Display the map
    if (err_map == ''){
        // get the coordinate of the location
        var coord = json.coord;
        var latt = coord['lat'];
        console.log(latt)
        var long = coord['lng'];
        var loca = {lat: latt, lng: long};
        var map = new google.maps.Map(document.getElementById('map-container-'+counter), {center: loca, zoom: 15});
        var var_marker = new google.maps.Marker({position: loca, map: map});
    }

    counter = counter + 1
    scrollDown();

}
