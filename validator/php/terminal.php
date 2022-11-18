<?php
class Terminal
{
  public static function getParams()
  {
    $args = getopt('q::j:e:', ['question::', 'json-data:', 'exam-path:']);
    $question = '';

    if (isset($args["q"])) {
      $question = $args["q"];
    } else if (isset($args["question"])) {
      $question = $args["question"];
    }

    if (isset($args["j"]) || isset($args["json-data"])) {
      $pathjson = isset($args["j"]) ? $args["j"] : $args["json-data"];
    } else {
      echo json_encode(['status' => 'error', 'message' => 'Invalid json path specified.']);
      die;
    }

    if (isset($args["e"]) || isset($args["exam-path"])) {
      $pathexam = isset($args["e"]) ? $args["e"] : $args["exam-path"];
    } else {
      echo json_encode(['status' => 'error', 'message' => 'Invalid exam path specified.']);
      die;
    }

    return [
      $pathjson,
      $pathexam,
      $question
    ];
  }
}
