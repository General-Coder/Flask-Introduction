$(function () {

    $(".btn-danger").click(function () {
        $del_btn = $(this);
        var c_id = $del_btn.attr("c_id");
        $.ajax({
            url: '/delete_data/',
            method: 'delete',
            data: {'c_id': c_id},
            success: function (res) {
                if (res.code == 1) {
                    $del_btn.parents('tr').remove();
                    alert(res.msg)
                }
            }
        })
    })

    $('.btn-info').click(function () {
        $chan_btn = $(this);
        var c_id = $chan_btn.attr('c_id');
        var longname = $('#longname').val();
        var fics = $('#fics').val();
        var price = $('#price').val();
        var mprice = $('#mprice').val();
        var nums = $('#nums').val();
        $.ajax({
            url:'/change_data/',
            method:'patch',
            data:{
                c_id:c_id,
                longname:longname,
                fics:fics,
                price:price,
                mprice:mprice,
                nums:nums
            },
            success:function (res) {
                if (res.code==1){
                    alert(res.msg);
                    window.open('/item/')
                }
            }
        })

    })

});