'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var promptSchema = Schema( {
  question: String, //prompt
  category: String, //villain, quest, hero, or setting
  answer: String, //gpt response
  createdAt: Date,
  userId: {type:ObjectId, ref:'user' }
} );

module.exports = mongoose.model( 'Prompt', promptSchema );
