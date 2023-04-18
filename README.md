# swagroutes

swagroutes is a command-line tool that extracts and lists API routes from Swagger files in YAML or JSON format. It simplifies the process of fetching the routes provided by an API and supports processing multiple files or directories at once.

![](https://user-images.githubusercontent.com/3582096/232892882-7755d610-a85a-4c21-8a35-543d24204d23.png)

## Install

```bash
pip install swagroutes
```

## Upgrade
```bash
pip install -U swagroutes
```

## Usage
To use swagroutes, simply provide input files or directories containing Swagger files as arguments. The tool will process the files and print the extracted routes.

#### Single YAML or JSON file
```bash
swagroutes file.yaml
```

```bash
swagroutes file.json
```

#### Multiple YAML and/or JSON files

```bash
swagroutes file1.yaml file2.json
```

#### Directory containing Swagger files
```bash
swagroutes directory/
```

#### Mix of files and directories
```bash
swagroutes file1.yaml directory1/ file2.json directory2/
```

#### Output to a file
Save the extracted routes to an output file using the `-o` or `--output` option:

```bash
swagroutes file.yaml -o output.txt 
```


## Examples
Given a Swagger file with the following content:

```yaml
basePath: /api
paths:
  /users:
    get: {}
    post: {}
  /profile/{profile_id}:
    put: {}
```

swagroutes will output:

```
GET /api/users
POST /api/users
PUT /api/profile/{profile_id}
```
