const { Printer } = require("./src/printer");
const { Terminal } = require("./src/terminal");
const { Validator } = require("./src/validator");

const { generateDataQuestions } = require("./src/generate-data-questions");
const { getQuestionsFunction } = require("./src/get-question-function");

const { pathExam, pathJSON, question } = Terminal.getParams();

const dataQuestions = require(pathJSON);
const questions = generateDataQuestions(dataQuestions);
const questionsFunction = getQuestionsFunction(pathExam);

const validator = new Validator(questions, questionsFunction)
const result = (question) 
    ? validator.test(question)
    : validator.testAll();

Printer.success(result)