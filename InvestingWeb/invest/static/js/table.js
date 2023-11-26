// Создание таблицы


var tbody = document.getElementById('mytbody');
var thead = document.getElementById('myth');
//var tbody = document.createElement('tbody');

//table.appendChild(tbody);

var list_thead = ['Название','Цена','Изменение цены']
var row_thead = document.createElement('tr');
for(var i=0;i< list_thead.length;i++){
    var column_thead = document.createElement('th')
    column_thead.innerHTML = list_thead[i]
    row_thead.appendChild(column_thead)
}
thead.appendChild(row_thead);

// Создание строки(элементы, "th"/"td")
function create_row(list, elem){
    var row_1 = document.createElement('tr');
    for(var i = 0; i < list.length; i++){
        var cell = document.createElement(elem);
        cell.innerHTML = list[i];
        row_1.appendChild(cell);
    }
    tbody.appendChild(row_1);
}

// Добавление таблицы в HTML
document.getElementById('mytable').appendChild(thead)
document.getElementById('mytable').appendChild(tbody);


var tvalues = [["Ivanov Ivan", "Samsung", "+7123123123"],
               ["Pupkin Vasya", "Apple", "+719291291232"]];

// Создание и добавление строк
for (var i = 0; i < tvalues.length; i++){
    create_row(tvalues[i], "td");
}
