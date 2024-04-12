function changeButtonColor(btnId) {
    var btn = document.getElementById(btnId);
    var otherBtnId = (btnId === 'btn-personal-data') ? 'btn-personal-posts' : 'btn-personal-data';
    var otherBtn = document.getElementById(otherBtnId);
    var hrId = (btnId === 'btn-personal-data') ? 'hr-personal-data' : 'hr-personal-posts';
    var hr = document.getElementById(hrId);
    var otherHrId = (btnId === 'btn-personal-data') ? 'hr-personal-posts' : 'hr-personal-data';
    var otherHr = document.getElementById(otherHrId);
    
    btn.classList.add("text-red-400");
    otherBtn.classList.remove("text-red-400");
    hr.classList.add("border-red-400");
    otherHr.classList.remove("border-red-400");

    sessionStorage.setItem('activeButton', btnId);
}

window.onload = function() {
    var activeButtonId = sessionStorage.getItem('activeButton');
    if (activeButtonId) {
        var activeButton = document.getElementById(activeButtonId);
        var otherButtonId = (activeButtonId === 'btn-personal-data') ? 'btn-personal-posts' : 'btn-personal-data';
        var otherButton = document.getElementById(otherButtonId);
        var activeHrId = (activeButtonId === 'btn-personal-data') ? 'hr-personal-data' : 'hr-personal-posts';
        var activeHr = document.getElementById(activeHrId);
        var otherHrId = (activeButtonId === 'btn-personal-data') ? 'hr-personal-posts' : 'hr-personal-data';
        var otherHr = document.getElementById(otherHrId);

        activeButton.classList.add("text-red-400");
        otherButton.classList.remove("text-red-400");
        activeHr.classList.add("border-red-400");
        otherHr.classList.remove("border-red-400");
    }
};