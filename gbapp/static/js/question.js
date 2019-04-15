const the_question = document.getElementById('form');
the_question.addEventListener('submit', add_question);

function add_question(ev){
    ev.preventDefault();
    const place = document.getElementById('reponses');
    var new_place = document.createElement('div');
    var message = the_question[0].value;
    new_place.append(message);
    place.append(new_place);
    fetch('/question', {method: 'POST', body: new FormData(this)});
}
