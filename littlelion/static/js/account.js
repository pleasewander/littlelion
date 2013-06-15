$( document ).ready(function() {
    $('#formRegister').submit(function(e){
        e.preventDefault();
        var params = $(this).serializeArray();
        $.post('/createaccount', params, function(data) {
            if(data.success){
               $('#registerSuccess').removeClass('hide');
               setTimeout(function(){
                          window.location = '/';
               }, 3000);
            }
            else{
               $('#registerError').removeClass('hide');
            }
        });
    });


    $('#loginButton').click(function(e){
        e.preventDefault();
        var params = $('#loginInfo').serializeArray();
        $.post('/login', params, function(data){
            if(data.status = 'success'){
                window.location = '/';
            }
        });
    });

    $('#createAccountEmail').blur(function(e){
        e.preventDefault();
        var email =  $('#createAccountEmail').val();
        $.post('/checkemail', {'email' : email} , function(data){
            if(!data.success){
            $('#registerError').removeClass('hide');
            }
        });

    $('.close').click(function(e){
        e.preventDefault();
        $('.alert').addClass('hide');
        });
    });


});