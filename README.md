# DomainSpellChecker
---

This lambda function provides a domain specific spell checker.

Licensed under the GNU General Public License ver3 or later. GNU General Public License: http://www.gnu.org/licenses/

#### Platform: Python 3.6

## Instructions
To deploy to Lambda, it requires the regex python package files.  These files must come from a 64-bit AMI linux image (not Windows).

Building Lambda functions on your host machine running Windows or Mac OS may not build lambda functions properly and may cause issues when executing on AWS. Compiling lambda functions for certain runtimes where the dependencies are compiled differently for each host OS is the culprit here. Hence the best way to ensure that the lambda function will execute seamlessly on AWS is to make sure that you compile it in an environment similar to where its going to run in. 

Please remember building lambda functions can be tricky. Its best to build it in an environment similar to the one its going to be run in, as sometime not doing so can create modules or dependency issues.

## How to Build

Building the function is really simple. You will need docker installed and setup on your machine to be able to build. To install docker, visit [https://www.docker.com/get-started](https://www.docker.com/get-started). 

Once you have docker installed and running, use the attached docker-compose file and it will take care of the whole building process. This can be done using

```
docker-compose up
```

This will build the docker image first if you don't already have one built, and then run the build command and output a deployable zip file in `target` folder. At this point if you already know your way around lambda function you can take the zip and deploy to the lambda.


## Setting up

You can trigger this lambda from API Gateway. You must can select proxy pass for method integration in the API Gateway.

### IAM Role for Lambda

Below is a copy for the role permissions that the lambda function will require.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```

## Using the function

Send a POST to the API Gateway with application/json formatted body: 

#### Request Body

```json
{
	"text": "spel checj thes."
}
```

#### Response Body

```json
{
  "output": { "words": "spell check these"}
}
```
