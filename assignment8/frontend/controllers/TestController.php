<?php

namespace frontend\controllers;

use yii\web\Controller;

class TestController extends Controller
{
    public function actionIndex()
    {
<<<<<<< HEAD
        echo 'test';
=======
        $data = 'data test';
        return $this->render('index', ['data' => $data]);
    }
    public function actionTest()
    {
        $data = 'test Test';
        return $this->render('test', ['data' => $data]);
>>>>>>> d4ac44532c1c1245e9404d555f8023caca16905e
    }
}