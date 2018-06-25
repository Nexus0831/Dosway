$('form').submit(function (event) {
    let keyNames = '';
    const keys = document.getElementsByName('key-names[]');

    for (let i = 0; i < keys.length; i++) {
        keyNames = keyNames + keys[i].value + ',';
    }

    keyNames = keyNames.slice(0, -1);

    keyNames = keyNames + '\n';
    localStorage.setItem('text', keyNames);
});