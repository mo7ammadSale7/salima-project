$(function () {
	var $muform = $("#msform");
	if ($muform.length) {
		$muform.validate({
			rules: {
				Tname: {
					required: true,
					alphanumeric: true,
				},
				fname: {
					required: true,
					noSpace: true,
				},
				fullAddress: {
					required: true,
				},
				age: {
					required: true,
				},
				mainPhoneNumber: {
					required: true,
				},
				prjdetail: {
					required: true,
				},
				awards: {
					required: true,
				},
				You_are: {
					required: true,
					noSpace: true,
				},
				Email: {
					required: true,
					customEmail: true,
				},
			},
			messages: {
				Tname: {
					required: "من فضلك املاء الحقل",
				},
				Email: {
					required: "من فضلك ادخل الايميل",
					email: "من فضلك ادخل ايميل صحيح",
				},
				fname: {
					required: "من فضلك ادخل الاسم",
				},
				fullAddress: {
					required: "من فضلك ادخل الاسم",
				},
				age: {
					required: "من فضلك ادخل الاسم",
				},
				mainPhoneNumber: {
					required: "من فضلك ادخل الاسم",
				},
				prjdetail: {
					required: "من فضلك ادخل الاسم",
				},
				awards: {
					required: "من فضلك ادخل الاسم",
				},
				You_are: {
					required: "من فضلك ادخل الاسم",
				},
            },
            errorPlacement: function(error, element) 
      {
        if (element.is(":radio")) 
        {
            error.appendTo(element.parents('.gender'));
        }
        else if(element.is(":checkbox")){
            error.appendTo(element.parents('.hobbies'));
        }
        else 
        { 
            error.insertAfter( element );
        }

		}
	});
}
