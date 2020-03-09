ARG BASE_IMAGE

FROM $BASE_IMAGE AS download
ARG KUBECTL_VERSION=v1.17.3
RUN \
  curl -sSfL https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl -o kubectl && \
  chmod +x kubectl && \
  mv kubectl /usr/local/bin/kubectl

FROM scratch AS kubectl
COPY --from=download /usr/local/bin/kubectl /usr/local/bin/kubectl
ENTRYPOINT [ "/usr/local/bin/kubectl" ]
