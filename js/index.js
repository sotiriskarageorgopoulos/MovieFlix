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

const createInputs = () => {
    let divInputActors = document.getElementById("inputActors");
    let numOfActors = parseInt(document.getElementById("numOfActors").value);

    divInputActors.innerHTML = "";

    for (let i = 0; i < numOfActors; i++) {
        let labelName = document.createElement("label");
        labelName.innerText = "Όνομα*";
        labelName.for = "name" + i;
        let inputName = document.createElement("input");
        inputName.type = "text";
        inputName.required = true;
        inputName.id = "name" + i
        labelName.appendChild(inputName);
        divInputActors.appendChild(labelName);

        let labelSurname = document.createElement("label");
        labelSurname.innerText = "Επώνυμο*";
        labelSurname.for = "surname" + i;
        let inputSurname = document.createElement("input");
        inputSurname.type = "text";
        inputSurname.required = true;
        inputSurname.id = "surname" + i
        labelSurname.appendChild(inputSurname);
        divInputActors.appendChild(labelSurname);
    }

    divInputActors.style.display = "flex";
    divInputActors.style.flexFlow = "column nowrap";
}

const logOut = () => {
    window.location.href = "./login.html";
}

const register = () => {
    window.location.href = "./register.html";
}