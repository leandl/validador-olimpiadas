<?php
include_once 'src/validator.php';
include_once 'src/question.php';
include_once 'src/test.php';

$jsonQuestions = json_decode(file_get_contents('./data.json'));
$questions = [];

foreach($jsonQuestions as $keyQuestion => $question){
    $tests = array_map(function($data){
        return new Test($data->args, $data->result);
    }, $question->tests);
    $questions[$keyQuestion] = new Question($keyQuestion, $tests);
}

$validator = new Validator($questions);
$validator->test("question_1");
