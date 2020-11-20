pipeline {
  agent { any }
  stages {
    stage('build') {
      steps {
        echo 'working'
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }   
    }
  }
}
