
$(function () {
    $("#btnAdd").bind("click", function () {
        var div = $("<tr />");
        div.html(GetDynamicTextBox(""));
        $("#TextBoxContainer").append(div);
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
    return '<td><input name = "DynamicTextBox" type="text" value = "' + value + '" class="form-control" /></td>' + '<td><input name = "DynamicTextBox" type="text" value = "' + value + '" class="form-control" /></td>' + '<td><input name = "DynamicTextBox" type="text" value = "' + value + '" class="form-control" /></td>' +
'<td><button type="button" class="btn btn-danger remove"><i class="glyphicon glyphicon-remove-sign"></i></button>' /*<button type="button" class="btn btn-info edit" id="edit" style="display: none;"><i class="glyphicon glyphicon-edit"></i> Edit</button> <button type="button" class="btn btn-success save" id="save"><i class="glyphicon glyphicon-save"></i> Save</button></td>'*/
  
}