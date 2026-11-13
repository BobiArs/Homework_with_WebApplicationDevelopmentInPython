document.addEventListener("DOMContentLoaded", () => {
    const registerForm = document.getElementById("registerForm");
    if (!registerForm) return;

    registerForm.addEventListener("submit", async function(e) {
        e.preventDefault();
        const form = e.target;
        const formData = new FormData(form);
        const csrfToken = form.querySelector('[name="csrfmiddlewaretoken"]').value;
        const messageBox = document.getElementById("registerMessage");

        try {
            const response = await fetch("/register/", {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken
                },
                body: formData
            });

            const result = await response.json();
            console.log(result);

            if (response.ok) {
                console.log("Користувача успішно зареєстровано:", result);
                if (messageBox) {
                    messageBox.innerHTML = `<div class="alert alert-success">${result.message}</div>`;
                }
                form.reset();
            } else {
                console.error(result);
                if (messageBox) {
                    messageBox.innerHTML = `<div class="alert alert-danger">${result.error || "Помилка реєстрації"}</div>`;
                }
            }
        } catch (error) {
            console.error("Помилка:", error);
            if (messageBox) {
                messageBox.innerHTML = `<div class="alert alert-danger">Помилка з'єднання із сервером</div>`;
            }
        }
    });
});