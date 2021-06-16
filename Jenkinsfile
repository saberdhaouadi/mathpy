pipeline {
   agent any

   stage('Clone repository') {
        checkout scm
   }

   stage('Test code') {
       steps {
          sh 'python3  test_calplus.py'
       }
   }
} 
