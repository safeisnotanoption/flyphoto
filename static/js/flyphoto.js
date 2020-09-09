// Init Sidebar
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
});


// Init Collapsible
var elem = document.querySelector('.collapsible');
var instance = M.Collapsible.init(elem, {
    accordion: true
});


// Init Tabs
$(document).ready(function(){
    $('.tabs').tabs();
  });


// Datepicker Language
inter_ru = {
    cancel: 'Отмена',
    clear: 'Очистить',
    done: 'Ок',
    previousMonth: '‹',
    nextMonth: '›',
    months: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
    monthsShort: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
    weekdays: ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'],
    weekdaysShort: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
    weekdaysAbbrev: ['В', 'П', 'В', 'С', 'Ч', 'П', 'С']
};
inter_en = {
    cancel: 'Cancel',
    clear: 'Clear',
    done: 'Ok',
    previousMonth: '‹',
    nextMonth: '›',
    months: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    monthsShort: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    weekdays: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    weekdaysShort: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
    weekdaysAbbrev: ['S', 'M', 'T', 'W', 'T', 'F', 'S']
};

// Datepicker Options
dateOptions = {
    format: 'yyyy-mm-dd',
    firstDay: 1,
    i18n: inter_ru,
}

// Init Datepicker
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, dateOptions);
});

//Timepicker Language
//Timepicker Options
timeOptions = {
    i18n: inter_ru,
    twelveHour: false,
}

// Init Timepicker
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.timepicker');
    var instances = M.Timepicker.init(elems, timeOptions);
});

// Init Datetimepicker
//$(document).ready(function(){
//
//    // Initialize materialize data picker
//    $('.datepicker').datepicker({'format': 'yyyy-mm-dd'});
//    $('select').formSelect();
//  
//  });


// Checkbox for central photos
// $(function () {
//     // Get the form fields and hidden div
//     var checkbox = $("#central_photo_checkbox");
//     var hidden = $("#central_photo_div");
//     // Hide the fields.
//     if (checkbox.is(':checked')) {
//         hidden.show();
//     } else {
//         hidden.hide();
//     }
//     // Setup an event listener for when the state of the 
//     // checkbox changes.
//     checkbox.change(function () {
//         if (checkbox.is(':checked')) {
//             hidden.show();
//         } else {
//             hidden.hide();
//         }
//     });
// });

// Init selects
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
});