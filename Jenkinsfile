pipeline{
    agent any;

    stages{
        stage("Install requirements"){
            steps{
                echo "Installing dependencies..."
                sh "pip3 install -r requirements.txt"
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