"use strict";
const mongoose = require("mongoose");
const Schema = mongoose.Schema;

var userSchema = Schema({
  username: String,
  passphrase: String,
});

module.exports = mongoose.model("user", userSchema);
