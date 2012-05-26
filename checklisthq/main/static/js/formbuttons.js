var qtype="";

$("#closebutton").click(function(e) {
  $("#myModal").hide()
});

$("#savebutton").click(function(e) {
  $("#myModal").hide()
  if (qtype=="heading")
  {
    $("#id_specification").val($("#id_specification").val()+"="+$("#modalval").val()+"=\n");
  }
  if (qtype=="checklistitem")
  {
    $("#id_specification").val($("#id_specification").val()+"[]"+$("#modalval").val()+"\n");
  }
  if (qtype=="checklistgroupitem")
  {
    $("#id_specification").val($("#id_specification").val()+"()"+$("#modalval").val()+"\n");
  }

  if (qtype=="textbox")
  {
    $("#id_specification").val($("#id_specification").val()+"[...]"+$("#modalval").val()+"\n");
  }

  $("#modalval").val("")

});

$("#backbutton").click(function(e) {
  history.go(-1);
});
$("#id_specification").focus();
$("#clear").click(function(e) {
  $("#id_specification").val("");
  $("#id_specification").focus();
});

$("#addheading").click(function(e) {
  qtype="heading";
  $("#modaltitle").val("Add Heading");
  $("#myModal").show();
});

$("#addchecklistitem").click(function(e) {
  qtype="checklistitem";
  $("#modaltitle").textContent="Add Checklist Item";
  $("#myModal").show()
});

$("#addchecklistgroupitem").click(function(e) {
  qtype="checklistgroupitem";
  $("#modaltitle").val("Add Checklist group item");
  $("#myModal").show();
});

$("#addtextbox").click(function(e) {
  qtype="textbox";
  $("#modaltitle").val("Add textbox");
  $("#myModal").show();
});

$("#preview").click(function(e) {
  $("#checklistform").submit();
});

