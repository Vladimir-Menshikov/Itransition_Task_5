function select_all(source) {
    checkboxes = document.getElementsByName('id');
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = source.checked;
    }
}