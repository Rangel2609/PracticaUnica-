








});
function inciando(){
$("tabla").empty();
    jQuery.each(table.rows, function(i, row){
        var r = "";
        $.each(row, function(tarea, valor){
         //   r = r + "<tr><td>" + valor + "</td>";
         if(tarea = "id"){
            r = r + "<tr><td>" + valor + "</td>";

         }
         else {
            r = r + "<td>" + valor + "</td>";
                }
           });
           r+= "</tr>";
           $("tabla").append(r);
       });
     }
});