# Helm-EKS
Goes along with the Blog on deploying apps in EKS using Helm and CloudFormation.

Pre-requisites

You will need to have the following completed prior to working through the deployment part of the blog. 

* Deploy EKS cluster using the “Modular and Scalable Amazon EKS Architecture” Quick Start by following the deployment guide at the following link. 
    * https://docs.aws.amazon.com/quickstart/latest/amazon-eks-architecture/welcome.html
* Once you have the EKS cluster deployed you will need to get the following outputs from the EKSStack in CloudFormation.
    * Needed Outputs both examples:
        * “HelmLambdaArn”
        * “KubeClusterName“
        * “KubeConfigPath“
        * “KubeGetLambdaArn“
    * Needed for build with external database example only
        * “NodeGroupSecurityGroupId” 
        * “BastionSecurityGroupId” 
    * How to retrieve the needed outputs:
        * In the AWS Console under Services select CloudFormation.
        * In CloudFormation select Stacks from the left side panel. 
        * In Stacks click on <Name-of-EKSStack>-EKSStack-<random suffix>
            * ex. “eks-run-1-EKSStack-1IOKX7GLR4KM5”

