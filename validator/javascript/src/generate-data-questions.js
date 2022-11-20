const { Question } = require("./question");
const { Test } = require("./test");

function generateDataQuestions(jsonDataQuestions) {
  const questions = {}

  for (const [keyQuestion, question] of Object.entries(jsonDataQuestions)) {
    const tests = question.tests.map(({ args, result }) => new Test(args, result));
    questions[keyQuestion] = new Question(keyQuestion, tests);
  }

  return questions
}

module.exports = {
  generateDataQuestions
}