$(function () {
   $('#login').click(login);
});

function login() {
    var email = $('#email').val();
    var pwd = $('#pwd').val();
    if(email.length < 6){
        alert('邮箱过短');
        return
    }
    if(pwd.length == 0){
        alert('请输入密码');
        return
    }
    var enc_pwd = md5(pwd);
    $.ajax({
        url:'/index/',
        method:'post',
        data:{
            'email':email,
            'pwd':enc_pwd
        },
        success:function (res) {
            if (res.code == 1) {
                window.open(res.data, target = '_self')
            }else{
                alert(res.msg)
            }

        }
    })
}

