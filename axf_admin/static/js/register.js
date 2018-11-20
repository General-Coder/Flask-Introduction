$(function () {
    $('#regis').click(register)
});

function register() {
    email = $('#email').val();
    pwd = $('#pwd').val();
    confirm_pwd = $('#confirm_pwd').val();
    if(email.length < 5){
        alert('邮箱过短');
        return;
    }
    if(pwd == confirm_pwd && pwd.length > 0) {
        env_pwd = md5(pwd);
        env_confirm_pwd = md5(confirm_pwd);
        $('#pwd').val(env_pwd);
        $('#confirm_pwd').val(env_confirm_pwd);
    }else {
        alert('密码为空或不一致');
        return false
    }

    $.ajax({
        url: '/register/',
        data: {
            'email': email,
            'pwd': env_pwd,
            'confirm_pwd': env_confirm_pwd
        },
        method: 'post',
        success: function (res) {

            if(res.code==1){
                alert('请去邮箱激活,否则您的账号将无法登陆');
                window.open(res.data,target='_self')
            }else{
                alert(res.msg)
            }
        }
    })
}