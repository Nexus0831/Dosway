$('#third-form').submit(function (event) {
    let line = '';
    const elements = document.getElementsByName('elements');
    const tableBody = document.getElementById('table-body');
    const tr = document.createElement('tr');

    for (let i = 0; i < elements.length; i++) {
        const td = document.createElement('td');
        td.textContent = elements[i].value;
        tr.appendChild(td);
        line = line + elements[i].value + ',';
        elements[i].value = '';
    }

    line = line.slice(0, -1) + '\n';

    line = localStorage.getItem('text') + line;

    localStorage.setItem('text', line);

    tableBody.appendChild(tr);

    return false
});

$('#last-form').submit(function (event) {
   const title = document.getElementsByName('title')[0];
   const text = document.getElementsByName('text')[0];

   title.value = localStorage.getItem('title');
   text.value = localStorage.getItem('text');
});