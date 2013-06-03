$( document ).ready(function() {
    $('#formRegister').submit(function(e){
        e.preventDefault();
        var params = $(this).serializeArray();
        $.post('/createaccount', params, function(data) {
            if(data.success){
               window.location = '/'
            }
        });
    });


    $('#loginButton').click(function(e){
        e.preventDefault();
        var params = $('#loginInfo').serializeArray();
        $.post('/login', params, function(data){
            if(data.status = 'success'){
                window.location = '/'
            }
        });
    });


});