group "default" {
  targets = [ "ui" ]
}

variable "TAG" {
    default = "latest"
}

target "ui" {
  context = "."
  dockerfile = "frontend/Dockerfile"
  tags = ["glitchdevx/custos-ui:${TAG}"]
}