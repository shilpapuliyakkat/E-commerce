$(document).ready(function () {

    $('.payWithRazorpay').click(function (e){
        e.preventDefault();
        let fname = $("[name='fname']").val();
        let lname = $("[name='lname']").val();
        let email = $("[name='email']").val();
        let phone = $("[name='phone']").val();

        let address = $("[name='address']").val();
        let city = $("[name='city']").val();

        let state = $("[name='state']").val();

        let country = $("[name='country']").val();
        let pincode = $("[name='pincode']").val();
        let token = $("[name='csrfmiddlewaretoken']").val();

      if(fname == "" || lname == ""|| email=="" ||phone==""|| address==""||city==""||state==""||country==""||pincode=="")
      {
        
        swal("Alert!", "All the fields are mandatory!", "error");
        return false;
      }
      else
      {

        $.ajax({
            method: "GET",
            url: "/proceed-to-pay",
            success: function (response) {
                console.log("payment", response);

                const options = {
                    "key": "rzp_test_w0uZSnCR8QfN2v", // Enter the Key ID generated from the Dashboard
                    "amount": response.TotalPrice * 100, // Amount is in currency sub units. Default currency is INR. Hence, 50000 refers to 50000 paise
                    "currency": "INR",
                    "name": "Developer", //your business name
                    "description": "Thank you",
                    // "image": "https://example.com/your_logo",
                    // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                    "handler": function (responseb){

                        alert(response.razorpay_payment_id);
                        
                      let  data = {
                            "fname": fname,
                            "lname": lname,
                            "email": email,
                            "phone": phone,
                            "address": address,
                            "city": city,
                            "state": state,
                            "country": country,
                            "pincode": pincode,
                            "payment_mode": "paid by Razorpay",
                            "payment_id": responseb.razorpay_payment_id,
                            csrfmiddlewaretoken: token
                        }

                        $.ajax({
                            method:"POST",
                            url:"/place-order",
                            data: data,
                            success: function (responsec){
                                swal("Congratulations!",responsec.status, "success").then((value) => {
                                    window.location.href = '/my-orders'
                                  });
                            }
                        });

                    },
                    "prefill": {
                        "name": fname+" "+fname, //your customer's name
                        "email": email,
                        "contact": phone
                    },                        
                
                   
                    "theme": {
                        "color": "#3399cc"
                    }
                };
                const rzp1 = new Razorpay(options);
            
                rzp1.open();
            }
        });
       

      }

       
})



})