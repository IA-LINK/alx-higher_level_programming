#!/usr/bin/node

const { error } = require('console');
const request = require('request');

const apiUrl = process.argv[2];

characterId = 18;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        const filmsData = JSON.parse(body).results;
        const movieWithWedge = filmsData.filter((film)=>
        film.characters.includes(
            `https://swapi-api.alx-tools.com/api/people/${characterId}/`
        )
        );
        console.log(movieWithWedge.length);
    }
});
