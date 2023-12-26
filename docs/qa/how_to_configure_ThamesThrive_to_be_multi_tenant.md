# How to configure ThamesThrive to be multi tenant?

To configure ThamesThrive as a multi-tenant system, you need to follow these steps:

## Understand ThamesThrive's Multi-Tenancy Concept

In ThamesThrive, multi-tenancy means that a single ThamesThrive container can serve data for multiple separated tenants. Each
tenant's data is stored in a separate namespace within the storage, ensuring data isolation and separation between
tenants. This feature is available only in commercial ThamesThrive version.

## Configure ThamesThrive as Single Tenant (Default)

By default, ThamesThrive operates as a single tenant system, connecting to the namespace of a single tenant. The name of the
tenant can be configured using the environment variable TENANT_NAME. If this variable is not set, the system will
generate a random name for the tenant.

## Enable Multi-Tenancy

To enable multi-tenancy in ThamesThrive, you need to set the environment variable MULTI_TENANT to "yes". This tells ThamesThrive
container that it should serve multiple tenants. The tenant name will be defined based on your API domain. For example,
if your API domain is company-x.ThamesThrive.com, the tenant name will be set as "companyx" by removing all non-alphanumeric
characters. All the data indices for each tenant will be prefixed with the tenant name, creating a namespace in the
storage.

## Prerequisites for Tenant Name

There are some prerequisites for the tenant name in ThamesThrive.

### Length Requirement

The tenant name must be at least 5 letters long, excluding non-alphanumeric characters.

### Non-Numeric

The tenant name cannot consist solely of numeric characters. It must include at least one non-numeric character.

### Domain Structure

The tenant name must be part of a domain that has three parts. For example, a domain like "mydomain.com" will not create
a valid tenant as it only has two parts ("com" and "mydomain"). However, a domain like "xxx.mydomain.com" will define a
tenant with the name "xxx". Similarly, in the case of "zzz.xxx.mydomain.com," the tenant name will be "zzz".

## Define Available Tenants

You can define the list of available tenants by setting the environment variable TENANT_API to the URL of the tenant
manager microservice. This microservice will manage the list of tenants and provide the necessary functionality to
create, update, and delete tenants.

## Set Multi Tenant GUI

Set the environment variable called MULTI_TENANT to "yes". This setting will disable index management on the graphical
user interface (GUI).

In a multi-tenant installation, managing indices is not available. Multi-tenant installations are designed to have
access to the entire Elasticsearch cluster, rather than tenant index management.

## Errors

If you encounter an issue while trying to start a multi-tenant ThamesThrive server API, you can check the logs for a
specific error message: "Can not find tenant for this instance." This error indicates that the prerequisites for the
tenant name have not been met. In other words, the tenant name provided does not meet the necessary criteria as
discussed earlier. By reviewing the logs and ensuring that the tenant name meets the required prerequisites, you can
resolve this issue and successfully start the multi-tenant ThamesThrive server API.

---
This document answers the following questions:
- How to set-up multitenacy in ThamesThrive?
- How to set-up GUI to be multi tenant installation?
- How multi tenant setup works in ThamesThrive?
- How tenants are differentiated in ThamesThrive?
- How to enable tenant in ThamesThrive?
- Is multi tenancy available in open-source version?
