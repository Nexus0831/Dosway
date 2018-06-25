$('#third-form').submit(function (event) {
    let line = '';
    const elements = document.getElementsByName('elements');

    for (let i = 0; i < elements.length; i++) {
        line = line + elements[i].value + ',';
        elements[i].value = '';
    }

    line = line.slice(0, -1) + '\n';

    line = localStorage.getItem('text') + line;

    localStorage.setItem('text', line);
    console.log(localStorage.getItem('text'));
    return false
});