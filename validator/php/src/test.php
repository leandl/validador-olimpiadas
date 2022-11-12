<?php

class Test{
    protected $args;
    protected $result;

    public function __construct($args, $result)
    {
        $this->args = $args;
        $this->result = $result;
    }

    public function getArgs(){
        return $this->args;
    }

    public function getResult(){
        return $this->result;
    }
}