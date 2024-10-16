# EFK stack

A sample environment running an [EFK stack][efk] on your local machine.

Includes:

- [Elasticsearch][elasticsearch]
- [Fluentd][fluentd]
- [Kibana][kibana]

## Introduction

As software systems grow and become more and more decoupled, log aggregation is a key aspect to take care of.

The issues to tackle down with logging are:

- Having a centralized overview of all log events
- Normalizing different log types
- Automated processing of log messages
- Supporting several and very different event sources

While [Elasticsearch][elasticsearch] and [Kibana][kibana] are the reference products *de facto* for log searching and visualization in the open source community, there's no such agreement for log collectors.

The two most-popular data collectors are:

- [Logstash][logstash], most known for being part of the [ELK Stack][elk]
- [Fluentd][fluentd], used by communities of users of software such as [Docker][docker-fluentd] and [GCP][gcp-fluentd]

Logging systems using Fluentd as collector are usually referenced as [EFK stack][efk].

Aim of this repository is to run an EFK stack on your local machine using docker-compose.

I'm not personally involved with companies supporting Logstash nor Fluentd.

If you need help to choose between Logstash and Fluent, take a look to the [reference](#reference).

## Launching the EFK stack

### Requirements

On your machine, make sure you have installed:

- [Docker][docker]
- [Docker Compose][docker-compose]

### Run

```bash
docker-compose up
```

Please note: in this example Fluentd will run on port `8080` instead of the default `24224`.

This settings has been changed to show how to configure Fluentd to listen on a different port.

Kibana is exposed on port `5601`.

### Testing with sample data


If you have curl client installed on your system, you can generate sample data by running:

```bash
curl -X POST -d 'json={"action":"login","userId":"5b07fbbb4e6b8"}' http://localhost:8080/myapp.log
```

## Reference

- [Quora - What is the ELK stack](https://www.quora.com/What-is-the-ELK-stack)
- [Fluentd vs. LogStash: A Feature Comparison](https://www.loomsystems.com/blog/single-post/2017/01/30/a-comparison-of-fluentd-vs-logstash-log-collector)
- [Panda Strike: Fluentd vs Logstash](https://www.pandastrike.com/posts/20150807-fluentd-vs-logstash)
- [Log Aggregation with Fluentd, Elasticsearch and Kibana - Haufe-Lexware.github.io](http://work.haufegroup.io/log-aggregation/)
- [Fluentd vs Logstash, An unbiased comparison](https://techstricks.com/fluentd-vs-logstash/)
- [Fluentd vs. Logstash: A Comparison of Log Collectors | Logz.io](https://logz.io/blog/fluentd-logstash/)

[elasticsearch]: https://www.elastic.co/products/elasticsearch
[fluentd]: https://www.fluentd.org/
[kibana]: https://www.elastic.co/products/kibana
[logstash]: https://www.elastic.co/products/logstash
[elk]: https://www.elastic.co/videos/introduction-to-the-elk-stack
[docker-fluentd]: https://docs.docker.com/reference/logging/fluentd/
[gcp-fluentd]: https://github.com/GoogleCloudPlatform/google-fluentd
[efk]: https://docs.openshift.com/enterprise/3.1/install_config/aggregate_logging.html#overview
[docker]: https://www.docker.com/
[docker-compose]: https://docs.docker.com/compose/
[rested]: https://itunes.apple.com/au/app/rested-simple-http-requests/id421879749?mt=12