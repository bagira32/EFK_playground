FROM fluent/fluentd:edge-debian
USER root
RUN fluent-gem install fluent-plugin-grok-parser \
    && fluent-gem install faraday -v 2.11.0 \
    && fluent-gem install elasticsearch-xpack \
    && fluent-gem install fluent-plugin-elasticsearch -v 5.4.2 \
    && fluent-gem install elasticsearch -v 7.12 \
    && fluent-gem sources --clear-all \
    && rm -rf /var/cache/apk/* /home/fluent/.gem/ruby/2.3.0/cache/*.gem
