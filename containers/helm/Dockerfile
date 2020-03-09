ARG BASE_IMAGE

FROM $BASE_IMAGE AS download
ARG HELM_VERSION=v3.1.1
RUN \
  curl -sSfL https://get.helm.sh/helm-$HELM_VERSION-linux-amd64.tar.gz | tar -xzf - --strip-components=1 && \
  chmod +x helm && \
  mv helm /usr/local/bin/helm

FROM scratch AS helm
COPY --from=download /usr/local/bin/helm /usr/local/bin/helm
ENTRYPOINT [ "/usr/local/bin/helm" ]
