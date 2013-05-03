$(document).ready(function() {
	$("#submit").click(function() {
		inserting();
	});
	$("#question").keydown(function(e) {
	    if (e.which == 13) {
        	inserting();
    	}
	});
});

function inserting() {
	question = $("#question").val();
	var html = $.ajax({
		url: "http://www.monodiary.net/test/api.php",
		type: "POST",
		data: "question="+question,
		dataType: "html",
		async: false
	}).responseText;

	append_question = "\
		<div class=\"clear\">\
				<img src=\"http://x86osx.com/bbs/emoticons/b_69.gif\" alt=\"\" class=\"right_img\" />\
				<div class=\"right\">\
	"+question+"\
				</div>\
				<div class=\"interline\"></div>\
			</div>\
	";
	append_response = "\
	<div class=\"clear\">\
				<img src=\"http://cfile237.uf.daum.net/image/116FBF024BA43FEC400D06\" alt=\"\" class=\"left_img\" />\
				<div class=\"left\">\
	<span style=\"color: white; font-weight: bold;\">"+html+"</span><br /><br />\
	Do you want to know more?\
				</div>\
				<div class=\"interline\"></div>\
			</div>\
	";

	$("#chat").append(append_question);
	$("#chat").append(append_response);
	$("#question").val("");
	document.body.scrollTop = document.body.scrollHeight;
	$("#question").focus();
}