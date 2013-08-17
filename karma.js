var http = require('http');
var express = require('express');
var mongoose = require('mongoose');
var restify = require('express-restify-mongoose')
var Schema = mongoose.Schema;
var bunyan = require('bunyan');

mongoose.connect('mongodb://localhost/karmapolice');

var Karma = new Schema({
        name: { type: String, required: true },
        total: { type: Number, required: true}
});
var KarmaModel = mongoose.model('Karma', Karma);


var app = express();
app.configure(function(){
    app.use(express.bodyParser());
    app.use(express.methodOverride());
    restify.serve(app, KarmaModel);
});

http.createServer(app).listen(3000, function() {
    console.log("Express server listening on port 3000");
});
