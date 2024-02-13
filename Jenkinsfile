pipeline {
    agent any
    environment {
        token = 'DZnyy741L7T6j9IWbrldx6Mur6LgZAtF7jNaQlodfjg '
        //token = 'TESTTESTTESTTESTTESTTESTTESTTEST '
        jobName = "${JOB_NAME} ${BRANCH_NAME != null ? BRANCH_NAME : ''}"
        buildNo = "${BUILD_NUMBER}"
        Job_url = "${BUILD_URL}"
        url = 'https://notify-api.line.me/api/notify'
        url_monitor = 'http://192.168.41.66:7902/?password=secret'
        url_website = 'https://www.irplus.in.th/Listed/KWM/home.asp'
        allureReportPath = 'reports'
    }

    stages {
        stage('AllureSetup') {
            steps {
                script {
                    allureReportPaths = []  // List to store Allure report paths
                }
            }
        }
        stage('Run KWM_news_clipping') {
            steps {
                sleep 5
                    // Run pytest command and generate test result data
                    sh 'pytest 3KWM_EN_PUBLIC.py --alluredir=Reports'
                    def firstPytestResult = currentBuild.result
                    def retryCount = 1
                    def maxRetryCount = 2
                    def retryAttempt = 0
                    while (firstPytestResult == 'FAILURE' && retryAttempt < retryCount && retryAttempt < maxRetryCount) {
                        sh 'pytest 3KWM_EN_PUBLIC.py --alluredir=Reports'
                    }   
                    // Append Allure report path to the list
                    script {
                        allureReportPaths.add("${allureReportPath}/")
                    }
                
            }
        }
    }

    post {
        always {
            // Publish accumulated Allure reports
            allure([
                includeProperties: false,
                jdk: '',
                results: allureReportPaths.collect { path -> [path: path] }
            ])
            
            // Send Line Notify message based on build result
            script {
                if (currentBuild.result == 'FAILURE') {
                    def message = """KWM
[🔴 การทดสอบสำเร็จ พบข้อผิดพลาด]
${jobName}
${url_website}  
${Job_url}"""
                    sh "curl $url -H \"Authorization: Bearer $token \" -F \"message= ${message}\""
                } else if (currentBuild.result == 'SUCCESS') {
                    def message = """KWM
[🟢 การทดสอบสำเร็จ ไม่พบข้อผิดพลาด] 
${jobName}
${url_website}  
${Job_url}"""
                    sh "curl $url -H \"Authorization: Bearer $token \" -F \"message= ${message}\""
                }
            }
        }
    }
}
