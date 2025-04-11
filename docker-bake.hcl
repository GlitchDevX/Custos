group "default" {
    targets = [ "backend-latest", "backend-version", "frontend-latest", "frontend-version" ]
}
group "backend" {
    targets = [ "backend-version", "backend-latest" ]
}
group "frontend" {
    targets = [ "frontend-latest", "frontend-version" ]
}

# overwritten by env
variable "CUSTOS_TAG" {
    default = "none"
}
variable "TAGS_MAP" {
    default = [["latest", "latest"], ["${CUSTOS_TAG}", "version"]]
}
variable "DOCKER_USERNAME" {
    default = "glitchdevx"
}

target "backend" {
    name = "backend-${tag[1]}"
    context = "backend"
    dockerfile = "Dockerfile"

    matrix = {
      "tag" = "${TAGS_MAP}"
    }

    tags = ["${DOCKER_USERNAME}/custos:${tag[0]}"]
}
target "frontend" {
    name = "frontend-${tag[1]}"
    context = "frontend"
    dockerfile = "Dockerfile"

    matrix = {
      "tag" = "${TAGS_MAP}"
    }

    tags = ["${DOCKER_USERNAME}/custos-ui:${tag[0]}"]
}