# Lambda's AL2023 container base ships a snapshot-safe OpenSSL. Tenant code may
# open TLS connections (pip install, HTTPS calls), and every MicroVM is cloned
# from one snapshot, so a stock OpenSSL could reuse random state across tenants.
FROM public.ecr.aws/lambda/microvms:al2023-minimal

# Needs the build-time egress connector (internet) to reach the package repos
RUN dnf install -y python3 shadow-utils \
 && dnf clean all \
 && useradd --create-home --uid 1000 sandbox \
 && mkdir -p /workspace \
 && chown sandbox:sandbox /workspace

WORKDIR /app
COPY server.py .

# Tenant code runs as this unprivileged user, never as root
USER sandbox

EXPOSE 8080 9000
CMD ["python3", "/app/server.py"]
