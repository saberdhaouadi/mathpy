node {
   def app

   stage('Clone repository') {
        checkout scm
   }

   stage('Test code') {
       steps {
          sh 'python3  test_calplus.py'
       }
   }
} 
