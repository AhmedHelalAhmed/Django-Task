$(document).ready(function () {
    $('#submit_btn').on("click", function (event) {
        event.preventDefault();
        var patient_name = $("#id_patient_name").val();
        var patient_number = $("#id_phone_number").val();
        //some validation
        if (patient_name == "") {
            $("#note").html('<div class="alert alert-danger" role="alert">\n' +
                '  Name can not be empty\n' +
                '</div>');

        } else if (patient_number == "") {
            $("#note").html('<div class="alert alert-danger" role="alert">\n' +
                '  Mobile can not be empty\n' +
                '</div>');
        } else {
            var url = window.location + "api/patients/";
            $.ajax({
                url: url,
                method: "POST",
                data: {patient_name: patient_name, phone_number: patient_number},
                success: function (response) {

                    $("#id_patient_name").val("");
                    $("#id_phone_number").val("");
                    $("#note").html('<div class="alert alert-success" role="alert">\n' +
                        '  Success :  the data stored \n' +
                        '</div>');
                },
                error: function (response) {
                    $("#note").html('<div class="alert alert-danger" role="alert">\n' +
                        '  Error : ' + response.responseJSON.phone_number[0] + '\n' +
                        '</div>');
                }

            });

        }


    });

});