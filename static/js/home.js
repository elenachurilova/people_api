"use strict";

$.get('/api/people', (res) => {
        for (const person of res)
//        $("#body").append(`<h3> ${person.fname} </h3>`)
        $("#body").append(`<tr>
                            <td>${person.fname}</td>
                            <td>${person.lname}</td>
                            <td>${person.timestamp}</td>
                          </tr>`)
        }
)


//            <table>
//                <caption>People</caption>
//                <thead>
//                    <tr>
//                        <th>First Name</th>
//                        <th>Last Name</th>
//                        <th>Update Time</th>
//                    </tr>
//                </thead>
//                <tbody id="body">
//                </tbody>
//            </table>

//<table>
//    <thead>
//        <tr>
//            <th colspan="2">The table header</th>
//        </tr>
//    </thead>
//    <tbody>
//        <tr>
//            <td>The table body</td>
//            <td>with two columns</td>
//        </tr>
//    </tbody>
//</table>