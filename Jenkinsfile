pipeline {
   agent any
   stages {
      stage('Build code') {
          steps {
            sh 'python3 app.py'
          }
      }
   }
    

       stage('Test code') {
         steps {
            sh 'python3  test_calplus.py'
       }
   }
} 
