function showHide(e_id, force) {
    // This is the global method that all application JS uses to hide or un-hide
    // an HTML element by using its ID value. The "visible" and "force" stuff
    // are commented out, because, with any luck, we won't need them

    // initialize CSS vars
    var hide_class = "hidden";
//    var visible_class = "visible";

    // check the input var
    var e = document.getElementById(e_id);

    if (e === null) {
        console.error(
            "showHide('" + e_id + "') -> No element with ID value '" + e_id + "' found on the page!"
        ); 
        return false;
    }

    if (e.classList.contains(hide_class)) {
        e.classList.remove(hide_class);
//        e.classList.add(visible_class);
    } else {
        e.classList.add(hide_class);
//        e.classList.remove(visible_class)
    };

    // handle the 'force' param
//    if (force === 'show') {
//        e.classList.remove(hide_class);
//        e.classList.add(visible_class);
//        return true;
//    } else if (force === 'hide') {
//        e.classList.remove(visible_class);
//        e.classList.add(hide_class);
//        return true;
//    };

 }
