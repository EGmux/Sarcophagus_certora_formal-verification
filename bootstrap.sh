#! /bin/bash

dockerfile_path="$PWD/dockerfile"
project_path="$PWD/project"
host_port=8080
docker_port=256
container_name="certora_container"
image_name="certora_image"
verbose='false'
certora_key="" # fill with your key, key can be obtained from here: https://www.certora.com/signup?plan=prover


function build_container () {
			printf "docker image hasn't being built.\n"
			printf "image being built...\n"
			if [[ $verbose == "true" ]]; then
				docker buildx build --file $dockerfile_path --tag $image_name . 2>&1 
			else
				docker buildx build --file $dockerfile_path --tag $image_name . >> out  2>&1 
			fi
			if [[ -z "$(docker images -q $image_name 2>&1 | head )" ]]; then
				printf "error while building the image $image_name\n"
			else
				printf "image built.\n"
			fi
}

function create_dirs () {
			printf "missing mounted directories.\n"
			printf "creating directories.\n"
			if [[ $verbose == "true" ]]; then
				mkdir -p $PWD/project/{conf,specs,src}  2>&1
			else
				mkdir -p $PWD/project/{conf,specs,src} >> out 2>&1
			fi
			printf "directories created\n"
}

function start_container () {
		if [[ "$(docker inspect $container_name --format {{.State.Running}}  2>&1 | head -n 1)" != "true" ]]; then
			printf "certora container not started\n"
			if [[ "$(docker inspect $container_name 2>&1 | head -n 1 )" == "[]" ]]; then
				printf "creating the certora container\n"
				if [[ $verbose == "true" ]]; then
					docker run -it -d \
						-e CERTORAKEY=$certora_key \
						--mount type=bind,src="$(pwd)"/project/conf,dst=/project/conf \
						--mount type=bind,src="$(pwd)"/project/specs,dst=/project/specs \
						--mount type=bind,src="$(pwd)"/project/src,dst=/project/src \
						-p $host_port:$docker_port \
						--name $container_name \
						$image_name 2>&1
				else
					docker run -it -d \
						-e CERTORAKEY=$certora_key \
						--mount type=bind,src="$(pwd)"/project/conf,dst=/project/conf \
						--mount type=bind,src="$(pwd)"/project/specs,dst=/project/specs \
						--mount type=bind,src="$(pwd)"/project/src,dst=/project/src \
						-p $host_port:$docker_port \
						--name $container_name \
						$image_name >> out 2>&1
				fi
					if [[ -z $certora_key ]]; then
					printf "certora key not provided, please provide it during container execution\n"
					fi

			else
			printf "starting the $container_name container\n"
				if [[ "$(docker start $container_name 2>&1 | head)" != "$container_name" ]]; then
					printf "error while starting the container\n"
				fi
			fi
			printf "certora container started\n"

		fi
}

function init_container () {
		if [[ ! -d "$project_path" ]]; then
			create_dirs
		fi

		if [[ -z "$(docker images -q $image_name 2>&1 | head )" ]]; then
			build_container
		fi

		start_container
	}

function stop_container () {
		printf "$container_name stopping...\n"
		if [[ $verbose == "true" ]]; then
			docker stop $container_name  2>&1
		else
			docker stop $container_name >> out  2>&1
		fi
		if [[ "$(docker inspect $container_name --format {{.State.Running}} 2>&1 | head -n 1)" == "true" ]]; then
			printf "error while stopping $container_name\n"
		else
			printf "$container_name stopped\n"
		fi
}

function delete_container () {
		printf "$container_name deleting container...\n"
		if [[ $verbose == "true" ]]; then
			docker rm $container_name  2>&1
		else
			docker rm $container_name >> out  2>&1
		fi
		if [[ "$(docker inspect $container_name 2>&1 | head -n 1)" != "[]" ]]; then
			printf "error while deleting $container_name container\n"
		else
			printf "container $container_name deleted\n"
		fi
}

function delete_image () {
	printf "image $image_name deleting...\n"
	if [[ $verbose == "true" ]]; then
		docker image rm -f $image_name 2>&1 
	else
		docker image rm -f $image_name >> out 2>&1 
	fi
	if [[ -n "$(docker images -q $image_name 2>&1 | head )" ]]; then
		printf "error while deleting the image $image_name\n"
	else 
		printf "image $image_name  deleted successfully\n"
	fi
}

function enter_container () {
	docker exec -it $container_name bash
}

case "$2" in
	-v|--verbose|-verbose)
		verbose='true'
esac


case "$1" in
	stop)
		stop_container
		;;
	start)
		init_container
		enter_container
		;;
	rebuild)
		stop_container
		delete_container
		delete_image
		init_container
		;;
	remove)
		stop_container
		delete_container
		delete_image
		;;
	enter)
		enter_container
		;;
	*)
		init_container
		enter_container
esac
