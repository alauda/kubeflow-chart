# -------------------------------------------------------
# jupyter lab image from kubeflow/components/example-notebook-servers
ARG BASE_IMAGE=ubuntu:22.04
FROM $BASE_IMAGE

ARG BUILDPLATFORM=linux/amd64
ARG TARGETPLATFORM=linux/amd64
ARG TARGETARCH=amd64

# common environemnt variables
ENV NB_USER jovyan
ENV NB_UID 1000
ENV NB_PREFIX /
ENV HOME /home/$NB_USER
ENV SHELL /bin/bash


# args - software versions
ARG KUBECTL_ARCH=${TARGETARCH}
ARG KUBECTL_VERSION=v1.23.0
 # renovate: datasource=github-tags depName=just-containers/s6-overlay versioning=loose
ARG S6_VERSION=v2.2.0.3

# set shell to bash
SHELL ["/bin/bash", "-c"]
RUN if [ "${TARGETARCH}" == "amd64" ]; then \
   sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list && \
   sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list; \
fi && \
if [ "${TARGETARCH}" == "arm64" ]; then \
    echo "deb http://mirrors.ustc.edu.cn/ubuntu-ports/ jammy main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb http://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-security main restricted universe multiverse" >> /etc/apt/sources.list; \
fi

# install - usefull linux packages
RUN export DEBIAN_FRONTEND=noninteractive \
 && apt-get -yq update \
 && apt-get -yq install --no-install-recommends \
    apt-transport-https \
    bash \
    bzip2 \
    ca-certificates \
    curl \
    git \
    gnupg \
    gnupg2 \
    locales \
    lsb-release \
    nano \
    software-properties-common \
    tzdata \
    unzip \
    vim \
    wget \
    zip \
    build-essential \
    cmake \
    sudo \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# install - s6 overlay
RUN export GNUPGHOME=/tmp/ && \
if [ "${TARGETARCH}" == "amd64" ]; then S6_ARCH="amd64"; fi && \
if [ "${TARGETARCH}" == "arm64" ]; then S6_ARCH="aarch64"; fi && \
curl -sL "https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-${S6_ARCH}-installer" -o /tmp/s6-overlay-${S6_VERSION}-installer && \
chmod +x /tmp/s6-overlay-${S6_VERSION}-installer && \
/tmp/s6-overlay-${S6_VERSION}-installer / && \
rm /tmp/s6-overlay-${S6_VERSION}-installer

# install - kubectl
RUN curl -sL "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/${KUBECTL_ARCH}/kubectl" -o /usr/local/bin/kubectl \
 && curl -sL "https://dl.k8s.io/${KUBECTL_VERSION}/bin/linux/${KUBECTL_ARCH}/kubectl.sha256" -o /tmp/kubectl.sha256 \
 && echo "$(cat /tmp/kubectl.sha256) /usr/local/bin/kubectl" | sha256sum --check \
 && rm /tmp/kubectl.sha256 \
 && chmod +x /usr/local/bin/kubectl

# create user and set required ownership
RUN useradd -M -s /bin/bash -N -u ${NB_UID} ${NB_USER} \
 && mkdir -p ${HOME} \
 && chown -R ${NB_USER}:users ${HOME} \
 && chown -R ${NB_USER}:users /usr/local/bin \
 && chown -R ${NB_USER}:users /etc/s6 \
 && echo "${NB_USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# set locale configs
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
 && locale-gen

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# setup environment for conda
ENV CONDA_DIR /opt/conda
ENV PATH "${CONDA_DIR}/bin:${PATH}"
RUN mkdir -p ${CONDA_DIR} \
 && echo ". /opt/conda/etc/profile.d/conda.sh" >> ${HOME}/.bashrc \
 && echo "alias ls='ls --color=auto'" >> ${HOME}/.bashrc \
 && echo ". /opt/conda/etc/profile.d/conda.sh" >> /etc/profile \
 && echo "conda activate base" >> ${HOME}/.bashrc \
 && echo "conda activate base" >> /etc/profile \
 && chown -R ${NB_USER}:users ${CONDA_DIR} \
 && chown -R ${NB_USER}:users ${HOME}

# switch to NB_UID for installs
USER ${NB_UID}

# install - conda, pip, python
RUN if [ "${TARGETARCH}" == "amd64" ]; then MINICONDA_ARCH="x86_64"; fi && \
if [ "${TARGETARCH}" == "arm64" ]; then MINICONDA_ARCH="aarch64"; fi && \
curl -sL "https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-Linux-${MINICONDA_ARCH}.sh" -o /tmp/miniconda3.sh && \
/bin/bash /tmp/miniconda3.sh -b -f -p ${CONDA_DIR} && \
rm /tmp/miniconda3.sh && \
conda config --system --set auto_update_conda false && \
conda config --system --set show_channel_urls true && \
conda update -y -q --all && \
conda clean -a -f -y && \
chown -R ${NB_USER}:users ${CONDA_DIR} && \
chown -R ${NB_USER}:users ${HOME}

RUN python3 -m pip install --upgrade pip && \
python3 -m pip install --quiet --no-cache-dir \
-i https://pypi.tuna.tsinghua.edu.cn/simple \
jupyterlab==3.6.3 \
notebook==6.4.12 \
ipykernel==6.15.0 \
pygwalker==0.1.7 \
elyra==3.15.0[kfp-tekton] \
jupyter-archive \
jupyterlab-s3-browser \
jupyterlab-language-pack-zh-CN \
matplotlib \
 && jupyter lab --generate-config \
 && rm -rf ${HOME}/.cache/yarn \
 && chown -R ${NB_USER}:users ${CONDA_DIR} \
 && chown -R ${NB_USER}:users ${HOME}

USER root
# s6 - copy scripts
COPY --chown=jovyan:users mlops-ide/s6/ /etc
# s6 - 01-copy-tmp-home
RUN mkdir -p /tmp_home \
 && cp -r ${HOME} /tmp_home \
 && chown -R ${NB_USER}:users /tmp_home

# cleanup
RUN rm -f README.md ${ELYRA_PACKAGE}

USER ${NB_UID}

EXPOSE 8888

ENTRYPOINT ["/init"]
