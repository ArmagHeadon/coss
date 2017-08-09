node('master'){
    def params
    switch(env.BRANCH_NAME) {
        case "master":
            environment = "staging"
            app_id_group = "/staging/"
        break
        case "production":
            environment = "production"
            app_id_group = ""
        break
        default:
            print "Invalid branch"
            currentBuild.result = "FAILURE"
            throw err
        break
    }
    type = 'group'
    slackSend color: 'good', message: "Starting build ${BUILD_NUMBER} for ${JOB_NAME} ${environment} | <${BUILD_URL}changes | Changes>"
}

node('mesos') {
    def image
    def app_id = "coss"
    def dockerRegistry = "docker-registry.ops.mozilla.community:443"

    stage('Prep') {
        checkout scm
        gitCommit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
        params = [string(name: 'environment', value: "production"),
                  string(name: 'commit_id', value: gitCommit),
                  string(name: 'marathon_id', value: app_id_group + app_id),
                  string(name: 'marathon_config', value: 'coss_' + environment + '.json'),
                  string(name: 'type', value: 'group')]
    }

    stage('Build') {
        image = docker.build(app_id + ":" + gitCommit, "-f docker/Dockerfile.prod .")
    }

    stage('Push') {
        sh "docker tag ${image.imageName()} " + dockerRegistry + "/${image.imageName()}"
        sh "docker push " + dockerRegistry + "/${image.imageName()}"
    }
}

node('master') {
    stage('Deploy') {
        build job: 'deploy-test', parameters: params
    }
}
