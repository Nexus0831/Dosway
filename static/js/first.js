$('form').submit(function (event) {
    const title = document.getElementsByName('title')[0].value;
    localStorage.setItem('title', title);
});

