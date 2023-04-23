# swagroutes

swagroutes is a command-line tool that extracts and lists API routes from Swagger files in YAML or JSON format. It simplifies the process of fetching the routes provided by an API and supports processing multiple files or directories at once.

![](https://user-images.githubusercontent.com/3582096/233068257-29adfadd-8cd3-45fd-9d1d-f22a9772d139.png)

## Install

```bash
pip install swagroutes
```

## Upgrade
```bash
pip install -U swagroutes
```

## Help
```
usage: swagroutes [-h] [-o OUTPUT] [-p] input [input ...]

Extract routes from Swagger files.

positional arguments:
  input                 Input file(s) or directory containing Swagger files.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file to store the results.
  -p, --include-params  Include query parameters in the extracted routes.
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

#### Extract parameters
```bash
swagroutes file1.yaml --include-params
```

#### Output to a file
Save the extracted routes to an output file using the `-o` or `--output` option:

```bash
swagroutes file.yaml -o output.txt 
```


## Examples

**Input:**
```yaml
basePath: /api
paths:
  /users:
    get: {}
    post: {}
  /profile/{profile_id}:
    put: {}
```

**Output:**

```
GET /api/users
POST /api/users
PUT /api/profile/{profile_id}
```

---

**Input:**
```yaml
basePath: /api/v1
paths:
  /users:
    get:
      parameters:
        - name: limit
          in: query
        - name: offset
          in: query

  /users/{userId}:
    get:
      parameters:
        - name: userId
          in: path
          required: true
          type: string
```

**Output:**
```
GET /api/v1/users/{userId}
GET /api/v1/users?limit&offset
```