ARG BASE_IMAGE
ARG HELM_IMAGE
ARG KUBECTL_IMAGE

FROM ${HELM_IMAGE} AS helm
FROM ${KUBECTL_IMAGE} AS kubectl

#
# Assembled container
#
FROM ${BASE_IMAGE}

#
# Packaged software
#

RUN \
  dnf install -y \
    ansible \
    buildah \
    findutils \
    jq \
    openssl \
    podman \
    python \
    skopeo

#
# Unpackaged software
#

COPY --from=helm /usr/local/bin/helm /usr/local/bin/helm
COPY --from=kubectl /usr/local/bin/kubectl /usr/local/bin/kubectl

#
# Scripts
#

COPY scripts /usr/local/bin
RUN find /usr/local/bin -type f -not -executable -print0 | xargs -r -0 chmod +x
