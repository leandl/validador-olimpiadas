const { Printer } = require("./printer");

class Validator {
    constructor(questions, questionsFunction) {
        this.questions = questions;
        this.questionsFunction = questionsFunction;
    }

    testAll() {
        return Object
            .entries(this.questionsFunction)
            .map(
                ([nameQuestion, _questionFunction]) => this.test(nameQuestion)
            );
    }
    
    #getIndexQuestion(nameQuestion) {
        const numberQuestion = Number(nameQuestion.slice(-1));
        return numberQuestion - 1;
    }
        
    test(nameQuestion) {
        const indexQuestion = this.#getIndexQuestion(nameQuestion);

        const question = this.questions[indexQuestion];
        const questionFunction = this.questionsFunction[nameQuestion];
        
        if (!question) {
            Printer.error("not existis question");
        }
            
        if (!questionFunction) {
            Printer.error("not existis question function");
        }

        return question.getTests().map((test) => {
            const result = questionFunction(...test.getArgs());
            const expectedResult =test.getResult();

            return {
                'args': test.getArgs(),
                'expected_result': expectedResult,
                'result': result,
                'passed': result == expectedResult
            }
        });
    } 
}

module.exports = {
    Validator
}
