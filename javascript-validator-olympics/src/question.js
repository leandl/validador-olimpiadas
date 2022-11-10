class Question {

    constructor(name, tests) {
        this.name = name;
        this.tests = tests;
    }
    
    getName() {
        return this.name;
    }

    getTests() {
        return this.tests;
    }
}

    
module.exports = {
   Question
}