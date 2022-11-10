const { Question } = require("./src/question");
const { Test } = require("./src/test");
const { Validator } = require("./src/validator");

const dataQuestions = require("./data.json");

const questions = {}

for (const [keyQuestion, question] of Object.entries(dataQuestions)) {
    const tests = question.tests.map(({ args, result }) => new Test(args, result));
    questions[keyQuestion] = new Question(keyQuestion, tests);
}

validator = new Validator(questions)
validator.test("question_1")