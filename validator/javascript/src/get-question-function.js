const path = require('node:path');
const fs = require("node:fs");
const { Printer } = require('./printer');

function getQuestionsFunction(pathExam) {
  const questionsFunction = {}

  if (!fs.existsSync(pathExam)) {
    Printer.error("Invalid path specified.");
  }

  const filesExam = fs.readdirSync(pathExam).filter(filename => filename.endsWith(".js"));
  filesExam.forEach(fileExam => {
    const pathFileExam = path.join(pathExam, fileExam);
    const nameQuestion = fileExam.replace(".js", "");

    const dataFileExam = require(pathFileExam);
    questionsFunction[nameQuestion] = dataFileExam[nameQuestion];
  });

  return questionsFunction
}

module.exports = {
  getQuestionsFunction
}
