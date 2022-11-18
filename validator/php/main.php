<?php
include_once 'terminal.php';

list($pathjson, $pathexam, $questionArgs) = Terminal::getParams();

include_once 'src/validator.php';
include_once 'src/question.php';
include_once 'src/test.php';

$method = $questionArgs ? 'test' : 'testAll';

$jsonQuestions = json_decode(file_get_contents($pathjson));
$questions = [];

foreach($jsonQuestions as $keyQuestion => $question){
    $tests = array_map(function($data){
        return new Test($data->args, $data->result);
    }, $question->tests);
    $questions[$keyQuestion] = new Question($keyQuestion, $tests);
}

$validator = new Validator($questions);
$result = $validator->$method($questionArgs);
echo json_encode(['status' => 'success', 'result' => $result]);