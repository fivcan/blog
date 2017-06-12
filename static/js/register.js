$(function(){

	var error_name = false;
	var error_email = false;


	$('#name').blur(function() {
		check_user_name();
	});

	$('#email').blur(function() {
		check_email();
	});

	function check_user_name(){
		var $name = $('#name');
		var len = $name.val().length;
		if(len<5||len>20)
		{
			$name.parent().next().html('请输入5-20个字符的用户名');
			$name.parent().next().css({'color':'#e62e2e'});
			$name.parent().next().show();
			error_name = true;
		}
		else
		{
			$name.parent().next().hide();
			error_name = false;

		}


	}




	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
		var $email = $('#email');
		if(re.test($email.val()))
		{
			$email.parent().next().hide();
			error_email = false;
		}
		else
		{
			$email.parent().next().html('你输入的邮箱格式不正确');
			$email.parent().next().css({'color':'#e62e2e'});
			$email.parent().next().show();
			error_email = true;
		}

	}


	$('#register_submit').click(function(){
		check_user_name();
		check_email();
		// alert([error_name,error_password,error_check_password,error_email])
		console.log(error_name, error_email);
		if(error_name == true || error_email == true)
		{
			return false;
		}

	})


});