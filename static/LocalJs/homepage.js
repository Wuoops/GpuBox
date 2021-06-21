function getHomepageTempData(){
    $.ajax({
        url: '/getHomepageTempData/',
        type: 'GET',
        success: function(data){
			for (i = 0;i<data.temp.length;i++){
				var ID= data.temp[i][0] ;
				// console.log(ID)

				$('#'+ID+'_temp').text(data.temp[i][1]+" ℃");
			}
        }
    })
}


function getStatus(){
    $.ajax({
        url: '/getHomePageStatus/',
        type: 'GET',
        success: function(data){
            // console.log(data)
            for (i = 0;i<data.data.length;i++){
                var ID= data.data[i][1] ;
                var px = data.data[i][4];
                $('#'+ID+'_status').text(data.data[i][2]);
				$('#'+ID+'_status').css({'font-size': data.data[i][4]+'px' });
				console.log(data.data[i][5])
				$('#'+ID+'_status').attr("class"," btn");
				$('#'+ID+'_status').addClass(data.data[i][5]);
            }

			 // $('#GPU1').html(data.temp)
        }
    })
}

// getHomepageTempData()
// getStatus()
setInterval(function () {
//在此处执行获取数据的方法
    getStatus();
	getHomepageTempData()
}, 1000);

