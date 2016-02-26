# -*- coding: utf-8 -*-

from tfstate.provider.aws.base import AwsResource
from tfstate.provider.aws.aws_eip import AwsEipResource
from tfstate.provider.aws.aws_internet_gateway import AwsInternetGatewayResource
from tfstate.provider.aws.aws_route_table import AwsRouteTableResource
from tfstate.provider.aws.aws_route_table_association import AwsRouteTableAssociationResource
from tfstate.provider.aws.aws_subnet import AwsSubnetResource
from tfstate.provider.aws.aws_vpc import AwsVpcResource
from tfstate.provider.aws.aws_key_pair import AwsKeyPairResource
from tfstate.provider.aws.aws_instance import AwsInstanceResource
from tfstate.provider.aws.aws_security_group import AwsSecurityGroupResource