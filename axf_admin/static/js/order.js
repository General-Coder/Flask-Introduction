$(function () {
    $('select').change(function () {
        var $cur_btn = $(this);
        var o_id = $cur_btn.attr('o_id');
        var op_value = $cur_btn.find('option:selected').val();
        var op_text = $cur_btn.find('option:selected').text();
        $.ajax({
            url:'/status/',
            method:'patch',
            data:{
              'o_id':o_id,
              'status':parseInt(op_value)
            },
            success:function (res) {
                if (res.code==1){
                    $cur_btn.parents('tr').find('.op_status').html(op_text)
                }
            }
        })
    })
});