document.getElementById('first').onclick = function () {
    const cardForm = document.getElementById('card-form');
    const title = document.getElementsByName('title')[0].value;
    const column = Number(document.getElementsByName('column')[0].value);

    localStorage.setItem('title', title);
    localStorage.setItem('column', column);

    while (cardForm.firstChild) {
        cardForm.removeChild(cardForm.firstChild);
        console.log('要素を削除しました');
    }

    // const script = document.createElement('script');
    // script.src = 'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js';

    for (var i = 1; i <= column; i++ ) {
        const filedContainer = document.createElement('div');
        filedContainer.classList.add('filed-container');

        // フィールドのラベル作成
        const filedLabel = document.createElement('span');
        filedLabel.classList.add('kyoto', 'filed-label');
        filedLabel.textContent = '項目' + i;

        // inputを囲むdivを作成
        const inputFiled = document.createElement('div');
        inputFiled.classList.add('input-field');
        inputFiled.style.width = '50%';

        // input生成
        const input = document.createElement('input');
        input.setAttribute('type', 'text');
        input.setAttribute('name', 'columns');
        input.setAttribute('id', 'autocomplete-input');
        input.classList.add('autocomplete', 'validate');
        input.setAttribute('pattern', '^([a-zA-Z0-9]{8,})$');
        input.required = true;

        // フローティングラベル生成
        const floatLabel = document.createElement('label');
        floatLabel.textContent = i + 'つ目の項目やで意味のわかる項目名にしてなぁ';
        floatLabel.setAttribute('for', 'autocomplete-input');
        floatLabel.classList.add('kyoto');


        inputFiled.appendChild(input);
        inputFiled.appendChild(floatLabel);

        filedContainer.appendChild(filedLabel);
        filedContainer.appendChild(inputFiled);

        cardForm.appendChild(filedContainer);
    }

    // ボタンを囲むdiv
    const cardButton = document.createElement('div');
    cardButton.classList.add('card-button');

    const button = document.createElement('button');
    button.classList.add('waves-effect', 'waves-light', 'btn', 'kyoto', 'pink', 'darken-1');
    button.setAttribute('id', 'second');
    button.setAttribute('type', 'submit');
    button.textContent = '各項目の名称を決定';

    cardButton.appendChild(button);

    cardForm.appendChild(cardButton);
};

