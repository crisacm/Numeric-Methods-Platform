function tabController(evt, tabName) {
    var i, tabContents, navButtons;
    tabContents = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabContents.length; i++) {
        tabContents[i].style.display = "none";
    }
    navButtons = document.getElementsByClassName("nav-link");
    for (i = 0; i < navButtons.length; i++) {
        navButtons[i].className = navButtons[i].className.replace("-active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += "-active";
}