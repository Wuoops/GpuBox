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
function getGpuTemp(){
        $.ajax({
        url: '/getGpuTemp/',
        type: 'GET',
        success: function(data){
			for (i = 0;i<data.temp.length;i++){
				var ID= data.temp[i][0] ;
				console.log(data.temp[i][1])

				$('#'+ID+'_temp').text(data.temp[i][1]+" ℃");
			}
        }
    })
}
function getGpuPower(){
        $.ajax({
        url: '/getGpuPower/',
        type: 'GET',
        success: function(data){
			for (i = 0;i<data.power.length;i++){
				var ID= data.power[i][0] ;
				console.log(data.power[i][1])

				$('#'+ID).text(data.power[i][1]+" W");
			}
        }
    })
}
function getGpuStatus(){
    $.ajax({
        url: '/getGpuStatus/',
        type: 'GET',
        success: function(data){
            // console.log(data)
            for (i = 0;i<data.data.length;i++){
                var ID= data.data[i][1] ;
                var px = data.data[i][4];
                $('#'+ID+'_status').text(data.data[i][1]);
				// $('#'+ID+'_status').css({'font-size': data.data[i][4]+'px' });
				console.log(data.data[i][5])
				$('#'+ID+'_status').attr("class"," btn");
				$('#'+ID+'_status').addClass(data.data[i][3]);
            }

			 // $('#GPU1').html(data.temp)
        }
    })
}
function getSwitchTemp(){
        $.ajax({
        url: '/getSwitchTemp/',
        type: 'GET',
        success: function(data){
			for (i = 0;i<data.temp.length;i++){
				var ID= data.temp[i][0] ;
				console.log(data.temp[i][1])

				$('#'+ID+'_temp').text(data.temp[i][1]+" ℃");
			}
        }
    })
}

function getSwitchStatus(){
    $.ajax({
        url: '/getSwitchStatus/',
        type: 'GET',
        success: function(data){
            // console.log(data)
            for (i = 0;i<data.data.length;i++){
                var ID= data.data[i][1] ;
                var px = data.data[i][4];
                $('#'+ID+'_status').text(data.data[i][1]);
				// $('#'+ID+'_status').css({'font-size': data.data[i][4]+'px' });
				console.log(data.data[i][5])
				$('#'+ID+'_status').attr("class"," btn");
				$('#'+ID+'_status').addClass(data.data[i][3]);
            }

			 // $('#GPU1').html(data.temp)
        }
    })
}

setInterval(function () {
// 在此处执行获取数据的方法
    getGpuPower();
    getGpuStatus();
    getGpuTemp();
    getSwitchTemp();
    getSwitchStatus()
}, 1000);

