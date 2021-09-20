
Object.size = function (obj) {
    var size = 0, key;
    for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
    }
    return size;
};


function handleFileSelect() {
    // evt.preventDefault();
    // var file = evt.target.files[0];
    var file = document.getElementById("interval_data_form_interval_data_file").files[0];
    console.log(file);
    Papa.parse(file, {
        header: true,
        dynamicTyping: true,
        complete: function (results) {
            // createChart(results.data);
            data = results.data;
            createChart(data);            
            // var Datetime = [];
            // var kW = [];
            // var kVA = [];
            // for (i = 0; i < data.length - 1; i = i + 1) {
            //     Datetime[i] = data[i].Datetime;
            //     kW[i] = data[i].kW;
            //     kVA[i] = data[i].kVA;
            // }
            
        }
    });
}

// --------------------------

$('#interval_data_form_interval_data_file').on('change', function () {
    handleFileSelect();
});


var $IntervalDataUploadForm = $('#media_upload');
$IntervalDataUploadForm.submit(function (event) {
    event.preventDefault();
    intervalDataUploadFunction();
});

showIntervalDataList();


//------------------------------------
function intervalDataUploadFunction() {
    var url = '/scenarios/interval_data_upload/'
    var formData = new FormData(document.getElementById("form_interval_data_upload"));
    var scenarioId = document.getElementById("hidden_scenario_id").value;
    // var fileSelect = document.getElementById("interval_data_form_interval_data_file")
    // var files = fileSelect.files;
    // var file = files[0];
    // formData.append('csv', file, file.name);
    var obj = new Object();
    obj.scenarioId = scenarioId
    var JSONobj = JSON.stringify(obj);
    formData.append('JSONobj', JSONobj);
    request = new ajaxRequest()
    request.open("POST", url, true)
    // request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    request.setRequestHeader('X-CSRFToken', csrfcookie());
    request.onreadystatechange = function () {
        if (this.readyState == 4)
            if (this.status == 200)
                if (this.responseText != null) {
                    var data = JSON.parse(this.responseText);
                    console.log(data.message)
                    showIntervalDataList();
                    // Fill Interval Data choices
                    selected_interval_data_id = document.getElementById("simulation_parameter_interval_data").value
                    $("#simulation_parameter_interval_data").empty();
                    var sel = document.getElementById('simulation_parameter_interval_data');
                    // create new option element
                    console.log(data)
                    for (i=0;i<data.idList.length;i++){
                        var opt = document.createElement('option');
                        opt.appendChild( document.createTextNode(data.fileNameList[i]) );
                        opt.value = data.idList[i];
                        sel.appendChild(opt); 
                        if (opt.value == selected_interval_data_id){
                            opt.setAttribute("selected", "selected");
                        }
                    }

                }
    }
    request.send(formData);
}


function showIntervalDataList() {
    var url = '/scenarios/file_list/'
    // var $UploadForm = $('#form_upload');     
    var scenarioId = document.getElementById("hidden_scenario_id").value;
    var obj = new Object();
    obj.scenarioId = scenarioId
    var JSONobj = JSON.stringify(obj);
    params = "JSONobj=" + JSONobj;
    request = new ajaxRequest()
    request.open("POST", url, true)
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    request.setRequestHeader('X-CSRFToken', csrfcookie());
    request.onreadystatechange = function () {
        if (this.readyState == 4)
            if (this.status == 200)
                if (this.responseText != null) {
                    var data = JSON.parse(this.responseText);
                    console.log(data)
                    table_html = [];
                    if (data.urlList.length > 0) {
                        for (i = 0; i < data.urlList.length; i++) {
                            table_html = table_html +
                                (
                                    "<tr>" +
                                    "<td><a class='btn text-secondary px-0' onclick='graphIntervalData(" + data.idList[i] + ")';>" + data.fileNameList[i] + "</a></td>" +
                                    "<td>" +
                                    "<a class='btn text-secondary px-0' href='" + data.urlList[i] + "'><i class='fa fa-download fa-sm'></i></a>" +
                                    "<button class='btn d-inline' onclick='deleteIntervalData(" + data.idList[i] + ")';>" +
                                    "<i class='far fa-trash-alt fa-sm text-danger float-right'></i>" +
                                    "</button>" +
                                    "</td>" +
                                    "</tr>"
                                )
                        }
                    }
                    document.getElementById("tbl_file_list_body").innerHTML = table_html
                }
    }
    request.send(params);
}

function deleteIntervalData(intervalDataId) {
    var url = '/scenarios/delete_interval_data/'
    var scenarioId = document.getElementById("hidden_scenario_id").value;
    var obj = new Object();
    obj.scenarioId = scenarioId    
    obj.intervalDataId = intervalDataId;

    var JSONobj = JSON.stringify(obj);
    params = "JSONobj=" + JSONobj;
    request = new ajaxRequest()
    request.open("POST", url, true)
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    request.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    request.setRequestHeader('X-CSRFToken', csrfcookie());
    request.onreadystatechange = function () {
        if (this.readyState == 4)
            if (this.status == 200)
                if (this.responseText != null) {
                    var data = JSON.parse(this.responseText);
                    console.log(data)
                    if (data.message == "Success") {
                        showIntervalDataList();
                        deleteErrorMessage("error_interval_data");

                        // Fill Interval Data choices
                        selected_interval_data_id = document.getElementById("simulation_parameter_interval_data").value
                        $("#simulation_parameter_interval_data").empty();
                        var sel = document.getElementById('simulation_parameter_interval_data');
                        // create new option element
                        console.log(data)
                        for (i=0;i<data.idList.length;i++){
                            var opt = document.createElement('option');
                            opt.appendChild( document.createTextNode(data.fileNameList[i]) );
                            opt.value = data.idList[i];
                            sel.appendChild(opt); 
                            if (opt.value == selected_interval_data_id){
                                opt.setAttribute("selected", "selected");
                            }
                        }
                    }
                    else {
                        createErrorMessage("error_interval_data", data.message);
                    }

                }
    }
    request.send(params);
}