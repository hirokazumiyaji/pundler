# Python Package Manager using pip

## Description
This can to divided to install require library for each environment using pip in a single config file.

## Command
### install

```
$ pundle install <-e environment> <-f config-file-path>
```

- config file path is `pwd/Pyfile` when executing command without `-f` or `--file` option

- environment is development when executing command without `-e` or `--environment` option


### list(pip list)

```
$ pundle list
Django (1.7)
pip (1.5.6)
py (1.4.26)
pytest (2.6.4)
PyYAML (3.11)
redis (2.10.3)
setuptools (3.6)
wsgiref (0.1.2)
```

## Config File

```yaml:Pyfile
common: &common
  Django: {version: '>=1.7'}
  redis:

development:
  <<: *common

production:
  <<: common

test:
  <<: *common
  pytest:
```

### Config of Library

- version ex) `{version: '0.0.1'}, {version: '>=0.0.1,<=0.0.2'}`
- git ex) `{git: repository_url}`
- hg ex) `{hg: repository_url}`
- svn ex) `{svn: repository_url}`
