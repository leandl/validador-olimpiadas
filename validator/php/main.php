<?php
include_once 'src/validator.php';
include_once 'src/question.php';
include_once 'src/test.php';

if(!isset($argv[1]) || !$argv[2]){
    throw new Exception('Args not valid.');
}

$questionArg = $argv[1];
$method = $argv[2];

$jsonQuestions = json_decode(file_get_contents(__DIR__ .'/data.json'));
$questions = [];

foreach($jsonQuestions as $keyQuestion => $question){
    $tests = array_map(function($data){
        return new Test($data->args, $data->result);
    }, $question->tests);
    $questions[$keyQuestion] = new Question($keyQuestion, $tests);
}

$validator = new Validator($questions);
$validator->$method($questionArg);
