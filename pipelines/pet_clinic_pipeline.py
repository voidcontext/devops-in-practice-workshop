#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating PetClinic Pipeline..."
go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
service_key={'GCLOUD_SERVICE_KEY': 'AES:lVCHjvAhBkxBVacvyO3L+Q==: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'}
pipeline = configurator\
	.ensure_pipeline_group("sample")\
	.ensure_replacement_of_pipeline("PetClinic")\
	.set_git_material(GitMaterial("https://github.com/voidcontext/devops-in-practice-workshop.git", ignore_patterns=set(['pipelines/*']))).ensure_environment_variables({'GCLOUD_PROJECT_ID': 'devops-workshop-gabor'}).ensure_encrypted_environment_variables(service_key)
stage = pipeline.ensure_stage("commit")
job = stage.ensure_job("build-and-publish").ensure_environment_variables({'MAVEN_OPTS': '-Xmx1024m'}).set_elastic_profile_id("docker-jdk")
job.add_task(ExecTask(['./mvnw', 'clean package']))
job.add_task(ExecTask(['bash', '-c', 'docker build --tag pet-app:$GO_PIPELINE_LABEL --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .']))
job.add_task(ExecTask(['bash', '-c', 'docker login -u _json_key -p"$(echo $GCLOUD_SERVICE_KEY | base64 -d)" https://us.gcr.io']))
job.add_task(ExecTask(['bash', '-c', 'docker tag pet-app:$GO_PIPELINE_LABEL us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
job.add_task(ExecTask(['bash', '-c', 'docker push us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
stage = pipeline.ensure_stage("deploy")
job = stage.ensure_job("deploy").ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_CLUSTER': 'devops-workshop-gke'}).set_elastic_profile_id("kubectl")
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', './deploy.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

stage = pipeline.ensure_stage("approve-canary")
stage.set_has_manual_approval()
job = stage \
    .ensure_job("complete-canary") \
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-gabor', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})
job.set_elastic_profile_id('kubectl')
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './complete-canary.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))


configurator.save_updated_config()
