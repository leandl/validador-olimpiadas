const { Question } = require("./question");
const { Test } = require("./test");

function generateDataQuestions(jsonDataQuestions) {
  return jsonDataQuestions.map(question => {
    const tests = question.tests.map(({ args, result }) => new Test(args, result));
    return new Question(question.name, tests);
  });
}

module.exports = {
  generateDataQuestions
}