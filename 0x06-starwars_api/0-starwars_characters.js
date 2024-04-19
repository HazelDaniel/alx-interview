#!/usr/bin/node

const request = require('request');

const thirdArg = process.argv[2]
if (thirdArg) {
	request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, async (error, response, body) => {
		if (!error && response.statusCode === 200) {
			const chars = JSON.parse(body).characters;
			for (const character of chars) {
				const charPromise = new Promise((resolve, reject) => {
					request(character, function (error, response, body) {
						if (error) {
							reject(error);
						} else {
							resolve(JSON.parse(body).name);
						}
					});
				});
				console.log(await charPromise);
			}
		}
	});
}
