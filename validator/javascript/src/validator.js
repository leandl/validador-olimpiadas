const { question_1 } = require("../exam/question_1.js");

const questionsFunction = {
    "question_1": question_1
}

class ValidatorError extends Error {}
class Validator {
    constructor(questions) {
        this.questions = questions
    }

    test(nameQuestion) {

        const question = this.questions[nameQuestion];
        const questionFunction = questionsFunction[nameQuestion];
        
        if (!question) {
            throw new ValidatorError("not existis question");
        }
            
        if (!questionFunction) {
            throw new  ValidatorError("not existis question function");
        }
            
        for (const test of question.getTests()) {
            console.log("=====================");
            console.log(`Args: ${test.getArgs()}`);
            console.log(`Expected Result: ${test.getResult()}`);
            
            const result = questionFunction(...test.getArgs());
            console.log(`Result: ${result}`);
        }
    } 
}

module.exports = {
    Validator
}
