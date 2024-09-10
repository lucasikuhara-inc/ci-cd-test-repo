pipeline{
    agent any;

    stages{
        stage("Install requirements"){
            steps{
                echo "Installing dependencies..."
                sh "poetry env use && poetry install"
            }
        }
        stage("Unit testing"){
            steps{
                echo "Executing 'test.sh' test script"
                sh "./test.sh"
            }
        }
    }

}