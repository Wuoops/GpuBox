
function getTempData(){
    $.ajax({
        url: '/getTempData/',
        type: 'GET',
        success: function(data){
			 $('#temp').html(data.temp)
        }
    })
}


setInterval(function () {
//在此处执行获取数据的方法
    getTempData();
}, 1000);

