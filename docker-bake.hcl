group "default" {
    targets = [ "backend", "frontend" ]
}

variable "TAG" {
    default = "latest"
}

target "backend" {
    context = "backend"
    dockerfile = "Dockerfile"
    tags = ["glitchdevx/custos:${TAG}"]
}
target "frontend" {
    context = "frontend"
    dockerfile = "Dockerfile"
    tags = ["glitchdevx/custos-ui:${TAG}"]
}