const the_question = document.getElementById('form');
the_question.addEventListener('submit', add_question);

function add_question(ev){
    ev.preventDefault();
    fetch('/question', {method: 'POST', body: new FormData(this)})
    .then(function(response) { return response.json()})
    .then(display_ans)
}

function display_ans(json){
    const place = document.getElementById('reponses');
    var new_place = document.createElement('div');
    var question = "Alors mon petit, ta question est donc: " + json.question;
    var result = json.result;
    var link_wiki = json.link_wiki
    var to_show = ` 
            <p> Alors mon petit, ta question est donc: ${question} </p> 
            <p> Voici ma réponse: ${result} </p>
            `;
    if (link_wiki != undefined){
        to_show = to_show +
            `
            <p> Mais je fatigue, va lire par toi même: <a href="${link_wiki}">vas-y mon petit</a></p>
            `;
    }
    new_place.innerHTML = to_show
    //new_place.append(question);
    place.append(new_place);
    //new_place = document.createElement('div');
    //new_place.append(result);
    //place.append(new_place);
}
