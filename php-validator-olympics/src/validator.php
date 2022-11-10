<?php
include_once __DIR__ . '/question.php';
include_once __DIR__ . '/../exam/question_1.php';

class ValidatorException extends Exception { }

class Validator{
    protected $questions;
    protected $questionsDef = ["question_1" => 'question_1'];

    public function __construct($questions)
    {
        $this->questions = $questions;    
    }

    public function testAll(){
        return;
    }

    public function test(string $nameQuestion){
        $question = $this->questions[$nameQuestion];
        $questionFunction = $this->questionsDef[$nameQuestion];

        if (!$question){
            throw new ValidatorException("Question doesn't exists.");
        }

        if (!$questionFunction){
            throw new ValidatorException("Function doesn't exists.");
        }

        foreach($question->getTests() as $test){
            $args = $test->getArgs();
            $results = $questionFunction(...$test->getArgs());
            $args = implode(',',$args);
            echo "=====================\n";
            echo "Args: {$args}\n";
            echo "Result: {$results}\n";
        }
        
    }

    

}







