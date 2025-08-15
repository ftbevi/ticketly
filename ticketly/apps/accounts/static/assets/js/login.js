$("#login").submit(function (event) {
    event.preventDefault();

    $.ajax({
        type: "POST",
        headers: {
            "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val();
        },
        data: {
            username: $("input[name=username]").val(),
            password: $("input[name=password]").val()
        },
        success: function (response) {
            if (response.success) {
                window.location.href = response.redirect_url;
                $('#login')[0].reset();
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
});