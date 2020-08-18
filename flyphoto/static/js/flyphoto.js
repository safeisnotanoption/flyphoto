// Init sidebar
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
});


// Init Collapsible
var elem = document.querySelector('.collapsible.expandable');
var instance = M.Collapsible.init(elem, {
    accordion: false
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
    format: 'dd/mm/yyyy',
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

// Init Colorpicker
$(function () {
    $('#colorpick').colorpicker({
        popover: false,
        inline: true,
        container: '#colorpick'
    });
});