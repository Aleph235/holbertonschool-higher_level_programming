#!/usr/bin/node
const id = process.argv[2];
const axios = require('axios').default;
axios.get(`https://swapi-api.hbtn.io/api/films/${id}`)
  .then(function (response) {
    console.log(response.data.title);
  });
