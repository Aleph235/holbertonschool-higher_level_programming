#!/usr/bin/node
const url = process.argv[2];
const FilePath = process.argv[3];
const fs = require('fs');
const axios = require('axios').default;
axios.get(`${url}`)
  .then(function (response) {
    const content = response.data;
    fs.writeFile(FilePath, content, err => {
      if (err) {
        console.error(err);
      }
    });
  });
