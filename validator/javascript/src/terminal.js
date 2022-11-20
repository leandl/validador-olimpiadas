const { Printer } = require("./printer");

function getArgs () {
  const args = {};
  process.argv
    .slice(2, process.argv.length)
    .forEach( arg => {
    // long arg
    if (arg.slice(0,2) === '--') {
      const longArg = arg.split('=');
      const longArgFlag = longArg[0].slice(2, longArg[0].length);
      const longArgValue = longArg.length > 1 ? longArg[1] : true;
      args[longArgFlag] = longArgValue;
    }
    // flags
    else if (arg[0] === '-') {
      const flags = arg.slice(1,arg.length).split('');
      flags.forEach(flag => {
      args[flag] = true;
      });
    }
  });
  return args;
}


class Terminal {
  static getParams() {
    const args = getArgs();

    const question = args["question"] || null;
    const pathJSON = args["json-data"] || null;
    const pathExam = args["exam-path"] || null;

    if (!pathJSON) {
      Printer.error('Invalid json path specified.');
    }

    if (!pathExam) {
      Printer.error('Invalid exam path specified.');
    }
    
    return {
      question,
      pathExam,
      pathJSON
    }
  }
}

module.exports = {
  Terminal
}