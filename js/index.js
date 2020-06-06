const checkOneOnly = () => {
    let checkboxes = document.getElementsByClassName("checkbox");
    let isChecked = false;

    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked === true) {
            isChecked = true;
            break;
        }
    }

    if (isChecked) {
        for (let i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked === false) {
                console.log(2)
                checkboxes[i].disabled = true;
            }
        }
    } else {
        for (let i = 0; i < checkboxes.length; i++) {
            checkboxes[i].disabled = false;
        }
    }
}