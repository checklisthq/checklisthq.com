$("#closebutton").click(function(e) {
  $("#myModal").hide()
});

function modal(type, text, pre, post) {
  $("#modaltitle").val(text);
  $("#myModal").show();
  $("#myModal input").focus();
  $("#savebutton").click(function(e) {
    $("#myModal").hide()
    $("#id_specification").val($("#id_specification").val()+pre+$("#modalval").val()+post+"\n");
    $("#modalval").val("");
    return false;
  });
}

$("#backbutton").click(function(e) {
  history.go(-1);
});
$("#id_specification").focus();
$("#clear").click(function(e) {
  $("#id_specification").val("");
  $("#id_specification").focus();
});

$("#addheading").click(function(e) {
  modal("heading", "Add Heading", "=", "=");
});

$("#addchecklistitem").click(function(e) {
  modal("checklistitem", "Add Checklist Item", "[]", "");
});

$("#addchecklistgroupitem").click(function(e) {
  modal("checklistgroupitem", "Add Checklist group item", "()", "");
});

$("#addtextbox").click(function(e) {
  modal("textbox", "Add textbox", "[...]", "");
});

$("#preview").click(function(e) {
  $("#checklistform").submit();
});

