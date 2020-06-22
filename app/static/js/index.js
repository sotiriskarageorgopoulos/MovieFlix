let actorCounter = 0;

const checkOneOnly = () => {
    let checkboxes = document.getElementsByClassName("checkbox");
    let isChecked = false;

    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked === true) {
            let inputEl = document.getElementById("mygrade1");
            inputEl.value = checkboxes[i].value;
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
        inputName.name = "name" + i;
        inputName.id = "name" + i;
        labelName.appendChild(inputName);
        divInputActors.appendChild(labelName);

        let labelSurname = document.createElement("label");
        labelSurname.innerText = "Επώνυμο*";
        labelSurname.for = "surname" + i;
        let inputSurname = document.createElement("input");
        inputSurname.type = "text";
        inputSurname.required = true;
        inputSurname.name = "surname" + i;
        inputSurname.id = "surname" + i;
        labelSurname.appendChild(inputSurname);
        divInputActors.appendChild(labelSurname);
    }

    divInputActors.style.display = "flex";
    divInputActors.style.flexFlow = "column nowrap";
}

const createActorsFields = () => {
    let divInputs = document.getElementById("inputActors1");
    let labelName = document.createElement("label");
    labelName.innerText = "Όνομα*";
    labelName.for = "name" + actorCounter;
    let inputName = document.createElement("input");
    inputName.type = "text";
    inputName.required = true;
    inputName.name = "name" + actorCounter;
    labelName.appendChild(inputName);
    divInputs.appendChild(labelName);

    let labelSurname = document.createElement("label");
    labelSurname.innerText = "Επώνυμο*";
    labelSurname.for = "surname" + actorCounter;
    let inputSurname = document.createElement("input");
    inputSurname.type = "text";
    inputSurname.required = true;
    inputSurname.name = "surname" + actorCounter;
    labelSurname.appendChild(inputSurname);
    divInputs.appendChild(labelSurname);

    divInputs.style.display = "flex";
    divInputs.style.flexFlow = "column nowrap";

    let divInputs1 = document.getElementById("actorsCount");
    divInputs1.innerHTML = "";
    actorCounter++;
    let numOfActors = document.createElement("input");
    numOfActors.type = "hidden";
    numOfActors.name = "actorsCounter";
    numOfActors.value = actorCounter;
    divInputs1.appendChild(numOfActors)
}

const displayActorForm = () => {
    let title = document.getElementById("upActorTitle");
    window.location.href = "update_actors?title=" + title.value;
}

const logOut = () => {
    window.location.href = "login";
}

const register = () => {
    window.location.href = "register";
}

const removeGradeForm = (form) => {
    form.style.display = "none";
}