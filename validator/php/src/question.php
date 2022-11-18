<?php
include_once __DIR__ . '/test.php';

class Question{
    protected $name;
    protected $tests;

    /** 
     * @param String 
     * @param Test[] 
    */
    public function __construct($name, $tests)
    {
        $this->name = $name;
        $this->tests = $tests;
    }

    public function getName(){
        return $this->name;
    }

    public function getTests(){
        return $this->tests;
    }

}
