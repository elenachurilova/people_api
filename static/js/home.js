"use strict";


    $.get('/api/people', (res) => {
            for (const person of res)
            $("#body").append(`<tr>
                                <td>${person.fname}</td>
                                <td>${person.lname}</td>
                                <td>${person.timestamp}</td>
                              </tr>`)
            }
    )



function create_new_person(evt) {
    evt.preventDefault();

    const formInputs = {
        'fname' : $("#fname").val(),
        'lname' : $("#lname").val(),
    }

    const person = JSON.stringify(formInputs)

    $.ajax({
        type: "POST",
        url: '/api/people',
        data: person,
        success: (res) => {
            $("#fname").val("")
            $("#lname").val("")
            $("#body").append(`<tr>
                                <td>${res.fname}</td>
                                <td>${res.lname}</td>
                                <td>${res.timestamp}</td>
                              </tr>`)
        },
        dataType: "json",
        headers: {"Content-Type" : "application/json"},
    });

  }

$("#create").on("click", create_new_person)

