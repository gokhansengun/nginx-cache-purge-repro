FROM openresty/openresty:1.25.3.1-bookworm-fat

RUN curl -LO https://github.com/magiclen/nginx-cache-purge/releases/download/v0.4.4/nginx-cache-purge_x86_64 && \
  mv nginx-cache-purge_x86_64 /usr/local/bin/nginx-cache-purge && \
  chmod +x /usr/local/bin/nginx-cache-purge

RUN opm get knyar/nginx-lua-prometheus=0.20230607
