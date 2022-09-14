#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios').default;
let count = 0;

axios.get(`${url}`)
  .then(function (response) {
    for (let i = 0; i < response.data.results.length; i++) {
      for (let j = 0; j < response.data.results[i].characters.length; j++) {
        if (response.data.results[i].characters[j].includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  })
  .catch(function (error) {
    console.log(error.response.status);
  });
