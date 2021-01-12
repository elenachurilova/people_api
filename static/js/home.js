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

function create_new_user(evt) {
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
            console.log("Created new person")
            console.log(res)
        },
        dataType: "json",
        headers: {"Content-Type" : "application/json"},
    });

$("#create").on("click", create_new_user)
