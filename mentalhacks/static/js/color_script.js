var colors = ["blue","green","red","yellow","pink","orange","violet",];
var bg_colors = ["green","blue","orange","violet","red","yellow","grey",];
var color_id = document.getElementById("main_color").innerHTML;

setInterval(
    function(){
        var random_index =  Math.floor(Math.random() * 7);
        var random_index_for_bg_color = Math.floor(Math.random()* 7);
        var final_color = colors[random_index];
        document.getElementById("main_color").innerHTML = final_color.fontcolor(bg_colors[random_index_for_bg_color]);

    },1000);