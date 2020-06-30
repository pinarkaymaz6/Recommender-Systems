'use strict';

window.addEventListener('load', function () {

    document.getElementById("submit").addEventListener("click", function (event) {
        const movie = document.getElementById('input_movies').value
        let url = "/movies/".concat(movie)
        fetch(url)
            .then((res)=> res.text())
            .then(function (data) {
                
                document.getElementById('result').innerHTML = data
            })
        .catch(function (error) {
            console.log("Poor girl")
        });   
    });
});