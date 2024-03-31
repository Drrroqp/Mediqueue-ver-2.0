document.addEventListener("DOMContentLoaded", function() {
    // Открыть модальное окно
    document.getElementById("open-modal-btn-registration3").addEventListener("click", function() {
      document.getElementById("my-modal-autorization").classList.add("open");
    });

    // Закрыть модальное окно
    document.getElementById("close-my-modal-btn-aut").addEventListener("click", function() {
      document.getElementById("my-modal-autorization").classList.remove("open");
    });

    // Закрыть модальное окно при нажатии на Esc
    window.addEventListener('keydown', (e) => {
      if (e.key === "Escape") {
        document.getElementById("my-modal-autorization").classList.remove("open");
      }
    });

    // Закрыть модальное окно при клике вне его
    window.addEventListener('click', function(event) {
        var modal = document.getElementById("my-modal-autorization");
        var modalBox = document.querySelector("#my-modal-autorization .modal__box");
        if (!modalBox.contains(event.target)) {
            modal.classList.remove("open");
        }
    });
});



document.getElementById('submit-reg').addEventListener('click', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    // Получение данных из формы
    var form = document.getElementById('registration-form');
    var formData = new FormData(form);

    document.getElementById('submit-reg').addEventListener('click', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    // Получение данных из формы
    var form = document.getElementById('registration-form');
    var formData = new FormData(form);

    fetch('/register/', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Ошибка ' + response.status);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            // Показываем всплывающее окно с сообщением об ошибке
            Swal.fire({
                icon: 'error',
                title: 'Ошибка регистрации',
                text: data.error,
                footer: data.solution
            });
        } else {
            // Очищаем поля формы
            form.reset();
            // Показываем сообщение об успешной регистрации
            alert('Регистрация прошла успешно!');
            // Проверяем URL ответа
            if (window.location.href.includes('/account/')) {
                // Перенаправляем на страницу /account/
                window.location.href = '/account/';
            } else {
                alert('Не удалось выполнить перенаправление на страницу /account/');
            }
        }
    })
    .catch(error => {
        alert('Произошла ошибка при отправке запроса: ' + error.message);
    });
});




