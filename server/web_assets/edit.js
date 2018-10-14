$(function () {
    $("#btnAdd").bind("click", function () {
        var div = $("<tr />");
        div.html(GetDynamicTextBox(""));
        $("#srdTbody").append(div);
    });

    $("#btnSaveAll").bind("click", function(){
      var array = [];
      var t = document.getElementById('srdTbody');
      for(var i = 0; i < t.children.length; i++){
        var tr = t.children[i];
        var row_array = [];
        for(var y = 0; y < tr.children.length-1; y++){
          row_array.push(tr.children[y].children[0].value);
        }
        array.push(row_array);
      }
      
      $.post('/account/update', JSON.stringify(array));

    });
  
    $("body").on("click", ".remove", function () {
        $(this).closest("tr").remove();
    });
    $("body").on("click", ".edit", function () {
        $('#edit').hide();
        $('#save').show();
    });
    $("body").on("click", ".save", function () {
        $('#save').hide();
        $('input').each(function(){
        var content = $(this).val();//.replace(/\n/g,"<br>");
        $(this).html(content);
        $(this).contents().unwrap(); 
        });
        $('#edit').show();
    });
});
function GetDynamicTextBox(value) {
    return '<td><input name = "sender" type="text" value = "' + value + '" class="form-control" /></td>' + '<td><input name = "receiver" type="text" value = "' + value + '" class="form-control" /></td>' + '<td><input name = "difficulty" type="text" value = "' + value + '" class="form-control" /></td>' +
'<td><button type="button" class="btn btn-danger remove"><i class="glyphicon glyphicon-remove-sign"></i></button>';
}