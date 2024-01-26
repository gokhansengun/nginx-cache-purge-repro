# Aim

This repo minimally reproduces the problem described in GitHub [issue](https://github.com/magiclen/nginx-cache-purge/issues/1)

# Usage

1. Get the proxy and test backend app up and running:

    ```bash
    docker compose up -d
    docker compose logs -f
    ```

1. Create 100 cache items in the proxy cache:

    ```bash
    for ((i=0;i<100;++i))
    do
      curl "http://localhost/category/cat-${i}" && echo
    done
    ```

1. Purge all cache items under `/category` using:

    ```bash
    docker compose exec proxy nginx-cache-purge p /cache 1:2 '/category/*'
    ```

1. List all cache items using:

    ```bash
    docker compose exec proxy ls /cache
    ```

You should see that NOT all the cache items under `/category` have been purged.
