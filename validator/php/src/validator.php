<?php
include_once __DIR__ . '/question.php';

$files = scandir(__DIR__.'/../../../exam');
$questionsDef = [];
foreach($files as $file){
    if(substr($file, -4) == '.php'){
        include_once __DIR__.'/../../../exam/' . $file;
        $aux = str_replace(".php", "", $file);
        $questionsDef[$aux] = $aux;
    }
}

class ValidatorException extends Exception { }

class Validator{
    protected $questions;

    public function __construct($questions)
    {
        $this->questions = $questions;    
    }

    public function testAll(){
        global $questionsDef;

        $response = [];
        foreach($questionsDef as $index => $question){
            $response[] = $this->test($index);
        }

        return $response;
    }

    private function getIndexQuestion(string $question){
        return substr($question, -1) - 1;
    }

    public function test(string $nameQuestion){
        global $questionsDef;
        $question = $this->questions[$this->getIndexQuestion($nameQuestion)];
        $questionFunction = $questionsDef[$nameQuestion];

        if (!$question){
            throw new ValidatorException("Question doesn't exists.");
        }

        if (!$questionFunction){
            throw new ValidatorException("Function doesn't exists.");
        }

        $response = [];

        foreach($question->getTests() as $test){
            $args = $test->getArgs();
            $expectedResult = $test->getResult();
            $results = $questionFunction(...$test->getArgs());
            $args = json_encode($args);
            $response[] = [
                'args' => $args,
                'expected_result' => $expectedResult,
                'result' => $results,
                'passed' => $results == $expectedResult
            ];
        }
        
        return $response;
    }
}







