$("#myClickButton").click(function() {
    $.get("apps/", function(data) {
        $("#myOutput").html(data);
    }, "html");
});

$("#myClickButton2").click(function() {
    // modify the url below to your YARN ResourceManager's API URL
    $.get("http://kyan-cdh03.novalocal:8088/ws/v1/cluster/apps?deSelects=resourceRequests", function(data) {
        $("#myOutput2").html(data);
    }, "html");
});