import https from "https";
const options = new URL(`https://jsonmock.hackerrank.com/api/article_users?username=epaga`);
console.log("options:", options);
https.request(options, (res) => {
	console.log(res.statusCode);
});
