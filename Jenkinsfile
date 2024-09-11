pipeline{
    agent any;

    stages{
        stage("Install requirements"){
            steps{
                echo "Installing dependencies..."
                sh 'export PATH="${HOME}/.local/bin:${PATH}"; poetry env use python3.11 && poetry install'
            }
        }
        stage("Unit testing"){
            steps{
                echo "Executing 'test.sh' test script"
                sh "./test.sh"
            }
        }
        stage('SonarQube analysis') {
            steps {
                script {
                    scannerHome = tool 'Sonar Scanner 6.1'
                }
                withSonarQubeEnv('local-sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }

}