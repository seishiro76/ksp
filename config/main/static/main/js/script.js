document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    const phoneInput = document.getElementById("id_phone");
    const emailInput = document.getElementById("id_email");
    const confirmEmailInput = document.getElementById("id_confirm_email");

    const sticker = document.createElement("div");
    sticker.id = "sticker";
    sticker.style.display = "none";
    sticker.style.position = "fixed";
    sticker.style.top = "20px";
    sticker.style.right = "20px";
    sticker.style.width = "320px";
    sticker.style.padding = "15px";
    sticker.style.backgroundColor = "#f8d7da";
    sticker.style.border = "1px solid #f5c2c7";
    sticker.style.color = "#842029";
    sticker.style.zIndex = "1000";
    sticker.style.fontSize = "16px";
    document.body.appendChild(sticker);

    function showSticker(message) {
        sticker.textContent = message;
        sticker.style.display = "block";

        setTimeout(function () {
            sticker.style.display = "none";
        }, 3000);
    }

    function clearInputBorder(input) {
        if (input) {
            input.style.border = "";
        }
    }

    if (phoneInput) {
        phoneInput.addEventListener("input", function () {
            clearInputBorder(phoneInput);
        });
    }

    if (emailInput) {
        emailInput.addEventListener("input", function () {
            clearInputBorder(emailInput);
        });
    }

    if (confirmEmailInput) {
        confirmEmailInput.addEventListener("input", function () {
            clearInputBorder(confirmEmailInput);
        });
    }

    if (form) {
        form.addEventListener("submit", function (event) {
            const phoneRegex = /^[0-9+\-\s()]{7,20}$/;
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (phoneInput && !phoneRegex.test(phoneInput.value)) {
                event.preventDefault();
                phoneInput.style.border = "2px solid red";
                showSticker("Номер телефона введён некорректно.");
                return;
            }

            if (emailInput && !emailRegex.test(emailInput.value)) {
                event.preventDefault();
                emailInput.style.border = "2px solid red";
                showSticker("Электронная почта введена некорректно.");
                return;
            }

            if (
                emailInput &&
                confirmEmailInput &&
                emailInput.value !== confirmEmailInput.value
            ) {
                event.preventDefault();
                confirmEmailInput.style.border = "2px solid red";
                showSticker("Электронные почты не совпадают.");
                return;
            }
        });
    }

    const upButton = document.createElement("button");
    upButton.textContent = "Наверх";
    upButton.id = "upButton";
    upButton.style.display = "none";
    upButton.style.position = "fixed";
    upButton.style.bottom = "20px";
    upButton.style.right = "20px";
    upButton.style.padding = "10px 15px";
    upButton.style.zIndex = "1000";
    document.body.appendChild(upButton);

    window.addEventListener("scroll", function () {
        if (window.scrollY > 300) {
            upButton.style.display = "block";
        } else {
            upButton.style.display = "none";
        }
    });

    upButton.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });

    const removeLinks = document.querySelectorAll(".remove-link");

    const modalBackground = document.createElement("div");
    modalBackground.id = "modalBackground";
    modalBackground.style.display = "none";
    modalBackground.style.position = "fixed";
    modalBackground.style.left = "0";
    modalBackground.style.top = "0";
    modalBackground.style.width = "100%";
    modalBackground.style.height = "100%";
    modalBackground.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
    modalBackground.style.zIndex = "2000";

    const modalWindow = document.createElement("div");
    modalWindow.style.backgroundColor = "white";
    modalWindow.style.width = "380px";
    modalWindow.style.margin = "150px auto";
    modalWindow.style.padding = "20px";
    modalWindow.style.border = "1px solid black";

    const modalTitleRow = document.createElement("div");
    modalTitleRow.style.display = "flex";
    modalTitleRow.style.justifyContent = "space-between";
    modalTitleRow.style.alignItems = "center";

    const modalTitle = document.createElement("h2");
    modalTitle.textContent = "Подтверждение удаления";

    const closeButton = document.createElement("button");
    closeButton.textContent = "Закрыть";

    modalTitleRow.appendChild(modalTitle);
    modalTitleRow.appendChild(closeButton);

    const modalText = document.createElement("p");
    modalText.textContent = "Вы действительно хотите удалить эту заявку?";

    const confirmButton = document.createElement("button");
    confirmButton.textContent = "Удалить";

    const cancelButton = document.createElement("button");
    cancelButton.textContent = "Отмена";
    cancelButton.style.marginLeft = "10px";

    modalWindow.appendChild(modalTitleRow);
    modalWindow.appendChild(modalText);
    modalWindow.appendChild(confirmButton);
    modalWindow.appendChild(cancelButton);

    modalBackground.appendChild(modalWindow);
    document.body.appendChild(modalBackground);

    let removeUrl = "";

    removeLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            removeUrl = link.href;
            modalBackground.style.display = "block";
        });
    });

    function closeModal() {
        modalBackground.style.display = "none";
        removeUrl = "";
    }

    closeButton.addEventListener("click", function () {
        closeModal();
    });

    cancelButton.addEventListener("click", function () {
        closeModal();
    });

    confirmButton.addEventListener("click", function () {
        if (removeUrl) {
            window.location.href = removeUrl;
        }
    });
});